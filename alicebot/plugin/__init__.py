"""
======
插件
======
所有 AliceBot 插件的基类。所有用户编写的插件必须继承自 ``Plugin`` 类。
"""
from abc import ABC, abstractmethod
from typing import Awaitable, Callable, TypeVar, Union, Optional, TYPE_CHECKING

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

    async def send(self, *args, **kwargs):
        """
        发送消息，具体实现和参数取决于适配器。
        """
        return await self.adapter.send(*args, **kwargs)

    async def get(self,
                  func: Optional[Callable[['T_Event'], Union[bool, Awaitable[bool]]]] = None,
                  max_try_times: int = None,
                  timeout: Optional[Union[int, float]] = None) -> Optional['T_Event']:
        """
        获取满足指定条件的的事件，协程会等待直到适配器接收到满足条件的事件、超过最大事件数或超时。
        当适配器接收到超过最大消息数的事件后仍未满足 func 的条件时，返回 ``None`` 。

        :param func: (optional) 协程或者函数，函数会被自动包装为协程执行。要求接受一个事件作为参数，返回布尔值。当协程返回 ``True`` 时返回当前事件。
            当为 ``None`` 时相当于输入对于任何事件均返回真的协程，即返回适配器接收到的下一个事件。
        :param max_try_times: 最大事件数。
        :param timeout: 超时。
        :return: 返回满足 func 条件的事件。
        :rtype: Optional['T_Event']
        """
        return await self.adapter.get(self.event, func, max_try_times, timeout)

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
