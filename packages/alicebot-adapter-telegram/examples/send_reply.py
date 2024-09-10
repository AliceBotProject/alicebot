"""发送 Reply 消息。"""

from typing_extensions import override

from alicebot import Plugin
from alicebot.adapter.telegram.event import MessageEvent
from alicebot.adapter.telegram.model import ReplyParameters


class SendReply(Plugin[MessageEvent, None, None]):
    """发送 Reply 消息。"""

    @override
    async def handle(self) -> None:
        await self.event.reply(
            "Hello, I am Alice.",
            reply_parameters=ReplyParameters(
                message_id=self.event.message.message_id,
            ),
        )

    @override
    async def rule(self) -> bool:
        return (
            isinstance(self.event, MessageEvent)
            and self.event.get_plain_text() == "/reply"
        )
