"""默认不会被传播的特殊事件。"""
# pyright: reportIncompatibleVariableOverride=false

from typing import Any, List, Literal, Optional

from .base import FriendInfo, GroupMemberInfo, MiraiEvent


class MetaEvent(MiraiEvent):
    """默认不会被传播的特殊事件"""


class BotEvent(MetaEvent):
    """Bot 自身事件"""

    qq: int


class BotOnlineEvent(BotEvent):
    """Bot 登录成功"""

    type: Literal["BotOnlineEvent"]


class BotOfflineEventActive(BotEvent):
    """Bot 主动离线"""

    type: Literal["BotOfflineEventActive"]


class BotOfflineEventForce(BotEvent):
    """Bot 被挤下线"""

    type: Literal["BotOfflineEventForce"]


class BotOfflineEventDropped(BotEvent):
    """Bot 被服务器断开或因网络问题而掉线"""

    type: Literal["BotOfflineEventDropped"]


class BotReloginEvent(BotEvent):
    """Bot 主动重新登录"""

    type: Literal["BotReloginEvent"]


class CommandExecutedEvent(MetaEvent):
    """命令被执行"""

    type: Literal["CommandExecutedEvent"]
    name: str
    friend: Optional[FriendInfo] = None
    member: Optional[GroupMemberInfo] = None
    args: List[Any]
