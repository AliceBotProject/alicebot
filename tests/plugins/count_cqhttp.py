from alicebot.plugin import Plugin


class Count(Plugin):
    async def handle(self) -> None:
        if self.state is None:
            self.state = 0
        self.state += 1
        await self.event.reply(f'count: {self.state}')

    async def rule(self) -> bool:
        return self.adapter.name == 'cqhttp' and self.event.type == 'message' and self.event.message.startswith('count')
