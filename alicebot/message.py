"""AliceBot 消息。

实现了常用的基本消息 `Message` 和消息字段 `MessageSegment` 模型供适配器使用。
适配器开发者可以根据需要实现此模块中消息类的子类或定义与此不同的消息类型，但建议若可行的话应尽量使用此模块中消息类的子类。
"""

from abc import ABC, abstractmethod
from typing import (
    Any,
    Dict,
    Generic,
    ItemsView,
    Iterator,
    KeysView,
    List,
    Mapping,
    Optional,
    SupportsIndex,
    Type,
    TypeVar,
    Union,
    ValuesView,
    overload,
)
from typing_extensions import Self

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import core_schema

__all__ = [
    "MessageT",
    "MessageSegmentT",
    "BuildMessageType",
    "Message",
    "MessageSegment",
]

MessageT = TypeVar("MessageT", bound="Message[Any]")
MessageSegmentT = TypeVar("MessageSegmentT", bound="MessageSegment[Any]")

# 可以转化为 Message 的类型
BuildMessageType = Union[List[MessageSegmentT], MessageSegmentT, str, Mapping[str, Any]]


class Message(ABC, List[MessageSegmentT]):
    """消息。

    本类是 `List` 的子类，并重写了 `__init__()` 方法，
    可以直接处理 `str`, `Mapping`, `MessageSegment`, `List[MessageSegment]`。
    本类重载了 `+` 和 `+=` 运算符，可以直接和 `Message`, `MessageSegment` 等类型的对象执行取和运算。
    适配器开发者需要继承本类并重写 `get_segment_class()` 方法。
    """

    def __init__(self, *messages: BuildMessageType[MessageSegmentT]) -> None:
        """初始化。

        Args:
            *messages: 可以被转化为消息的数据。
        """
        segment_class = self.get_segment_class()
        for message in messages:
            if isinstance(message, list):
                self.extend(message)
            elif isinstance(message, segment_class):
                self.append(message)
            elif isinstance(message, str):
                self.append(segment_class.from_str(message))
            elif isinstance(message, Mapping):
                self.append(segment_class.from_mapping(message))
            else:
                raise TypeError(
                    f"message type error, expect List[{segment_class}], "
                    f"{segment_class}, str or Mapping, get {type(message)}"
                )

    @classmethod
    @abstractmethod
    def get_segment_class(cls) -> Type[MessageSegmentT]:
        """获取消息字段类。

        Returns:
            消息字段类。
        """

    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: Type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        """Pydantic 自定义模式。"""
        return core_schema.union_schema(
            [
                core_schema.is_instance_schema(cls),
                core_schema.no_info_after_validator_function(
                    cls,
                    handler.generate_schema(
                        List[cls.get_segment_class()]  # type: ignore[misc]
                    ),
                ),
            ]
        )

    def __repr__(self) -> str:
        """返回消息的描述。

        Returns:
            消息的描述。
        """
        return f"Message:[{','.join(map(repr, self))}]"

    def __str__(self) -> str:
        """返回消息的文本表示。

        Returns:
            消息的文本表示。
        """
        return "".join(map(str, self))

    def __contains__(self, item: object) -> bool:
        """判断消息中是否包含指定文本或消息字段。

        Args:
            item: 文本或消息字段。

        Returns:
            消息中是否包含指定文本或消息字段。
        """
        if isinstance(item, str):
            return item in str(self)
        return super().__contains__(item)

    def __add__(self, other: BuildMessageType[MessageSegmentT]) -> Self:  # type: ignore
        """自定义消息与其他对象相加的方法。

        Args:
            other: 其他对象。

        Returns:
            相加的结果。
        """
        return self.__class__(self).__iadd__(other)

    def __radd__(self, other: BuildMessageType[MessageSegmentT]) -> Self:
        """自定义消息与其他对象相加的方法。

        Args:
            other: 其他对象。

        Returns:
            相加的结果。
        """
        return self.__class__(other).__iadd__(self)

    def __iadd__(self, other: BuildMessageType[MessageSegmentT]) -> Self:  # type: ignore
        """自定义消息与其他对象相加的方法。

        Args:
            other: 其他对象。

        Returns:
            相加的结果。
        """
        try:
            self.extend(self.__class__(other))
        except TypeError as e:
            raise TypeError(
                f"unsupported operand type(s) for +: '{type(self)}' and '{type(other)}'",
            ) from e
        return self

    def is_text(self) -> bool:
        """是否是纯文本消息。"""
        return all(x.is_text() for x in self)

    def get_plain_text(self) -> str:
        """获取消息中的纯文本部分。

        Returns:
            消息中的纯文本部分。
        """
        return "".join(map(str, filter(lambda x: x.is_text(), self)))

    def copy(self) -> Self:
        """返回自身的浅复制。

        Returns:
            自身的浅复制。
        """
        return self.__class__(self)

    def startswith(
        self,
        prefix: Union[str, MessageSegmentT],
        start: Optional[SupportsIndex] = None,
        end: Optional[SupportsIndex] = None,
    ) -> bool:
        """实现类似字符串的 `startswith()` 方法。

        当 `prefix` 类型是 `str` 时，会将自身转换为 `str` 类型，再调用 `str` 类型的 `startswith()` 方法。
        当 `prefix` 类型是 `MessageSegment` 时，`start` 和 `end` 参数将不其作用，
            会判断列表的第一个消息字段是否和 `prefix` 相等。

        Args:
            prefix: 前缀。
            start: 开始检查位置。
            end: 停止检查位置。

        Returns:
            检查结果。
        """  # noqa: D402
        if isinstance(prefix, str):
            return str(self).startswith(prefix, start, end)
        if isinstance(prefix, self.get_segment_class()):
            if len(self) == 0:
                return False
            return self[0] == prefix
        raise TypeError(
            f"first arg must be str or {self.get_segment_class()}, not {type(prefix)}"
        )

    def endswith(
        self,
        suffix: Union[str, MessageSegmentT],
        start: Optional[SupportsIndex] = None,
        end: Optional[SupportsIndex] = None,
    ) -> bool:
        """实现类似字符串的 `endswith()` 方法。

        当 `suffix` 类型是 `str` 时，会将自身转换为 `str` 类型，再调用 `str` 类型的 `endswith()` 方法。
        当 `suffix` 类型是 MessageSegment 时，`start` 和 `end` 参数将不其作用，
            会判断列表的最后一个消息字段是否和 `suffix` 相等。

        Args:
            suffix: 后缀。
            start: 开始检查位置。
            end: 停止检查位置。

        Returns:
            检查结果。
        """  # noqa: D402
        if isinstance(suffix, str):
            return str(self).endswith(suffix, start, end)
        if isinstance(suffix, self.get_segment_class()):
            if len(self) == 0:
                return False
            return self[-1] == suffix
        raise TypeError(
            f"first arg must be str or {self.get_segment_class()}, not {type(suffix)}"
        )

    @overload
    def replace(self, old: str, new: str, count: int = -1) -> Self: ...

    @overload
    def replace(
        self, old: MessageSegmentT, new: Optional[MessageSegmentT], count: int = -1
    ) -> Self: ...

    def replace(
        self,
        old: Union[str, MessageSegmentT],
        new: Optional[Union[str, MessageSegmentT]],
        count: int = -1,
    ) -> Self:
        """实现类似字符串的 `replace()` 方法。

        当 `old` 为 `str` 类型时，`new` 也必须是 `str`，本方法将仅对 `is_text()` 为 `True` 的消息字段进行处理。
        当 `old` 为 MessageSegment 类型时，`new` 可以是 `MessageSegment` 或 `None`，本方法将对所有消息字段进行处理，
            并替换符合条件的消息字段。`None` 表示删除匹配到的消息字段。

        Args:
            old: 被匹配的字符串或消息字段。
            new: 被替换为的字符串或消息字段。
            count: 替换的次数。

        Returns:
            替换后的消息对象。
        """  # noqa: D402
        if isinstance(old, str):
            if not isinstance(new, str):
                raise TypeError("when type of old is str, type of new must be str.")
            return self._replace_str(old, new, count)
        if isinstance(old, self.get_segment_class()):
            if not (isinstance(new, self.get_segment_class()) or new is None):
                raise TypeError(
                    "when type of old is MessageSegment, "
                    "type of new must be MessageSegment or None."
                )
            new_msg = self.__class__()
            for item in self:
                if count != 0 and item == old:
                    count -= 1
                    if new is not None:
                        new_msg.append(new)
                else:
                    new_msg.append(item)
            return new_msg
        raise TypeError("type of old must be str or MessageSegment")

    def _replace_str(self, old: str, new: str, count: int = -1) -> Self:
        """实现类似字符串的 `replace()` 方法。

        本方法将被 `replace()` 方法调用以处理 `str` 类型的替换，
        默认将 `MessageSegment` 对象的 `data['text']` 视为存放纯文本的位置。
        适配器开发者可自行重写此方法以适配其他情况。

        Args:
            old: 被匹配的字符串或消息字段。
            new: 被替换为的字符串或消息字段。
            count: 替换的次数。

        Returns:
            替换后的消息对象。
        """
        temp_msg = self.__class__(*(x.model_copy(deep=True) for x in self))
        for index, item in enumerate(temp_msg):
            if count == 0:
                break
            if item.is_text() and old in item.data["text"]:
                if count == -1:
                    temp_msg[index].data["text"] = item.data["text"].replace(old, new)
                else:
                    replace_times = min(count, item.data["text"].count(old))
                    temp_msg[index].data["text"] = item.data["text"].replace(
                        old, new, replace_times
                    )
                    count -= replace_times
        return temp_msg


class MessageSegment(ABC, BaseModel, Mapping[str, Any], Generic[MessageT]):
    """消息字段。

    本类实现了所有 `Mapping` 类型的方法，这些方法全部是对 `data` 属性的操作。
    本类重写了 `+` 和 `+=` 运算符，可以直接和 `Message`, `MessageSegment` 等类型的对象执行取和运算，返回 `Message` 对象。
    适配器开发者需要继承本类并重写 `get_message_class()` 方法。

    Attributes:
        type: 消息字段类型。
        data: 消息字段内容。
    """

    type: str
    data: Dict[str, Any] = Field(default_factory=dict)

    @classmethod
    @abstractmethod
    def get_message_class(cls) -> Type[MessageT]:
        """获取消息类。

        Returns:
            消息类。
        """

    @classmethod
    @abstractmethod
    def from_str(cls, msg: str) -> Self:
        """用于将 `str` 转换为消息字段，子类应重写此方法。

        Args:
            msg: 要解析为消息字段的数据。

        Returns:
            由 `str` 转换的消息字段。
        """

    @classmethod
    def from_mapping(cls, msg: Mapping[Any, Any]) -> Self:
        """用于将 `Mapping` 转换为消息字段。

        如有需要，子类可重写此方法以更改对 `Mapping` 的默认行为。

        Args:
            msg: 要解析为消息字段的数据。

        Returns:
            由 Mapping 转换的消息字段。
        """
        return cls(**msg)

    def __str__(self) -> str:
        """返回消息字段的文本表示。

        Returns:
            消息字段的文本表示。
        """
        return str(self.data)

    def __repr__(self) -> str:
        """返回消息字段的描述。

        Returns:
            消息字段的描述。
        """
        return f"MessageSegment<{self.type}>:{self!s}"

    def __getitem__(self, key: str) -> Any:
        """取索引。相当于对 `data` 属性进行此操作。

        Args:
            key: 键。

        Returns:
            `data` 字典对应索引的值。
        """
        return self.data[key]

    def __setitem__(self, key: str, value: Any) -> None:
        """设置指定索引的值。相当于对 `data` 属性进行此操作。

        Args:
            key: 键。
            value: 值。
        """
        self.data[key] = value

    def __delitem__(self, key: str) -> None:
        """删除索引。相当于对 `data` 属性进行此操作。

        Args:
            key: 键。
        """
        del self.data[key]

    def __len__(self) -> int:
        """取长度。相当于对 `data` 属性进行此操作。

        Returns:
            `data` 字典的长度。
        """
        return len(self.data)

    def __iter__(self) -> Iterator[str]:  # type: ignore
        """迭代。相当于对 `data` 属性进行此操作。

        Returns:
            `data` 字典的迭代器。
        """
        yield from self.data.__iter__()

    def __contains__(self, key: object) -> bool:
        """索引是否包含在对象内。相当于对 `data` 属性进行此操作。

        Args:
            key: 键。

        Returns:
            索引是否包含在 `data` 字典内。
        """
        return key in self.data

    def __eq__(self, other: object) -> bool:
        """判断是否相等。

        Args:
            other: 其他对象。

        Returns:
            是否相等。
        """
        return (
            isinstance(other, self.__class__)
            and self.type == other.type
            and self.data == other.data
        )

    def __ne__(self, other: object) -> bool:
        """判断是否不相等。

        Args:
            other: 其他对象。

        Returns:
            是否不相等。
        """
        return not self.__eq__(other)

    def __add__(self, other: Any) -> MessageT:
        """自定义消息字段与其他对象相加的方法。

        Args:
            other: 其他对象。

        Returns:
            相加的结果。
        """
        return self.get_message_class()(self) + other

    def __radd__(self, other: Any) -> MessageT:
        """自定义消息字段与其他对象相加的方法。

        Args:
            other: 其他对象。

        Returns:
            相加的结果。
        """
        return self.get_message_class()(other) + self

    def get(self, key: str, default: Any = None) -> Any:
        """如果 `key` 存在于 `data` 字典中则返回 `key` 的值，否则返回 `default`。"""
        return self.data.get(key, default)

    def keys(self) -> KeysView[str]:
        """返回由 `data` 字典键组成的一个新视图。"""
        return self.data.keys()

    def values(self) -> ValuesView[Any]:
        """返回由 `data` 字典值组成的一个新视图。"""
        return self.data.values()

    def items(self) -> ItemsView[str, Any]:
        """返回由 `data` 字典项 (`(键, 值)` 对) 组成的一个新视图。"""
        return self.data.items()

    def is_text(self) -> bool:
        """是否是纯文本消息字段。

        Returns:
            是否是纯文本消息字段。
        """
        return self.type == "text"
