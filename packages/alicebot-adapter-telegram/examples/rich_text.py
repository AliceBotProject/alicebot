"""富文本消息示例。"""

from typing_extensions import override

from alicebot import Plugin
from alicebot.adapter.telegram.event import MessageEvent
from alicebot.adapter.telegram.message import TelegramMessage, TelegramMessageSegment


class RichText(Plugin[MessageEvent, None, None]):
    """富文本消息示例。"""

    @override
    async def handle(self) -> None:
        if (
            self.event.message.from_ is None
            or self.event.message.from_.username is None
        ):
            return
        message = TelegramMessage()
        for segment in (
            TelegramMessageSegment.text("text"),
            TelegramMessageSegment.mention("@" + self.event.message.from_.username),
            TelegramMessageSegment.hashtag("#hashtag"),
            TelegramMessageSegment.cashtag("$USD"),
            TelegramMessageSegment.bot_command("/rich"),
            TelegramMessageSegment.url("https://telegram.org"),
            TelegramMessageSegment.email("do-not-reply@telegram.org"),
            TelegramMessageSegment.phone_number("+1-212-555-0123"),
            TelegramMessageSegment.bold("bold"),
            TelegramMessageSegment.italic("italic"),
            TelegramMessageSegment.underline("underline"),
            TelegramMessageSegment.strikethrough("strikethrough"),
            TelegramMessageSegment.spoiler("spoiler"),
            TelegramMessageSegment.blockquote("blockquote"),
            TelegramMessageSegment.expandable_blockquote("expandable_blockquote"),
            TelegramMessageSegment.code("code"),
            TelegramMessageSegment.pre("pre", language="python"),
            TelegramMessageSegment.text_link("text_link", url="https://telegram.org"),
            TelegramMessageSegment.text_mention(
                "text_mention", user=self.event.message.from_
            ),
        ):
            message += segment + "\n"
        await self.event.reply(message)

    @override
    async def rule(self) -> bool:
        return (
            isinstance(self.event, MessageEvent)
            and self.event.get_plain_text() == "/rich"
        )
