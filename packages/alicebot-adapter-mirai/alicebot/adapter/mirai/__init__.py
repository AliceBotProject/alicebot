"""Mirai 协议适配器。

本适配器适配了 mirai-api-http 协议，仅支持 mirai-api-http 2.0 及以上版本。
本适配器支持 mirai-api-http 的 Websocket Adapter 模式和 Reverse Websocket Adapter 模式。
协议详情请参考: [mirai-api-http](https://github.com/project-mirai/mirai-api-http) 。
"""
import sys
import time
import json
import asyncio
from functools import partial
from typing import Any, Dict, Iterable, Literal, Optional, Union, Mapping, TYPE_CHECKING

import aiohttp
from aiohttp import web

from alicebot.log import logger
from alicebot.utils import Condition
from alicebot.adapter import Adapter
from alicebot.message import DataclassEncoder

from .config import Config
from .message import MiraiMessage
from .exceptions import NetworkError, ActionFailed, ApiTimeout
from .event import BotEvent, CommandExecutedEvent, MateEvent, get_event_class

if TYPE_CHECKING:
    from .event import T_MiraiEvent
    from .message import MiraiMessageSegment

__all__ = ['MiraiAdapter']


class MiraiAdapter(Adapter):
    """Mirai 协议适配器。

    在插件中可以直接使用 `self.adapter.xxx_api(**params)` 调用名称为 `xxx_api` 的 API，和调用 `call_api()` 方法相同。
    """

    name: str = 'mirai'

    websocket: Union[web.WebSocketResponse, aiohttp.ClientWebSocketResponse] = None

    # ws
    session: aiohttp.ClientSession = None

    # reverse-ws
    app: web.Application = None
    runner: web.AppRunner = None
    site: web.TCPSite = None

    api_response_cond: Condition = None
    _sync_id: int = 0

    @property
    def config(self):
        """本适配器的配置。"""
        return getattr(self.bot.config, Config.__config_name__)

    def __getattr__(self, item):
        return partial(self.call_api, item)

    async def startup(self):
        """初始化适配器。"""
        self.api_response_cond = Condition()
        if self.config.adapter_type == 'ws':
            self.session = aiohttp.ClientSession()
        elif self.config.adapter_type == 'reverse-ws':
            self.app = web.Application()
            self.app.add_routes([web.get(self.config.url, self.handle_response)])
        else:
            logger.error(f'Config "adapter_type" must be "ws" or "reverse-ws", not {self.config.adapter_type}')

    async def run(self):
        """运行适配器。"""
        if self.config.adapter_type == 'ws':
            await self.websocket_connect()
        elif self.config.adapter_type == 'reverse-ws':
            self.runner = web.AppRunner(self.app)
            await self.runner.setup()
            self.site = web.TCPSite(self.runner, self.config.host, self.config.port)
            await self.site.start()

    async def shutdown(self):
        """关闭并清理连接。"""
        if self.websocket is not None:
            await self.websocket.close()
        if self.config.adapter_type == 'ws':
            if self.session is not None:
                await self.session.close()
        elif self.config.adapter_type == 'reverse-ws':
            if self.site is not None:
                await self.site.stop()
            if self.runner is not None:
                await self.runner.cleanup()

    async def handle_response(self, request: web.Request):
        """处理 aiohttp WebSocket 服务器的接收。

        Args:
            request: aiohttp WebSocket 服务器的 Request 对象。
        """
        logger.info(f'WebSocket connected!')
        self.websocket = web.WebSocketResponse()
        await self.websocket.prepare(request)
        asyncio.create_task(self.verify_identity())
        await self.handle_websocket_msg()
        return self.websocket

    async def websocket_connect(self):
        """创建正向 WebSocket 连接。"""
        while not self.bot.should_exit.is_set():
            logger.info('Trying to verify identity and create connection...')
            try:
                async with self.session.ws_connect('ws://{}:{}/all?verifyKey={}&qq={}'.format(
                        self.config.host,
                        self.config.port,
                        self.config.verify_key,
                        self.config.qq
                )) as self.websocket:
                    await self.handle_websocket_msg()
            except aiohttp.ClientError as e:
                logger.warning(f'Create connection with exception {e!r}, retrying...')
                await asyncio.sleep(3)

    async def handle_websocket_msg(self):
        """处理 WebSocket 消息。"""
        first_websocket_msg = True
        msg: aiohttp.WSMessage
        async for msg in self.websocket:
            if msg.type == aiohttp.WSMsgType.TEXT:
                if first_websocket_msg:
                    first_websocket_msg = False
                    if self.config.adapter_type == 'ws':
                        # 当 adapter_type 为 ws 时，第一条消息一定是验证消息，不进行处理
                        msg_dict = msg.json()
                        if msg_dict.get('data', {}).get('code') == 0:
                            logger.info(f'Verify success! Session key: {msg_dict.get("data").get("session")}')
                        else:
                            logger.warning(f'Verify failed with code {msg_dict.get("code") or msg_dict}, retrying...')
                            await asyncio.sleep(3)
                        continue

                try:
                    msg_dict = msg.json()
                except json.JSONDecodeError:
                    await self.handle_non_standard_response(msg.data)
                    continue

                if 'syncId' in msg_dict:
                    if msg_dict.get('syncId') == '-1':
                        await self.handle_mirai_event(msg_dict.get('data'))
                    else:
                        async with self.api_response_cond:
                            self.api_response_cond.notify_all(msg_dict)
                else:
                    await self.handle_non_standard_response(msg_dict)

            elif msg.type == aiohttp.WSMsgType.ERROR:
                logger.error(f'WebSocket connection closed with exception {self.websocket.exception()!r}')

        if not self.bot.should_exit.is_set():
            logger.warning(f'WebSocket connection closed!')

    def _get_sync_id(self) -> int:
        self._sync_id = (self._sync_id + 1) % sys.maxsize
        return self._sync_id

    async def handle_mirai_event(self, msg: Dict[str, Any]):
        """处理 Mirai 事件。

        Args:
            msg: 接收到的信息。
        """
        mirai_event = get_event_class(msg.get('type'))(**msg)
        mirai_event.adapter = self

        if isinstance(mirai_event, MateEvent):
            # meta_event 不交由插件处理
            if isinstance(mirai_event, BotEvent):
                logger.info(f'Bot {mirai_event.qq}: {mirai_event.type}')
            elif isinstance(mirai_event, CommandExecutedEvent):
                logger.info(f'Command "{mirai_event.name}" was executed: {mirai_event!r}')
        else:
            await self.handle_event(mirai_event)

    async def handle_non_standard_response(self, data: Union[str, Dict[str, Any]]):
        """处理 Mirai 返回的非标准响应。

        Args:
            data: 接收到的信息。
        """
        error_code = None
        if isinstance(data, str):
            if data == '指定Bot不存在':
                # 进行 verify 时具有非标准返回，会返回文本而非 json，测试使用的 mirai-api-http 版本：2.2.0
                error_code = 2
            else:
                logger.error(f'WebSocket message parsing error, not json: {data}')
        elif isinstance(data, dict):
            if data.get('code') is not None:
                # 进行 verify 时具有非标准返回，会返回不具有 syncId 的数据，测试使用的 mirai-api-http 版本：2.2.0
                error_code = data.get('code')
            else:
                logger.error(f'Unknown webSocket message: {data!r}')

        if error_code is not None:
            async with self.api_response_cond:
                self.api_response_cond.notify_all((error_code, data))

    async def verify_identity(self):
        """验证身份，创建与 Mirai-api-http 的连接。"""
        while not self.bot.should_exit.is_set():
            await asyncio.sleep(3)
            try:
                logger.info('Trying to verify identity and create connection...')
                await self.call_api('verify', **{
                    'verifyKey': self.config.verify_key,
                    'sessionKey': None,
                    'qq': self.config.qq
                })
            except ActionFailed as e:
                logger.warning(f'Verify failed with code {e.code}, retrying...')
            else:
                logger.info('Verify success!')

    async def call_api(self, command: str, sub_command: Optional[str] = None, **content) -> Dict[str, Any]:
        """调用 Mirai API，协程会等待直到获得 API 响应。

        Args:
            command: 命令字。
            sub_command: 子命令字。
            **content: 请求内容。

        Returns:
            API 响应中的 data 字段，即 Mirai-api-http API 通用接口中的内容。

        Raises:
            NetworkError: 网络错误。
            ActionFailed: API 操作失败。
            ApiTimeout: API 请求响应超时。
        """
        # content['sessionKey'] = self.session_key
        # content = {key: value
        #            for key, value in content.items()
        #            if value is not None}
        sync_id = str(self._get_sync_id())
        try:
            await self.websocket.send_str(json.dumps({
                'syncId': sync_id,
                'command': command,
                "subCommand": sub_command,
                "content": content
            }, cls=DataclassEncoder))
        except Exception:
            raise NetworkError

        start_time = time.time()
        while not self.bot.should_exit.is_set() and (time.time() - start_time < self.config.api_timeout):
            async with self.api_response_cond:
                try:
                    resp = await asyncio.wait_for(self.api_response_cond.wait(),
                                                  timeout=start_time + self.config.api_timeout - time.time())
                except asyncio.TimeoutError:
                    break
                if isinstance(resp, tuple):
                    raise ActionFailed(code=resp[0], resp=resp[1])
                if resp.get('syncId') == sync_id:
                    status_code = resp.get('data', {}).get('code')
                    if status_code is not None and status_code != 0:
                        raise ActionFailed(code=status_code, resp=resp)
                    return resp.get('data')

        if not self.bot.should_exit.is_set():
            raise ApiTimeout

    async def send(self,
                   message_: Union[str, Mapping, Iterable[Mapping], 'MiraiMessageSegment', 'MiraiMessage'],
                   message_type: Literal['private', 'friend', 'group'],
                   target: int,
                   quote: int = None) -> Dict[str, Any]:
        """调用 Mirai API 发送消息。

        Args:
            message_: 消息内容，可以是 str, Mapping, Iterable[Mapping], 'MiraiMessageSegment', 'MiraiMessage'。
                将使用 `MiraiMessage` 进行封装。
            message_type: 消息类型。应该是 private, friend 或者 group。其中 private 和 friend 相同。
            target: 发送对象的 ID ，QQ 号码或者群号码。
            quote: 引用的消息的 messageId。默认为 `None` ，不引用任何消息。

        Returns:
            API 响应。

        Raises:
            TypeError: message_type 非法。
            ...: 同 `call_api()` 方法。
        """
        if message_type == 'private' or message_type == 'friend':
            return await self.sendFriendMessage(target=target, messageChain=MiraiMessage(message_), quote=quote)
        elif message_type == 'group':
            return await self.sendGroupMessage(target=target, messageChain=MiraiMessage(message_), quote=quote)
        else:
            raise TypeError('message_type must be "private", "friend" or "group"')
