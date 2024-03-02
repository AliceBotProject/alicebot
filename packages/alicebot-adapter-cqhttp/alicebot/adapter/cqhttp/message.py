"""CQHTTP 适配器消息。"""

from typing import Literal, Optional, Type, Union
from typing_extensions import Self

from alicebot.message import Message, MessageSegment

__all__ = ["CQHTTPMessage", "CQHTTPMessageSegment", "escape"]


class CQHTTPMessage(Message["CQHTTPMessageSegment"]):
    """CQHTTP 消息。"""

    @classmethod
    def get_segment_class(cls) -> Type["CQHTTPMessageSegment"]:
        """获取消息字段类。

        Returns:
            消息字段类。
        """
        return CQHTTPMessageSegment


class CQHTTPMessageSegment(MessageSegment["CQHTTPMessage"]):
    """CQHTTP 消息字段。"""

    @classmethod
    def get_message_class(cls) -> Type[CQHTTPMessage]:
        """获取消息类。

        Returns:
            消息类。
        """
        return CQHTTPMessage

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
        """返回消息字段的文本表示。

        Returns:
            消息字段的文本表示。
        """
        if self.type == "text":
            return self.data.get("text", "")
        return self.get_cqcode()

    def get_cqcode(self) -> str:
        """获取此消息字段的 CQ 码形式。

        Returns:
            此消息字段的 CQ 码形式。
        """
        if self.type == "text":
            return escape(self.data.get("text", ""), escape_comma=False)

        params = ",".join(
            [f"{k}={escape(str(v))}" for k, v in self.data.items() if v is not None]
        )
        return f'[CQ:{self.type}{"," if params else ""}{params}]'

    @classmethod
    def text(cls, text: str) -> Self:
        """纯文本"""
        return cls(type="text", data={"text": text})

    @classmethod
    def face(cls, id_: int) -> Self:
        """QQ 表情"""
        return cls(type="face", data={"id": str(id_)})

    @classmethod
    def image(
        cls,
        file: str,
        type_: Optional[Literal["flash"]] = None,
        cache: bool = True,
        proxy: bool = True,
        timeout: Optional[int] = None,
    ) -> Self:
        """图片"""
        return cls(
            type="image",
            data={
                "file": file,
                "type": type_,
                "cache": cache,
                "proxy": proxy,
                "timeout": timeout,
            },
        )

    @classmethod
    def record(
        cls,
        file: str,
        magic: bool = False,
        cache: bool = True,
        proxy: bool = True,
        timeout: Optional[int] = None,
    ) -> Self:
        """语音"""
        return cls(
            type="record",
            data={
                "file": file,
                "magic": magic,
                "cache": cache,
                "proxy": proxy,
                "timeout": timeout,
            },
        )

    @classmethod
    def video(
        cls,
        file: str,
        cache: bool = True,
        proxy: bool = True,
        timeout: Optional[int] = None,
    ) -> Self:
        """短视频"""
        return cls(
            type="video",
            data={"file": file, "cache": cache, "proxy": proxy, "timeout": timeout},
        )

    @classmethod
    def at(cls, qq: Union[int, Literal["all"]]) -> Self:  # pylint: disable=invalid-name
        """@某人"""
        return cls(type="at", data={"qq": str(qq)})

    @classmethod
    def rps(cls) -> Self:
        """猜拳魔法表情"""
        return cls(type="rps", data={})

    @classmethod
    def dice(cls) -> Self:
        """掷骰子魔法表情"""
        return cls(type="dice", data={})

    @classmethod
    def shake(cls) -> Self:
        """窗口抖动 (戳一戳)"""
        return cls(type="shake", data={})

    @classmethod
    def poke(cls, type_: str, id_: int) -> Self:
        """戳一戳"""
        return cls(type="poke", data={"type": type_, "id": str(id_)})

    @classmethod
    def anonymous(cls, ignore: Optional[bool] = None) -> Self:
        """匿名发消息"""
        return cls(type="anonymous", data={"ignore": ignore})

    @classmethod
    def share(
        cls,
        url: str,
        title: str,
        content: Optional[str] = None,
        image: Optional[str] = None,
    ) -> Self:
        """链接分享"""
        return cls(
            type="share",
            data={"url": url, "title": title, "content": content, "image": image},
        )

    @classmethod
    def contact(cls, type_: Literal["qq", "group"], id_: int) -> Self:
        """推荐好友/推荐群"""
        return cls(type="contact", data={"type": type_, "id": str(id_)})

    @classmethod
    def contact_friend(cls, id_: int) -> Self:
        """推荐好友"""
        return cls(type="contact", data={"type": "qq", "id": str(id_)})

    @classmethod
    def contact_group(cls, id_: int) -> Self:
        """推荐好友"""
        return cls(type="contact", data={"type": "group", "id": str(id_)})

    @classmethod
    def location(
        cls, lat: float, lon: float, title: Optional[str], content: Optional[str] = None
    ) -> Self:
        """位置"""
        return cls(
            type="location",
            data={"lat": str(lat), "lon": str(lon), "title": title, "content": content},
        )

    @classmethod
    def music(cls, type_: Literal["qq", "163", "xm"], id_: int) -> Self:
        """音乐分享"""
        return cls(type="music", data={"type": type_, "id": str(id_)})

    @classmethod
    def music_custom(
        cls,
        url: str,
        audio: str,
        title: str,
        content: Optional[str] = None,
        image: Optional[str] = None,
    ) -> Self:
        """音乐自定义分享"""
        return cls(
            type="music",
            data={
                "type": "custom",
                "url": url,
                "audio": audio,
                "title": title,
                "content": content,
                "image": image,
            },
        )

    @classmethod
    def reply(cls, id_: int) -> Self:
        """回复"""
        return cls(type="reply", data={"id": str(id_)})

    @classmethod
    def node(cls, id_: int) -> Self:
        """合并转发节点"""
        return cls(type="node", data={"id": str(id_)})

    @classmethod
    def node_custom(cls, user_id: int, nickname: str, content: "CQHTTPMessage") -> Self:
        """合并转发自定义节点"""
        return cls(
            type="node",
            data={
                "user_id": str(user_id),
                "nickname": str(nickname),
                "content": content,
            },
        )

    @classmethod
    def xml_message(cls, data: str) -> Self:
        """XML 消息"""
        return cls(type="xml", data={"data": data})

    @classmethod
    def json_message(cls, data: str) -> Self:
        """JSON 消息"""
        return cls(type="json", data={"data": data})


def escape(string: str, *, escape_comma: bool = True) -> str:
    """对 CQ 码中的特殊字符进行转义。

    Args:
        string: 待转义的字符串。
        escape_comma: 是否转义 `,`。

    Returns:
        转义后的字符串。
    """
    string = string.replace("&", "&amp;").replace("[", "&#91;").replace("]", "&#93;")
    if escape_comma:
        string = string.replace(",", "&#44;")
    return string
