from alicebot.plugin import Plugin


class HalloAlice(Plugin):
    async def handle(self) -> None:
        await self.event.reply("Hello, Alice!")

    async def rule(self) -> bool:
        if self.event.adapter.name != "mirai":
            return False
        if self.event.type != "FriendMessage":
            return False
        return self.event.message.get_plain_text().lower() == "hello"
