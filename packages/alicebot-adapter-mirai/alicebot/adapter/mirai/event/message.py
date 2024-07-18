"""消息事件。"""
# pyright: reportIncompatibleVariableOverride=false

from typing import TYPE_CHECKING, Any, Literal, Union
from typing_extensions import override

from alicebot.event import MessageEvent as BaseMessageEvent
from alicebot.message import BuildMessageType

from ..message import MiraiMessage, MiraiMessageSegment
from .base import FriendInfo, GroupMemberInfo, MiraiEvent, OtherClientSender

if TYPE_CHECKING:
    from .. import MiraiAdapter


class MiraiBaseMessageEvent(MiraiEvent, BaseMessageEvent["MiraiAdapter"]):
    """Mirai 消息事件基类"""

    messageChain: MiraiMessage

    @property
    def message(self) -> MiraiMessage:
        """与 messageChain 相同。"""
        return self.messageChain

    @override
    def __repr__(self) -> str:
        return f'Event<{self.type}>: "{self.messageChain}"'

    @override
    def get_plain_text(self) -> str:
        return self.messageChain.get_plain_text()

    @override
    async def reply(
        self,
        message: BuildMessageType[MiraiMessageSegment],
        quote: bool = False,
    ) -> dict[str, Any]:
        """回复消息。

        Args:
            message: 回复消息的内容，同 `call_api()` 方法。
            quote: 引用消息，默认为 `False`。

        Returns:
            API 请求响应。
        """
        raise NotImplementedError


class MessageEvent(MiraiBaseMessageEvent):
    """消息事件"""

    sender: Union[FriendInfo, GroupMemberInfo, OtherClientSender]

    @override
    def get_sender_id(self) -> int:
        return self.sender.id

    @override
    async def reply(
        self,
        message: BuildMessageType[MiraiMessageSegment],
        quote: bool = False,
    ) -> dict[str, Any]:
        """回复消息。

        Args:
            message: 回复消息的内容，同 `call_api()` 方法。
            quote: 引用消息，默认为 `False`。

        Returns:
            API 请求响应。
        """
        raise NotImplementedError


class FriendMessage(MessageEvent):
    """好友消息"""

    type: Literal["FriendMessage"]
    sender: FriendInfo

    @override
    async def reply(
        self,
        message: BuildMessageType[MiraiMessageSegment],
        quote: bool = False,
    ) -> dict[str, Any]:
        if quote:
            return await self.adapter.send(
                message,
                message_type="friend",
                target=self.sender.id,
                quote=self.messageChain[0]["id"],
            )
        return await self.adapter.send(
            message, message_type="friend", target=self.sender.id
        )


class GroupMessage(MessageEvent):
    """群消息"""

    type: Literal["GroupMessage"]
    sender: GroupMemberInfo

    @override
    async def reply(
        self,
        message: BuildMessageType[MiraiMessageSegment],
        quote: bool = False,
    ) -> dict[str, Any]:
        if quote:
            return await self.adapter.send(
                message,
                message_type="group",
                target=self.sender.group.id,
                quote=self.messageChain[0]["id"],
            )
        return await self.adapter.send(
            message, message_type="group", target=self.sender.group.id
        )


class TempMessage(MessageEvent):
    """群临时消息"""

    type: Literal["TempMessage"]
    sender: GroupMemberInfo

    @override
    async def reply(
        self,
        message: BuildMessageType[MiraiMessageSegment],
        quote: bool = False,
    ) -> dict[str, Any]:
        if quote:
            return await self.adapter.sendTempMessage(
                qq=self.sender.id,
                group=self.sender.group.id,
                messageChain=message,
                quote=self.messageChain[0]["id"],
            )
        return await self.adapter.sendTempMessage(
            qq=self.sender.id, group=self.sender.group.id, messageChain=message
        )


class StrangerMessage(MessageEvent):
    """陌生人消息"""

    type: Literal["StrangerMessage"]
    sender: FriendInfo

    @override
    async def reply(
        self,
        message: BuildMessageType[MiraiMessageSegment],
        quote: bool = False,
    ) -> dict[str, Any]:
        if quote:
            return await self.adapter.send(
                message,
                message_type="friend",
                target=self.sender.id,
                quote=self.messageChain[0]["id"],
            )
        return await self.adapter.send(
            message, message_type="friend", target=self.sender.id
        )


class OtherClientMessage(MessageEvent):
    """其他客户端消息"""

    type: Literal["OtherClientMessage"]
    sender: OtherClientSender

    @override
    async def reply(
        self,
        message: BuildMessageType[MiraiMessageSegment],
        quote: bool = False,
    ) -> dict[str, Any]:
        raise NotImplementedError


class SyncMessage(MiraiBaseMessageEvent):
    """同步消息"""

    subject: Union[FriendInfo, GroupMemberInfo]

    @override
    def get_sender_id(self) -> None:
        return

    @override
    async def reply(
        self,
        message: BuildMessageType[MiraiMessageSegment],
        quote: bool = False,
    ) -> dict[str, Any]:
        raise NotImplementedError


class FriendSyncMessage(SyncMessage):
    """同步好友消息"""

    type: Literal["FriendSyncMessage"]
    subject: FriendInfo

    @override
    async def reply(
        self,
        message: BuildMessageType[MiraiMessageSegment],
        quote: bool = False,
    ) -> dict[str, Any]:
        raise NotImplementedError


class GroupSyncMessage(SyncMessage):
    """同步群消息"""

    type: Literal["GroupSyncMessage"]
    subject: GroupMemberInfo

    @override
    async def reply(
        self,
        message: BuildMessageType[MiraiMessageSegment],
        quote: bool = False,
    ) -> dict[str, Any]:
        raise NotImplementedError


class TempSyncMessage(SyncMessage):
    """同步群临时消息"""

    type: Literal["TempSyncMessage"]
    subject: GroupMemberInfo

    @override
    async def reply(
        self,
        message: BuildMessageType[MiraiMessageSegment],
        quote: bool = False,
    ) -> dict[str, Any]:
        raise NotImplementedError


class StrangerSyncMessage(SyncMessage):
    """同步陌生人消息"""

    type: Literal["StrangerSyncMessage"]
    subject: FriendInfo

    @override
    async def reply(
        self,
        message: BuildMessageType[MiraiMessageSegment],
        quote: bool = False,
    ) -> dict[str, Any]:
        raise NotImplementedError
