"""AliceBot 事件。

事件类的基类。适配器开发者应实现此事件类基类的子类。
"""

from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING, Any, Generic, NamedTuple, Self
from typing_extensions import override

from pydantic import BaseModel, ConfigDict

from alicebot.typing import AdapterT

__all__ = ["Event", "EventHandleOption", "MessageEvent"]


class Event(BaseModel, Generic[AdapterT], metaclass=ABCMeta):
    """事件类的基类。

    Attributes:
        adapter: 产生当前事件的适配器对象。
        type: 事件类型。
    """

    model_config = ConfigDict(extra="allow")

    if TYPE_CHECKING:
        adapter: AdapterT
    else:
        adapter: Any
    type: str | None

    @override
    def __str__(self) -> str:
        return f"Event<{self.type}>"

    @override
    def __repr__(self) -> str:
        return self.__str__()


class EventHandleOption(NamedTuple):
    """事件处理选项。

    Attributes:
        event: 当前事件。
        handle_get: 当前事件是否可以被 get 方法捕获。
    """

    event: Event[Any]
    handle_get: bool


class MessageEvent(Event[AdapterT], Generic[AdapterT], metaclass=ABCMeta):
    """通用的消息事件类的基类。"""

    @abstractmethod
    def get_sender_id(self) -> None | int | str:
        """获取消息的发送者的唯一标识符。

        Returns:
            消息的发送者的唯一标识符。
        """

    @abstractmethod
    def get_plain_text(self) -> str:
        """获取消息的纯文本内容。

        Returns:
            消息的纯文本内容。
        """

    @abstractmethod
    async def reply(self, message: str) -> Any:
        """回复消息。

        Args:
            message: 回复消息的内容。

        Returns:
            回复消息动作的响应。
        """

    async def is_same_sender(self, other: Self) -> bool:
        """判断自身和另一个事件是否是同一个发送者。

        Args:
            other: 另一个事件。

        Returns:
            是否是同一个发送者。
        """
        return self.get_sender_id() == other.get_sender_id()

    async def get(
        self,
        *,
        max_try_times: int | None = None,
        timeout: float | None = None,
    ) -> Self:
        """获取用户回复消息。

        相当于 `Bot` 的 `get()`，条件为适配器、事件类型、发送人相同。

        Args:
            max_try_times: 最大事件数。
            timeout: 超时时间。

        Returns:
            用户回复的消息事件。

        Raises:
            GetEventTimeout: 超过最大事件数或超时。
        """
        return await self.adapter.get(
            self.is_same_sender,
            event_type=type(self),
            max_try_times=max_try_times,
            timeout=timeout,
        )

    async def ask(
        self,
        message: str,
        max_try_times: int | None = None,
        timeout: float | None = None,
    ) -> Self:
        """询问消息。

        表示回复一个消息后获取用户的回复。
        相当于 `reply()` 后执行 `get()`。

        Args:
            message: 回复消息的内容。
            max_try_times: 最大事件数。
            timeout: 超时时间。

        Returns:
            用户回复的消息事件。
        """
        await self.reply(message)
        return await self.get(max_try_times=max_try_times, timeout=timeout)
