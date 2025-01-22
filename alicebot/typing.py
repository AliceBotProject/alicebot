"""AliceBot 类型提示支持。

此模块定义了部分 AliceBot 使用的类型。
"""

# ruff: noqa: A005

from collections.abc import Awaitable
from typing import TYPE_CHECKING, Callable, Optional
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

EventT = TypeVar("EventT", bound="Event[Any]", default="Event[Any]")
StateT = TypeVar("StateT", default=None)
ConfigT = TypeVar("ConfigT", bound=Optional["ConfigModel"], default=None)
PluginT = TypeVar("PluginT", bound="Plugin[Any, Any, Any]")
AdapterT = TypeVar("AdapterT", bound="Adapter[Any, Any]")

BotHook = Callable[["Bot"], Awaitable[None]]
AdapterHook = Callable[["Adapter[Any, Any]"], Awaitable[None]]
EventHook = Callable[["Event[Any]"], Awaitable[None]]
