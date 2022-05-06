from alicebot.plugin import Plugin


class Count(Plugin):
    async def handle(self) -> None:
        if self.state is None:
            self.state = 0
        self.state += 1
        await self.event.reply(f'count: {self.state}')

    async def rule(self) -> bool:
        if self.event.adapter.name != 'cqhttp':
            return False
        if self.event.type != 'message':
            return False
        return self.event.message.get_plain_text() == 'count'
