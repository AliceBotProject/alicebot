"""Telegram 适配器事件。"""
# autogenerated by codegen.py, do not edit manually.
# ruff: noqa: TID252

from ..model import (
    BusinessConnection,
    BusinessMessagesDeleted,
    CallbackQuery,
    ChatBoostRemoved,
    ChatBoostUpdated,
    ChatJoinRequest,
    ChatMemberUpdated,
    ChosenInlineResult,
    InlineQuery,
    Message,
    MessageReactionCountUpdated,
    MessageReactionUpdated,
    PaidMediaPurchased,
    Poll,
    PollAnswer,
    PreCheckoutQuery,
    ShippingQuery,
)
from .base import TelegramEvent


class EditedMessageEvent(TelegramEvent):
    """New version of a message that is known to the bot and was edited."""

    __event_type__ = "edited_message"

    @property
    def edited_message(self) -> Message:
        """The edited_message object."""
        assert self.update.edited_message is not None
        return self.update.edited_message


class ChannelPostEvent(TelegramEvent):
    """New incoming channel post of any kind - text, photo, sticker, etc.."""

    __event_type__ = "channel_post"

    @property
    def channel_post(self) -> Message:
        """The channel_post object."""
        assert self.update.channel_post is not None
        return self.update.channel_post


class EditedChannelPostEvent(TelegramEvent):
    """New version of a channel post that is known to the bot and was edited."""

    __event_type__ = "edited_channel_post"

    @property
    def edited_channel_post(self) -> Message:
        """The edited_channel_post object."""
        assert self.update.edited_channel_post is not None
        return self.update.edited_channel_post


class BusinessConnectionEvent(TelegramEvent):
    """The bot was connected to or disconnected from a business account, or a user edited an existing connection with the bot."""

    __event_type__ = "business_connection"

    @property
    def business_connection(self) -> BusinessConnection:
        """The business_connection object."""
        assert self.update.business_connection is not None
        return self.update.business_connection


class BusinessMessageEvent(TelegramEvent):
    """New message from a connected business account."""

    __event_type__ = "business_message"

    @property
    def business_message(self) -> Message:
        """The business_message object."""
        assert self.update.business_message is not None
        return self.update.business_message


class EditedBusinessMessageEvent(TelegramEvent):
    """New version of a message from a connected business account."""

    __event_type__ = "edited_business_message"

    @property
    def edited_business_message(self) -> Message:
        """The edited_business_message object."""
        assert self.update.edited_business_message is not None
        return self.update.edited_business_message


class DeletedBusinessMessagesEvent(TelegramEvent):
    """Messages were deleted from a connected business account."""

    __event_type__ = "deleted_business_messages"

    @property
    def deleted_business_messages(self) -> BusinessMessagesDeleted:
        """The deleted_business_messages object."""
        assert self.update.deleted_business_messages is not None
        return self.update.deleted_business_messages


class MessageReactionEvent(TelegramEvent):
    """A reaction to a message was changed by a user."""

    __event_type__ = "message_reaction"

    @property
    def message_reaction(self) -> MessageReactionUpdated:
        """The message_reaction object."""
        assert self.update.message_reaction is not None
        return self.update.message_reaction


class MessageReactionCountEvent(TelegramEvent):
    """Reactions to a message with anonymous reactions were changed."""

    __event_type__ = "message_reaction_count"

    @property
    def message_reaction_count(self) -> MessageReactionCountUpdated:
        """The message_reaction_count object."""
        assert self.update.message_reaction_count is not None
        return self.update.message_reaction_count


class InlineQueryEvent(TelegramEvent):
    """New incoming inline query."""

    __event_type__ = "inline_query"

    @property
    def inline_query(self) -> InlineQuery:
        """The inline_query object."""
        assert self.update.inline_query is not None
        return self.update.inline_query


class ChosenInlineResultEvent(TelegramEvent):
    """The result of an inline query that was chosen by a user and sent to their chat partner."""

    __event_type__ = "chosen_inline_result"

    @property
    def chosen_inline_result(self) -> ChosenInlineResult:
        """The chosen_inline_result object."""
        assert self.update.chosen_inline_result is not None
        return self.update.chosen_inline_result


class CallbackQueryEvent(TelegramEvent):
    """New incoming callback query."""

    __event_type__ = "callback_query"

    @property
    def callback_query(self) -> CallbackQuery:
        """The callback_query object."""
        assert self.update.callback_query is not None
        return self.update.callback_query


class ShippingQueryEvent(TelegramEvent):
    """New incoming shipping query."""

    __event_type__ = "shipping_query"

    @property
    def shipping_query(self) -> ShippingQuery:
        """The shipping_query object."""
        assert self.update.shipping_query is not None
        return self.update.shipping_query


class PreCheckoutQueryEvent(TelegramEvent):
    """New incoming pre-checkout query."""

    __event_type__ = "pre_checkout_query"

    @property
    def pre_checkout_query(self) -> PreCheckoutQuery:
        """The pre_checkout_query object."""
        assert self.update.pre_checkout_query is not None
        return self.update.pre_checkout_query


class PurchasedPaidMediaEvent(TelegramEvent):
    """A user purchased paid media with a non-empty payload sent by the bot in a non-channel chat."""

    __event_type__ = "purchased_paid_media"

    @property
    def purchased_paid_media(self) -> PaidMediaPurchased:
        """The purchased_paid_media object."""
        assert self.update.purchased_paid_media is not None
        return self.update.purchased_paid_media


class PollEvent(TelegramEvent):
    """New poll state."""

    __event_type__ = "poll"

    @property
    def poll(self) -> Poll:
        """The poll object."""
        assert self.update.poll is not None
        return self.update.poll


class PollAnswerEvent(TelegramEvent):
    """A user changed their answer in a non-anonymous poll."""

    __event_type__ = "poll_answer"

    @property
    def poll_answer(self) -> PollAnswer:
        """The poll_answer object."""
        assert self.update.poll_answer is not None
        return self.update.poll_answer


class MyChatMemberEvent(TelegramEvent):
    """The bot's chat member status was updated in a chat."""

    __event_type__ = "my_chat_member"

    @property
    def my_chat_member(self) -> ChatMemberUpdated:
        """The my_chat_member object."""
        assert self.update.my_chat_member is not None
        return self.update.my_chat_member


class ChatMemberEvent(TelegramEvent):
    """A chat member's status was updated in a chat."""

    __event_type__ = "chat_member"

    @property
    def chat_member(self) -> ChatMemberUpdated:
        """The chat_member object."""
        assert self.update.chat_member is not None
        return self.update.chat_member


class ChatJoinRequestEvent(TelegramEvent):
    """A request to join the chat has been sent."""

    __event_type__ = "chat_join_request"

    @property
    def chat_join_request(self) -> ChatJoinRequest:
        """The chat_join_request object."""
        assert self.update.chat_join_request is not None
        return self.update.chat_join_request


class ChatBoostEvent(TelegramEvent):
    """A chat boost was added or changed."""

    __event_type__ = "chat_boost"

    @property
    def chat_boost(self) -> ChatBoostUpdated:
        """The chat_boost object."""
        assert self.update.chat_boost is not None
        return self.update.chat_boost


class RemovedChatBoostEvent(TelegramEvent):
    """A boost was removed from a chat."""

    __event_type__ = "removed_chat_boost"

    @property
    def removed_chat_boost(self) -> ChatBoostRemoved:
        """The removed_chat_boost object."""
        assert self.update.removed_chat_boost is not None
        return self.update.removed_chat_boost