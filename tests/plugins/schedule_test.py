from alicebot.plugin import Plugin


class Schedule(Plugin):
    __schedule__ = True
    trigger = "interval"
    trigger_args = {"seconds": 10}

    async def handle(self) -> None:
        print(self.event.type, self.event.adapter)

    async def rule(self) -> bool:
        return (
            self.event.type == "apscheduler" and type(self) == self.event.plugin_class
        )
