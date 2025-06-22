"""DingTalk 适配器消息。"""

from typing import Any
from typing_extensions import override

from pydantic import model_serializer

from alicebot.message import MessageSegment

__all__ = ["DingTalkMessage"]


class DingTalkMessage(MessageSegment):  # type: ignore
    """DingTalk 消息"""

    @override
    @classmethod
    def get_message_class(cls) -> None:  # type: ignore
        return None

    @override
    def __str__(self) -> str:
        if self.type == "text":
            return self.data["content"]
        return super().__str__()

    @model_serializer
    def ser_model(self) -> dict[str, Any]:
        """返回符合钉钉消息标准的消息字段字典。

        Returns:
            符合钉钉消息标准的消息字段字典。
        """
        if self.type == "raw":
            return self.data
        return {self.type: self.data}

    def get_plain_text(self) -> str:
        """获取消息中的纯文本部分。

        Returns:
            消息中的纯文本部分。
        """
        if self.type == "text":
            return self.data["content"]
        return ""

    @classmethod
    def raw(cls, data: dict[str, Any]) -> "DingTalkMessage":
        """DingTalk 原始消息"""
        return cls(type="raw", data=data)

    @classmethod
    def text(cls, content: str) -> "DingTalkMessage":
        """DingTalk text 消息"""
        return cls(type="text", data={"content": content})

    @classmethod
    def link(
        cls, text: str, title: str, message_url: str, pic_url: str | None = None
    ) -> "DingTalkMessage":
        """DingTalk link 消息"""
        return cls(
            type="link",
            data={
                "text": text,
                "title": title,
                "messageUrl": message_url,
                "picUrl": pic_url,
            },
        )

    @classmethod
    def markdown(cls, title: str, text: str) -> "DingTalkMessage":
        """DingTalk markdown 消息"""
        return cls(type="markdown", data={"title": title, "text": text})

    @classmethod
    def action_card_single_btn(
        cls,
        title: str,
        text: str,
        single_title: str,
        single_url: str,
        btn_orientation: str = "0",
    ) -> "DingTalkMessage":
        """DingTalk 整体跳转 actionCard 消息"""
        return cls(
            type="actionCard",
            data={
                "title": title,
                "text": text,
                "singleTitle": single_title,
                "singleURL": single_url,
                "btnOrientation": btn_orientation,
            },
        )

    @classmethod
    def action_card_multi_btns(
        cls, title: str, text: str, btns: list[Any], btn_orientation: str = "0"
    ) -> "DingTalkMessage":
        """DingTalk 独立跳转 actionCard 消息"""
        return cls(
            type="actionCard",
            data={
                "title": title,
                "text": text,
                "btns": btns,
                "btnOrientation": btn_orientation,
            },
        )

    @classmethod
    def feed_card(cls, links: list[Any]) -> "DingTalkMessage":
        """DingTalk feedCard 消息"""
        return cls(type="feedCard", data={"links": links})

    @classmethod
    def at(
        cls,
        at_mobiles: list[str] | None = None,
        at_user_ids: list[str] | None = None,
        is_at_all: bool = False,
    ) -> "DingTalkMessage":
        """DingTalk At 信息"""
        return cls(
            type="at",
            data={
                "atMobiles": at_mobiles,
                "atUserIds": at_user_ids,
                "isAtAll": is_at_all,
            },
        )
