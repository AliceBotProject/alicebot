"""CQHTTP 协议适配器。

本适配器适配了 OneBot v11 协议。
协议详情请参考: [OneBot](https://github.com/howmanybots/onebot/blob/master/README.md) 。
"""
import sys
import json
import time
import asyncio
from functools import partial
from typing import TYPE_CHECKING, Any, Dict, Literal

import aiohttp

from alicebot.utils import DataclassEncoder
from alicebot.adapter.utils import WebSocketAdapter
from alicebot.log import logger, error_or_exception

from .config import Config
from .message import CQHTTPMessage
from .event import CQHTTPEvent, get_event_class
from .exceptions import ApiTimeout, ActionFailed, NetworkError, ApiNotAvailable

if TYPE_CHECKING:
    from .message import T_CQMSG

__all__ = ["CQHTTPAdapter"]


class CQHTTPAdapter(WebSocketAdapter[CQHTTPEvent, Config]):
    """CQHTTP 协议适配器。"""

    name = "cqhttp"
    Config = Config

    _api_response: Dict[Any, Any]
    _api_response_cond: asyncio.Condition = None
    _api_id: int = 0

    def __getattr__(self, item):
        return partial(self.call_api, item)

    async def startup(self):
        """初始化适配器。"""
        self.adapter_type = self.config.adapter_type
        if self.adapter_type == "ws-reverse":
            self.adapter_type = "reverse-ws"
        self.host = self.config.host
        self.port = self.config.port
        self.url = self.config.url
        self.reconnect_interval = self.config.reconnect_interval
        self._api_response_cond = asyncio.Condition()
        await super().startup()

    async def reverse_ws_connection_hook(self):
        """反向 WebSocket 连接建立时的钩子函数。"""
        logger.info(f"WebSocket connected!")
        if self.config.access_token:
            if (
                self.websocket.headers.get("Authorization", "")
                != f"Bearer {self.config.access_token}"
            ):
                await self.websocket.close()

    async def websocket_connect(self):
        """创建正向 WebSocket 连接。"""
        logger.info("Tying to connect to WebSocket server...")
        async with self.session.ws_connect(
            f"ws://{self.host}:{self.port}/",
            headers={"Authorization": f"Bearer {self.config.access_token}"}
            if self.config.access_token
            else None,
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

            if "post_type" in msg_dict:
                await self.handle_cqhttp_event(msg_dict)
            else:
                async with self._api_response_cond:
                    self._api_response = msg_dict
                    self._api_response_cond.notify_all()

        elif msg.type == aiohttp.WSMsgType.ERROR:
            logger.error(
                f"WebSocket connection closed "
                f"with exception {self.websocket.exception()!r}"
            )

    def _get_api_echo(self) -> int:
        self._api_id = (self._api_id + 1) % sys.maxsize
        return self._api_id

    async def handle_cqhttp_event(self, msg: Dict[str, Any]):
        """处理 CQHTTP 事件。

        Args:
            msg: 接收到的信息。
        """
        post_type = msg.get("post_type")
        event_type = msg.get(post_type + "_type")
        sub_type = msg.get("sub_type", None)
        event_class = get_event_class(post_type, event_type, sub_type)

        cqhttp_event = event_class(adapter=self, **msg)

        if cqhttp_event.post_type == "meta_event":
            # meta_event 不交由插件处理
            if (
                cqhttp_event.meta_event_type == "lifecycle"
                and cqhttp_event.sub_type == "connect"
            ):
                logger.info(
                    f"WebSocket connection "
                    f"from CQHTTP Bot {msg.get('self_id')} accepted!"
                )
            elif cqhttp_event.meta_event_type == "heartbeat":
                if cqhttp_event.status.good and cqhttp_event.status.online:
                    pass
                else:
                    logger.error(
                        f"CQHTTP Bot status is not good: {cqhttp_event.status.dict()}"
                    )
        else:
            await self.handle_event(cqhttp_event)

    async def call_api(self, api: str, **params) -> Any:
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
            await self.websocket.send_str(
                json.dumps(
                    {"action": api, "params": params, "echo": api_echo},
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
                if self._api_response["echo"] == api_echo:
                    if self._api_response.get("retcode") == 1404:
                        raise ApiNotAvailable(resp=self._api_response)
                    if self._api_response.get("status") == "failed":
                        raise ActionFailed(resp=self._api_response)
                    return self._api_response.get("data")

        if not self.bot.should_exit.is_set():
            raise ApiTimeout

    async def send(
        self, message_: "T_CQMSG", message_type: Literal["private", "group"], id_: int
    ) -> Dict[str, Any]:
        """发送消息，调用 send_private_msg 或 send_group_msg API 发送消息。

        Args:
            message_: 消息内容，可以是 str, Mapping, Iterable[Mapping],
                'CQHTTPMessageSegment', 'CQHTTPMessage'。
                将使用 `CQHTTPMessage` 进行封装。
            message_type: 消息类型。应该是 private 或者 group。
            id_: 发送对象的 ID ，QQ 号码或者群号码。

        Returns:
            API 响应。

        Raises:
            TypeError: message_type 不是 'private' 或 'group'。
            ...: 同 `call_api()` 方法。
        """
        if message_type == "private":
            return await self.send_private_msg(
                user_id=id_, message=CQHTTPMessage(message_)
            )
        elif message_type == "group":
            return await self.send_group_msg(
                group_id=id_, message=CQHTTPMessage(message_)
            )
        else:
            raise TypeError('message_type must be "private" or "group"')
