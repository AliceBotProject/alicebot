"""AliceBot 类型提示支持。

此模块定义了部分 AliceBot 使用的类型。
"""

from collections.abc import Awaitable, Callable
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from alicebot.adapter import Adapter
    from alicebot.bot import Bot
    from alicebot.event import Event
    from alicebot.plugin import Plugin

__all__ = [
    "AdapterHook",
    "AnyAdapter",
    "AnyEvent",
    "AnyPlugin",
    "BotHook",
    "EventHook",
]

type AnyEvent = Event[Any]
type AnyPlugin = Plugin[Any, Any, Any]
type AnyAdapter = Adapter[Any, Any]

type BotHook = Callable[[Bot], Awaitable[None]]
type AdapterHook = Callable[[AnyAdapter], Awaitable[None]]
type EventHook = Callable[[AnyEvent], Awaitable[None]]
