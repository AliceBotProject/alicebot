from typing import Any, Dict, Iterable, Literal, Union, Mapping, TYPE_CHECKING

from ..message import MiraiMessage
from .base import MiraiEvent, FriendInfo, GroupMemberInfo, OtherClientSender

if TYPE_CHECKING:
    from ..message import MiraiMessage, MiraiMessageSegment


class MessageEvent(MiraiEvent):
    """消息事件"""
    messageChain: MiraiMessage

    @property
    def message(self):
        return self.messageChain

    def __repr__(self) -> str:
        return f'Event<{self.type}>: "{self.messageChain}"'

    def get_plain_text(self) -> str:
        """
        :return: 消息的纯文本内容。
        :rtype: str
        """
        return self.messageChain.get_plain_text()

    async def replay(self, msg: Union[str, Mapping, Iterable[Mapping], 'MiraiMessageSegment', 'MiraiMessage'],
                     quote: bool = False) -> Dict[str, Any]:
        """
        回复消息。

        :param msg: 回复消息的内容，同 ``call_api()`` 方法。
        :param quote: 引用消息，默认为 ``False``。
        :return: API 请求响应。
        :rtype: Dict[str, Any]
        """
        raise NotImplementedError


class FriendMessage(MessageEvent):
    """好友消息"""
    type: Literal['FriendMessage']
    sender: FriendInfo

    async def replay(self, msg: Union[str, Mapping, Iterable[Mapping], 'MiraiMessageSegment', 'MiraiMessage'],
                     quote: bool = False) -> Dict[str, Any]:
        if quote:
            return await self.adapter.send(msg,
                                           message_type='friend',
                                           target=self.sender.id,
                                           quote=self.messageChain[0].id)
        else:
            return await self.adapter.send(msg,
                                           message_type='friend',
                                           target=self.sender.id)


class GroupMessage(MessageEvent):
    """群消息"""
    type: Literal['GroupMessage']
    sender: GroupMemberInfo

    async def replay(self, msg: Union[str, Mapping, Iterable[Mapping], 'MiraiMessageSegment', 'MiraiMessage'],
                     quote: bool = False) -> Dict[str, Any]:
        if quote:
            return await self.adapter.send(msg,
                                           message_type='group',
                                           target=self.sender.group.id,
                                           quote=self.messageChain[0].id)
        else:
            return await self.adapter.send(msg,
                                           message_type='group',
                                           target=self.sender.group.id)


class TempMessage(MessageEvent):
    """群临时消息"""
    type: Literal['TempMessage']
    sender: GroupMemberInfo

    async def replay(self, msg: Union[str, Mapping, Iterable[Mapping], 'MiraiMessageSegment', 'MiraiMessage'],
                     quote: bool = False) -> Dict[str, Any]:
        if quote:
            return await self.adapter.sendTempMessage(qq=self.sender.id,
                                                      group=self.sender.group.id,
                                                      quote=self.messageChain[0].id,
                                                      messageChain=msg)
        else:
            return await self.adapter.sendTempMessage(qq=self.sender.id,
                                                      group=self.sender.group.id,
                                                      messageChain=msg)


class StrangerMessage(MessageEvent):
    """陌生人消息"""
    type: Literal['StrangerMessage']
    sender: FriendInfo

    async def replay(self, msg: Union[str, Mapping, Iterable[Mapping], 'MiraiMessageSegment', 'MiraiMessage'],
                     quote: bool = False) -> Dict[str, Any]:
        if quote:
            return await self.adapter.send(msg,
                                           message_type='friend',
                                           target=self.sender.id,
                                           quote=self.messageChain[0].id)
        else:
            return await self.adapter.send(msg,
                                           message_type='friend',
                                           target=self.sender.id)


class OtherClientMessage(MessageEvent):
    """其他客户端消息"""
    type: Literal['OtherClientMessage']
    sender: OtherClientSender

    async def replay(self, msg: Union[str, Mapping, Iterable[Mapping], 'MiraiMessageSegment', 'MiraiMessage'],
                     quote: bool = False) -> Dict[str, Any]:
        raise NotImplementedError
