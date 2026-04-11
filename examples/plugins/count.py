from typing import Any, override

from alicebot import MessageEvent, Plugin


class Count(Plugin[MessageEvent[Any], int | None]):
    @override
    async def handle(self) -> None:
        if self.state is None:
            self.state = 0
        self.state += 1
        await self.event.reply(f"count: {self.state}")

    @override
    async def rule(self) -> bool:
        if not isinstance(self.event, MessageEvent):
            return False
        return self.event.get_plain_text() == "count"
