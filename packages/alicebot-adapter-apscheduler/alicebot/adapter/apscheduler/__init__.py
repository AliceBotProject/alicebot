"""APScheduler 适配器。

本适配器用于实现定时任务，适配器将使用 APScheduler 实现定时任务，在设定的时间产生一个事件供插件处理。
APScheduler 使用方法请参考: [APScheduler](https://apscheduler.readthedocs.io/) 。
"""
import asyncio
import inspect
from functools import wraps
from typing import Any, Dict, Type, TYPE_CHECKING

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from alicebot.log import logger
from alicebot.plugin import Plugin
from alicebot.adapter import BaseAdapter

from .config import Config
from .event import APSchedulerEvent

if TYPE_CHECKING:
    from alicebot.plugin import T_Plugin
    from apscheduler.job import Job

__all__ = ['APSchedulerAdapter', 'scheduler_decorator']


class APSchedulerAdapter(BaseAdapter):
    name: str = 'apscheduler'
    scheduler: AsyncIOScheduler = None
    plugin_class_to_job: Dict[Type['T_Plugin'], 'Job'] = {}

    @property
    def config(self):
        """本适配器的配置。"""
        return getattr(self.bot.config, Config.__config_name__)

    async def startup(self):
        """创建 AsyncIOScheduler 对象。"""
        self.scheduler = AsyncIOScheduler(self.config.scheduler_config)

    async def run(self):
        """启动调度器。"""
        for plugin in self.bot.plugins:
            if getattr(plugin, '__schedule__', False):
                if getattr(plugin, 'trigger', None) is None or getattr(plugin, 'trigger_args', None) is None:
                    logger.error(
                        f'Plugin {plugin.__name__} __schedule__ is True, but did not set trigger or trigger_args')
                elif not isinstance(plugin.trigger, str) or not isinstance(plugin.trigger_args, dict):
                    logger.error(f'Plugin {plugin.__name__} trigger or trigger_args type error')
                else:
                    try:
                        self.plugin_class_to_job[plugin] = self.scheduler.add_job(self.create_event,
                                                                                  args=(plugin,),
                                                                                  trigger=plugin.trigger,
                                                                                  **plugin.trigger_args)
                    except Exception as e:
                        logger.error(
                            f'Plugin {plugin.__name__} add_job filed, please check trigger and trigger_args: {e}')
                    else:
                        logger.info(f'Plugin {plugin.__name__} has been scheduled to run')

        self.scheduler.start()

    async def shutdown(self):
        """关闭调度器。"""
        if self.scheduler is not None:
            self.scheduler.shutdown()

    async def create_event(self, plugin_class: Type['T_Plugin']):
        """创建 APSchedulerEvent 事件。

        Args:
            plugin_class: Plugin 类。
        """
        logger.info(f'APSchedulerEvent set by {plugin_class} is created as scheduled')
        asyncio.create_task(self.bot.handle_event(APSchedulerEvent(adapter=self, plugin_class=plugin_class)))


def scheduler_decorator(trigger: str, trigger_args: Dict[str, Any], override_rule: bool = False):
    """用于为插件类添加计划任务功能的装饰器。

    Args:
        trigger: APScheduler 触发器。
        trigger_args: APScheduler 触发器参数。
        override_rule: 是否重写 rule() 方法，若为 True，则会在 rule() 方法中添加处理本插件定义的计划任务事件的逻辑。
    """

    def _decorator(cls: Type):
        if not inspect.isclass(cls):
            raise TypeError(f'can only decorate class')
        if not issubclass(cls, Plugin):
            raise TypeError(f'can only decorate Plugin class')
        setattr(cls, '__schedule__', True)
        setattr(cls, 'trigger', trigger)
        setattr(cls, 'trigger_args', trigger_args)
        if override_rule:
            def _rule_decorator(func):
                @wraps(func)
                async def _wrapper(self, *args, **kwargs):
                    if self.event.type == 'apscheduler' and type(self) == self.event.plugin_class:
                        return True
                    else:
                        return await func(self, *args, **kwargs)

                return _wrapper

            handle_func = getattr(cls, 'rule')
            setattr(cls, 'rule', _rule_decorator(handle_func))
        return cls

    return _decorator
