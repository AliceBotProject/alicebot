"""AliceBot 插件。

所有 AliceBot 插件的基类。所有用户编写的插件必须继承自 `Plugin` 类。
"""
from enum import Enum
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Type, Generic, NoReturn, Optional

from alicebot.config import ConfigModel
from alicebot.utils import is_config_class
from alicebot.typing import T_Event, T_State, T_Config
from alicebot.exceptions import SkipException, StopException

if TYPE_CHECKING:
    from alicebot.bot import Bot

__all__ = ["Plugin", "PluginLoadType"]


class PluginLoadType(Enum):
    """插件加载类型。"""

    DIR = "dir"
    NAME = "name"
    FILE = "file"
    CLASS = "class"


class Plugin(ABC, Generic[T_Event, T_State, T_Config]):
    """所有 AliceBot 插件的基类。

    Attributes:
        event: 当前正在被此插件处理的事件。
        priority: 插件的优先级，数字越小表示优先级越高，默认为 0。
        block: 插件执行结束后是否阻止事件的传播。True 表示阻止。
        __plugin_load_type__: 插件加载类型，由 AliceBot 自动设置，反映了此插件是如何被加载的。
        __plugin_file_path__: 当插件加载类型为 `PluginLoadType.CLASS` 时为 `None`，
            否则为定义插件在的 Python 模块的位置。
    """

    event: T_Event
    priority: int = 0
    block: bool = False
    Config: Type[ConfigModel]

    __plugin_load_type__: PluginLoadType
    __plugin_file_path__: Optional[str]

    def __init__(self, event: T_Event):
        self.event = event

        if not hasattr(self, "priority"):
            self.priority = 0
        if not hasattr(self, "block"):
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
    def config(self) -> Optional[T_Config]:
        """插件配置。"""
        config_class: ConfigModel = getattr(self, "Config", None)
        if is_config_class(config_class):
            return getattr(self.bot.config.plugin, config_class.__config_name__, None)
        return None

    def stop(self) -> NoReturn:
        """停止当前事件传播。"""
        raise StopException()

    def skip(self) -> NoReturn:
        """跳过自身继续当前事件传播。"""
        raise SkipException()

    @property
    def state(self) -> T_State:
        """插件状态。"""
        return self.bot.plugin_state[self.name]

    @state.setter
    def state(self, value: T_State):
        self.bot.plugin_state[self.name] = value

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
