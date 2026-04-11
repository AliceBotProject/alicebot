"""事件基类。"""
# pyright: reportIncompatibleVariableOverride=false

from typing import TYPE_CHECKING, Literal, override

from pydantic import BaseModel, ConfigDict

from alicebot.event import Event

if TYPE_CHECKING:
    from .. import MiraiAdapter  # noqa: TID252

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


class MiraiEvent(BaseModel, Event["MiraiAdapter"]):  # pyright: ignore[reportUnsafeMultipleInheritance]
    """Mirai 事件基类"""

    model_config = ConfigDict(extra="allow")

    _adapter: "MiraiAdapter"

    type: str

    @property
    @override
    def adapter(self) -> "MiraiAdapter":
        return self._adapter

    @adapter.setter
    def adapter(self, value: "MiraiAdapter") -> None:
        self._adapter = value

    @override
    def __str__(self) -> str:
        return f"<{self.__class__.__name__} type={self.type}>"

    @override
    def __repr__(self) -> str:
        return self.__str__()
