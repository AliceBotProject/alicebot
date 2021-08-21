"""
==================
Mirai 协议适配器
==================
本适配器适配了 mirai-api-http 协议。
本适配器支持 mirai-api-http 的 Reverse Websocket Adapter 模式，此模式于 mirai-api-http 2.0 初次引入，故不本适配器仅支持 mirai-api-http 2.0 及以上版本。
协议详情请参考: `mirai-api-http`_ 。

.. _mirai-api-http: https://github.com/project-mirai/mirai-api-http
"""
import sys
import time
import json
import asyncio
from functools import partial
from typing import Any, Dict, Iterable, List, Literal, Optional, Union, Mapping, TYPE_CHECKING

import aiohttp
from aiohttp import web

from alicebot.log import logger
from alicebot.adapter import AbstractAdapter

from .config import Config
from .message import MiraiMessage, DataclassEncoder
from .exception import NetworkError, ActionFailed, ApiTimeout
from .event import BotEvent, CommandExecutedEvent, MateEvent, get_event_class

if TYPE_CHECKING:
    from .event import T_MiraiEvent
    from .message import T_MiraiMessage, T_MiraiMessageSegment


class MiraiAdapter(AbstractAdapter):
    """
    Mirai 协议适配器。
    在插件中可以直接使用 ``self.adapter.xxx_api(**params)`` 调用名称为 ``xxx_api`` 的 API，和调用 ``call_api()`` 方法相同。
    """

    name: str = 'mirai'
    app: web.Application = None
    runner: web.AppRunner = None
    site: web.TCPSite = None
    websocket: web.WebSocketResponse = None
    api_response: List[Dict[str, Any]] = []
    wait_for_get_api_response: bool = False
    api_response_error_code: int = 0
    api_response_error_data: Union[str, Dict[str, Any]] = ''
    # session_key = None
    _sync_id: int = 0

    @property
    def config(self):
        """
        :return: 本适配器的配置。
        """
        return getattr(self.bot.config, Config.__config_name__)

    def __getattr__(self, item):
        return partial(self.call_api, item)

    async def startup(self):
        """
        创建 aiohttp Application。
        """
        self.app = web.Application()
        self.app.add_routes([web.get(self.config.url, self.handle_response)])

    async def run(self):
        """
        运行 aiohttp WebSockets 服务器。
        """
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, self.config.host, self.config.port)
        await self.site.start()

    async def shutdown(self):
        """
        清理 aiohttp AppRunner。
        """
        if self.websocket is not None:
            await self.websocket.close()
        if self.site is not None:
            await self.site.stop()
        if self.runner is not None:
            await self.runner.cleanup()

    async def handle_response(self, request: web.Request):
        """
        处理 aiohttp WebSockets 服务器的接收。

        :param request: aiohttp WebSockets 服务器的 Request 对象。
        """
        logger.info(f'WebSocket connected!')
        ws = web.WebSocketResponse()
        await ws.prepare(request)
        self.websocket = ws

        asyncio.create_task(self.create_connection())

        msg: aiohttp.WSMessage
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                try:
                    msg_dict = msg.json()
                except json.JSONDecodeError:
                    self.handle_non_standard_response(msg.data)
                    continue

                if 'syncId' in msg_dict:
                    if msg_dict.get('syncId') == '-1':
                        self.handle_mirai_event(msg_dict.get('data'))
                    else:
                        self.handle_api_api_response(msg_dict)
                else:
                    self.handle_non_standard_response(msg_dict)

            elif msg.type == aiohttp.WSMsgType.ERROR:
                logger.error(f'WebSocket connection closed with exception {ws.exception()!r}')

        if not self.bot.should_exit:
            logger.warning(f'WebSocket connection closed!')

        return ws

    def _get_sync_id(self) -> int:
        self._sync_id = (self._sync_id + 1) % sys.maxsize
        return self._sync_id

    def handle_mirai_event(self, msg: Dict[str, Any]):
        """
        处理 Mirai 事件。

        :param msg: 接收到的信息。
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
            self.handle_event(mirai_event)

    def handle_api_api_response(self, msg: Dict[str, Any]):
        """
        处理 Mirai API 调用的响应内容。

        :param msg: 接收到的信息。
        """
        self.wait_for_get_api_response = False
        self.api_response.append(msg)
        if len(self.api_response) > self.bot.config.max_event_queue_len:
            self.api_response.pop(0)

    def handle_non_standard_response(self, data: Union[str, Dict[str, Any]]):
        """
        处理 Mirai 返回的非标准响应。

        :param data: 接收到的信息。
        """
        self.api_response_error_data = data
        if isinstance(data, str):
            if data == '指定Bot不存在':
                # 进行 verify 时具有非标准返回，会返回文本而非 json，测试使用的 mirai-api-http 版本：2.2.0
                self.api_response_error_code = 2
            else:
                logger.error(f'WebSocket message parsing error, not json: {data}')
        elif isinstance(data, dict):
            if data.get('code') is not None:
                # 进行 verify 时具有非标准返回，会返回不具有 syncId 的数据，测试使用的 mirai-api-http 版本：2.2.0
                self.api_response_error_code = data.get('code')
            else:
                logger.error(f'Unknown webSocket message: {data!r}')

    async def create_connection(self):
        """
        验证身份，创建与 Mirai-api-http 的连接。
        """
        while True:
            await asyncio.sleep(3)
            try:
                logger.info(f'Trying to verify identity and create connection...')
                await self.call_api('verify', **{
                    'verifyKey': self.config.verify_key,
                    'sessionKey': None,
                    'qq': self.config.qq
                })
            except ActionFailed as e:
                logger.warning(f'Verify failed with code {e.code}, retrying...')
            else:
                logger.info('Verify success!')
                return True

    async def call_api(self, command: str, sub_command: Optional[str] = None, **content) -> Dict[str, Any]:
        """
        调用 Mirai API，协程会等待直到获得 API 响应。

        :param command: 命令字。
        :param sub_command: 子命令字。
        :param content: 请求内容。
        :return: API 响应中的 data 字段，即 Mirai-api-http API 通用接口中的内容。
        :rtype: Dict[str, Any]
        :exception NetworkError: 网络错误。
        :exception ActionFailed: API 操作失败。
        :exception ApiTimeout: API 请求响应超时。
        """

        def while_condition():
            return not self.bot.should_exit and (time.time() - start_time < self.config.api_timeout) and \
                   not self.api_response_error_code

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
        while while_condition():
            for index, resp in enumerate(self.api_response):
                if resp.get('syncId') == sync_id:
                    status_code = resp.get('data', {}).get('code', None)
                    if status_code is not None and status_code != 0:
                        raise ActionFailed(code=status_code, resp=resp)
                    return self.api_response.pop(index).get('data')
            self.wait_for_get_api_response = True
            while self.wait_for_get_api_response and while_condition():
                await asyncio.sleep(0)

        if self.api_response_error_code:
            temp = self.api_response_error_code
            self.api_response_error_code = 0
            raise ActionFailed(code=temp, resp=None)
        elif not self.bot.should_exit:
            raise ApiTimeout

    async def send(self,
                   message_: Union[str, Mapping, Iterable[Mapping], 'T_MiraiMessageSegment', 'T_MiraiMessage'],
                   message_type: Literal['private', 'friend', 'group'],
                   target: int,
                   quote: int = None) -> Dict[str, Any]:
        """
        调用 Mirai API 发送消息。

        :param message_: 消息内容，可以是 str, Mapping, Iterable[Mapping], 'T_MiraiMessageSegment', 'T_MiraiMessage'。
            将使用 ``MiraiMessage`` 进行封装。
        :param message_type: 消息类型。应该是 private, friend 或者 group。其中 private 和 friend 相同。
        :param target: 发送对象的 ID ，QQ 号码或者群号码。
        :param quote: 引用的消息的 messageId。默认为 ``None`` ，不引用任何消息。
        :return: API 响应。
        :rtype: Dict[str, Any]
        :exception TypeError: message_type 非法。
        :exception ...: 同 ``call_api()`` 方法。
        """
        if message_type == 'private' or message_type == 'friend':
            return await self.sendFriendMessage(target=target, messageChain=MiraiMessage(message_), quote=quote)
        elif message_type == 'group':
            return await self.sendGroupMessage(target=target, messageChain=MiraiMessage(message_), quote=quote)
        else:
            raise TypeError('message_type must be "private", "friend" or "group"')
