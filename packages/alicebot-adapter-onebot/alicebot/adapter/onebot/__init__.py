"""OneBot 协议适配器。

本适配器适配了 OneBot v12 协议。
协议详情请参考：[OneBot](https://12.onebot.dev/)。
"""

import asyncio
import inspect
import json
import sys
import time
from functools import partial
from typing import (
    Any,
    Awaitable,
    Callable,
    ClassVar,
    Dict,
    Literal,
    Optional,
    Tuple,
    Type,
    Union,
)

import aiohttp
import structlog
from aiohttp import web

from alicebot.adapter.utils import WebSocketAdapter
from alicebot.message import BuildMessageType
from alicebot.utils import PydanticEncoder

from . import event
from .config import Config
from .event import (
    BotSelf,
    ConnectMetaEvent,
    HeartbeatMetaEvent,
    MetaEvent,
    OntBotEvent,
    StatusUpdateMetaEvent,
)
from .exceptions import ActionFailed, ApiTimeout, NetworkError
from .message import OneBotMessage, OneBotMessageSegment

__all__ = ["OneBotAdapter"]

logger = structlog.stdlib.get_logger()

EventModels = Dict[
    Tuple[Optional[str], Optional[str], Optional[str]], Type[OntBotEvent]
]

DEFAULT_EVENT_MODELS: EventModels = {}
for _, model in inspect.getmembers(event, inspect.isclass):
    if issubclass(model, OntBotEvent):
        DEFAULT_EVENT_MODELS[model.get_event_type()] = model


class OneBotAdapter(WebSocketAdapter[OntBotEvent, Config]):
    """OneBot 协议适配器。"""

    name = "onebot"
    Config = Config

    event_models: ClassVar[EventModels] = DEFAULT_EVENT_MODELS

    _api_response: Dict[str, Any]
    _api_response_cond: asyncio.Condition
    _api_id: int = 0

    def __getattr__(self, item: str) -> Callable[..., Awaitable[Any]]:
        """用于调用 API。可以直接通过访问适配器的属性访问对应名称的 API。

        Args:
            item: API 名称。

        Returns:
            用于调用 API 的函数。
        """
        return partial(self.call_api, item)

    async def startup(self) -> None:
        """初始化适配器。"""
        adapter_type = self.config.adapter_type
        if adapter_type == "ws-reverse":
            adapter_type = "reverse-ws"
        self.adapter_type = adapter_type
        self.host = self.config.host
        self.port = self.config.port
        self.url = self.config.url
        self.reconnect_interval = self.config.reconnect_interval
        self._api_response_cond = asyncio.Condition()
        await super().startup()

    async def reverse_ws_connection_hook(self) -> None:
        """反向 WebSocket 连接建立时的钩子函数。"""
        logger.info("WebSocket connected!")
        if self.config.access_token:
            assert isinstance(self.websocket, web.WebSocketResponse)
            if (
                self.websocket.headers.get("Authorization", "")
                != f"Bearer {self.config.access_token}"
            ):
                await self.websocket.close()

    async def websocket_connect(self) -> None:
        """创建正向 WebSocket 连接。"""
        assert self.session is not None
        logger.info("Tying to connect to WebSocket server...")
        async with self.session.ws_connect(
            f"ws://{self.host}:{self.port}/",
            headers={"Authorization": f"Bearer {self.config.access_token}"}
            if self.config.access_token
            else None,
        ) as self.websocket:
            await self.handle_websocket()

    async def handle_websocket_msg(self, msg: aiohttp.WSMessage) -> None:
        """处理 WebSocket 消息。"""
        assert self.websocket is not None
        if msg.type == aiohttp.WSMsgType.TEXT:
            try:
                msg_dict = msg.json()
            except json.JSONDecodeError:
                logger.exception("WebSocket message parsing error, not json")
                return

            if "post_type" in msg_dict:
                await self.handle_onebot_event(msg_dict)
            else:
                async with self._api_response_cond:
                    self._api_response = msg_dict
                    self._api_response_cond.notify_all()

        elif msg.type == aiohttp.WSMsgType.ERROR:
            logger.error(
                "WebSocket connection closed with exception",
                exception=self.websocket.exception(),
            )

    def _get_api_echo(self) -> int:
        self._api_id = (self._api_id + 1) % sys.maxsize
        return self._api_id

    @classmethod
    def add_event_model(cls, event_model: Type[OntBotEvent]) -> None:
        """添加自定义事件模型，事件模型类必须继承于 `OntBotEvent`。

        Args:
            event_model: 事件模型类。
        """
        cls.event_models[event_model.get_event_type()] = event_model

    @classmethod
    def get_event_model(
        cls,
        post_type: Optional[str],
        detail_type: Optional[str],
        sub_type: Optional[str],
    ) -> Type[OntBotEvent]:
        """根据接收到的消息类型返回对应的事件类。

        Args:
            post_type: 请求类型。
            detail_type: 事件类型。
            sub_type: 子类型。

        Returns:
            对应的事件类。
        """
        event_model = (
            cls.event_models.get((post_type, detail_type, sub_type))
            or cls.event_models.get((post_type, detail_type, None))
            or cls.event_models.get((post_type, None, None))
        )
        return event_model or cls.event_models[(None, None, None)]

    async def handle_onebot_event(self, msg: Dict[str, Any]) -> None:
        """处理 OneBot 事件。

        Args:
            msg: 接收到的信息。
        """
        post_type = msg.get("post_type")
        if post_type is None:
            event_class = self.get_event_model(None, None, None)
        else:
            event_class = self.get_event_model(
                post_type,
                msg.get(post_type + "_type"),
                msg.get("sub_type"),
            )

        onebot_event = event_class(adapter=self, **msg)

        if onebot_event.type == "meta":
            # meta_event 不交由插件处理
            assert isinstance(onebot_event, MetaEvent)
            if onebot_event.detail_type == "connect":
                assert isinstance(onebot_event, ConnectMetaEvent)
                logger.info(
                    "WebSocket connection from OneBot accepted!",
                    id=msg.get("self_id"),
                )
            elif onebot_event.detail_type == "heartbeat":
                assert isinstance(onebot_event, HeartbeatMetaEvent)

            elif onebot_event.detail_type == "status_update":
                assert isinstance(onebot_event, StatusUpdateMetaEvent)
                logger.info("OneBot status update", status=onebot_event.status)
        else:
            await self.handle_event(onebot_event)

    async def call_api(self, api: str, bot_self: BotSelf, **params: Any) -> Any:
        """调用 OneBot API，协程会等待直到获得 API 响应。

        Args:
            api: API 名称。
            bot_self: `Self` 字段。
            **params: API 参数。

        Returns:
            API 响应中的 data 字段。

        Raises:
            NetworkError: 网络错误。
            ApiNotAvailable: API 请求响应 404， API 不可用。
            ActionFailed: API 请求响应 failed， API 操作失败。
            ApiTimeout: API 请求响应超时。
        """
        assert self.websocket is not None
        api_echo = self._get_api_echo()
        try:
            await self.websocket.send_str(
                json.dumps(
                    {
                        "action": api,
                        "params": params,
                        "echo": api_echo,
                        "self": bot_self.model_dump(),
                    },
                    cls=PydanticEncoder,
                )
            )
        except Exception as e:
            raise NetworkError from e

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
                    if (
                        self._api_response.get("retcode") != 0
                        or self._api_response.get("status") == "failed"
                    ):
                        raise ActionFailed(resp=self._api_response)
                    return self._api_response.get("data")

        if not self.bot.should_exit.is_set():
            raise ApiTimeout
        return None

    async def send(
        self,
        message_: BuildMessageType[OneBotMessageSegment],
        message_type: Union[Literal["private", "group"], str],  # noqa: PYI051
        id_: str,
    ) -> Any:
        """发送消息，调用 `send_message` API 发送消息。

        Args:
            message_: 消息内容，可以是 `str`, `Mapping`, `Iterable[Mapping]`,
                `OneBotMessageSegment`, `OneBotMessage`。
                将使用 `OneBotMessage` 进行封装。
            message_type: 消息类型。
                可以为 "private", "group" 或扩展的类型，和消息事件的 `detail_type` 字段对应。
            id_: 发送对象的 ID， QQ 号码或者群号码。

        Returns:
            API 响应。

        Raises:
            TypeError: message_type 不是 "private" 或 "group"。
            ...: 同 `call_api()` 方法。
        """
        if message_type == "private":
            return await self.send_message(
                detail_type=message_type, user_id=id_, message=OneBotMessage(message_)
            )
        if message_type == "group":
            return await self.send_message(
                detail_type=message_type, group_id=id_, message=OneBotMessage(message_)
            )
        raise TypeError('message_type must be "private" or "group"')
