"""Telegram 适配器消息。"""
# Based on: https://github.com/nonebot/adapter-telegram/blob/beta/nonebot/adapters/telegram/message.py
# ruff: noqa: D102

from typing import Self
from typing_extensions import override

from alicebot.message import Message

from .entity import Entity
from .model import MessageEntity

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


class TelegramMessageSegment(Entity["TelegramMessage"]):
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
