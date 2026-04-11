from typing import override

from alicebot import Plugin
from alicebot.adapter.apscheduler import scheduler_decorator
from alicebot.adapter.apscheduler.event import APSchedulerEvent


@scheduler_decorator(
    trigger="interval", trigger_args={"seconds": 10}, override_rule=True
)
class ScheduleDecorator(Plugin[APSchedulerEvent]):
    @override
    async def handle(self) -> None:
        print("scheduler_decorator", self.event.type, self.event.adapter)

    @override
    async def rule(self) -> bool:
        return False
