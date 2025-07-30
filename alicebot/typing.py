"""AliceBot 类型提示支持。

此模块定义了部分 AliceBot 使用的类型。
"""

from collections.abc import Awaitable, Callable
from typing import TYPE_CHECKING, TypeAlias
from typing_extensions import TypeVar

from alicebot.message import BuildMessageType, MessageSegmentT, MessageT

if TYPE_CHECKING:
    from typing import Any

    from alicebot.adapter import Adapter
    from alicebot.bot import Bot
    from alicebot.config import ConfigModel
    from alicebot.event import Event
    from alicebot.plugin import Plugin

__all__ = [
    "AdapterHook",
    "AdapterT",
    "AnyAdapter",
    "AnyEvent",
    "AnyPlugin",
    "BotHook",
    "BuildMessageType",
    "ConfigT",
    "EventHook",
    "EventT",
    "MessageSegmentT",
    "MessageT",
    "PluginT",
    "StateT",
]

AnyEvent: TypeAlias = "Event[Any]"
AnyPlugin: TypeAlias = "Plugin[Any, Any, Any]"
AnyAdapter: TypeAlias = "Adapter[Any, Any]"

EventT = TypeVar("EventT", bound=AnyEvent, default=AnyEvent)
StateT = TypeVar("StateT", default=None)
ConfigT = TypeVar("ConfigT", bound="ConfigModel | None", default=None)
PluginT = TypeVar("PluginT", bound=AnyPlugin)
AdapterT = TypeVar("AdapterT", bound=AnyAdapter)

BotHook: TypeAlias = Callable[["Bot"], Awaitable[None]]
AdapterHook: TypeAlias = Callable[[AnyAdapter], Awaitable[None]]
EventHook: TypeAlias = Callable[[AnyEvent], Awaitable[None]]
