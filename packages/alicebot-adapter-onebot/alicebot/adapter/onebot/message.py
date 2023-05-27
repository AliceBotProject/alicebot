"""OneBot 适配器消息。"""
from typing import Any, Iterable, Mapping, Type, Union

from alicebot.message import Message, MessageSegment

__all__ = ["T_OBMSG", "OneBotMessage", "OneBotMessageSegment"]

T_OBMSG = Union[
    str,
    Mapping[str, Any],
    Iterable[Mapping[str, Any]],
    "OneBotMessageSegment",
    "OneBotMessage",
]


class OneBotMessage(Message["OneBotMessageSegment"]):
    """OneBot 消息。"""

    @property
    def _message_segment_class(self) -> Type["OneBotMessageSegment"]:
        return OneBotMessageSegment

    def _str_to_message_segment(self, msg: str) -> "OneBotMessageSegment":
        return OneBotMessageSegment.text(msg)


class OneBotMessageSegment(MessageSegment["OneBotMessage"]):
    """OneBot 消息字段。"""

    @property
    def _message_class(self) -> Type["OneBotMessage"]:
        return OneBotMessage

    def __str__(self) -> str:
        if self.type == "text":
            return self.data.get("text", "")
        return f"[{self.type}: {repr(self.data)}]"

    @classmethod
    def text(cls, text: str) -> "OneBotMessageSegment":
        """纯文本"""
        return cls(type="text", data={"text": text})

    @classmethod
    def mention(cls, user_id: str) -> "OneBotMessageSegment":
        """提及"""
        return cls(type="mention", data={"user_id": user_id})

    @classmethod
    def mention_all(cls) -> "OneBotMessageSegment":
        """提及所有人"""
        return cls(type="mention_all", data={})

    @classmethod
    def image(cls, file_id: str) -> "OneBotMessageSegment":
        """图片"""
        return cls(type="image", data={"file_id": file_id})

    @classmethod
    def voice(cls, file_id: str) -> "OneBotMessageSegment":
        """语音"""
        return cls(type="voice", data={"file_id": file_id})

    @classmethod
    def audio(cls, file_id: str) -> "OneBotMessageSegment":
        """音频"""
        return cls(type="audio", data={"file_id": file_id})

    @classmethod
    def video(cls, file_id: str) -> "OneBotMessageSegment":
        """视频"""
        return cls(type="video", data={"file_id": file_id})

    @classmethod
    def file(cls, file_id: str) -> "OneBotMessageSegment":
        """文件"""
        return cls(type="file", data={"file_id": file_id})

    @classmethod
    def location(
        cls, latitude: float, longitude: float, title: str, content: str
    ) -> "OneBotMessageSegment":
        """位置"""
        return cls(
            type="file",
            data={
                "latitude": latitude,
                "longitude": longitude,
                "title": title,
                "content": content,
            },
        )

    @classmethod
    def reply(cls, message_id: str, user_id: str) -> "OneBotMessageSegment":
        """回复"""
        return cls(type="reply", data={"message_id": message_id, "user_id": user_id})
