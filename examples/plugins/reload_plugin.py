from typing import Any, override

from alicebot import MessageEvent, Plugin


class ReloadPlugin(Plugin[MessageEvent[Any]]):
    @override
    async def handle(self) -> None:
        self.bot.reload_plugins()
        await self.event.reply("\n".join(map(repr, self.bot.plugins)))

    @override
    async def rule(self) -> bool:
        if not isinstance(self.event, MessageEvent):
            return False
        return self.event.get_plain_text() == "reload"
