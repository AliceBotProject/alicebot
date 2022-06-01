"""AliceBot 插件。

所有 AliceBot 插件的基类。所有用户编写的插件必须继承自 `Plugin` 类。
"""
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Generic, NoReturn

from alicebot.typing import T_Event, T_State
from alicebot.exceptions import SkipException, StopException

if TYPE_CHECKING:
    from alicebot import Bot
    from alicebot.config import MainConfig

__all__ = ["Plugin"]


class Plugin(ABC, Generic[T_Event, T_State]):
    """所有 AliceBot 插件的基类。

    Attributes:
        event: 当前正在被此插件处理的事件。
        priority: 插件的优先级，数字越小表示优先级越高，默认为 0。
        block: 插件执行结束后是否阻止事件的传播。True 表示阻止。
    """

    event: T_Event
    priority: int = 0
    block: bool = False

    def __init__(self, event: T_Event):
        self.event = event

        if not hasattr(self, "priority"):
            self.priority = 0
        if not hasattr(self, "priority"):
            self.block = False

        self.get = self.bot.get

        self.__post_init__()

    def __post_init__(self):
        """用于初始化后处理，被 `__init__()` 方法调用。"""
        pass

    @property
    def name(self) -> str:
        """插件类名称。"""
        return self.__class__.__name__

    @property
    def bot(self) -> "Bot":
        """机器人对象。"""
        return self.event.adapter.bot

    @property
    def config(self) -> "MainConfig":
        """机器人配置。"""
        return self.bot.config

    def stop(self) -> NoReturn:
        """停止当前事件传播。"""
        raise StopException()

    def skip(self) -> NoReturn:
        """跳过自身继续当前事件传播。"""
        raise SkipException()

    @property
    def state(self) -> T_State:
        """插件状态。"""
        return self.bot.plugin_state[self.__class__]

    @state.setter
    def state(self, value: T_State):
        self.bot.plugin_state[self.__class__] = value

    @abstractmethod
    async def handle(self) -> None:
        """处理事件的方法。当 `rule()` 方法返回 `True` 时 AliceBot 会调用此方法。每个插件必须实现此方法。"""
        raise NotImplementedError

    @abstractmethod
    async def rule(self) -> bool:
        """匹配事件的方法。事件处理时，会按照插件的优先级依次调用此方法，当此方法返回 `True` 时将事件交由此插件处理。每个插件必须实现此方法。

        注意：不建议直接在此方法内实现对事件的处理，事件的具体处理请交由 `handle()` 方法。
        """
        raise NotImplementedError
