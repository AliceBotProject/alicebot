"""APScheduler 适配器。

本适配器用于实现定时任务，适配器将使用 APScheduler 实现定时任务，在设定的时间产生一个事件供插件处理。
APScheduler 使用方法请参考: [APScheduler](https://apscheduler.readthedocs.io/) 。
"""
import asyncio
import inspect
from functools import wraps
from typing import Any, Dict, Type, Union, Callable, Awaitable

from apscheduler.job import Job
from apscheduler.triggers.base import BaseTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from alicebot.plugin import Plugin
from alicebot.adapter import Adapter
from alicebot.log import logger, error_or_exception

from .config import Config
from .event import APSchedulerEvent

__all__ = ["APSchedulerAdapter", "scheduler_decorator"]


class APSchedulerAdapter(Adapter[APSchedulerEvent, Config]):
    name: str = "apscheduler"
    Config = Config

    scheduler: AsyncIOScheduler
    plugin_class_to_job: Dict[Type[Plugin], Job]

    async def startup(self):
        """创建 AsyncIOScheduler 对象。"""
        self.scheduler = AsyncIOScheduler(self.config.scheduler_config)
        self.plugin_class_to_job = {}

    async def run(self):
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

            trigger: Union[str, BaseTrigger] = getattr(plugin, "trigger")
            trigger_args: Dict[str, Any] = getattr(plugin, "trigger_args")

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
                error_or_exception(
                    f"Plugin {plugin.__name__} add_job filed, "
                    "please check trigger and trigger_args:",
                    e,
                    self.bot.config.bot.log.verbose_exception,
                )
            else:
                logger.info(f"Plugin {plugin.__name__} has been scheduled to run")

        self.scheduler.start()

    async def shutdown(self):
        """关闭调度器。"""
        self.scheduler.shutdown()

    async def create_event(self, plugin_class: Type[Plugin]):
        """创建 APSchedulerEvent 事件。

        Args:
            plugin_class: Plugin 类。
        """
        logger.info(f"APSchedulerEvent set by {plugin_class} is created as scheduled")
        asyncio.create_task(
            self.bot.handle_event(
                APSchedulerEvent(
                    adapter=self, type="apscheduler", plugin_class=plugin_class
                ),
                handle_get=False,
                show_log=False,
            )
        )

    async def send(self, *args: Any, **kwargs: Any):
        raise NotImplementedError


def scheduler_decorator(
    trigger: str, trigger_args: Dict[str, Any], override_rule: bool = False
):
    """用于为插件类添加计划任务功能的装饰器。

    Args:
        trigger: APScheduler 触发器。
        trigger_args: APScheduler 触发器参数。
        override_rule: 是否重写 rule() 方法，若为 True ，则会在 rule() 方法中添加处理本插件定义的计划任务事件的逻辑。
    """

    def _decorator(cls: Type[Plugin]):
        if not inspect.isclass(cls):
            raise TypeError(f"can only decorate class")
        if not issubclass(cls, Plugin):
            raise TypeError(f"can only decorate Plugin class")
        setattr(cls, "__schedule__", True)
        setattr(cls, "trigger", trigger)
        setattr(cls, "trigger_args", trigger_args)
        if override_rule:

            def _rule_decorator(func: Callable[[Plugin], Awaitable[bool]]):
                @wraps(func)
                async def _wrapper(self: Plugin):
                    if (
                        self.event.type == "apscheduler"
                        and type(self) == self.event.plugin_class
                    ):
                        return True
                    else:
                        return await func(self)

                return _wrapper

            cls.rule = _rule_decorator(cls.rule)
        return cls

    return _decorator
