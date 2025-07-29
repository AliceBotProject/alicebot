"""Who are you 插件。"""

from typing_extensions import override

from alicebot import Plugin
from alicebot.adapter.telegram.event import MessageEvent


class Who(Plugin[MessageEvent, None, None]):
    """Who are you 插件。"""

    @override
    async def handle(self) -> None:
        answer = await self.event.ask("Who are you?")
        await self.event.reply(f"Hello, {answer.get_plain_text()}")

    @override
    async def rule(self) -> bool:
        return (
            isinstance(self.event, MessageEvent)
            and self.event.get_plain_text() == "/who"
        )
