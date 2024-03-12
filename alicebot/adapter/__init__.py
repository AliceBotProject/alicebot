"""AliceBot 协议适配器。

所有协议适配器都必须继承自 `Adapter` 基类。
"""

import os
from abc import ABC, abstractmethod
from typing import (
    TYPE_CHECKING,
    Any,
    Awaitable,
    Callable,
    Generic,
    Optional,
    Type,
    TypeVar,
    Union,
    final,
    overload,
)

import structlog

from alicebot.event import Event
from alicebot.typing import ConfigT, EventT
from alicebot.utils import is_config_class

if TYPE_CHECKING:
    from alicebot.bot import Bot

__all__ = ["Adapter"]

logger = structlog.stdlib.get_logger()

if os.getenv("ALICEBOT_DEV") == "1":  # pragma: no cover
    # 当处于开发环境时，使用 pkg_resources 风格的命名空间包
    __import__("pkg_resources").declare_namespace(__name__)


_EventT = TypeVar("_EventT", bound="Event[Any]")


class Adapter(Generic[EventT, ConfigT], ABC):
    """协议适配器基类。

    Attributes:
        name: 适配器的名称。
        bot: 当前的机器人对象。
    """

    name: str
    bot: "Bot"
    Config: Type[ConfigT]

    def __init__(self, bot: "Bot") -> None:
        """初始化。

        Args:
            bot: 当前机器人对象。
        """
        if not hasattr(self, "name"):
            self.name = self.__class__.__name__
        self.bot: Bot = bot
        self.handle_event = self.bot.handle_event

    @property
    def config(self) -> ConfigT:
        """适配器配置。"""
        default: Any = None
        config_class = getattr(self, "Config", None)
        if is_config_class(config_class):
            return getattr(
                self.bot.config.adapter,
                config_class.__config_name__,
                default,
            )
        return default

    @final
    async def safe_run(self) -> None:
        """附带有异常处理地安全运行适配器。"""
        try:
            await self.run()
        except Exception:
            logger.exception("Run adapter failed", adapter_name=self.__class__.__name__)

    @abstractmethod
    async def run(self) -> None:
        """适配器运行方法，适配器开发者必须实现该方法。

        适配器运行过程中保持保持运行，当此方法结束后， AliceBot 不会自动重新启动适配器。
        """
        raise NotImplementedError

    async def startup(self) -> None:
        """在适配器开始运行前运行的方法，用于初始化适配器。

        AliceBot 依次运行并等待所有适配器的 `startup()` 方法，待运行完毕后再创建 `run()` 任务。
        """

    async def shutdown(self) -> None:
        """在适配器结束运行时运行的方法，用于安全地关闭适配器。

        AliceBot 在接收到系统的结束信号后依次运行并等待所有适配器的 `shutdown()` 方法。
        当强制退出时此方法可能未被执行。
        """

    @overload
    async def get(
        self,
        func: Optional[Callable[[EventT], Union[bool, Awaitable[bool]]]] = None,
        *,
        event_type: None = None,
        max_try_times: Optional[int] = None,
        timeout: Optional[Union[int, float]] = None,
    ) -> EventT: ...

    @overload
    async def get(
        self,
        func: Optional[Callable[[_EventT], Union[bool, Awaitable[bool]]]] = None,
        *,
        event_type: Type[_EventT],
        max_try_times: Optional[int] = None,
        timeout: Optional[Union[int, float]] = None,
    ) -> _EventT: ...

    @final
    async def get(
        self,
        func: Optional[Callable[[Any], Union[bool, Awaitable[bool]]]] = None,
        *,
        event_type: Any = None,
        max_try_times: Optional[int] = None,
        timeout: Optional[Union[int, float]] = None,
    ) -> Event[Any]:
        """获取满足指定条件的的事件，协程会等待直到适配器接收到满足条件的事件、超过最大事件数或超时。

        类似 `Bot` 类的 `get()` 方法，但是隐含了判断产生事件的适配器是本适配器。
        等效于 `Bot` 类的 `get()` 方法传入 adapter_type 为本适配器类型。

        Args:
            func: 协程或者函数，函数会被自动包装为协程执行。
                要求接受一个事件作为参数，返回布尔值。
                当协程返回 `True` 时返回当前事件。
                当为 `None` 时相当于输入对于任何事件均返回真的协程，即返回适配器接收到的下一个事件。
            event_type: 当指定时，只接受指定类型的事件，先于 func 条件生效。默认为 `None`。
            max_try_times: 最大事件数。
            timeout: 超时时间。

        Returns:
            返回满足 func 条件的事件。

        Raises:
            GetEventTimeout: 超过最大事件数或超时。
        """
        return await self.bot.get(
            func,
            event_type=event_type,
            adapter_type=type(self),
            max_try_times=max_try_times,
            timeout=timeout,
        )
