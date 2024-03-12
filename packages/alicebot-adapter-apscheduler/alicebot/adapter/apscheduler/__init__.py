"""APScheduler 适配器。

本适配器用于实现定时任务，适配器将使用 APScheduler 实现定时任务，在设定的时间产生一个事件供插件处理。
APScheduler 使用方法请参考：[APScheduler](https://apscheduler.readthedocs.io/)。
"""

# ruff: noqa: B009, B010
import inspect
from functools import wraps
from typing import TYPE_CHECKING, Any, Awaitable, Callable, Dict, Type, Union

import structlog
from apscheduler.job import Job
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from alicebot.adapter import Adapter
from alicebot.plugin import Plugin
from alicebot.typing import PluginT

from .config import Config
from .event import APSchedulerEvent

if TYPE_CHECKING:
    from apscheduler.triggers.base import BaseTrigger

__all__ = ["APSchedulerAdapter", "scheduler_decorator"]

logger = structlog.stdlib.get_logger()


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
                    "Plugin __schedule__ is True, but did not set trigger or trigger_args",
                    plugin=plugin,
                )
                continue

            trigger: Union[str, BaseTrigger] = getattr(plugin, "trigger")
            trigger_args: Dict[str, Any] = getattr(plugin, "trigger_args")

            if not isinstance(trigger, str) or not isinstance(trigger_args, dict):
                logger.error("Plugin trigger or trigger_args type error", plugin=plugin)
                continue

            try:
                self.plugin_class_to_job[plugin] = self.scheduler.add_job(
                    self.create_event, args=(plugin,), trigger=trigger, **trigger_args
                )
            except Exception:
                logger.exception(
                    "Plugin add_job filed, please check trigger and trigger_args:",
                    plugin=plugin,
                )
            else:
                logger.info("Plugin has been scheduled to run", plugin=plugin)

        self.scheduler.start()

    async def shutdown(self) -> None:
        """关闭调度器。"""
        self.scheduler.shutdown()

    async def create_event(self, plugin_class: Type[Plugin[Any, Any, Any]]) -> None:
        """创建 `APSchedulerEvent` 事件。

        Args:
            plugin_class: `Plugin` 类。
        """
        logger.info(
            "APSchedulerEvent set by plugin is created as scheduled",
            plugin=plugin_class,
        )
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
        setattr(cls, "__schedule__", True)
        setattr(cls, "trigger", trigger)
        setattr(cls, "trigger_args", trigger_args)
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
