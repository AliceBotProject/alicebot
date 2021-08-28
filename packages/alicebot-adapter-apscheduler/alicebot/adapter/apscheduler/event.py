"""
==================
APScheduler 事件
==================
"""
from typing import Any, Dict, Type, TYPE_CHECKING

from alicebot.event import Event

if TYPE_CHECKING:
    from apscheduler.job import Job


class APSchedulerEvent(Event):
    """APSchedulerEvent 事件基类"""
    type = 'apscheduler'
    plugin_class: Type

    @property
    def job(self) -> 'Job':
        """
        :return: 产生当前事件的 APScheduler Job 对象。
        """
        return self.adapter.plugin_class_to_job.get(self.plugin_class)

    @property
    def trigger(self) -> str:
        """
        :return: 当前事件对应的 Plugin 的 trigger。
        """
        return getattr(self.plugin_class, 'trigger', None)

    @property
    def trigger_args(self) -> Dict[str, Any]:
        """
        :return: 当前事件对应的 Plugin 的 trigger_args。
        """
        return getattr(self.plugin_class, 'trigger_args', None)
