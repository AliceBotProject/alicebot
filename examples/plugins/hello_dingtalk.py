from alicebot import Plugin


class HalloAlice(Plugin):
    async def handle(self) -> None:
        await self.event.reply("Hello, Alice!")

    async def rule(self) -> bool:
        if self.event.adapter.name != "dingtalk":
            return False
        return str(self.event.message).strip().lower() == "hello"
