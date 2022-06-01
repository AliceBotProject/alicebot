from typing import TYPE_CHECKING, Literal, TypeVar

from pydantic import BaseModel

from alicebot.event import Event

if TYPE_CHECKING:
    from .. import MiraiAdapter  # noqa

T_MiraiEvent = TypeVar("T_MiraiEvent", bound="MiraiEvent")

Permission = Literal["OWNER", "ADMINISTRATOR", "MEMBER"]


class Subject(BaseModel):
    id: int
    kind: Literal["Friend", "Group"]


class FriendInfo(BaseModel):
    id: int
    nickname: str
    remark: str


class GroupInfo(BaseModel):
    id: int
    name: str
    permission: Permission


class GroupMemberInfo(BaseModel):
    id: int
    memberName: str
    permission: Permission
    specialTitle: str
    joinTimestamp: int
    lastSpeakTimestamp: int
    muteTimeRemaining: int
    group: GroupInfo


class OtherClientSender(BaseModel):
    id: int
    platform: str


class MiraiEvent(Event["MiraiAdapter"]):
    """Mirai 事件基类"""

    type: str
