"""AliceBot 消息。

实现了常用的基本消息 `Message` 和消息字段 `MessageSegment` 模型供适配器使用。
适配器开发者可以根据需要实现此模块中消息类的子类或定义与此不同的消息类型，但建议若可行的话应尽量使用此模块中消息类的子类。
"""
import dataclasses
from copy import copy, deepcopy
from dataclasses import field, dataclass
from typing import (
    Any,
    Dict,
    List,
    Type,
    Union,
    Generic,
    Mapping,
    TypeVar,
    Iterable,
    Iterator,
)

__all__ = ["T_Message", "T_MessageSegment", "T_MS", "Message", "MessageSegment"]

T_Message = TypeVar("T_Message", bound="Message")
T_MessageSegment = TypeVar("T_MessageSegment", bound="MessageSegment")

# 可以转化为 MessageSegment 的类型
T_MS = Union[T_MessageSegment, str, Mapping]


class Message(List[T_MessageSegment]):
    """消息。

    本类是 `List` 的子类，并重写了 `__init__()` 方法，
    可以直接处理 str, Mapping, Iterable[Mapping], T_MessageSegment, T_Message。
    其中 str 的支持需要适配器开发者重写 `_str_to_message_segment()` 方法实现。
    本类重写了 `+` 和 `+=` 运算符，可以直接和 Message, MessageSegment 等类型的对象执行取和运算。
    若开发者实现了 MessageSegment 的子类则需要重写 `_message_segment_class()` 方法，
    并在 MessageSegment 的子类中重写 `_message_class()` 方法。
    """

    def __init__(
        self,
        message: Union[None, T_Message, T_MS, Iterable[T_MS]] = None,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        if message is None:
            return
        elif isinstance(message, self.__class__):
            self.extend(message)
        else:
            self.extend(self._construct(message))

    @property
    def _message_segment_class(self) -> Type[T_MessageSegment]:
        """若开发者实现了 MessageSegment 的子类则需要重写此方法。

        Returns:
            MessageSegment 类。
        """
        return MessageSegment

    @classmethod
    def __get_validators__(cls):
        """pydantic 自定义校验器。"""
        yield cls._validate

    @classmethod
    def _validate(cls, value):
        return cls(value)

    def _construct(
        self, msg: Union[T_MS, Iterable[T_MS]]
    ) -> Iterator[T_MessageSegment]:
        """用于将 str, Mapping, Iterable[Mapping] 等类型转换为 MessageSegment。
        用于 pydantic 数据解析和方便用户使用。

        Args:
            msg: 要解析为 MessageSegment 的数据。

        Returns:
            MessageSegment 生成器。
        """
        if isinstance(msg, self._message_segment_class):
            yield msg
        elif isinstance(msg, Mapping):
            yield self._mapping_to_message_segment(msg)
        elif isinstance(msg, str):
            yield self._str_to_message_segment(msg)
        elif isinstance(msg, Iterable):
            for seg in msg:
                for i in self._construct(seg):
                    yield i

    def _mapping_to_message_segment(self, msg: Mapping) -> T_MessageSegment:
        """用于将 Mapping 转换为 MessageSegment，如有需要，子类可重写此方法以更改对 Mapping 的默认行为。

        Args:
            msg: 要解析为 MessageSegment 的数据。

        Returns:
            由 Mapping 转换的 MessageSegment。
        """
        return self._message_segment_class(**msg)

    def _str_to_message_segment(self, msg: str) -> T_MessageSegment:
        """用于将 str 转换为 MessageSegment，子类应重写此方法以支持 str 及支持新的消息字段类。

        Args:
            msg: 要解析为 MessageSegment 的数据。

        Returns:
            由 str 转换的 MessageSegment。
        """
        raise NotImplementedError

    def __repr__(self) -> str:
        return "Message:[{}]".format(",".join(map(lambda x: repr(x), self)))

    def __str__(self) -> str:
        return "".join(map(lambda x: str(x), self))

    def __contains__(self, item) -> bool:
        if isinstance(item, str):
            return item in str(self)
        return super().__contains__(item)

    def __add__(
        self: T_Message, other: Union[T_Message, T_MessageSegment, str]
    ) -> T_Message:
        return self.__class__(self).__iadd__(other)

    def __radd__(
        self: T_Message, other: Union[T_Message, T_MessageSegment, str]
    ) -> T_Message:
        return self.__class__(other).__iadd__(self)

    def __iadd__(
        self: T_Message, other: Union[T_Message, T_MessageSegment, str]
    ) -> T_Message:
        if isinstance(other, type(self)):
            self.extend(other)
        if isinstance(other, self._message_segment_class):
            self.append(other)
        elif isinstance(other, str):
            self.extend(self._construct(other))
        else:
            raise TypeError(
                f"unsupported operand type(s) for +: '{type(self)}' and '{type(other)}'"
            )
        return self

    def is_text(self) -> bool:
        """
        Returns:
            是否是纯文本消息。
        """
        return all(map(lambda x: x.is_text(), self))

    def get_plain_text(self) -> str:
        """获取消息中的纯文本部分。

        Returns:
            消息中的纯文本部分。
        """
        return "".join(map(lambda x: str(x), filter(lambda x: x.is_text(), self)))

    def copy(self) -> T_Message:
        """返回自身的浅复制。

        Returns:
            自身的浅复制。
        """
        return self.__class__(self)

    def deepcopy(self) -> T_Message:
        """返回自身的深复制。

        Returns:
            自身的深复制。
        """
        return deepcopy(self)

    def startswith(
        self, prefix: Union[str, T_MessageSegment], start=None, end=None
    ) -> bool:
        """实现类似字符串的 `startswith()` 方法。

        当 `prefix` 类型是 str 时，会将自身转换为 str 类型，再调用 str 类型的 `startswith()` 方法。
        当 `prefix` 类型是 T_MessageSegment 时，`start` 和 `end` 参数将不其作用，
            会判断列表的第一个消息字段是否和 `prefix` 相等。

        Args:
            prefix: 前缀。
            start: 开始检查位置。
            end: 停止检查位置。

        Returns:
            检查结果。
        """
        if isinstance(prefix, str):
            return str(self).startswith(prefix, start, end)
        elif isinstance(prefix, self._message_segment_class):
            if len(self) == 0:
                return False
            return self[0] == prefix
        raise TypeError(
            f"first arg must be str or {self._message_segment_class}，not {type(prefix)}"
        )

    def endswith(
        self, suffix: Union[str, T_MessageSegment], start=None, end=None
    ) -> bool:
        """实现类似字符串的 `endswith()` 方法。

        当 `suffix` 类型是 str 时，会将自身转换为 str 类型，再调用 str 类型的 `endswith()` 方法。
        当 `suffix` 类型是 T_MessageSegment 时，`start` 和 `end` 参数将不其作用，
            会判断列表的最后一个消息字段是否和 `suffix` 相等。

        Args:
            suffix: 后缀。
            start: 开始检查位置。
            end: 停止检查位置。

        Returns:
            检查结果。
        """
        if isinstance(suffix, str):
            return str(self).endswith(suffix, start, end)
        elif isinstance(suffix, self._message_segment_class):
            if len(self) == 0:
                return False
            return self[-1] == suffix
        raise TypeError(
            f"first arg must be str or {self._message_segment_class}，not {type(suffix)}"
        )

    def replace(
        self,
        old: Union[str, T_MessageSegment],
        new: Union[str, T_MessageSegment, None],
        count: int = -1,
    ) -> T_Message:
        """实现类似字符串的 `replace()` 方法。

        当 `old` 为 str 类型时，`new` 也必须是 str ，本方法将仅对 `is_text()` 为 True 的消息字段进行处理。
        当 `old` 为 MessageSegment 类型时，`new` 可以是 MessageSegment 或 None，本方法将对所有消息字段进行处理，
            并替换符合条件的消息字段。None 表示删除匹配到的消息字段。

        Args:
            old: 被匹配的字符串或消息字段。
            new: 被替换为的字符串或消息字段。
            count: 替换的次数。

        Returns:
            替换后的消息对象。
        """
        if type(old) == str:
            if type(new) != str:
                raise TypeError("when type of old is str, type of new must be str.")
            return self._replace_str(old, new, count)
        elif isinstance(old, self._message_segment_class):
            if not (isinstance(new, self._message_segment_class) or new is None):
                raise TypeError(
                    "when type of old is MessageSegment, "
                    "type of new must be MessageSegment or None."
                )
            temp_msg = self.deepcopy()
            for index, item in enumerate(temp_msg):
                if count == 0:
                    break
                if item == old:
                    temp_msg[index] = new
                    count -= 1
            if new is None:
                temp_msg = self.__class__(filter(lambda x: x is not None, self))
            return temp_msg
        else:
            raise TypeError("type of old must be str or MessageSegment")

    def _replace_str(self, old: str, new: str, count: int = -1) -> T_Message:
        """实现类似字符串的 `replace()` 方法。

        本方法将被 `replace()` 方法调用以处理 str 类型的替换，
        默认将 MessageSegment 对象的 data['text'] 视为存放纯文本的位置。
        适配器开发者可自行重写此方法以适配其他情况。

        Args:
            old: 被匹配的字符串或消息字段。
            new: 被替换为的字符串或消息字段。
            count: 替换的次数。

        Returns:
            替换后的消息对象。
        """
        temp_msg = self.deepcopy()
        for index, item in enumerate(temp_msg):
            item: MessageSegment
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


@dataclass
class MessageSegment(Mapping, Generic[T_Message]):
    """消息字段。

    本类实现了所有映射类型的方法，这些方法全部是对 `data` 属性的操作。
    本类重写了 `+` 和 `+=` 运算符，可以直接和 Message, MessageSegment 等类型的对象执行取和运算，返回 Message 对象。
    若开发者实现了 Message 和 MessageSegment 的子类则需要重写 `_message_class()` 方法。

    Attributes:
        type: 消息字段类型。
        data: 消息字段内容。
    """

    type: str
    data: Dict[str, Any] = field(default_factory=dict)

    @property
    def _message_class(self) -> Type[T_Message]:
        """若开发者实现了 Message 和 MessageSegment 的子类则需要重写此方法。

        Returns:
            Message 类。
        """
        return Message

    def as_dict(self) -> Dict[str, Any]:
        """将当前对象解析为 Dict 对象，开发者可重写本方法以适配特殊的解析方式。

        Returns:
            Dict 对象。
        """
        return dataclasses.asdict(self)

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return f"MessageSegment<{self.type}>:{str(self)}"

    def __getitem__(self, key) -> Any:
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self):
        yield from self.data.__iter__()

    def __contains__(self, key) -> bool:
        return key in self.data

    def __eq__(self, other: T_MessageSegment) -> bool:
        return self.type == other.type and self.data == other.data

    def __ne__(self, other: T_MessageSegment) -> bool:
        return not self.__eq__(other)

    def __add__(self, other) -> T_Message:
        return self._message_class(self) + other

    def __radd__(self, other) -> T_Message:
        return self._message_class(other) + self

    def get(self, key: str, default=None):
        return self.data.get(key, default)

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()

    def is_text(self) -> bool:
        """
        Returns:
            是否是纯文本消息字段。
        """
        return self.type == "text"

    def copy(self) -> T_MessageSegment:
        """返回自身的浅复制。

        Returns:
            自身的浅复制。
        """
        return copy(self)

    def deepcopy(self) -> T_MessageSegment:
        """返回自身的深复制。

        Returns:
            自身的深复制。
        """
        return deepcopy(self)
