from typing import TYPE_CHECKING, Any, Dict, Literal

from alicebot.event import MessageEvent as BaseMessageEvent

from ..message import MiraiMessage
from .base import FriendInfo, MiraiEvent, GroupMemberInfo, OtherClientSender

if TYPE_CHECKING:
    from .. import MiraiAdapter
    from ..message import T_MiraiMSG


class MessageEvent(MiraiEvent, BaseMessageEvent["MiraiAdapter", MiraiMessage]):
    """消息事件"""

    messageChain: MiraiMessage

    @property
    def message(self) -> MiraiMessage:
        return self.messageChain

    def __repr__(self) -> str:
        return f'Event<{self.type}>: "{self.messageChain}"'

    def get_plain_text(self) -> str:
        """
        Returns:
            消息的纯文本内容。
        """
        return self.messageChain.get_plain_text()

    async def reply(self, message: "T_MiraiMSG", quote: bool = False) -> Dict[str, Any]:
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

    async def reply(self, message: "T_MiraiMSG", quote: bool = False) -> Dict[str, Any]:
        if quote:
            return await self.adapter.send(
                message,
                message_type="friend",
                target=self.sender.id,
                quote=self.messageChain[0]["id"],
            )
        else:
            return await self.adapter.send(
                message, message_type="friend", target=self.sender.id
            )


class GroupMessage(MessageEvent):
    """群消息"""

    type: Literal["GroupMessage"]
    sender: GroupMemberInfo

    async def reply(self, message: "T_MiraiMSG", quote: bool = False) -> Dict[str, Any]:
        if quote:
            return await self.adapter.send(
                message,
                message_type="group",
                target=self.sender.group.id,
                quote=self.messageChain[0]["id"],
            )
        else:
            return await self.adapter.send(
                message, message_type="group", target=self.sender.group.id
            )


class TempMessage(MessageEvent):
    """群临时消息"""

    type: Literal["TempMessage"]
    sender: GroupMemberInfo

    async def reply(self, message: "T_MiraiMSG", quote: bool = False) -> Dict[str, Any]:
        if quote:
            return await self.adapter.sendTempMessage(
                qq=self.sender.id,
                group=self.sender.group.id,
                messageChain=message,
                quote=self.messageChain[0]["id"],
            )
        else:
            return await self.adapter.sendTempMessage(
                qq=self.sender.id, group=self.sender.group.id, messageChain=message
            )


class StrangerMessage(MessageEvent):
    """陌生人消息"""

    type: Literal["StrangerMessage"]
    sender: FriendInfo

    async def reply(self, msg: "T_MiraiMSG", quote: bool = False) -> Dict[str, Any]:
        if quote:
            return await self.adapter.send(
                msg,
                message_type="friend",
                target=self.sender.id,
                quote=self.messageChain[0]["id"],
            )
        else:
            return await self.adapter.send(
                msg, message_type="friend", target=self.sender.id
            )


class OtherClientMessage(MessageEvent):
    """其他客户端消息"""

    type: Literal["OtherClientMessage"]
    sender: OtherClientSender

    async def reply(self, msg: "T_MiraiMSG", quote: bool = False) -> Dict[str, Any]:
        raise NotImplementedError
