from typing import Type
from typing_extensions import Self

from alicebot.message import Message, MessageSegment


class FakeMessage(Message["FakeMessageSegment"]):
    """用于测试的消息。"""

    @classmethod
    def get_segment_class(cls) -> Type["FakeMessageSegment"]:
        """获取消息字段类。

        Returns:
            消息字段类。
        """
        return FakeMessageSegment


class FakeMessageSegment(MessageSegment["FakeMessage"]):
    """用于测试的消息字段。"""

    @classmethod
    def get_message_class(cls) -> Type["FakeMessage"]:
        """获取消息类。

        Returns:
            消息类。
        """
        return FakeMessage

    @classmethod
    def from_str(cls, msg: str) -> Self:
        """用于将 `str` 转换为消息字段。

        Args:
            msg: 要解析为消息字段的数据。

        Returns:
            由 `str` 转换的消息字段。
        """
        return cls.text(msg)

    def __str__(self) -> str:
        """返回消息的文本表示。

        Returns:
            消息的文本表示。
        """
        if self.type == "text":
            return self.data.get("text", "")
        return super().__str__()

    @classmethod
    def text(cls, text: str) -> Self:
        """纯文本"""
        return cls(type="text", data={"text": text})
