"""APScheduler 适配器事件。"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from alicebot.event import Event

if TYPE_CHECKING:
    from apscheduler.job import Job
    from apscheduler.triggers.base import BaseTrigger

    from alicebot.plugin import Plugin

    from . import APSchedulerAdapter  # noqa: F401


__all__ = ["APSchedulerEvent"]


class APSchedulerEvent(Event["APSchedulerAdapter"]):
    """APSchedulerEvent 事件基类。"""

    type: str = "apscheduler"
    plugin_class: type[Plugin]  # type: ignore

    @property
    def job(self) -> Job:
        """产生当前事件的 APScheduler `Job` 对象。"""
        return self.adapter.plugin_class_to_job[self.plugin_class]

    @property
    def trigger(self) -> str | BaseTrigger:
        """当前事件对应的 Plugin 的 `trigger`。"""
        return getattr(self.plugin_class, "trigger")  # noqa: B009

    @property
    def trigger_args(self) -> dict[str, Any]:
        """当前事件对应的 Plugin 的 `trigger_args`。"""
        return getattr(self.plugin_class, "trigger_args")  # noqa: B009
