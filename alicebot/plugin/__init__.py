"""
======
插件
======
所有 AliceBot 插件的基类。所有用户编写的插件必须继承自 ``Plugin`` 类。
"""
from abc import ABC, abstractmethod
from typing import TypeVar, TYPE_CHECKING

from alicebot.exception import StopException, SkipException

if TYPE_CHECKING:
    from alicebot import Bot
    from alicebot.event import T_Event
    from alicebot.adapter import T_Adapter

T_Plugin = TypeVar('T_Plugin', bound='Plugin')


class Plugin(ABC):
    """
    所有 AliceBot 插件的基类。
    """
    event: 'T_Event'
    """
    当前正在被此插件处理的事件。
    """
    priority: int = 0
    """
    插件的优先级，数字越小表示优先级越高，默认为 0。
    """
    block: bool = False
    """
    插件执行结束后是否阻止事件的传播。``True`` 表示阻止。
    相当于在 ``handle()`` 方法最后调用 ``self.stop()`` 。
    """

    def __init__(self, event):
        self.event = event

        self.get = getattr(self.adapter, 'get', None)
        self.send = getattr(self.adapter, 'send', None)

        self.__post_init__()

    def __post_init__(self):
        """
        用于初始化后处理，被 ``__init__()`` 方法调用。
        """
        pass

    @property
    def name(self) -> str:
        """
        :return: 插件类名称。
        :rtype: str
        """
        return self.__class__.__name__

    @property
    def adapter(self) -> 'T_Adapter':
        """
        :return: 产生当前事件的适配器对象。
        :rtype: T_Adapter
        """
        return self.event.adapter

    @property
    def bot(self) -> 'Bot':
        """
        :return: 机器人对象。
        """
        return self.adapter.bot

    @property
    def config(self):
        """
        :return: 机器人配置。
        """
        return self.bot.config

    def stop(self):
        """
        停止当前事件传播。
        """
        raise StopException()

    def skip(self):
        """
        跳过自身继续当前事件传播。
        """
        raise SkipException()

    @abstractmethod
    async def handle(self) -> None:
        """
        处理事件的方法。当 ``rule()`` 方法返回 ``True`` 时 AliceBot 会调用此方法。每个插件必须实现此方法。
        """
        pass

    @abstractmethod
    async def rule(self) -> bool:
        """
        匹配事件的方法。事件处理时，会按照插件的优先级依次调用此方法，当此方法返回 ``True`` 时将事件交由此插件处理。每个插件必须实现此方法。
        注意：不建议直接在此方法内实现对事件的处理，事件的具体处理请交由 ``handle()`` 方法。

        :rtype: bool
        """
        pass
