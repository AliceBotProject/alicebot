from alicebot import Plugin


class GlobalStateTest1(Plugin):
    async def handle(self) -> None:
        if self.bot.global_state.get("count") is None:
            self.bot.global_state["count"] = 0
        self.bot.global_state["count"] += 1
        await self.event.reply(f"add: {self.bot.global_state['count']}")

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return self.event.message.get_plain_text() == "add"
