"""Mirai 协议适配器。

本适配器适配了 mirai-api-http 协议，仅支持 mirai-api-http 2.3.0 及以上版本。
本适配器支持 mirai-api-http 的 Websocket Adapter 模式和 Reverse Websocket Adapter 模式。
协议详情请参考: [mirai-api-http](https://github.com/project-mirai/mirai-api-http) 。
"""
import sys
import json
import time
import asyncio
from functools import partial
from typing import TYPE_CHECKING, Any, Dict, Literal, Optional

import aiohttp

from alicebot.utils import DataclassEncoder
from alicebot.adapter.utils import WebSocketAdapter
from alicebot.log import logger, error_or_exception

from .config import Config
from .message import MiraiMessage
from .exceptions import ApiTimeout, ActionFailed, NetworkError
from .event import (
    BotEvent,
    MateEvent,
    MiraiEvent,
    CommandExecutedEvent,
    get_event_class,
)

if TYPE_CHECKING:
    from .message import T_MiraiMSG

__all__ = ["MiraiAdapter"]


class MiraiAdapter(WebSocketAdapter[MiraiEvent, Config]):
    """Mirai 协议适配器。

    在插件中可以直接使用 `self.adapter.xxx_api(**params)` 调用名称为 `xxx_api` 的 API，
    和调用 `call_api()` 方法相同。
    """

    name: str = "mirai"
    Config = Config

    _api_response: Any
    _api_response_cond: asyncio.Condition = None
    _sync_id: int = 0

    def __getattr__(self, item):
        return partial(self.call_api, item)

    async def startup(self):
        """初始化适配器。"""
        self.adapter_type = self.config.adapter_type
        self.host = self.config.host
        self.port = self.config.port
        self.url = self.config.url
        self.reconnect_interval = self.config.reconnect_interval
        self._api_response_cond = asyncio.Condition()
        await super().startup()

    async def reverse_ws_connection_hook(self):
        """反向 WebSocket 连接建立时的钩子函数。"""
        logger.info(f"WebSocket connected!")
        asyncio.create_task(self.verify_identity())

    async def websocket_connect(self):
        """创建正向 WebSocket 连接。"""
        logger.info("Trying to verify identity and create connection...")
        async with self.session.ws_connect(
            f"ws://{self.host}:{self.port}/all?"
            f"verifyKey={self.config.verify_key}&qq={self.config.qq}"
        ) as self.websocket:
            await self.handle_websocket()

    async def handle_websocket_msg(self, msg: aiohttp.WSMessage):
        """处理 WebSocket 消息。"""
        if msg.type == aiohttp.WSMsgType.TEXT:
            try:
                msg_dict = msg.json()
            except json.JSONDecodeError as e:
                error_or_exception(
                    "WebSocket message parsing error, not json:",
                    e,
                    self.bot.config.bot.log.verbose_exception,
                )
                return

            if msg_dict.get("syncId") == "":
                if msg_dict.get("data", {}).get("code") == 0:
                    logger.info(
                        f"Verify success! "
                        f"Session key: {msg_dict.get('data').get('session')}"
                    )
                else:
                    logger.warning(
                        f"Verify failed with code {msg_dict.get('code') or msg_dict}, "
                        f"retrying..."
                    )
                    await asyncio.sleep(self.reconnect_interval)
            elif msg_dict.get("syncId") == "-1":
                await self.handle_mirai_event(msg_dict.get("data"))
            else:
                async with self._api_response_cond:
                    self._api_response = msg_dict
                    self._api_response_cond.notify_all()

        elif msg.type == aiohttp.WSMsgType.ERROR:
            logger.error(
                f"WebSocket connection closed "
                f"with exception {self.websocket.exception()!r}"
            )

    def _get_sync_id(self) -> int:
        self._sync_id = (self._sync_id + 1) % sys.maxsize
        return self._sync_id

    async def handle_mirai_event(self, msg: Dict[str, Any]):
        """处理 Mirai 事件。

        Args:
            msg: 接收到的信息。
        """
        mirai_event = get_event_class(msg.get("type"))(adapter=self, **msg)

        if isinstance(mirai_event, MateEvent):
            # meta_event 不交由插件处理
            if isinstance(mirai_event, BotEvent):
                logger.info(f"Bot {mirai_event.qq}: {mirai_event.type}")
            elif isinstance(mirai_event, CommandExecutedEvent):
                logger.info(
                    f'Command "{mirai_event.name}" was executed: {mirai_event!r}'
                )
        else:
            await self.handle_event(mirai_event)

    async def verify_identity(self):
        """验证身份，创建与 Mirai-api-http 的连接。"""
        while not self.bot.should_exit.is_set():
            await asyncio.sleep(self.reconnect_interval)
            try:
                logger.info("Trying to verify identity and create connection...")
                await self.call_api(
                    "verify",
                    **{
                        "verifyKey": self.config.verify_key,
                        "sessionKey": None,
                        "qq": self.config.qq,
                    },
                )
            except ActionFailed as e:
                logger.warning(f"Verify failed with code {e.code}, retrying...")
            else:
                logger.info("Verify success!")
                return

    async def call_api(
        self, command: str, sub_command: Optional[str] = None, **content
    ) -> Dict[str, Any]:
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
        sync_id = str(self._get_sync_id())
        try:
            await self.websocket.send_str(
                json.dumps(
                    {
                        "syncId": sync_id,
                        "command": command,
                        "subCommand": sub_command,
                        "content": content,
                    },
                    cls=DataclassEncoder,
                )
            )
        except Exception:
            raise NetworkError

        start_time = time.time()
        while not self.bot.should_exit.is_set():
            if time.time() - start_time > self.config.api_timeout:
                break
            async with self._api_response_cond:
                try:
                    await asyncio.wait_for(
                        self._api_response_cond.wait(),
                        timeout=start_time + self.config.api_timeout - time.time(),
                    )
                except asyncio.TimeoutError:
                    break
                if self._api_response.get("syncId") == sync_id:
                    status_code = self._api_response.get("data", {}).get("code")
                    if status_code is not None and status_code != 0:
                        raise ActionFailed(code=status_code, resp=self._api_response)
                    return self._api_response.get("data")

        if not self.bot.should_exit.is_set():
            raise ApiTimeout

    async def send(
        self,
        message_: "T_MiraiMSG",
        message_type: Literal["private", "friend", "group"],
        target: int,
        quote: int = None,
    ) -> Any:
        """调用 Mirai API 发送消息。

        Args:
            message_: 消息内容，可以是 str, Mapping, Iterable[Mapping],
                'MiraiMessageSegment', 'MiraiMessage'。
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
        if message_type == "private" or message_type == "friend":
            return await self.sendFriendMessage(
                target=target, messageChain=MiraiMessage(message_), quote=quote
            )
        elif message_type == "group":
            return await self.sendGroupMessage(
                target=target, messageChain=MiraiMessage(message_), quote=quote
            )
        else:
            raise TypeError('message_type must be "private", "friend" or "group"')
