"""APScheduler 适配器事件。"""
from typing import TYPE_CHECKING, Any, Dict, Type, Union

from alicebot.event import Event
from alicebot.plugin import Plugin

if TYPE_CHECKING:
    from apscheduler.job import Job
    from apscheduler.triggers.base import BaseTrigger

    from . import APSchedulerAdapter


class APSchedulerEvent(Event["APSchedulerAdapter"]):
    """APSchedulerEvent 事件基类。"""

    plugin_class: Type[Plugin]

    @property
    def job(self) -> "Job":
        """产生当前事件的 APScheduler Job 对象。"""
        return self.adapter.plugin_class_to_job[self.plugin_class]

    @property
    def trigger(self) -> Union[str, "BaseTrigger"]:
        """当前事件对应的 Plugin 的 trigger。"""
        return getattr(self.plugin_class, "trigger")

    @property
    def trigger_args(self) -> Dict[str, Any]:
        """当前事件对应的 Plugin 的 trigger_args。"""
        return getattr(self.plugin_class, "trigger_args")
