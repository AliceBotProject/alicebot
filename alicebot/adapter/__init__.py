"""
============
协议适配器
============
所有协议适配器都必须继承自 ``AbstractAdapter`` 基类。
"""
import time
import asyncio
from functools import wraps
from abc import ABC, abstractmethod
from typing import Awaitable, Callable, TypeVar, Union, Optional, TYPE_CHECKING

from alicebot.log import logger
from alicebot.exception import AdapterTimeout

if TYPE_CHECKING:
    from alicebot import Bot
    from alicebot.event import T_Event

T_Adapter = TypeVar('T_Adapter', bound='AbstractAdapter')


class EventQueue:
    """
    事件队列。
    使用限定长度的链队列。
    """
    def __init__(self, max_len=None):
        self._head: ['T_Event'] = None
        self._rear: ['T_Event'] = None
        self._len: int = 0

        self.max_len = max_len

    def __len__(self):
        return self._len

    def push(self, event: 'T_Event') -> None:
        if self._head is None:
            self._head = event
            self._rear = event
            self._len = 1
            return
        self._rear.next_event = event
        self._rear = event
        self._len += 1
        while self._len > self.max_len:
            self.pop()

    def pop(self):
        if self._head is None:
            raise ValueError('EventQueue is empty.')
        temp = self._head
        self._head = self._head.next_event
        temp.next_event = None
        if self._head is None:
            self._rear = None
        self._len -= 1
        return temp

    def top(self) -> ['T_Event']:
        return self._head

    def append(self, obj: 'T_Event'):
        self.push(obj)

    def clear(self):
        self._head = None
        self._rear = None
        self._len = None

    def index(self, obj: 'T_Event', start=None, end=None):
        for index, item in enumerate(self):
            if item == obj and (start is None or start <= index) and (end is None or index <= end):
                return index
        raise ValueError(f'{obj} is not in EventQueue')

    def __contains__(self, item):
        try:
            self.index(item)
        except ValueError:
            return False
        else:
            return True

    def __iter__(self):
        point = self._head
        while point.next_event is not None:
            yield point
            point = point.next_event
        yield point


class AbstractAdapter(ABC):
    """
    协议适配器基类。
    """
    name: str
    """
    适配器的名称。
    """
    bot: 'Bot'
    """
    当前的机器人对象。
    """
    event_queue: EventQueue
    """
    事件队列，用于 ``get()`` 方法。
    """
    max_event_queue_len: int = 1024
    """
    最大事件队列长度。
    """
    wait_for_get: bool = False
    """
    当此属性为 ``Ture`` 时，``handle_event()`` 将不对当前事件进行传播和处理，用于 ``get()`` 方法。
    """

    def __init__(self, bot: 'Bot'):
        self.event_queue = EventQueue(max_len=self.max_event_queue_len)
        self.bot: 'Bot' = bot

    async def safe_run(self):
        """
        附带有异常处理地安全运行适配器。
        """
        try:
            await self.run()
        except Exception as e:
            logger.error(f'Run adapter {self.__class__.__name__} failed: {e!r}')

    @abstractmethod
    async def run(self):
        """
        适配器运行方法，适配器开发者必须实现该方法。
        适配器运行过程中保持保持运行，当此方法结束后，AliceBot 不会自动重新启动适配器。
        """
        pass

    async def startup(self):
        """
        在适配器开始运行前运行的方法。
        AliceBot 依次运行并等待所有适配器的 ``startup()`` 方法，待运行完毕后再创建 ``run()`` 任务。
        """
        pass

    async def shutdown(self):
        """
        在适配器结束后运行后运行的方法。
        AliceBot 在接收到系统的结束信号后依次运行并等待所有适配器的 ``shutdown()`` 方法。当强制退出时此方法可能未被执行。
        """
        pass

    def handle_event(self, event: 'T_Event'):
        """
        调用 ``Bot`` 对象进行事件处理，并维护一个事件队列用于 ``get()`` 方法，所有适配器在接收到事件后必须使用此方法进行事件处理。
        :param event: 待处理的事件。
        """
        logger.info(f'Adapter {self.__class__.__name__} received: {event!r}')
        self.event_queue.push(event)
        if self.wait_for_get:
            self.wait_for_get = False
        else:
            event.handled = True
            self.bot.loop.create_task(self.bot.handle_event(event))

    async def get(self, current_event: 'T_Event',
                  func: Optional[Callable[['T_Event'], Union[bool, Awaitable[bool]]]] = None,
                  max_try_times: Optional[int] = None,
                  timeout: Optional[Union[int, float]] = None) -> 'T_Event':
        """
        获取满足指定条件的的事件，协程会等待直到适配器接收到满足条件的事件、超过最大事件数或超时。

        :param current_event: 当前事件，方法将仅检索此事件后接收到的事件。
        :param func: (optional) 协程或者函数，函数会被自动包装为协程执行。要求接受一个事件作为参数，返回布尔值。当协程返回 ``True`` 时返回当前事件。
            当为 ``None`` 时相当于输入对于任何事件均返回真的协程，即返回适配器接收到的下一个事件。
        :param max_try_times: 最大事件数。
        :param timeout: 超时。
        :return: 返回满足 func 条件的事件。
        :rtype: 'T_Event'
        :exception AdapterTimeout: 超过最大事件数或超时。
        """

        async def always_true(_):
            return True

        def async_wrapper(_func):
            @wraps(_func)
            async def _wrapper(*args, **kwargs):
                return _func(*args, **kwargs)

            return _wrapper

        def while_condition():
            return not self.bot.should_exit and (max_try_times is None or (try_times < max_try_times)) and (
                    timeout is None or (time.time() - start_time < timeout))

        if func is None:
            func = always_true
        elif not asyncio.iscoroutinefunction(func):
            func = async_wrapper(func)

        try_times = 0
        start_time = time.time()
        event = current_event
        while while_condition():
            while event.next_event is not None:
                event = event.next_event
                if not event.handled:
                    if await func(event):
                        event.handled = True
                        return event
                    else:
                        self.handle_event(event)
            self.wait_for_get = True
            while self.wait_for_get and while_condition():
                await asyncio.sleep(0)
            try_times += 1

        self.wait_for_get = False
        if not self.bot.should_exit:
            raise AdapterTimeout
