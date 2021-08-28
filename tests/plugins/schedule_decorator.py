from alicebot.plugin import Plugin
from alicebot.adapter.apscheduler import scheduler_decorator


@scheduler_decorator(trigger='interval', trigger_args={'seconds': 10}, override_rule=True)
class Schedule(Plugin):
    async def handle(self) -> None:
        print('scheduler_decorator', self.event.type, self.event.adapter)

    async def rule(self) -> bool:
        return False
