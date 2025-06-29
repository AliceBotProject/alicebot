from typing import Self
from typing_extensions import override

from alicebot.message import Message, MessageSegment


class FakeMessage(Message["FakeMessageSegment"]):
    """用于测试的消息。"""

    @override
    @classmethod
    def get_segment_class(cls) -> type["FakeMessageSegment"]:
        return FakeMessageSegment


class FakeMessageSegment(MessageSegment["FakeMessage"]):
    """用于测试的消息字段。"""

    @override
    @classmethod
    def get_message_class(cls) -> type["FakeMessage"]:
        return FakeMessage

    @override
    @classmethod
    def from_str(cls, msg: str) -> Self:
        return cls.text(msg)

    @override
    def __str__(self) -> str:
        if self.type == "text":
            return self.data.get("text", "")
        return super().__str__()

    @classmethod
    def text(cls, text: str) -> Self:
        """纯文本"""
        return cls(type="text", data={"text": text})
