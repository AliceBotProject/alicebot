from typing import Literal

from pydantic import create_model

from .base import (
    Subject,
    GroupInfo,
    FriendInfo,
    MiraiEvent,
    Permission,
    GroupMemberInfo,
)


class NoticeEvent(MiraiEvent):
    """通知事件"""


class NudgeEvent(NoticeEvent):
    """戳一戳事件"""

    type: Literal["NudgeEvent"]
    fromId: int
    subject: Subject
    action: str
    suffix: str
    target: int


class FriendEvent(NoticeEvent):
    """好友事件"""

    friend: FriendInfo


class FriendInputStatusChangedEvent(FriendEvent):
    """好友输入状态改变"""

    type: Literal["FriendInputStatusChangedEvent"]
    inputting: bool


# 因为 from 是 python 关键字，所以不能直接定义
FriendNickChangedEvent = create_model(
    "FriendNickChangedEvent",
    **{
        "type": (Literal["FriendNickChangedEvent"], None),
        "from": (str, None),
        "to": (str, None),
    },
    __base__=FriendEvent,
)
"""好友昵称改变"""


class FriendRecallEvent(FriendEvent):
    """好友消息撤回"""

    type: Literal["FriendRecallEvent"]
    authorId: int
    messageId: int
    time: int
    operator: int


class GroupEvent(NoticeEvent):
    """群事件"""


class GroupBotEvent(GroupEvent):
    """与 Bot 相关的群事件"""


class BotGroupPermissionChangeEvent(GroupBotEvent):
    """Bot 在群里的权限被改变. 操作人一定是群主"""

    type: Literal["BotGroupPermissionChangeEvent"]
    origin: Permission
    current: Permission
    group: GroupInfo


class BotMuteEvent(GroupBotEvent):
    """Bot 被禁言"""

    type: Literal["BotMuteEvent"]
    operator: GroupMemberInfo


class BotUnmuteEvent(GroupBotEvent):
    """Bot 被取消禁言"""

    type: Literal["BotUnmuteEvent"]
    operator: GroupMemberInfo


class BotJoinGroupEvent(GroupBotEvent):
    """Bot加入了一个新群"""

    type: Literal["BotJoinGroupEvent"]
    group: GroupInfo


class BotLeaveEventActive(GroupBotEvent):
    """Bot 主动退出一个群"""

    type: Literal["BotLeaveEventActive"]
    group: GroupInfo


class BotLeaveEventKick(GroupBotEvent):
    """Bot 被踢出一个群"""

    type: Literal["BotLeaveEventKick"]
    group: GroupInfo


class GroupNoticeEvent(GroupEvent):
    """其他群事件"""


class GroupRecallEvent(GroupNoticeEvent):
    """群消息撤回"""

    type: Literal["GroupRecallEvent"]
    authorId: int
    messageId: int
    time: int
    group: GroupInfo
    operator: GroupMemberInfo


class GroupNameChangeEvent(GroupNoticeEvent):
    """某个群名改变"""

    type: Literal["GroupNameChangeEvent"]
    origin: str
    current: str
    group: GroupInfo
    operator: GroupMemberInfo


class GroupEntranceAnnouncementChangeEvent(GroupNoticeEvent):
    """某群入群公告改变"""

    type: Literal["GroupEntranceAnnouncementChangeEvent"]
    origin: str
    current: str
    group: GroupInfo
    operator: GroupMemberInfo


class GroupMuteAllEvent(GroupNoticeEvent):
    """全员禁言"""

    type: Literal["GroupMuteAllEvent"]
    origin: bool
    current: bool
    group: GroupInfo
    operator: GroupMemberInfo


class GroupAllowAnonymousChatEvent(GroupNoticeEvent):
    """匿名聊天"""

    type: Literal["GroupAllowAnonymousChatEvent"]
    origin: bool
    current: bool
    group: GroupInfo
    operator: GroupMemberInfo


class GroupAllowConfessTalkEvent(GroupNoticeEvent):
    """坦白说"""

    type: Literal["GroupAllowAnonymousChatEvent"]
    origin: bool
    current: bool
    group: GroupInfo
    isByBot: bool


class GroupAllowMemberInviteEvent(GroupNoticeEvent):
    """允许群员邀请好友加群"""

    type: Literal["GroupAllowMemberInviteEvent"]
    origin: bool
    current: bool
    group: GroupInfo
    operator: GroupMemberInfo


class GroupMemberEvent(GroupEvent):
    """群成员相关事件"""

    member: GroupMemberInfo


class MemberJoinEvent(GroupMemberEvent):
    """新人入群的事件"""

    type: Literal["MemberJoinEvent"]


class MemberLeaveEventKick(GroupMemberEvent):
    """成员被踢出群（该成员不是Bot）"""

    type: Literal["MemberLeaveEventKick"]
    operator: GroupMemberInfo


class MemberLeaveEventQuit(GroupMemberEvent):
    """成员主动离群（该成员不是Bot）"""

    type: Literal["MemberLeaveEventQuit"]


class MemberCardChangeEvent(GroupMemberEvent):
    """群名片改动"""

    type: Literal["MemberCardChangeEvent"]
    origin: str
    current: str


class MemberSpecialTitleChangeEvent(GroupMemberEvent):
    """群头衔改动（只有群主有操作限权）"""

    type: Literal["MemberSpecialTitleChangeEvent"]
    origin: str
    current: str


class MemberPermissionChangeEvent(GroupMemberEvent):
    """成员权限改变的事件（该成员不是Bot）"""

    type: Literal["MemberPermissionChangeEvent"]
    origin: Permission
    current: Permission


class MemberMuteEvent(GroupMemberEvent):
    """群成员被禁言事件（该成员不是Bot）"""

    type: Literal["MemberMuteEvent"]
    durationSeconds: int
    operator: GroupMemberInfo


class MemberUnmuteEvent(GroupMemberEvent):
    """群成员被取消禁言事件（该成员不是Bot）"""

    type: Literal["MemberUnmuteEvent"]
    operator: GroupMemberInfo


class MemberHonorChangeEvent(GroupMemberEvent):
    """群员称号改变"""

    type: Literal["MemberHonorChangeEvent"]
    action: Literal["achieve", "lose"]
