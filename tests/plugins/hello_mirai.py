from alicebot.plugin import Plugin


class HalloAlice(Plugin):
    async def handle(self) -> None:
        await self.event.replay('Hello, Alice!')

    async def rule(self) -> bool:
        return self.adapter.name == 'mirai' and self.event.type == 'FriendMessage' and \
               self.event.message.get_plain_text().lower() == 'hello'
