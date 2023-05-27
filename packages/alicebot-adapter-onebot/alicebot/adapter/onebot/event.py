"""OntBot 适配器事件。"""
from typing import TYPE_CHECKING, Any, Dict, List, Literal, Optional, Tuple
from typing_extensions import Self

from pydantic import BaseModel, Extra
from pydantic.fields import ModelField
from pydantic.typing import all_literal_values, is_literal_type

from alicebot.event import Event
from alicebot.event import MessageEvent as BaseMessageEvent

from .message import OneBotMessage

if TYPE_CHECKING:
    from . import OneBotAdapter  # noqa: F401
    from .message import T_OBMSG


class BotSelf(BaseModel):
    """机器人自身标识"""

    platform: str
    user_id: str


class ImplVersion(BaseModel):
    """实现版本"""

    impl: str
    version: str
    onebot_version: str


class BotStatus(BaseModel):
    """机器人状态"""

    self: BotSelf
    online: bool


class Status(BaseModel, extra=Extra.allow):
    """运行状态"""

    good: bool
    bots: List[BotStatus]


def _get_literal_field(field: ModelField) -> Optional[str]:
    if not is_literal_type(field.outer_type_):
        return None
    literal_values = all_literal_values(field.outer_type_)
    if len(literal_values) != 1:
        return None
    return literal_values[0]


class OntBotEvent(Event["OneBotAdapter"]):
    """CQHTTP 事件基类"""

    id: str
    time: float
    type: Literal["meta", "message", "notice", "request"]
    detail_type: str
    sub_type: str

    @classmethod
    def get_event_type(cls) -> Tuple[Optional[str], Optional[str], Optional[str]]:
        """获取事件类型。

        Returns:
            事件类型。
        """
        type_field = cls.__fields__.get("type", None)
        type = type_field and _get_literal_field(type_field)
        detail_type_field = cls.__fields__.get("detail_type", None)
        detail_type = detail_type_field and _get_literal_field(detail_type_field)
        sub_type_field = cls.__fields__.get("sub_type", None)
        sub_type = sub_type_field and _get_literal_field(sub_type_field)
        return (type, detail_type, sub_type)


class BotEvent(OntBotEvent):
    """包含 self 字段的机器人事件"""

    self: BotSelf

    @property
    def to_me(self) -> bool:
        """是否是发给自己的。"""
        return getattr(self, "user_id", None) == self.self.user_id


class MetaEvent(OntBotEvent):
    """元事件"""

    type: Literal["meta"]


class ConnectMetaEvent(MetaEvent):
    """连接事件"""

    detail_type: Literal["connect"]
    version: ImplVersion


class HeartbeatMetaEvent(MetaEvent):
    """心跳事件"""

    detail_type: Literal["heartbeat"]
    interval: int


class StatusUpdateMetaEvent(MetaEvent):
    """状态更新事件"""

    detail_type: Literal["status_update"]
    status: Status


class MessageEvent(BotEvent, BaseMessageEvent["OneBotAdapter", OneBotMessage]):
    """消息事件"""

    type: Literal["message"]
    message_id: str
    message: OneBotMessage
    alt_message: str
    user_id: str

    def __repr__(self) -> str:
        return f'Event<{self.type}>: "{self.message}"'

    def get_plain_text(self) -> str:
        """获取消息的纯文本内容。

        Returns:
            消息的纯文本内容。
        """
        return self.message.get_plain_text()

    async def reply(self, message: "T_OBMSG") -> Dict[str, Any]:
        """回复消息。

        Args:
            message: 回复消息的内容，同 `call_api()` 方法。

        Returns:
            API 请求响应。
        """
        raise NotImplementedError

    async def is_same_sender(self, other: Self) -> bool:
        """判断自身和另一个事件是否是同一个发送者。

        Args:
            other: 另一个事件。

        Returns:
            是否是同一个发送者。
        """
        return self.user_id == other.user_id


class PrivateMessageEvent(MessageEvent):
    """私聊消息事件"""

    detail_type: Literal["private"]

    async def reply(self, message: "T_OBMSG") -> Dict[str, Any]:
        """回复消息。

        Args:
            message: 回复消息的内容，同 `call_api()` 方法。

        Returns:
            API 请求响应。
        """
        return await self.adapter.send_message(
            detail_type="private",
            user_id=self.user_id,
            message=message,
        )


class GroupMessageEvent(MessageEvent):
    """群消息事件"""

    detail_type: Literal["group"]
    group_id: str

    async def reply(self, message: "T_OBMSG") -> Dict[str, Any]:
        """回复消息。

        Args:
            message: 回复消息的内容，同 `call_api()` 方法。

        Returns:
            API 请求响应。
        """
        return await self.adapter.send_message(
            detail_type="group",
            group_id=self.group_id,
            message=message,
        )


class ChannelMessageEvent(MessageEvent):
    """频道消息事件"""

    detail_type: Literal["channel"]
    guild_id: str
    channel_id: str

    async def reply(self, message: "T_OBMSG") -> Dict[str, Any]:
        """回复消息。

        Args:
            message: 回复消息的内容，同 `call_api()` 方法。

        Returns:
            API 请求响应。
        """
        return await self.adapter.send_message(
            detail_type="channel",
            guild_id=self.guild_id,
            channel_id=self.channel_id,
            message=message,
        )


class NoticeEvent(BotEvent):
    """通知事件"""

    type: Literal["notice"]


class FriendIncreaseEvent(NoticeEvent):
    """好友增加事件"""

    detail_type: Literal["friend_increase"]
    user_id: str


class FriendDecreaseEvent(NoticeEvent):
    """好友减少事件"""

    detail_type: Literal["friend_decrease"]
    user_id: str


class PrivateMessageDeleteEvent(NoticeEvent):
    """私聊消息删除"""

    detail_type: Literal["private_message_delete"]
    message_id: str
    user_id: str


class GroupMemberIncreaseEvent(NoticeEvent):
    """群成员增加事件"""

    detail_type: Literal["group_member_increase"]
    group_id: str
    user_id: str
    operator_id: str


class GroupMemberDecreaseEvent(NoticeEvent):
    """群成员减少事件"""

    detail_type: Literal["group_member_decrease"]
    group_id: str
    user_id: str
    operator_id: str


class GroupMessageDeleteEvent(NoticeEvent):
    """群消息删除事件"""

    detail_type: Literal["group_message_delete"]
    group_id: str
    message_id: str
    user_id: str
    operator_id: str


class GuildMemberIncreaseEvent(NoticeEvent):
    """群组成员增加事件"""

    detail_type: Literal["guild_member_increase"]
    guild_id: str
    user_id: str
    operator_id: str


class GuildMemberDecreaseEvent(NoticeEvent):
    """群组成员减少事件"""

    detail_type: Literal["guild_member_decrease"]
    guild_id: str
    user_id: str
    operator_id: str


class ChannelMemberIncreaseEvent(NoticeEvent):
    """频道成员增加事件"""

    detail_type: Literal["channel_member_increase"]
    guild_id: str
    channel_id: str
    user_id: str
    operator_id: str


class ChannelMemberDecreaseEvent(NoticeEvent):
    """频道成员减少事件"""

    detail_type: Literal["channel_member_decrease"]
    guild_id: str
    channel_id: str
    user_id: str
    operator_id: str


class ChannelMessageDeleteEvent(NoticeEvent):
    """频道消息删除事件"""

    detail_type: Literal["channel_message_delete"]
    guild_id: str
    channel_id: str
    message_id: str
    user_id: str
    operator_id: str


class ChannelCreateEvent(NoticeEvent):
    """频道新建事件"""

    detail_type: Literal["channel_create"]
    guild_id: str
    channel_id: str
    operator_id: str


class ChannelDeleteEvent(NoticeEvent):
    """频道删除事件"""

    detail_type: Literal["channel_delete"]
    guild_id: str
    channel_id: str
    operator_id: str


class RequestEvent(BotEvent):
    """请求事件"""

    type: Literal["request"]
