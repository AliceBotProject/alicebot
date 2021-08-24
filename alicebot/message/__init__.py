"""
======
消息
======
实现了常用的基本消息 ``Message`` 和消息字段 ``MessageSegment`` 模型供适配器使用。
适配器开发者可以根据需要实现此模块中消息类的子类或定义与此不同的消息类型，但建议若可行的话应尽量使用此模块中消息类的子类。
"""
import json
import dataclasses
from copy import copy, deepcopy
from dataclasses import dataclass, field
from typing import Any, Dict, Generic, List, Mapping, Union, Type, TypeVar, Iterable, Iterator

T_Message = TypeVar('T_Message', bound='Message')
T_MessageSegment = TypeVar('T_MessageSegment', bound='MessageSegment')


class Message(List[T_MessageSegment]):
    """
    消息。
    本类是 ``List`` 的子类，并重写了 ``__init__()`` 方法，可以直接处理 str, Mapping, Iterable[Mapping], T_MessageSegment, T_Message。
    其中 str 的支持需要适配器开发者重写 ``_str_to_message_segment()`` 方法实现。
    本类重写了 ``+`` 和 ``+=`` 运算符，可以直接和 Message, MessageSegment 等类型的对象执行取和运算。
    若开发者实现了 MessageSegment 的子类则需要重写 ``_message_segment_class()`` 方法，
    并在 MessageSegment 的子类中重写 ``_message_class()`` 方法。
    """

    def __init__(self,
                 message: Union[str, None, Mapping, Iterable[Mapping], T_MessageSegment, T_Message, Any] = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        if message is None:
            return
        elif isinstance(message, self.__class__):
            self.extend(message)
        else:
            self.extend(self._construct(message))

    @property
    def _message_segment_class(self) -> Type[T_MessageSegment]:
        """
        若开发者实现了 MessageSegment 的子类则需要重写此方法。

        :return: MessageSegment 类。
        :rtype: Type[T_MessageSegment]
        """
        return MessageSegment

    @classmethod
    def __get_validators__(cls):
        """
        pydantic 自定义校验器
        """
        yield cls._validate

    @classmethod
    def _validate(cls, value):
        return cls(value)

    def _construct(self, msg: Union[str, Mapping, Iterable[Mapping], Any]) -> Iterator[T_MessageSegment]:
        """
        用于将 str, Mapping, Iterable[Mapping] 等类型转换为 MessageSegment。
        用于 pydantic 数据解析和方便用户使用。

        :param msg: 要解析为 MessageSegment 的数据。
        :return: MessageSegment 生成器。
        :rtype: Iterable[T_MessageSegment]
        """
        if isinstance(msg, self._message_segment_class):
            yield msg
        elif isinstance(msg, Mapping):
            yield self._mapping_to_message_segment(msg)
        elif isinstance(msg, str):
            yield self._str_to_message_segment(msg)
        elif isinstance(msg, Iterable):
            for seg in msg:
                yield self._mapping_to_message_segment(seg)
        return

    def _mapping_to_message_segment(self, msg: Mapping) -> T_MessageSegment:
        """
        用于将 Mapping 转换为 MessageSegment，如有需要，子类可重写此方法以更改对 Mapping 的默认行为。

        :return: 由 Mapping 转换的 MessageSegment。
        :rtype: T_MessageSegment
        """
        return self._message_segment_class(**msg)

    def _str_to_message_segment(self, msg: str) -> T_MessageSegment:
        """
        用于将 str 转换为 MessageSegment，子类应重写此方法以支持 str 及支持新的消息字段类。

        :return: 由 str 转换的 MessageSegment。
        :rtype: T_MessageSegment
        """
        raise NotImplementedError

    def __repr__(self) -> str:
        return 'Message:[{}]'.format(','.join(map(lambda x: repr(x), self)))

    def __str__(self) -> str:
        return ''.join(map(lambda x: str(x), self))

    def __contains__(self, item) -> bool:
        if isinstance(item, str):
            return item in str(self)
        return super().__contains__(item)

    def __add__(self: T_Message, other: Union[T_Message, T_MessageSegment, str]) -> T_Message:
        return self.__class__(self).__iadd__(other)

    def __radd__(self: T_Message, other: Union[T_Message, T_MessageSegment, str]) -> T_Message:
        return self.__class__(other).__iadd__(self)

    def __iadd__(self: T_Message, other: Union[T_Message, T_MessageSegment, str]) -> T_Message:
        if isinstance(other, type(self)):
            self.extend(other)
        if isinstance(other, self._message_segment_class):
            self.append(other)
        elif isinstance(other, str):
            self.extend(self._construct(other))
        else:
            raise TypeError(f"unsupported operand type(s) for +: '{type(self)!r}' and '{type(other)!r}'")
        return self

    def copy(self) -> T_Message:
        """
        返回自身的浅复制。

        :return: 自身的浅复制。
        :rtype: T_Message
        """
        return self.__class__(self)

    def deepcopy(self) -> T_Message:
        """
        返回自身的深复制。

        :return: 自身的深复制。
        :rtype: T_Message
        """
        return deepcopy(self)

    def startswith(self, prefix: Union[str, T_MessageSegment], start=None, end=None) -> bool:
        """
        实现类似字符串的 ``startswith()`` 方法。
        当 ``prefix`` 类型是 str 时，会将自身转换为 str 类型，再调用 str 类型的 ``startswith()`` 方法。
        当 ``prefix`` 类型是 T_MessageSegment 时，``start`` 和 ``end`` 参数将不其作用，会判断列表的第一个消息字段是否和 ``prefix`` 相等。

        :param prefix: 前缀。
        :param start: 开始检查位置。
        :param end: 停止检查位置。
        :return: 检查结果。
        :rtype: bool
        """
        if isinstance(prefix, str):
            return str(self).startswith(prefix, start, end)
        elif isinstance(prefix, self._message_segment_class):
            if len(self) == 0:
                return False
            return self[0] == prefix
        raise TypeError(f'first arg must be str or {self._message_segment_class}，not {type(prefix)}')

    def endswith(self, suffix: Union[str, T_MessageSegment], start=None, end=None) -> bool:
        """
        实现类似字符串的 ``endswith()`` 方法。
        当 ``suffix`` 类型是 str 时，会将自身转换为 str 类型，再调用 str 类型的 ``endswith()`` 方法。
        当 ``suffix`` 类型是 T_MessageSegment 时，``start`` 和 ``end`` 参数将不其作用，会判断列表的最后一个消息字段是否和 ``suffix`` 相等。

        :param suffix: 后缀。
        :param start: 开始检查位置。
        :param end: 停止检查位置。
        :return: 检查结果。
        :rtype: bool
        """
        if isinstance(suffix, str):
            return str(self).endswith(suffix, start, end)
        elif isinstance(suffix, self._message_segment_class):
            if len(self) == 0:
                return False
            return self[-1] == suffix
        raise TypeError(f'first arg must be str or {self._message_segment_class}，not {type(suffix)}')


@dataclass
class MessageSegment(Mapping, Generic[T_Message]):
    """
    消息字段。
    本类实现了所有映射类型的方法，这些方法全部是对 ``data`` 属性的操作。
    本类重写了 ``+`` 和 ``+=`` 运算符，可以直接和 Message, MessageSegment 等类型的对象执行取和运算，返回 Message 对象。
    若开发者实现了 Message 和 MessageSegment 的子类则需要重写 ``_message_class()`` 方法。
    """
    type: str
    """
    消息字段类型。
    """
    data: Dict[str, Any] = field(default_factory=lambda: {})
    """
    消息字段内容。
    """

    @property
    def _message_class(self) -> Type[T_Message]:
        """
        若开发者实现了 Message 和 MessageSegment 的子类则需要重写此方法。

        :return: Message 类。
        :rtype: Type[T_Message]
        """
        return Message

    def as_dict(self) -> Dict[str, Any]:
        """
        将当前对象解析为 Dict 对象，开发者可重写本方法以适配特殊的解析方式。

        :return: Dict 对象。
        :rtype: Dict[str, Any]
        """
        return dataclasses.asdict(self)

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return f'MessageSegment<{self.type}>:{str(self)}'

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
        return getattr(self.data, key, default)

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()

    def copy(self) -> T_MessageSegment:
        """
        返回自身的浅复制。

        :return: 自身的浅复制。
        :rtype: T_MessageSegment
        """
        return copy(self)

    def deepcopy(self) -> T_MessageSegment:
        """
        返回自身的深复制。

        :return: 自身的深复制。
        :rtype: T_MessageSegment
        """
        return deepcopy(self)


class DataclassEncoder(json.JSONEncoder):
    """
    用于解析 MessageSegment 的 JSONEncoder 类。
    """

    def default(self, o):
        if dataclasses.is_dataclass(o):
            return o.as_dict()
        return super().default(o)
