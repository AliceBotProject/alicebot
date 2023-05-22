"""AliceBot 类型提示支持。

此模块定义了部分 AliceBot 使用的类型。
"""

from typing import TYPE_CHECKING, Any, TypeVar, Callable, Optional, Awaitable

from alicebot.message import T_MS, T_Message, T_MessageSegment

if TYPE_CHECKING:
    from alicebot.bot import Bot
    from alicebot.event import Event
    from alicebot.plugin import Plugin
    from alicebot.adapter import Adapter
    from alicebot.config import ConfigModel

__all__ = [
    "T_State",
    "T_Event",
    "T_Plugin",
    "T_Adapter",
    "T_Config",
    "T_Message",
    "T_MessageSegment",
    "T_MS",
    "T_BotHook",
    "T_AdapterHook",
    "T_EventHook",
]

T_State = TypeVar("T_State")
T_Event = TypeVar("T_Event", bound="Event[Any]")
T_Plugin = TypeVar("T_Plugin", bound="Plugin[Any, Any, Any]")
T_Adapter = TypeVar("T_Adapter", bound="Adapter[Any, Any]")
T_Config = TypeVar("T_Config", bound=Optional["ConfigModel"])

T_BotHook = Callable[["Bot"], Awaitable[None]]
T_AdapterHook = Callable[["Adapter[Any, Any]"], Awaitable[None]]
T_EventHook = Callable[["Event[Any]"], Awaitable[None]]
