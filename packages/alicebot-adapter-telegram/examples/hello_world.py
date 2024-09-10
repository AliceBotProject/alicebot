"""Hello World 插件。"""

from typing_extensions import override

from alicebot import Plugin
from alicebot.adapter.telegram.event import MessageEvent


class HelloWorld(Plugin[MessageEvent, None, None]):
    """Hello World 插件。"""

    @override
    async def handle(self) -> None:
        await self.event.reply("Hello, I am Alice.")

    @override
    async def rule(self) -> bool:
        return (
            isinstance(self.event, MessageEvent)
            and self.event.get_plain_text() == "/hello"
        )
