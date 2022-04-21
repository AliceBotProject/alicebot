"""CQHTTP 协议适配器。

本适配器适配了 OneBot v11 协议。
协议详情请参考: [OneBot](https://github.com/howmanybots/onebot/blob/master/README.md) 。
"""
import sys
import time
import json
import asyncio
from functools import partial
from typing import Any, Dict, Literal, TYPE_CHECKING

import aiohttp
from aiohttp import web

from alicebot.log import logger
from alicebot.utils import Condition
from alicebot.adapter import Adapter
from alicebot.message import DataclassEncoder

from .config import Config
from .event import get_event_class
from .message import CQHTTPMessage
from .exceptions import NetworkError, ActionFailed, ApiNotAvailable, ApiTimeout

if TYPE_CHECKING:
    from .message import T_CQMSG

__all__ = ['CQHTTPAdapter']


class CQHTTPAdapter(Adapter):
    """CQHTTP 协议适配器。
    
    在插件中可以直接使用 `self.adapter.xxx_api(**params)` 调用名称为 `xxx_api` 的 API，和调用 `call_api()` 方法相同。
    """
    name: str = 'cqhttp'
    app: web.Application = None
    runner: web.AppRunner = None
    site: web.TCPSite = None
    websocket: web.WebSocketResponse = None
    api_response_cond: Condition = None
    _api_id: int = 0

    @property
    def config(self):
        """本适配器的配置。"""
        return getattr(self.bot.config, Config.__config_name__)

    def __getattr__(self, item):
        return partial(self.call_api, item)

    async def startup(self):
        """创建 aiohttp Application。"""
        self.api_response_cond = Condition()
        self.app = web.Application()
        self.app.add_routes([web.get(self.config.url, self.handle_response)])

    async def run(self):
        """运行 aiohttp WebSocket 服务器。"""
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, self.config.host, self.config.port)
        await self.site.start()

    async def shutdown(self):
        """清理 aiohttp AppRunner。"""
        if self.websocket is not None:
            await self.websocket.close()
        if self.site is not None:
            await self.site.stop()
        if self.runner is not None:
            await self.runner.cleanup()

    async def handle_response(self, request: web.Request):
        """处理 aiohttp WebSocket 服务器的接收。

        Args:
            request: aiohttp WebSocket 服务器的 Request 对象。
        """
        ws = web.WebSocketResponse()
        await ws.prepare(request)
        self.websocket = ws

        msg: aiohttp.WSMessage
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                try:
                    msg_dict = msg.json()
                except json.JSONDecodeError as e:
                    logger.error(f'WebSocket message parsing error, not json: {e!r}')
                    continue

                if 'post_type' in msg_dict:
                    await self.handle_cqhttp_event(msg_dict)
                else:
                    async with self.api_response_cond:
                        self.api_response_cond.notify_all(msg_dict)

            elif msg.type == aiohttp.WSMsgType.ERROR:
                logger.error(f'WebSocket connection closed with exception {ws.exception()!r}')

        if not self.bot.should_exit.is_set():
            logger.warning('WebSocket connection closed!')

        return ws

    def _get_api_echo(self) -> int:
        self._api_id = (self._api_id + 1) % sys.maxsize
        return self._api_id

    async def handle_cqhttp_event(self, msg: Dict[str, Any]):
        """处理 CQHTTP 事件。

        Args:
            msg: 接收到的信息。
        """
        post_type = msg.get('post_type')
        event_type = msg.get(post_type + '_type')
        sub_type = msg.get('sub_type', None)
        event_class = get_event_class(post_type, event_type, sub_type)

        cqhttp_event = event_class(**msg)
        cqhttp_event.adapter = self

        if cqhttp_event.post_type == 'meta_event':
            # meta_event 不交由插件处理
            if cqhttp_event.meta_event_type == 'lifecycle' and cqhttp_event.sub_type == 'connect':
                logger.info(f'WebSocket connection from CQHTTP Bot {msg.get("self_id")} accepted!')
            elif cqhttp_event.meta_event_type == 'heartbeat':
                if cqhttp_event.status.good and cqhttp_event.status.online:
                    pass
                else:
                    logger.error(f'CQHTTP Bot status is not good: {cqhttp_event.status.dict()}')
        else:
            await self.handle_event(cqhttp_event)

    async def call_api(self, api: str, **params) -> Dict[str, Any]:
        """调用 CQHTTP API，协程会等待直到获得 API 响应。

        Args:
            api: API 名称。
            **params: API 参数。

        Returns:
            API 响应中的 data 字段。

        Raises:
            NetworkError: 网络错误。
            ApiNotAvailable: API 请求响应 404， API 不可用。
            ActionFailed: API 请求响应 failed， API 操作失败。
            ApiTimeout: API 请求响应超时。
        """
        api_echo = self._get_api_echo()
        try:
            await self.websocket.send_str(json.dumps({
                'action': api,
                'params': params,
                'echo': api_echo
            }, cls=DataclassEncoder))
        except Exception:
            raise NetworkError

        start_time = time.time()
        while not self.bot.should_exit.is_set():
            if time.time() - start_time > self.config.api_timeout:
                break
            async with self.api_response_cond:
                try:
                    resp = await asyncio.wait_for(self.api_response_cond.wait(),
                                                  timeout=start_time + self.config.api_timeout - time.time())
                except asyncio.TimeoutError:
                    break
                if resp['echo'] == api_echo:
                    if resp.get('retcode') == 1404:
                        raise ApiNotAvailable(resp=resp)
                    if resp.get('status') == 'failed':
                        raise ActionFailed(resp=resp)
                    return resp.get('data')

        if not self.bot.should_exit.is_set():
            raise ApiTimeout

    async def send(self, message_: 'T_CQMSG', message_type: Literal['private', 'group'], id_: int) -> Dict[str, Any]:
        """发送消息，调用 send_private_msg 或 send_group_msg API 发送消息。

        Args:
            message_: 消息内容，可以是 str, Mapping, Iterable[Mapping], 'CQHTTPMessageSegment', 'CQHTTPMessage'。
                将使用 `CQHTTPMessage` 进行封装。
            message_type: 消息类型。应该是 private 或者 group。
            id_: 发送对象的 ID ，QQ 号码或者群号码。

        Returns:
            API 响应。

        Raises:
            TypeError: message_type 不是 'private' 或 'group'。
            ...: 同 `call_api()` 方法。
        """
        if message_type == 'private':
            return await self.send_private_msg(user_id=id_, message=CQHTTPMessage(message_))
        elif message_type == 'group':
            return await self.send_group_msg(group_id=id_, message=CQHTTPMessage(message_))
        else:
            raise TypeError('message_type must be "private" or "group"')
