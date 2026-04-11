"""APScheduler 适配器事件。"""

# pyright: reportMissingTypeStubs = false
from typing import TYPE_CHECKING, Any, override

from apscheduler.job import Job
from apscheduler.triggers.base import BaseTrigger

from alicebot.event import Event

if TYPE_CHECKING:
    import builtins

    from alicebot.typing import AnyPlugin

    from . import APSchedulerAdapter


__all__ = ["APSchedulerEvent"]


class APSchedulerEvent(Event["APSchedulerAdapter"]):
    """APSchedulerEvent 事件基类。"""

    type: str = "apscheduler"
    _adapter: "APSchedulerAdapter"
    _plugin_class: "builtins.type[AnyPlugin]"

    def __init__(
        self,
        *,
        adapter: "APSchedulerAdapter",
        plugin_class: "builtins.type[AnyPlugin]",
    ) -> None:
        """初始化 APSchedulerEvent 事件对象。"""
        super().__init__()
        self._adapter = adapter
        self._plugin_class = plugin_class

    @property
    @override
    def adapter(self) -> "APSchedulerAdapter":
        return self._adapter

    @property
    def plugin_class(self) -> "builtins.type[AnyPlugin]":
        """产生当前事件的 Plugin 类。"""
        return self._plugin_class

    @property
    def job(self) -> Job:
        """产生当前事件的 APScheduler `Job` 对象。"""
        return self.adapter.plugin_class_to_job[self.plugin_class]

    @property
    def trigger(self) -> str | BaseTrigger | None:
        """当前事件对应的 Plugin 的 `trigger`。"""
        return getattr(self.plugin_class, "trigger", None)

    @property
    def trigger_args(self) -> dict[str, Any] | None:
        """当前事件对应的 Plugin 的 `trigger_args`。"""
        return getattr(self.plugin_class, "trigger_args", None)

    @override
    def __str__(self) -> str:
        return f"<{self.__class__.__name__} plugin_class={self.plugin_class.__name__}>"

    @override
    def __repr__(self) -> str:
        return self.__str__()
