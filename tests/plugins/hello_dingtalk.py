from alicebot.plugin import Plugin


class HalloAlice(Plugin):
    async def handle(self) -> None:
        await self.event.reply('Hello, Alice!')

    async def rule(self) -> bool:
        return self.adapter.name == 'dingtalk' and str(self.event.message).strip().lower() == 'hello'
