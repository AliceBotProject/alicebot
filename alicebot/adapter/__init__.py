"""AliceBot 协议适配器。

所有协议适配器都必须继承自 `Adapter` 基类。
"""
from abc import ABC, abstractmethod
import os
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

from alicebot.log import error_or_exception
from alicebot.typing import T_Config, T_Event
from alicebot.utils import is_config_class

if TYPE_CHECKING:
    from alicebot.bot import Bot
    from alicebot.event import Event

__all__ = ["Adapter"]

if os.getenv("ALICEBOT_DEV") == "1":
    # 当处于开发环境时，使用 pkg_resources 风格的命名空间包
    __import__("pkg_resources").declare_namespace(__name__)


_T_Event = TypeVar("_T_Event", bound="Event[Any]")


class Adapter(Generic[T_Event, T_Config], ABC):
    """协议适配器基类。

    Attributes:
        name: 适配器的名称。
        bot: 当前的机器人对象。
    """

    name: str
    bot: "Bot"
    Config: Type[T_Config]

    def __init__(self, bot: "Bot"):
        """初始化。

        Args:
            bot: 当前机器人对象。
        """
        if not hasattr(self, "name"):
            self.name = self.__class__.__name__
        self.bot: "Bot" = bot
        self.handle_event = self.bot.handle_event

    @property
    def config(self) -> T_Config:
        """适配器配置。"""
        config_class = getattr(self, "Config", None)
        if is_config_class(config_class):
            return getattr(
                self.bot.config.adapter,
                config_class.__config_name__,
                None,
            )  # type: ignore
        return None  # type: ignore

    @final
    async def safe_run(self):
        """附带有异常处理地安全运行适配器。"""
        try:
            await self.run()
        except Exception as e:
            error_or_exception(
                f"Run adapter {self.__class__.__name__} failed:",
                e,
                self.bot.config.bot.log.verbose_exception,
            )

    @abstractmethod
    async def run(self) -> None:
        """适配器运行方法，适配器开发者必须实现该方法。

        适配器运行过程中保持保持运行，当此方法结束后， AliceBot 不会自动重新启动适配器。
        """
        raise NotImplementedError

    async def startup(self):
        """在适配器开始运行前运行的方法，用于初始化适配器。

        AliceBot 依次运行并等待所有适配器的 `startup()` 方法，待运行完毕后再创建 `run()` 任务。
        """

    async def shutdown(self):
        """在适配器结束运行时运行的方法，用于安全地关闭适配器。

        AliceBot 在接收到系统的结束信号后依次运行并等待所有适配器的 `shutdown()` 方法。
        当强制退出时此方法可能未被执行。
        """

    async def send(self, *args: Any, **kwargs: Any) -> Any:
        """发送消息，需要适配器开发者实现。"""
        raise NotImplementedError

    @overload
    async def get(
        self,
        func: Optional[Callable[[T_Event], Union[bool, Awaitable[bool]]]] = None,
        *,
        event_type: None = None,
        max_try_times: Optional[int] = None,
        timeout: Optional[Union[int, float]] = None,
    ) -> T_Event:
        ...

    @overload
    async def get(
        self,
        func: Optional[Callable[[_T_Event], Union[bool, Awaitable[bool]]]] = None,
        *,
        event_type: Type[_T_Event],
        max_try_times: Optional[int] = None,
        timeout: Optional[Union[int, float]] = None,
    ) -> _T_Event:
        ...

    @final
    async def get(
        self,
        func: Optional[Callable[[T_Event], Union[bool, Awaitable[bool]]]] = None,
        *,
        event_type: Optional[Union[Type[T_Event], Type[_T_Event]]] = None,
        max_try_times: Optional[int] = None,
        timeout: Optional[Union[int, float]] = None,
    ) -> Union[T_Event, _T_Event]:
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
