from typing import override

from alicebot import Plugin
from alicebot.adapter.apscheduler.event import APSchedulerEvent


class Schedule(Plugin[APSchedulerEvent]):
    __schedule__ = True
    trigger = "interval"
    trigger_args = {"seconds": 10}  # noqa: RUF012

    @override
    async def handle(self) -> None:
        print(self.event.type, self.event.adapter)

    @override
    async def rule(self) -> bool:
        return (
            self.event.type == "apscheduler" and type(self) is self.event.plugin_class
        )
