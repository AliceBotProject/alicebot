"""事件基类。"""
# pyright: reportIncompatibleVariableOverride=false

from typing import TYPE_CHECKING, Literal

from pydantic import BaseModel

from alicebot.event import Event

if TYPE_CHECKING:
    from .. import MiraiAdapter

Permission = Literal["OWNER", "ADMINISTRATOR", "MEMBER"]


class Subject(BaseModel):
    """来源"""

    id: int
    kind: Literal["Friend", "Group"]


class FriendInfo(BaseModel):
    """好友信息"""

    id: int
    nickname: str
    remark: str


class GroupInfo(BaseModel):
    """群聊信息"""

    id: int
    name: str
    permission: Permission


class GroupMemberInfo(BaseModel):
    """群成员信息"""

    id: int
    memberName: str
    permission: Permission
    specialTitle: str
    joinTimestamp: int
    lastSpeakTimestamp: int
    muteTimeRemaining: int
    group: GroupInfo


class OtherClientSender(BaseModel):
    """其他客户端信息"""

    id: int
    platform: str


class MiraiEvent(Event["MiraiAdapter"]):
    """Mirai 事件基类"""

    type: str
