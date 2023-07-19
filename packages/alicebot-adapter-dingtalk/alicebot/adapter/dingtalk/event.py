"""DingTalk 适配器事件。"""
from __future__ import annotations

import time
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, Field

from alicebot.event import MessageEvent

from .exceptions import WebhookExpiredError
from .message import DingTalkMessage

if TYPE_CHECKING:
    from typing_extensions import Self

    from . import DingTalkAdapter  # noqa: F401

__all__ = ["UserInfo", "Text", "DingTalkEvent"]


class UserInfo(BaseModel):
    """用户信息"""

    dingtalkId: str
    staffId: str | None = None


class Text(BaseModel):
    """文本消息"""

    content: str


class DingTalkEvent(MessageEvent["DingTalkAdapter"]):
    """DingTalk 事件基类"""

    type: str | None = Field(alias="msgtype")

    msgtype: str
    msgId: str
    createAt: str
    conversationType: Literal["1", "2"]
    conversationId: str
    conversationTitle: str | None = None
    senderId: str
    senderNick: str
    senderCorpId: str | None = None
    sessionWebhook: str
    sessionWebhookExpiredTime: int
    isAdmin: bool | None = None
    chatbotCorpId: str | None = None
    isInAtList: bool | None = None
    senderStaffId: str | None = None
    chatbotUserId: str
    atUsers: list[UserInfo]
    text: Text

    response_msg: None | str | dict[str, Any] | DingTalkMessage = None
    response_at: None | dict[str, Any] | DingTalkMessage = None

    @property
    def message(self) -> DingTalkMessage:
        """返回 message 字段。"""
        return DingTalkMessage.text(self.text.content)

    def get_plain_text(self) -> str:
        """获取消息的纯文本内容。

        Returns:
            消息的纯文本内容。
        """
        return self.message.get_plain_text()

    async def reply(
        self,
        message: str | dict[str, Any] | DingTalkMessage,
        at: None | dict[str, Any] | DingTalkMessage = None,
    ) -> dict[str, Any]:
        """回复消息。

        Args:
            message: 回复消息的内容，可以是 `str`, `Dict` 或 `DingTalkMessage`。
            at: 回复消息时 At 的对象，必须时 at 类型的 `DingTalkMessage`，或者符合标准的 `Dict`。

        Returns:
            调用 Webhook 地址后钉钉服务器的响应。

        Raises:
            WebhookExpiredError: 当前事件的 Webhook 地址已经过期。
            ...: 同 `DingTalkAdapter.send()` 方法。
        """
        if self.sessionWebhookExpiredTime > time.time() * 1000:
            return await self.adapter.send(
                webhook=self.sessionWebhook,
                conversation_type=self.conversationType,
                msg=message,
                at=at,
            )
        raise WebhookExpiredError

    async def is_same_sender(self, other: Self) -> bool:
        """判断自身和另一个事件是否是同一个发送者。

        Args:
            other: 另一个事件。

        Returns:
            是否是同一个发送者。
        """
        return self.senderId == other.senderId
