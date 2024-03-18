"""AliceBot 类型提示支持。

此模块定义了部分 AliceBot 使用的类型。
"""

from typing import TYPE_CHECKING, Awaitable, Callable, Optional, TypeVar

from alicebot.message import BuildMessageType, MessageSegmentT, MessageT

if TYPE_CHECKING:
    from typing import Any

    from alicebot.adapter import Adapter
    from alicebot.bot import Bot
    from alicebot.config import ConfigModel
    from alicebot.event import Event
    from alicebot.plugin import Plugin

__all__ = [
    "StateT",
    "EventT",
    "PluginT",
    "AdapterT",
    "ConfigT",
    "MessageT",
    "MessageSegmentT",
    "BuildMessageType",
    "BotHook",
    "AdapterHook",
    "EventHook",
]

StateT = TypeVar("StateT")
EventT = TypeVar("EventT", bound="Event[Any]")
PluginT = TypeVar("PluginT", bound="Plugin[Any, Any, Any]")
AdapterT = TypeVar("AdapterT", bound="Adapter[Any, Any]")
ConfigT = TypeVar("ConfigT", bound=Optional["ConfigModel"])

BotHook = Callable[["Bot"], Awaitable[None]]
AdapterHook = Callable[["Adapter[Any, Any]"], Awaitable[None]]
EventHook = Callable[["Event[Any]"], Awaitable[None]]
