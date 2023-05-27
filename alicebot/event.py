"""AliceBot 事件。

事件类的基类。适配器开发者应实现此事件类基类的子类。
"""
from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar, Union, final
from typing_extensions import Self

from pydantic import BaseModel, PrivateAttr

from alicebot.message import Message
from alicebot.typing import T_Adapter
from alicebot.utils import DataclassEncoder

__all__ = ["Event"]


class Event(ABC, BaseModel, Generic[T_Adapter]):
    """事件类的基类。

    Attributes:
        adapter: 产生当前事件的适配器对象。
        type: 事件类型。
        __handled__: 表示事件是否被处理过了，用于适配器处理。警告：请勿手动更改此属性的值。
    """

    adapter: T_Adapter  # type: ignore
    # 这里的 adapter 类型定义只是为了 IDE 的类型检查工具能够正常工作，这个字段将永远不会被实际使用
    # IDE 对 BaseModel 实例化时的提示会将 BaseModel 视为 dataclasses，而忽略 __init__ 定义
    # 因此需要此定义防止类型提示出错
    # 参考：
    # https://pydantic-docs.helpmanual.io/visual_studio_code/#technical-details
    # https://koxudaxi.github.io/pydantic-pycharm-plugin/ignore-init-arguments/

    type: Optional[str]

    _adapter: T_Adapter = PrivateAttr()  # adapter 实际上放在这里
    __handled__: bool = PrivateAttr(default=False)

    def __init__(self, adapter: T_Adapter, **data: Any):
        """初始化。

        Args:
            adapter: 产生此事件的适配器对象。
            **data: 事件数据。
        """
        self._adapter = adapter
        super().__init__(**data)

    @final
    @property
    def adapter(self) -> T_Adapter:
        """产生当前事件的适配器对象。"""
        return self._adapter

    def __str__(self) -> str:
        return f"Event<{self.type}>"

    def __repr__(self) -> str:
        return self.__str__()

    class Config:
        extra = "allow"
        json_encoders = {Message: DataclassEncoder}


_T = TypeVar("_T")


class MessageEvent(Event[T_Adapter], Generic[T_Adapter, _T]):
    @abstractmethod
    def get_plain_text(self) -> str:
        """获取消息的纯文本内容。

        Returns:
            消息的纯文本内容。
        """

    @abstractmethod
    async def reply(self, message: str, *args: Any, **kwargs: Any) -> Any:  # noqa: D417
        """回复消息。

        Args:
            message: 回复消息的内容。

        Returns:
            回复消息动作的响应。
        """

    @abstractmethod
    async def is_same_sender(self, other: Self) -> bool:
        """判断自身和另一个事件是否是同一个发送者。

        Args:
            other: 另一个事件。

        Returns:
            是否是同一个发送者。
        """

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
        return await self.adapter.get(
            self.is_same_sender,
            event_type=type(self),
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
