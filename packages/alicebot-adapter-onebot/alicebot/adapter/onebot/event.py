"""OntBot 适配器事件。"""
import inspect
from typing import TYPE_CHECKING, List, Type, Tuple, Literal, Optional

from pydantic import Extra, BaseModel
from pydantic.fields import ModelField
from pydantic.typing import is_literal_type, all_literal_values

from alicebot.event import Event

from .message import OneBotMessage

if TYPE_CHECKING:
    from . import OneBotAdapter


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


class MessageEvent(BotEvent):
    """消息事件"""

    type: Literal["message"]
    message_id: str
    message: OneBotMessage
    alt_message: str
    user_id: str


class PrivateMessageEvent(MessageEvent):
    """私聊消息事件"""

    detail_type: Literal["private"]


class GroupMessageEvent(MessageEvent):
    """群消息事件"""

    detail_type: Literal["group"]
    group_id: str


class ChannelMessageEvent(MessageEvent):
    """频道消息事件"""

    detail_type: Literal["channel"]
    guild_id: str
    channel_id: str


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


_onebot_events = {
    name: model
    for name, model in globals().items()
    if inspect.isclass(model) and issubclass(model, OntBotEvent)
}


def get_event_class(event_type: str) -> Type[OntBotEvent]:
    """根据接收到的消息类型返回对应的事件类。

    Args:
        event_type: 事件类型。

    Returns:
        对应的事件类。
    """
    return _onebot_events[event_type]
