"""Telegram 适配器事件。"""

# ruff: noqa: TID252
from typing import TYPE_CHECKING, Any, Optional, Union
from typing_extensions import override

from alicebot.event import MessageEvent as BaseMessageEvent

from ..media import TelegramMedia
from ..message import TelegramMessage
from ..model import (
    ForceReply,
    InlineKeyboardMarkup,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ReplyParameters,
)
from .base import TelegramEvent

if TYPE_CHECKING:
    from .. import TelegramAdapter


class MessageEvent(TelegramEvent, BaseMessageEvent["TelegramAdapter"]):
    """New incoming message of any kind - text, photo, sticker, etc."""

    __event_type__ = "message"

    @property
    def message(self) -> Message:
        """The message object."""
        assert self.update.message is not None
        return self.update.message

    def get_message(self) -> TelegramMessage:
        """获取 TelegramMessage 对象。

        Returns:
            TelegramMessage 对象。
        """
        return TelegramMessage.from_entities(
            text=self.message.text or "",
            entities=self.message.entities or [],
        )

    @override
    def get_sender_id(self) -> Union[None, int, str]:
        if self.message.from_ is None:
            return None
        return self.message.from_.id

    @override
    def get_plain_text(self) -> str:
        return self.message.text or ""

    @override
    async def reply(
        self,
        message: Union[str, TelegramMessage, TelegramMedia],
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
        **kwargs: Any,
    ) -> Any:
        return await self.adapter.send(
            message,
            chat_id=self.message.chat.id,
            disable_notification=disable_notification,
            protect_content=protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
            **kwargs,
        )
