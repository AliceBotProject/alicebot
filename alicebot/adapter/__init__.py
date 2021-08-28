"""
============
协议适配器
============
所有协议适配器都必须继承自 ``Adapter`` 基类。
"""
import os
import time
import asyncio
from functools import wraps
from abc import ABC, abstractmethod
from typing import Awaitable, Callable, TypeVar, Union, Optional, TYPE_CHECKING

from alicebot.log import logger
from alicebot.config import config
from alicebot.utils import Condition
from alicebot.exception import AdapterTimeout

if TYPE_CHECKING:
    from alicebot import Bot
    from alicebot.event import T_Event

T_Adapter = TypeVar('T_Adapter', bound='BaseAdapter')

current_config = config.get()
if os.getenv('dev_env') == '1' or (current_config is not None and current_config.dev_env):
    # 当处于开发环境时，使用 pkg_resources 风格的命名空间包
    __import__('pkg_resources').declare_namespace(__name__)


class BaseAdapter(ABC):
    """
    协议适配器基类，仅实现最基础的适配器功能，通常情况下，适配器开发者开发的适配器应继承自 ``Adapter`` 而非本类。
    """
    name: str
    """
    适配器的名称。
    """
    bot: 'Bot'
    """
    当前的机器人对象。
    """

    def __init__(self, bot: 'Bot'):
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
        在适配器开始运行前运行的方法，用于初始化适配器。
        AliceBot 依次运行并等待所有适配器的 ``startup()`` 方法，待运行完毕后再创建 ``run()`` 任务。
        """
        pass

    async def shutdown(self):
        """
        在适配器结束运行时运行的方法，用于安全地关闭适配器。
        AliceBot 在接收到系统的结束信号后依次运行并等待所有适配器的 ``shutdown()`` 方法。当强制退出时此方法可能未被执行。
        """
        pass


class Adapter(BaseAdapter, ABC):
    """
    协议适配器基类，在 ``BaseAdapter`` 的基础上提供了 ``handle_event()`` 和 ``get()`` 等方法，通常情况下推荐使用。
    """
    cond: Condition
    """
    Condition 对象，用于事件处理。
    """

    def __init__(self, bot: 'Bot'):
        super().__init__(bot)
        self.cond = Condition()

    async def handle_event(self, event: 'T_Event'):
        """
        进行事件处理。

        :param event: 待处理的事件。
        """
        logger.info(f'Adapter {self.name} received: {event!r}')
        self.bot.loop.create_task(self._handle_event())
        await asyncio.sleep(0)
        async with self.cond:
            self.cond.notify_all(event)

    async def _handle_event(self):
        """
        调用 ``Bot`` 对象进行事件处理，将在所有正在等待的 ``get()`` 方法处理后没有被捕获时被调用。
        """
        async with self.cond:
            event = await self.cond.wait()
        if not event.handled:
            await self.bot.handle_event(event)

    async def get(self,
                  func: Optional[Callable[['T_Event'], Union[bool, Awaitable[bool]]]] = None,
                  max_try_times: Optional[int] = None,
                  timeout: Optional[Union[int, float]] = None) -> 'T_Event':
        """
        获取满足指定条件的的事件，协程会等待直到适配器接收到满足条件的事件、超过最大事件数或超时。

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

        if func is None:
            func = always_true
        elif not asyncio.iscoroutinefunction(func):
            func = async_wrapper(func)

        try_times = 0
        start_time = time.time()
        while not self.bot.should_exit and (max_try_times is None or (try_times < max_try_times)) and \
                (timeout is None or (time.time() - start_time < timeout)):
            async with self.cond:
                if timeout is None:
                    event = await self.cond.wait()
                else:
                    try:
                        event = await asyncio.wait_for(self.cond.wait(), timeout=start_time + timeout - time.time())
                    except asyncio.TimeoutError:
                        break
                if not event.handled:
                    if await func(event):
                        event.handled = True
                        return event
                try_times += 1

        if not self.bot.should_exit:
            raise AdapterTimeout

    async def send(self, *args, **kwargs):
        """
        发送消息，需要适配器开发者实现。
        """
        raise NotImplementedError
