"""APScheduler 适配器。

本适配器用于实现定时任务，适配器将使用 APScheduler 实现定时任务，在设定的时间产生一个事件供插件处理。
APScheduler 使用方法请参考：[APScheduler](https://apscheduler.readthedocs.io/)。
"""
import inspect
from functools import wraps
from typing import TYPE_CHECKING, Any, Awaitable, Callable, Dict, Type, Union

from apscheduler.job import Job
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from alicebot.adapter import Adapter
from alicebot.log import logger
from alicebot.plugin import Plugin
from alicebot.typing import PluginT

from .config import Config
from .event import APSchedulerEvent

if TYPE_CHECKING:
    from apscheduler.triggers.base import BaseTrigger

__all__ = ["APSchedulerAdapter", "scheduler_decorator"]


class APSchedulerAdapter(Adapter[APSchedulerEvent, Config]):
    """APScheduler 适配器。"""

    name: str = "apscheduler"
    Config = Config

    scheduler: AsyncIOScheduler
    plugin_class_to_job: Dict[Type[Plugin[Any, Any, Any]], Job]

    async def startup(self) -> None:
        """创建 `AsyncIOScheduler` 对象。"""
        self.scheduler = AsyncIOScheduler(self.config.scheduler_config)
        self.plugin_class_to_job = {}

    async def run(self) -> None:
        """启动调度器。"""
        for plugin in self.bot.plugins:
            if not hasattr(plugin, "__schedule__"):
                continue

            if not hasattr(plugin, "trigger") or not hasattr(plugin, "trigger_args"):
                logger.error(
                    f"Plugin {plugin.__name__} __schedule__ is True, "
                    f"but did not set trigger or trigger_args"
                )
                continue

            trigger: Union[str, BaseTrigger] = getattr(plugin, "trigger")  # noqa: B009
            trigger_args: Dict[str, Any] = getattr(plugin, "trigger_args")  # noqa: B009

            if not isinstance(trigger, str) or not isinstance(trigger_args, dict):
                logger.error(
                    f"Plugin {plugin.__name__} trigger or trigger_args type error"
                )
                continue

            try:
                self.plugin_class_to_job[plugin] = self.scheduler.add_job(
                    self.create_event, args=(plugin,), trigger=trigger, **trigger_args
                )
            except Exception as e:
                self.bot.error_or_exception(
                    f"Plugin {plugin.__name__} add_job filed, "
                    "please check trigger and trigger_args:",
                    e,
                )
            else:
                logger.info(f"Plugin {plugin.__name__} has been scheduled to run")

        self.scheduler.start()

    async def shutdown(self) -> None:
        """关闭调度器。"""
        self.scheduler.shutdown()

    async def create_event(self, plugin_class: Type[Plugin[Any, Any, Any]]) -> None:
        """创建 `APSchedulerEvent` 事件。

        Args:
            plugin_class: `Plugin` 类。
        """
        logger.info(f"APSchedulerEvent set by {plugin_class} is created as scheduled")
        await self.handle_event(
            APSchedulerEvent(adapter=self, plugin_class=plugin_class),
            handle_get=False,
            show_log=False,
        )

    async def send(self, *args: Any, **kwargs: Any) -> Any:
        """APScheduler 适配器不适用发送消息。"""
        raise NotImplementedError


def scheduler_decorator(
    trigger: str, trigger_args: Dict[str, Any], override_rule: bool = False
) -> Callable[[Type[PluginT]], Type[PluginT]]:
    """用于为插件类添加计划任务功能的装饰器。

    Args:
        trigger: APScheduler 触发器。
        trigger_args: APScheduler 触发器参数。
        override_rule: 是否重写 `rule()` 方法。
            若为 `True`，则会在 `rule()` 方法中添加处理本插件定义的计划任务事件的逻辑。
    """

    def _decorator(cls: Type[PluginT]) -> Type[PluginT]:
        if not inspect.isclass(cls):
            raise TypeError("can only decorate class")
        if not issubclass(cls, Plugin):
            raise TypeError("can only decorate Plugin class")
        setattr(cls, "__schedule__", True)  # noqa: B010
        setattr(cls, "trigger", trigger)  # noqa: B010
        setattr(cls, "trigger_args", trigger_args)  # noqa: B010
        if override_rule:

            def _rule_decorator(func: Callable[[PluginT], Awaitable[bool]]) -> Any:
                @wraps(func)
                async def _wrapper(self: PluginT) -> bool:
                    if (
                        self.event.type == "apscheduler"
                        # pylint: disable-next=unidiomatic-typecheck
                        and type(self) is self.event.plugin_class
                    ):
                        return True
                    return await func(self)

                return _wrapper

            cls.rule = _rule_decorator(cls.rule)  # type: ignore
        return cls  # type: ignore

    return _decorator
