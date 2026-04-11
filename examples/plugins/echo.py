from typing import Any, override

from alicebot import MessageEvent, Plugin


class Echo(Plugin[MessageEvent[Any]]):
    @override
    async def handle(self) -> None:
        await self.event.reply(self.event.get_plain_text().replace("echo ", ""))

    @override
    async def rule(self) -> bool:
        if not isinstance(self.event, MessageEvent):
            return False
        return self.event.get_plain_text().startswith("echo ")
