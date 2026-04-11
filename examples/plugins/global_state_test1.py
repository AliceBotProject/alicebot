from typing import Any, override

from alicebot import MessageEvent, Plugin


class GlobalStateTest1(Plugin[MessageEvent[Any]]):
    @override
    async def handle(self) -> None:
        if self.bot.global_state.get("count") is None:
            self.bot.global_state["count"] = 0
        self.bot.global_state["count"] += 1
        await self.event.reply(f"add: {self.bot.global_state['count']}")

    @override
    async def rule(self) -> bool:
        if not isinstance(self.event, MessageEvent):
            return False
        return self.event.get_plain_text() == "add"
