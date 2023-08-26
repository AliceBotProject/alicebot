"""消息事件。"""
from typing import TYPE_CHECKING, Any, Dict, Literal, Union
from typing_extensions import Self

from alicebot.event import MessageEvent as BaseMessageEvent
from alicebot.message import BuildMessageType

from ..message import MiraiMessage, MiraiMessageSegment
from .base import FriendInfo, GroupMemberInfo, MiraiEvent, OtherClientSender

if TYPE_CHECKING:
    from .. import MiraiAdapter  # noqa: F401


class MessageEvent(MiraiEvent, BaseMessageEvent["MiraiAdapter"]):
    """消息事件"""

    sender: Union[FriendInfo, GroupMemberInfo, OtherClientSender]
    messageChain: MiraiMessage

    @property
    def message(self) -> MiraiMessage:
        """与 messageChain 相同。"""
        return self.messageChain

    def __repr__(self) -> str:
        """返回消息事件的描述。

        Returns:
            消息事件的描述。
        """
        return f'Event<{self.type}>: "{self.messageChain}"'

    def get_plain_text(self) -> str:
        """获取消息的纯文本内容。

        Returns:
            消息的纯文本内容。
        """
        return self.messageChain.get_plain_text()

    async def reply(
        self,
        message: BuildMessageType[MiraiMessageSegment],
        quote: bool = False,
    ) -> Dict[str, Any]:
        """回复消息。

        Args:
            message: 回复消息的内容，同 `call_api()` 方法。
            quote: 引用消息，默认为 `False`。

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
        return self.sender.id == other.sender.id


class FriendMessage(MessageEvent):
    """好友消息"""

    type: Literal["FriendMessage"]
    sender: FriendInfo

    async def reply(
        self,
        message: BuildMessageType[MiraiMessageSegment],
        quote: bool = False,
    ) -> Dict[str, Any]:
        """回复消息。

        Args:
            message: 回复消息的内容，同 `call_api()` 方法。
            quote: 引用消息，默认为 `False`。

        Returns:
            API 请求响应。
        """
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

    async def reply(
        self,
        message: BuildMessageType[MiraiMessageSegment],
        quote: bool = False,
    ) -> Dict[str, Any]:
        """回复消息。

        Args:
            message: 回复消息的内容，同 `call_api()` 方法。
            quote: 引用消息，默认为 `False`。

        Returns:
            API 请求响应。
        """
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

    async def reply(
        self,
        message: BuildMessageType[MiraiMessageSegment],
        quote: bool = False,
    ) -> Dict[str, Any]:
        """回复消息。

        Args:
            message: 回复消息的内容，同 `call_api()` 方法。
            quote: 引用消息，默认为 `False`。

        Returns:
            API 请求响应。
        """
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

    async def reply(
        self,
        message: BuildMessageType[MiraiMessageSegment],
        quote: bool = False,
    ) -> Dict[str, Any]:
        """回复消息。

        Args:
            message: 回复消息的内容，同 `call_api()` 方法。
            quote: 引用消息，默认为 `False`。

        Returns:
            API 请求响应。
        """
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

    async def reply(
        self,
        message: BuildMessageType[MiraiMessageSegment],
        quote: bool = False,
    ) -> Dict[str, Any]:
        """回复消息。

        Args:
            message: 回复消息的内容，同 `call_api()` 方法。
            quote: 引用消息，默认为 `False`。

        Returns:
            API 请求响应。
        """
        raise NotImplementedError
