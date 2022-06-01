"""DingTalk 适配器事件。"""
import time
from typing import TYPE_CHECKING, Any, Dict, List, Union, Literal, Optional

from pydantic import Field, BaseModel, validator

from alicebot.event import Event

from .message import DingTalkMessage
from .exceptions import WebhookExpiredError

if TYPE_CHECKING:
    from . import DingTalkAdapter  # noqa


class UserInfo(BaseModel):
    dingtalkId: str
    staffId: Optional[str]


class Text(BaseModel):
    content: str


class DingTalkEvent(Event["DingTalkAdapter"]):
    """DingTalk 事件基类"""

    type: Optional[str] = Field(alias="msgtype")

    msgtype: str
    msgId: str
    createAt: str
    conversationType: Literal["1", "2"]
    conversationId: str
    conversationTitle: Optional[str]
    senderId: str
    senderNick: str
    senderCorpId: Optional[str]
    sessionWebhook: str
    sessionWebhookExpiredTime: int
    isAdmin: Optional[bool]
    chatbotCorpId: Optional[str]
    isInAtList: Optional[bool]
    senderStaffId: Optional[str]
    chatbotUserId: str
    atUsers: List[UserInfo]
    text: Text

    message: Optional[DingTalkMessage]
    response_msg: Union[None, str, Dict, DingTalkMessage] = None
    response_at: Union[None, Dict, DingTalkMessage] = None

    @validator("message", always=True)
    def set_ts_now(cls, v, values, **kwargs):  # noqa
        return DingTalkMessage.text(values["text"].content)

    async def reply(
        self,
        msg: Union[str, Dict, DingTalkMessage],
        at: Union[None, Dict, DingTalkMessage] = None,
    ) -> Dict[str, Any]:
        """回复消息。

        Args:
            msg: 回复消息的内容，可以是 str, Dict 或 DingTalkMessage。
            at: 回复消息时 At 的对象，必须时 at 类型的 DingTalkMessage，或者符合标准的 Dict。

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
                msg=msg,
                at=at,
            )
        else:
            raise WebhookExpiredError
