"""CQHTTP 适配器事件。"""
# pyright: reportIncompatibleVariableOverride=false

from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Literal,
    Optional,
    Tuple,
    get_args,
    get_origin,
)

from pydantic import BaseModel, ConfigDict, Field
from pydantic.fields import FieldInfo

from alicebot.event import Event
from alicebot.event import MessageEvent as BaseMessageEvent
from alicebot.message import BuildMessageType

from .message import CQHTTPMessage, CQHTTPMessageSegment

if TYPE_CHECKING:
    from . import CQHTTPAdapter


class Sender(BaseModel):
    """发送人信息"""

    user_id: Optional[int] = None
    nickname: Optional[str] = None
    card: Optional[str] = None
    sex: Optional[Literal["male", "female", "unknown"]] = None
    age: Optional[int] = None
    area: Optional[str] = None
    level: Optional[str] = None
    role: Optional[str] = None
    title: Optional[str] = None


class Anonymous(BaseModel):
    """匿名信息"""

    id: int
    name: str
    flag: str


class File(BaseModel):
    """文件信息"""

    id: str
    name: str
    size: int
    busid: int


class Status(BaseModel):
    """状态信息"""

    model_config = ConfigDict(extra="allow")

    online: bool
    good: bool


def _get_literal_field(field: Optional[FieldInfo]) -> Optional[str]:
    if field is None:
        return None
    annotation = field.annotation
    if annotation is None or get_origin(annotation) is not Literal:
        return None
    literal_values = get_args(annotation)
    if len(literal_values) != 1:
        return None
    return literal_values[0]


class CQHTTPEvent(Event["CQHTTPAdapter"]):
    """CQHTTP 事件基类"""

    __event__ = ""
    type: Optional[str] = Field(alias="post_type")
    time: int
    self_id: int
    post_type: str

    @property
    def to_me(self) -> bool:
        """当前事件的 `user_id` 是否等于 `self_id`。"""
        return getattr(self, "user_id", None) == self.self_id

    @classmethod
    def get_event_type(cls) -> Tuple[Optional[str], Optional[str], Optional[str]]:
        """获取事件类型。

        Returns:
            事件类型。
        """
        post_type = _get_literal_field(cls.model_fields.get("post_type"))
        if post_type is None:
            return (None, None, None)
        return (
            post_type,
            _get_literal_field(cls.model_fields.get(post_type + "_type")),
            _get_literal_field(cls.model_fields.get("sub_type")),
        )


class MessageEvent(CQHTTPEvent, BaseMessageEvent["CQHTTPAdapter"]):
    """消息事件"""

    __event__ = "message"
    post_type: Literal["message"]
    message_type: Literal["private", "group"]
    sub_type: str
    message_id: int
    user_id: int
    message: CQHTTPMessage
    raw_message: str
    font: int
    sender: Sender

    def __repr__(self) -> str:
        """返回消息事件的描述。

        Returns:
            消息事件的描述。
        """
        return f'Event<{self.type}>: "{self.message}"'

    def get_sender_id(self) -> Optional[int]:
        """获取消息的发送者的唯一标识符。

        Returns:
            消息的发送者的唯一标识符。
        """
        return self.sender.user_id

    def get_plain_text(self) -> str:
        """获取消息的纯文本内容。

        Returns:
            消息的纯文本内容。
        """
        return self.message.get_plain_text()

    async def reply(
        self, message: BuildMessageType[CQHTTPMessageSegment]
    ) -> Dict[str, Any]:
        """回复消息。

        Args:
            message: 回复消息的内容，同 `call_api()` 方法。

        Returns:
            API 请求响应。
        """
        raise NotImplementedError


class PrivateMessageEvent(MessageEvent):
    """私聊消息"""

    __event__ = "message.private"
    message_type: Literal["private"]
    sub_type: Literal["friend", "group", "other"]

    async def reply(
        self, message: BuildMessageType[CQHTTPMessageSegment]
    ) -> Dict[str, Any]:
        """回复消息。

        Args:
            message: 回复消息的内容，同 `call_api()` 方法。

        Returns:
            API 请求响应。
        """
        return await self.adapter.send_private_msg(
            user_id=self.user_id, message=CQHTTPMessage(message)
        )


class GroupMessageEvent(MessageEvent):
    """群消息"""

    __event__ = "message.group"
    message_type: Literal["group"]
    sub_type: Literal["normal", "anonymous", "notice"]
    group_id: int
    anonymous: Optional[Anonymous] = None

    async def reply(
        self, message: BuildMessageType[CQHTTPMessageSegment]
    ) -> Dict[str, Any]:
        """回复消息。

        Args:
            message: 回复消息的内容，同 `call_api()` 方法。

        Returns:
            API 请求响应。
        """
        return await self.adapter.send_group_msg(
            group_id=self.group_id, message=CQHTTPMessage(message)
        )


class NoticeEvent(CQHTTPEvent):
    """通知事件"""

    __event__ = "notice"
    post_type: Literal["notice"]
    notice_type: str


class GroupUploadNoticeEvent(NoticeEvent):
    """群文件上传"""

    __event__ = "notice.group_upload"
    notice_type: Literal["group_upload"]
    user_id: int
    group_id: int
    file: File


class GroupAdminNoticeEvent(NoticeEvent):
    """群管理员变动"""

    __event__ = "notice.group_admin"
    notice_type: Literal["group_admin"]
    sub_type: Literal["set", "unset"]
    user_id: int
    group_id: int


class GroupDecreaseNoticeEvent(NoticeEvent):
    """群成员减少"""

    __event__ = "notice.group_decrease"
    notice_type: Literal["group_decrease"]
    sub_type: Literal["leave", "kick", "kick_me"]
    group_id: int
    operator_id: int
    user_id: int


class GroupIncreaseNoticeEvent(NoticeEvent):
    """群成员增加"""

    __event__ = "notice.group_increase"
    notice_type: Literal["group_increase"]
    sub_type: Literal["approve", "invite"]
    group_id: int
    operator_id: int
    user_id: int


class GroupBanNoticeEvent(NoticeEvent):
    """群禁言"""

    __event__ = "notice.group_ban"
    notice_type: Literal["group_ban"]
    sub_type: Literal["ban", "lift_ban"]
    group_id: int
    operator_id: int
    user_id: int
    duration: int


class FriendAddNoticeEvent(NoticeEvent):
    """好友添加"""

    __event__ = "notice.friend_add"
    notice_type: Literal["friend_add"]
    user_id: int


class GroupRecallNoticeEvent(NoticeEvent):
    """群消息撤回"""

    __event__ = "notice.group_recall"
    notice_type: Literal["group_recall"]
    group_id: int
    operator_id: int
    user_id: int
    message_id: int


class FriendRecallNoticeEvent(NoticeEvent):
    """好友消息撤回"""

    __event__ = "notice.friend_recall"
    notice_type: Literal["friend_recall"]
    user_id: int
    message_id: int


class NotifyEvent(NoticeEvent):
    """提醒事件"""

    __event__ = "notice.notify"
    notice_type: Literal["notify"]
    sub_type: str
    group_id: Optional[int] = None
    user_id: int


class PokeNotifyEvent(NotifyEvent):
    """戳一戳"""

    __event__ = "notice.notify.poke"
    sub_type: Literal["poke"]
    target_id: int
    group_id: Optional[int] = None


class GroupLuckyKingNotifyEvent(NotifyEvent):
    """群红包运气王"""

    __event__ = "notice.notify.lucky_king"
    sub_type: Literal["lucky_king"]
    group_id: int
    target_id: int


class GroupHonorNotifyEvent(NotifyEvent):
    """群成员荣誉变更"""

    __event__ = "notice.notify.honor"
    sub_type: Literal["honor"]
    group_id: int
    honor_type: Literal["talkative", "performer", "emotion"]


class RequestEvent(CQHTTPEvent):
    """请求事件"""

    __event__ = "request"
    post_type: Literal["request"]
    request_type: str

    async def approve(self) -> Dict[str, Any]:
        """同意请求。

        Returns:
            API 请求响应。
        """
        raise NotImplementedError

    async def refuse(self) -> Dict[str, Any]:
        """拒绝请求。

        Returns:
            API 请求响应。
        """
        raise NotImplementedError


class FriendRequestEvent(RequestEvent):
    """加好友请求"""

    __event__ = "request.friend"
    request_type: Literal["friend"]
    user_id: int
    comment: str
    flag: str

    async def approve(self, remark: str = "") -> Dict[str, Any]:
        """同意请求。

        Args:
            remark: 好友备注。

        Returns:
            API 请求响应。
        """
        return await self.adapter.set_friend_add_request(
            flag=self.flag, approve=True, remark=remark
        )

    async def refuse(self) -> Dict[str, Any]:
        """拒绝请求。

        Returns:
            API 请求响应。
        """
        return await self.adapter.set_friend_add_request(flag=self.flag, approve=False)


class GroupRequestEvent(RequestEvent):
    """加群请求 / 邀请"""

    __event__ = "request.group"
    request_type: Literal["group"]
    sub_type: Literal["add", "invite"]
    group_id: int
    user_id: int
    comment: str
    flag: str

    async def approve(self) -> Dict[str, Any]:
        """同意请求。

        Returns:
            API 请求响应。
        """
        return await self.adapter.set_group_add_request(
            flag=self.flag, sub_type=self.sub_type, approve=True
        )

    async def refuse(self, reason: str = "") -> Dict[str, Any]:
        """拒绝请求。

        Args:
            reason: 拒绝原因。

        Returns:
            API 请求响应。
        """
        return await self.adapter.set_group_add_request(
            flag=self.flag, sub_type=self.sub_type, approve=False, reason=reason
        )


class MetaEvent(CQHTTPEvent):
    """元事件"""

    __event__ = "meta_event"
    post_type: Literal["meta_event"]
    meta_event_type: str


class LifecycleMetaEvent(MetaEvent):
    """生命周期"""

    __event__ = "meta_event.lifecycle"
    meta_event_type: Literal["lifecycle"]
    sub_type: Literal["enable", "disable", "connect"]


class HeartbeatMetaEvent(MetaEvent):
    """心跳"""

    __event__ = "meta_event.heartbeat"
    meta_event_type: Literal["heartbeat"]
    status: Status
    interval: int
