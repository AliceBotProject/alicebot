from typing import Any, Dict, Literal

from .base import MiraiEvent


class RequestEvent(MiraiEvent):
    """申请事件"""

    async def approve(self, message: str = "") -> Dict[str, Any]:
        """同意请求。

        Args:
            message: 回复的信息，默认为空。

        Returns:
            API 请求响应。
        """
        raise NotImplementedError

    async def refuse(self, message: str = "") -> Dict[str, Any]:
        """拒绝请求。

        Args:
            message: 回复的信息，默认为空。

        Returns:
            API 请求响应。
        """
        raise NotImplementedError


class NewFriendRequestEvent(RequestEvent):
    """添加好友申请"""

    type: Literal["NewFriendRequestEvent"]
    eventId: int
    fromId: int
    groupId: int
    nick: str
    message: str

    async def approve(self, message: str = "") -> Dict[str, Any]:
        return await self.adapter.resp_newFriendRequestEvent(
            eventId=self.eventId,
            fromId=self.fromId,
            groupId=self.groupId,
            operate=0,
            message=message,
        )

    async def refuse(
        self, message: str = "", black_list: bool = False
    ) -> Dict[str, Any]:
        """拒绝请求。

        Args:
            message: 回复的信息，默认为空。
            black_list: 是否加入黑名单，默认为 `False`。

        Returns:
            API 请求响应。
        """
        return await self.adapter.resp_newFriendRequestEvent(
            eventId=self.eventId,
            fromId=self.fromId,
            groupId=self.groupId,
            operate=2 if black_list else 1,
            message=message,
        )


class MemberJoinRequestEvent(RequestEvent):
    """用户入群申请（Bot需要有管理员权限）"""

    type: Literal["MemberJoinRequestEvent"]
    eventId: int
    fromId: int
    groupId: int
    groupName: str
    nick: str
    message: str

    async def approve(self, message: str = "") -> Dict[str, Any]:
        return await self.adapter.resp_memberJoinRequestEvent(
            eventId=self.eventId,
            fromId=self.fromId,
            groupId=self.groupId,
            operate=0,
            message=message,
        )

    async def refuse(
        self, message: str = "", black_list: bool = False
    ) -> Dict[str, Any]:
        """拒绝请求。

        Args:
            message: 回复的信息，默认为空。
            black_list: 是否加入黑名单，默认为 `False`。

        Returns:
            API 请求响应。
        """
        return await self.adapter.resp_memberJoinRequestEvent(
            eventId=self.eventId,
            fromId=self.fromId,
            groupId=self.groupId,
            operate=3 if black_list else 1,
            message=message,
        )

    async def ignore(
        self, message: str = "", black_list: bool = False
    ) -> Dict[str, Any]:
        """忽略请求。

        Args:
            message: 回复的信息，默认为空。
            black_list: 是否加入黑名单，默认为 `False`。

        Returns:
            API 请求响应。
        """
        return await self.adapter.resp_memberJoinRequestEvent(
            eventId=self.eventId,
            fromId=self.fromId,
            groupId=self.groupId,
            operate=4 if black_list else 2,
            message=message,
        )


class BotInvitedJoinGroupRequestEvent(RequestEvent):
    """Bot 被邀请入群申请"""

    type: Literal["BotInvitedJoinGroupRequestEvent"]
    eventId: int
    fromId: int
    groupId: int
    groupName: str
    nick: str
    message: str

    async def approve(self, message: str = "") -> Dict[str, Any]:
        return await self.adapter.resp_botInvitedJoinGroupRequestEvent(
            eventId=self.eventId,
            fromId=self.fromId,
            groupId=self.groupId,
            operate=0,
            message=message,
        )

    async def refuse(self, message: str = "") -> Dict[str, Any]:
        return await self.adapter.resp_botInvitedJoinGroupRequestEvent(
            eventId=self.eventId,
            fromId=self.fromId,
            groupId=self.groupId,
            operate=1,
            message=message,
        )
