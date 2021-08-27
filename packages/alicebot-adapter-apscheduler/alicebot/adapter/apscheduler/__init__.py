"""
==================
APScheduler 适配器
==================
本适配器用于实现定时任务，适配器将使用 APScheduler 实现定时任务，在设定的时间产生一个事件供插件处理。
APScheduler 使用方法请参考: `APScheduler`_ 。

.. _APScheduler: https://apscheduler.readthedocs.io/
"""
import asyncio
from typing import Dict, Type, TYPE_CHECKING

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from alicebot.log import logger
from alicebot.adapter import BaseAdapter

from .config import Config
from .event import APSchedulerEvent

if TYPE_CHECKING:
    from alicebot.plugin import T_Plugin
    from apscheduler.job import Job


class APSchedulerAdapter(BaseAdapter):
    name: str = 'apscheduler'
    scheduler: AsyncIOScheduler = None
    plugin_class_to_job: Dict[Type['T_Plugin'], 'Job'] = {}

    @property
    def config(self):
        """
        :return: 本适配器的配置。
        """
        return getattr(self.bot.config, Config.__config_name__)

    async def startup(self):
        """
        创建 AsyncIOScheduler 对象。
        """
        self.scheduler = AsyncIOScheduler(self.config.scheduler_config)

    async def run(self):
        """
        启动调度器。
        """
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
        """
        关闭调度器。
        """
        if self.scheduler is not None:
            self.scheduler.shutdown()

    async def create_event(self, plugin_class: Type['T_Plugin']):
        """
        创建 APSchedulerEvent 事件。

        :param plugin_class:
        """
        logger.info(f'APSchedulerEvent set by {plugin_class} is created as scheduled')
        asyncio.create_task(self.bot.handle_event(APSchedulerEvent(adapter=self, plugin_class=plugin_class)))
