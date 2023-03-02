"""Mirai 适配器消息。"""
import json
from typing import Any, Dict, List, Type, Union, Mapping, Iterable, Optional

from alicebot.utils import DataclassEncoder
from alicebot.message import Message, MessageSegment

__all__ = ["T_MiraiMSG", "MiraiMessage", "MiraiMessageSegment"]

T_MiraiMSG = Union[
    str, Mapping, Iterable[Mapping], "MiraiMessageSegment", "MiraiMessage"
]


class MiraiMessage(Message["MiraiMessageSegment"]):
    @property
    def _message_segment_class(self) -> Type["MiraiMessageSegment"]:
        return MiraiMessageSegment

    def _str_to_message_segment(self, msg: str) -> "MiraiMessageSegment":
        return self._message_segment_class.plain(msg)

    def as_message_chain(self) -> List[Dict[str, Any]]:
        """返回符合 Mirai-api-http 标准的 messageChain 数组。

        Returns:
            messageChain 数组。
        """
        return list(map(lambda x: x.as_dict(), self))


class MiraiMessageSegment(MessageSegment["MiraiMessage"]):
    def __init__(self, type: str, **data):  # noqa
        super().__init__(
            type=type, data={k: v for k, v in data.items() if v is not None}
        )

    @property
    def _message_class(self) -> Type["MiraiMessage"]:
        return MiraiMessage

    def __str__(self) -> str:
        if self.type == "Plain":
            return self.data.get("text", "")
        return json.dumps(self, cls=DataclassEncoder)

    def as_dict(self) -> Dict[str, Any]:
        """返回符合 Mirai-api-http 标准的消息字段字典。

        Returns:
            符合 Mirai-api-http 标准的消息字段字典。
        """
        return {"type": self.type, **self.data}

    def is_text(self) -> bool:
        """
        Returns:
            是否是纯文本消息字段。
        """
        return self.type == "Plain"

    @classmethod
    def source(cls, id_: int, time: int):
        return cls(type="Source", id=id_, time=time)

    @classmethod
    def quote(
        cls,
        id_: int,
        group_id: int,
        sender_id: int,
        target_id: int,
        origin: MiraiMessage,
    ):
        return cls(
            type="Quote",
            id=id_,
            groupId=group_id,
            senderId=sender_id,
            targetId=target_id,
            origin=origin.as_message_chain(),
        )

    @classmethod
    def at(cls, target: int):
        return cls(type="At", target=target)

    @classmethod
    def at_all(cls):
        return cls(type="AtAll")

    @classmethod
    def face(cls, face_id: Optional[int] = None, name: Optional[str] = None):
        return cls(type="Face", faceId=face_id, name=name)

    @classmethod
    def plain(cls, text: str):
        return cls(type="Plain", text=text)

    @classmethod
    def image(
        cls,
        image_id: Optional[str] = None,
        url: Optional[str] = None,
        path: Optional[str] = None,
    ):
        return cls(type="Image", imageId=image_id, url=url, path=path)

    @classmethod
    def flash_image(
        cls,
        image_id: Optional[str] = None,
        url: Optional[str] = None,
        path: Optional[str] = None,
    ):
        return cls(type="FlashImage", imageId=image_id, url=url, path=path)

    @classmethod
    def voice(
        cls,
        voice_id: Optional[str] = None,
        url: Optional[str] = None,
        path: Optional[str] = None,
    ):
        return cls(type="Voice", imageId=voice_id, url=url, path=path)

    @classmethod
    def xml(cls, xml: str):
        return cls(type="Xml", xml=xml)

    @classmethod
    def json(cls, json_: str):
        return cls(type="Json", json=json_)

    @classmethod
    def app(cls, content: str):
        return cls(type="App", content=content)

    @classmethod
    def poke(cls, name: str):
        return cls(type="Poke", name=name)

    @classmethod
    def dice(cls, value: int):
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
    ):
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
