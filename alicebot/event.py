"""AliceBot 事件。

事件类的基类。适配器开发者应实现此事件类基类的子类。
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Generic, Optional, Union
from typing_extensions import Self

from pydantic import BaseModel, ConfigDict

from alicebot.typing import AdapterT

__all__ = ["Event", "MessageEvent"]


class Event(ABC, BaseModel, Generic[AdapterT]):
    """事件类的基类。

    Attributes:
        adapter: 产生当前事件的适配器对象。
        type: 事件类型。
        __handled__: 表示事件是否被处理过了，用于适配器处理。警告：请勿手动更改此属性的值。
    """

    model_config = ConfigDict(extra="allow")

    if TYPE_CHECKING:
        adapter: AdapterT
    else:
        adapter: Any
    type: Optional[str]
    __handled__: bool = False

    def __str__(self) -> str:
        """返回事件的文本表示。

        Returns:
            事件的文本表示。
        """
        return f"Event<{self.type}>"

    def __repr__(self) -> str:
        """返回事件的描述。

        Returns:
            事件的描述。
        """
        return self.__str__()


class MessageEvent(Event[AdapterT], Generic[AdapterT]):
    """通用的消息事件类的基类。"""

    @abstractmethod
    def get_sender_id(self) -> Union[None, int, str]:
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
        max_try_times: Optional[int] = None,
        timeout: Optional[Union[int, float]] = None,
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
        return await self.adapter.get(  # pyright: ignore
            self.is_same_sender,
            event_type=type(self),  # pyright: ignore
            max_try_times=max_try_times,
            timeout=timeout,
        )

    async def ask(
        self,
        message: str,
        max_try_times: Optional[int] = None,
        timeout: Optional[Union[int, float]] = None,
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
