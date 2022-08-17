from alicebot.plugin import Plugin


class Restart(Plugin):
    async def handle(self) -> None:
        self.bot.restart()

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return self.event.message.get_plain_text() == "restart"
