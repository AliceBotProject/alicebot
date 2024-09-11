"""Telegram 适配器事件。"""

from typing import TYPE_CHECKING, Any, Optional, Union
from typing_extensions import override

from alicebot.event import Event
from alicebot.event import MessageEvent as BaseMessageEvent

from .media import TelegramMedia
from .message import TelegramMessage
from .model import (
    BusinessConnection,
    BusinessMessagesDeleted,
    CallbackQuery,
    ChatBoostRemoved,
    ChatBoostUpdated,
    ChatJoinRequest,
    ChatMemberUpdated,
    ChosenInlineResult,
    ForceReply,
    InlineKeyboardMarkup,
    InlineQuery,
    Message,
    MessageReactionCountUpdated,
    MessageReactionUpdated,
    Poll,
    PollAnswer,
    PreCheckoutQuery,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ReplyParameters,
    ShippingQuery,
    Update,
)

if TYPE_CHECKING:
    from . import TelegramAdapter


class TelegramEvent(Event["TelegramAdapter"]):
    """Telegram Event Baseclass."""

    update: Update

    @property
    def update_id(self) -> int:
        """The update's unique identifier."""
        return self.update.update_id


class MessageEvent(TelegramEvent, BaseMessageEvent["TelegramAdapter"]):
    """New incoming message of any kind - text, photo, sticker, etc."""

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


class EditedMessageEvent(TelegramEvent):
    """New version of a message that is known to the bot and was edited."""

    @property
    def edited_message(self) -> Message:
        """The edited_message object."""
        assert self.update.edited_message is not None
        return self.update.edited_message


class ChannelPostEvent(TelegramEvent):
    """New incoming channel post of any kind - text, photo, sticker, etc."""

    @property
    def channel_post(self) -> Message:
        """The channel_post object."""
        assert self.update.channel_post is not None
        return self.update.channel_post


class EditedChannelPostEvent(TelegramEvent):
    """New version of a channel post that is known to the bot and was edited."""

    @property
    def edited_channel_post(self) -> Message:
        """The edited_channel_post object."""
        assert self.update.edited_channel_post is not None
        return self.update.edited_channel_post


class BusinessConnectionEvent(TelegramEvent):
    """The bot was connected to or disconnected from a business account."""

    @property
    def business_connection(self) -> BusinessConnection:
        """The business_connection object."""
        assert self.update.business_connection is not None
        return self.update.business_connection


class BusinessMessageEvent(TelegramEvent):
    """New message from a connected business account."""

    @property
    def business_message(self) -> Message:
        """The business_message object."""
        assert self.update.business_message is not None
        return self.update.business_message


class EditedBusinessMessageEvent(TelegramEvent):
    """New version of a message from a connected business account."""

    @property
    def edited_business_message(self) -> Message:
        """The edited_business_message object."""
        assert self.update.edited_business_message is not None
        return self.update.edited_business_message


class DeletedBusinessMessagesEvent(TelegramEvent):
    """Messages were deleted from a connected business account."""

    @property
    def deleted_business_messages(self) -> BusinessMessagesDeleted:
        """The deleted_business_messages object."""
        assert self.update.deleted_business_messages is not None
        return self.update.deleted_business_messages


class MessageReactionEvent(TelegramEvent):
    """A reaction to a message was changed by a user."""

    @property
    def message_reaction(self) -> MessageReactionUpdated:
        """The message_reaction object."""
        assert self.update.message_reaction is not None
        return self.update.message_reaction


class MessageReactionCountEvent(TelegramEvent):
    """Reactions to a message with anonymous reactions were changed."""

    @property
    def message_reaction_count(self) -> MessageReactionCountUpdated:
        """The message_reaction_count object."""
        assert self.update.message_reaction_count is not None
        return self.update.message_reaction_count


class InlineQueryEvent(TelegramEvent):
    """New incoming inline query."""

    @property
    def inline_query(self) -> InlineQuery:
        """The inline_query object."""
        assert self.update.inline_query is not None
        return self.update.inline_query


class ChosenInlineResultEvent(TelegramEvent):
    """The result of an inline query that was chosen by a user and sent to their chat partner."""

    @property
    def chosen_inline_result(self) -> ChosenInlineResult:
        """The chosen_inline_result object."""
        assert self.update.chosen_inline_result is not None
        return self.update.chosen_inline_result


class CallbackQueryEvent(TelegramEvent):
    """New incoming callback query."""

    @property
    def callback_query(self) -> CallbackQuery:
        """The callback_query object."""
        assert self.update.callback_query is not None
        return self.update.callback_query


class ShippingQueryEvent(TelegramEvent):
    """New incoming shipping query."""

    @property
    def shipping_query(self) -> ShippingQuery:
        """The shipping_query object."""
        assert self.update.shipping_query is not None
        return self.update.shipping_query


class PreCheckoutQueryEvent(TelegramEvent):
    """New incoming pre-checkout query."""

    @property
    def pre_checkout_query(self) -> PreCheckoutQuery:
        """The pre_checkout_query object."""
        assert self.update.pre_checkout_query is not None
        return self.update.pre_checkout_query


class PollEvent(TelegramEvent):
    """New poll state."""

    @property
    def poll(self) -> Poll:
        """The poll object."""
        assert self.update.poll is not None
        return self.update.poll


class PollAnswerEvent(TelegramEvent):
    """A user changed their answer in a non-anonymous poll."""

    @property
    def poll_answer(self) -> PollAnswer:
        """The poll_answer object."""
        assert self.update.poll_answer is not None
        return self.update.poll_answer


class MyChatMemberEvent(TelegramEvent):
    """The bot's chat member status was updated in a chat."""

    @property
    def my_chat_member(self) -> ChatMemberUpdated:
        """The my_chat_member object."""
        assert self.update.my_chat_member is not None
        return self.update.my_chat_member


class ChatMemberEvent(TelegramEvent):
    """A chat member's status was updated in a chat."""

    @property
    def chat_member(self) -> ChatMemberUpdated:
        """The chat_member object."""
        assert self.update.chat_member is not None
        return self.update.chat_member


class ChatJoinRequestEvent(TelegramEvent):
    """A request to join the chat has been sent."""

    @property
    def chat_join_request(self) -> ChatJoinRequest:
        """The chat_join_request object."""
        assert self.update.chat_join_request is not None
        return self.update.chat_join_request


class ChatBoostEvent(TelegramEvent):
    """A chat boost was added or changed."""

    @property
    def chat_boost(self) -> ChatBoostUpdated:
        """The chat_boost object."""
        assert self.update.chat_boost is not None
        return self.update.chat_boost


class RemovedChatBoostEvent(TelegramEvent):
    """A boost was removed from a chat."""

    @property
    def removed_chat_boost(self) -> ChatBoostRemoved:
        """The removed_chat_boost object."""
        assert self.update.removed_chat_boost is not None
        return self.update.removed_chat_boost
