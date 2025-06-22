"""处理 Inline Query。"""

from typing_extensions import override

from alicebot import Plugin
from alicebot.adapter.telegram.event import CallbackQueryEvent, InlineQueryEvent
from alicebot.adapter.telegram.model import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
)


class InlineQuery(Plugin[InlineQueryEvent | CallbackQueryEvent, None, None]):
    """处理 Inline Query。"""

    @override
    async def handle(self) -> None:
        if isinstance(self.event, InlineQueryEvent):
            await self.event.adapter.answer_inline_query(
                inline_query_id=self.event.inline_query.id,
                results=[
                    InlineQueryResultArticle(
                        type="article",
                        id="alicebot_telegram_adapter",
                        title="Alicebot Telegram Adapter",
                        input_message_content=InputTextMessageContent(
                            message_text="InlineQuery"
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(
                                        text="Alicebot",
                                        url="https://github.com/AliceBotProject/alicebot",
                                    )
                                ],
                                [
                                    InlineKeyboardButton(
                                        text="Telegram Bot API",
                                        url="https://core.telegram.org/bots/api",
                                    )
                                ],
                                [
                                    InlineKeyboardButton(
                                        text="Say hello to me",
                                        callback_data="hello",
                                    )
                                ],
                            ]
                        ),
                    ),
                ],
            )
        elif isinstance(self.event, CallbackQueryEvent):
            await self.event.adapter.answer_callback_query(
                callback_query_id=self.event.callback_query.id,
                text="Hello, I am Alice.",
            )

    @override
    async def rule(self) -> bool:
        return isinstance(self.event, (InlineQueryEvent, CallbackQueryEvent))
