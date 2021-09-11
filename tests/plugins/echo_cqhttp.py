from alicebot.plugin import Plugin


class Echo(Plugin):
    async def handle(self) -> None:
        await self.event.reply(self.event.message.replace('echo ', ''))

    async def rule(self) -> bool:
        return self.adapter.name == 'cqhttp' and self.event.type == 'message' and self.event.message.startswith('echo ')
