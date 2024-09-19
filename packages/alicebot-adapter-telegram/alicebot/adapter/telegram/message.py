"""Telegram 适配器消息。"""
# Based on: https://github.com/nonebot/adapter-telegram/blob/beta/nonebot/adapters/telegram/message.py
# ruff: noqa: D102

from typing_extensions import Self, override

from alicebot.message import Message, MessageSegment

from .model import MessageEntity, User

__all__ = ["TelegramMessage", "TelegramMessageSegment"]


class TelegramMessage(Message["TelegramMessageSegment"]):
    """Telegram 消息。"""

    @override
    @classmethod
    def get_segment_class(cls) -> type["TelegramMessageSegment"]:
        return TelegramMessageSegment

    @classmethod
    def from_entities(cls, text: str, entities: list[MessageEntity]) -> Self:
        message = cls()
        offset = 0
        text_bytes = text.encode("utf-16-le")
        for entity in entities:
            if entity.offset > offset:
                message.append(
                    TelegramMessageSegment(
                        type="text",
                        data={
                            "text": text_bytes[offset * 2 : entity.offset * 2].decode(
                                "utf-16-le"
                            )
                        },
                    )
                )
            message.append(
                TelegramMessageSegment(
                    type=entity.type,
                    data={
                        "text": text_bytes[
                            entity.offset * 2 : (entity.offset + entity.length) * 2
                        ].decode("utf-16-le"),
                        **entity.model_dump(
                            exclude={"type", "offset", "length"},
                            exclude_none=True,
                        ),
                    },
                )
            )
            offset = entity.offset + entity.length
        if offset < len(text_bytes):
            message.append(
                TelegramMessageSegment(
                    type="text",
                    data={"text": text_bytes[offset * 2 :].decode("utf-16-le")},
                )
            )
        return message

    def to_text(self) -> str:
        return "".join(message_segment.data["text"] for message_segment in self)

    def to_entities(self) -> list[MessageEntity]:
        return [
            MessageEntity(
                type=entity.type,
                offset=sum(entity.length for entity in self[:i]),
                length=entity.length,
                url=entity.data.get("url"),
                user=entity.data.get("user"),
                language=entity.data.get("language"),
                custom_emoji_id=entity.data.get("custom_emoji_id"),
            )
            for i, entity in enumerate(self)
            if entity.type != "text"
        ]


class TelegramMessageSegment(MessageSegment["TelegramMessage"]):
    """Telegram 消息字段，对应 Telegram 的 MessageEntity。"""

    @override
    @classmethod
    def get_message_class(cls) -> type["TelegramMessage"]:
        return TelegramMessage

    @override
    @classmethod
    def from_str(cls, msg: str) -> Self:
        return cls.text(msg)

    @override
    def __str__(self) -> str:
        if self.type == "text":
            return self.data.get("text", "")
        return f"[{self.type}: {self.data!r}]"

    @override
    def is_text(self) -> bool:
        return True

    @property
    def length(self) -> int:
        return len(self.data["text"].encode("utf-16-le")) // 2

    @classmethod
    def text(cls, text: str) -> Self:
        return cls(type="text", data={"text": text})

    @classmethod
    def mention(cls, text: str) -> Self:
        return cls(type="mention", data={"text": text})

    @classmethod
    def hashtag(cls, text: str) -> Self:
        return cls(type="hashtag", data={"text": text})

    @classmethod
    def cashtag(cls, text: str) -> Self:
        return cls(type="cashtag", data={"text": text})

    @classmethod
    def bot_command(cls, text: str) -> Self:
        return cls(type="bot_command", data={"text": text})

    @classmethod
    def url(cls, text: str) -> Self:
        return cls(type="url", data={"text": text})

    @classmethod
    def email(cls, text: str) -> Self:
        return cls(type="email", data={"text": text})

    @classmethod
    def phone_number(cls, text: str) -> Self:
        return cls(type="phone_number", data={"text": text})

    @classmethod
    def bold(cls, text: str) -> Self:
        return cls(type="bold", data={"text": text})

    @classmethod
    def italic(cls, text: str) -> Self:
        return cls(type="italic", data={"text": text})

    @classmethod
    def underline(cls, text: str) -> Self:
        return cls(type="underline", data={"text": text})

    @classmethod
    def strikethrough(cls, text: str) -> Self:
        return cls(type="strikethrough", data={"text": text})

    @classmethod
    def spoiler(cls, text: str) -> Self:
        return cls(type="spoiler", data={"text": text})

    @classmethod
    def blockquote(cls, text: str) -> Self:
        return cls(type="blockquote", data={"text": text})

    @classmethod
    def expandable_blockquote(cls, text: str) -> Self:
        return cls(type="expandable_blockquote", data={"text": text})

    @classmethod
    def code(cls, text: str) -> Self:
        return cls(type="code", data={"text": text})

    @classmethod
    def pre(cls, text: str, language: str) -> Self:
        return cls(type="pre", data={"text": text, "language": language})

    @classmethod
    def text_link(cls, text: str, url: str) -> Self:
        return cls(type="text_link", data={"text": text, "url": url})

    @classmethod
    def text_mention(cls, text: str, user: User) -> Self:
        return cls(type="text_mention", data={"text": text, "user": user})

    @classmethod
    def custom_emoji(cls, text: str, custom_emoji_id: str) -> Self:
        return cls(
            type="custom_emoji", data={"text": text, "custom_emoji_id": custom_emoji_id}
        )
