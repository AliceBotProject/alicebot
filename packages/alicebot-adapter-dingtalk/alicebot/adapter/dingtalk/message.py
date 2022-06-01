"""DingTalk 适配器消息。"""
from typing import Any, Dict, List, Optional

from alicebot.message import MessageSegment

__all__ = ["DingTalkMessage"]


class DingTalkMessage(MessageSegment[None]):
    """DingTalk 消息"""

    @property
    def _message_class(self) -> None:
        return None

    def __str__(self):
        if self.type == "text":
            return self.data["content"]
        else:
            return super().__str__()

    def as_dict(self) -> Dict[str, Dict[str, Any]]:
        """返回符合钉钉消息标准的消息字段字典。

        Returns:
            符合钉钉消息标准的消息字段字典。
        """
        if self.type == "raw":
            return self.data
        else:
            return {self.type: self.data}

    @classmethod
    def raw(cls, data: Dict[str, Any]) -> "DingTalkMessage":
        """DingTalk 原始消息"""
        return cls(type="raw", data=data)

    @classmethod
    def text(cls, content: str) -> "DingTalkMessage":
        """DingTalk text 消息"""
        return cls(type="text", data={"content": content})

    @classmethod
    def link(
        cls, text: str, title: str, message_url: str, pic_url: Optional[str] = None
    ):
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
    def markdown(cls, title: str, text: str):
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
    ):
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
        cls, title: str, text: str, btns: list, btn_orientation: str = "0"
    ):
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
    def feed_card(cls, links: list):
        """DingTalk feedCard 消息"""
        return cls(type="feedCard", data={"links": links})

    @classmethod
    def at(
        cls,
        at_mobiles: Optional[List[str]] = None,
        at_user_ids: Optional[List[str]] = None,
        is_at_all: bool = False,
    ):
        """DingTalk At 信息"""
        return cls(
            type="at",
            data={
                "atMobiles": at_mobiles,
                "atUserIds": at_user_ids,
                "isAtAll": is_at_all,
            },
        )
