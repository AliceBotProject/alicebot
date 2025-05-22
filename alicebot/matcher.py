"""事件匹配器。

事件匹配器是 `Bot.get()` 方法的底层实现。
"""

import inspect
import time
from typing import TYPE_CHECKING, Any, Callable, Optional, Union, cast

import anyio
import anyio.to_thread

from alicebot.adapter import Adapter
from alicebot.event import Event
from alicebot.exceptions import GetEventTimeout
from alicebot.typing import GetFunction

if TYPE_CHECKING:
    from alicebot.bot import Bot

__all__ = ["EventMatcher"]


class EventMatcher:
    """事件匹配器。"""

    func: GetFunction
    bot: "Bot"
    event_type: Optional[type[Event[Any]]]
    adapter_type: Optional[type[Adapter[Any, Any]]]
    max_try_times: Optional[int]
    timeout: Optional[Union[int, float]]
    to_thread: bool

    event: anyio.Event
    try_times: int
    start_time: float
    result: Optional[Event[Any]]
    exception: Optional[BaseException]

    def __init__(
        self,
        func: GetFunction,
        *,
        bot: "Bot",
        event_type: Optional[type[Event[Any]]],
        adapter_type: Optional[type[Adapter[Any, Any]]],
        max_try_times: Optional[int],
        timeout: Optional[Union[int, float]],
        to_thread: bool,
    ) -> None:
        """实例化一个 `EventMatcher` 对象。

        Args:
            func: 原始函数。
            bot: 当前 Bot 对象。
            event_type: 当指定时，只接受指定类型的事件，先于 func 条件生效。默认为 `None`。
            adapter_type: 当指定时，只接受指定适配器产生的事件，先于 func 条件生效。默认为 `None`。
            max_try_times: 最大事件数。
            timeout: 超时时间。
            to_thread: 是否在独立的线程中运行同步函数。仅当 func 为同步函数时生效。
        """
        self.func = func
        self.bot = bot
        self.event_type = event_type
        self.adapter_type = adapter_type
        self.max_try_times = max_try_times
        self.timeout = timeout
        self.to_thread = to_thread

        self.event = anyio.Event()
        self.try_times = 0
        self.start_time = time.time()
        self.result = None
        self.exception = None

    async def wait(self) -> Event[Any]:
        """等待当前事件匹配器直到满足条件或者超时。

        Raises:
            GetEventTimeout: 事件匹配器超时。
            RuntimeError: 内部错误。

        Returns:
            匹配到的事件。
        """
        try:
            with anyio.fail_after(self.timeout):
                await self.event.wait()
        except TimeoutError:
            self.exception = GetEventTimeout()

        if self.exception is not None:
            raise self.exception
        if self.result is not None:
            return self.result

        raise RuntimeError("Event has no result.")  # pragma: no cover

    async def run(self, event: Event[Any]) -> Optional[bool]:
        """运行 `get()` 函数，检查当前 `get()` 是否成功。

        Args:
            event: 当前被处理的事件。

        Returns:
            返回 True 说明 Event 被 EventMatcher 成功处理了。
            返回 False 说明 Event 未被 EventMatcher 成功处理。
            返回 None 说明当前 EventMatcher 已经失效 (超时或异常)。
        """
        try:
            if await self.match(event):
                self.result = event
                self.event.set()
                return True
        except BaseException as e:  # noqa: BLE001
            self.exception = e
            return None
        else:
            return False

    async def match(self, event: Event[Any]) -> bool:
        """检查当前事件是否被匹配。

        Args:
            event: 事件。

        Raises:
            GetEventTimeout: 超过最大事件数或超时。

        Returns:
            是否被匹配。
        """
        if self.max_try_times is not None and self.try_times > self.max_try_times:
            raise GetEventTimeout
        if self.timeout is not None and time.time() - self.start_time > self.timeout:
            raise GetEventTimeout  # pragma: no cover

        self.try_times += 1

        if self.event_type is not None and not isinstance(event, self.event_type):
            return False
        if self.adapter_type is not None and not isinstance(
            event.adapter, self.adapter_type
        ):
            return False

        if self.func is None:
            return True
        if not inspect.iscoroutinefunction(self.func):
            func = cast("Callable[[Event[Any]], bool]", self.func)
            if self.to_thread:
                return await anyio.to_thread.run_sync(func, event)
            return func(event)

        return await self.func(event)
