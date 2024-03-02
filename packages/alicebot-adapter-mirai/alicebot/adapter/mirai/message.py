"""Mirai 适配器消息。"""

import json
from typing import Any, Dict, List, Optional, Type
from typing_extensions import Self

from pydantic import model_serializer

from alicebot.message import Message, MessageSegment
from alicebot.utils import PydanticEncoder

__all__ = ["MiraiMessage", "MiraiMessageSegment"]


class MiraiMessage(Message["MiraiMessageSegment"]):
    """Mirai 消息"""

    @classmethod
    def get_segment_class(cls) -> Type["MiraiMessageSegment"]:
        """获取消息字段类。

        Returns:
            消息字段类。
        """
        return MiraiMessageSegment

    def as_message_chain(self) -> List[Dict[str, Any]]:
        """返回符合 Mirai-api-http 标准的 messageChain 数组。

        Returns:
            messageChain 数组。
        """
        return [x.model_dump() for x in self]


class MiraiMessageSegment(MessageSegment["MiraiMessage"]):
    """Mirai 消息段"""

    def __init__(self, type: str, **data: Any) -> None:
        """初始化。

        Args:
            type: 消息类型。
            **data: 消息内容。
        """
        super().__init__(
            type=type, data={k: v for k, v in data.items() if v is not None}
        )

    @classmethod
    def get_message_class(cls) -> Type["MiraiMessage"]:
        """获取消息类。

        Returns:
            消息类。
        """
        return MiraiMessage

    @classmethod
    def from_str(cls, msg: str) -> Self:
        """用于将 `str` 转换为消息字段。

        Args:
            msg: 要解析为消息字段的数据。

        Returns:
            由 `str` 转换的消息字段。
        """
        return cls.plain(msg)

    def __str__(self) -> str:
        """返回消息字段的文本表示。

        Returns:
            消息字段的文本表示。
        """
        if self.type == "Source":
            return ""
        if self.type == "Plain":
            return self.data.get("text", "")
        return json.dumps(self, cls=PydanticEncoder)

    @model_serializer
    def ser_model(self) -> Dict[str, Any]:
        """返回符合 Mirai-api-http 标准的消息字段字典。

        Returns:
            符合 Mirai-api-http 标准的消息字段字典。
        """
        return {"type": self.type, **self.data}

    def is_text(self) -> bool:
        """是否是纯文本消息字段。

        Returns:
            是否是纯文本消息字段。
        """
        return self.type == "Plain"

    @classmethod
    def source(cls, id_: int, time: int) -> Self:
        """Source 消息"""
        return cls(type="Source", id=id_, time=time)

    @classmethod
    def quote(
        cls,
        id_: int,
        group_id: int,
        sender_id: int,
        target_id: int,
        origin: MiraiMessage,
    ) -> Self:
        """Quote 消息"""
        return cls(
            type="Quote",
            id=id_,
            groupId=group_id,
            senderId=sender_id,
            targetId=target_id,
            origin=origin.as_message_chain(),
        )

    @classmethod
    def at(cls, target: int) -> Self:
        """At 消息"""
        return cls(type="At", target=target)

    @classmethod
    def at_all(cls) -> Self:
        """AtAll 消息"""
        return cls(type="AtAll")

    @classmethod
    def face(cls, face_id: Optional[int] = None, name: Optional[str] = None) -> Self:
        """Face 消息"""
        return cls(type="Face", faceId=face_id, name=name)

    @classmethod
    def plain(cls, text: str) -> Self:
        """Plain 消息"""
        return cls(type="Plain", text=text)

    @classmethod
    def image(
        cls,
        image_id: Optional[str] = None,
        url: Optional[str] = None,
        path: Optional[str] = None,
    ) -> Self:
        """Image 消息"""
        return cls(type="Image", imageId=image_id, url=url, path=path)

    @classmethod
    def flash_image(
        cls,
        image_id: Optional[str] = None,
        url: Optional[str] = None,
        path: Optional[str] = None,
    ) -> Self:
        """FlashImage 消息"""
        return cls(type="FlashImage", imageId=image_id, url=url, path=path)

    @classmethod
    def voice(
        cls,
        voice_id: Optional[str] = None,
        url: Optional[str] = None,
        path: Optional[str] = None,
    ) -> Self:
        """Voice 消息"""
        return cls(type="Voice", imageId=voice_id, url=url, path=path)

    @classmethod
    def xml(cls, xml: str) -> Self:
        """Xml 消息"""
        return cls(type="Xml", xml=xml)

    @classmethod
    def json(cls, json_: str) -> Self:  # type: ignore
        """Json 消息"""
        return cls(type="Json", json=json_)

    @classmethod
    def app(cls, content: str) -> Self:
        """App 消息"""
        return cls(type="App", content=content)

    @classmethod
    def poke(cls, name: str) -> Self:
        """Poke 消息"""
        return cls(type="Poke", name=name)

    @classmethod
    def dice(cls, value: int) -> Self:
        """Dice 消息"""
        return cls(type="Dice", value=value)

    @classmethod
    def music_share(
        cls,
        kind: str,
        title: str,
        summary: str,
        jump_url: str,
        picture_url: str,
        music_url: str,
        brief: str,
    ) -> Self:
        """MusicShare 消息"""
        return cls(
            type="MusicShare",
            kind=kind,
            title=title,
            summary=summary,
            jumpUrl=jump_url,
            pictureUrl=picture_url,
            musicUrl=music_url,
            brief=brief,
        )
