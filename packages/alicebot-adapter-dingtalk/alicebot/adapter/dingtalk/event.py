"""
============
DingTalk 事件
============
"""
from typing import Dict, List, Literal, Optional, Union

from pydantic import BaseModel, Field, validator

from alicebot.event import Event

from .message import DingTalkMessage


class UserInfo(BaseModel):
    dingtalkId: str
    staffId: Optional[str]


class Text(BaseModel):
    content: str


class DingTalkEvent(Event):
    """DingTalk 事件基类"""
    type: Optional[str] = Field(alias='msgtype')

    msgtype: str
    msgId: str
    createAt: str
    conversationType: Literal['1', '2']
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

    @validator('message', always=True)
    def set_ts_now(cls, v, values, **kwargs):
        return DingTalkMessage.text(values['text'].content)

    async def replay(self, msg: Union[str, Dict, DingTalkMessage], at: Union[None, Dict, DingTalkMessage] = None):

        if isinstance(msg, DingTalkMessage):
            pass
        elif isinstance(msg, dict):
            msg = DingTalkMessage.raw(msg)
        elif isinstance(msg, str):
            msg = DingTalkMessage.text(msg)
        else:
            raise TypeError(f'msg must be str, Dict or DingTalkMessage, not {type(msg)!r}')

        if at is not None:
            if isinstance(at, DingTalkMessage):
                if at.type == 'at':
                    pass
                else:
                    raise ValueError(f'at.type must be "at", not {at.type}')
            elif isinstance(at, dict):
                at = DingTalkMessage.raw(at)
            else:
                raise TypeError(f'at must be Dict or DingTalkMessage, not {type(at)!r}')

        self.response_msg = msg
        self.response_at = at
