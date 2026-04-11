from typing import Any, override

from alicebot import MessageEvent, Plugin


class Hallo(Plugin[MessageEvent[Any]]):
    @override
    async def handle(self) -> None:
        await self.event.reply("Hello, Alice!")

    @override
    async def rule(self) -> bool:
        if not isinstance(self.event, MessageEvent):
            return False
        return self.event.get_plain_text().lower() == "hello"
