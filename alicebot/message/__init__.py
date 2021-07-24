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
from typing import Any, Dict, Mapping, Union, TypeVar, Iterable

T_Message = TypeVar('T_Message', bound='Message')
T_MessageSegment = TypeVar('T_MessageSegment', bound='MessageSegment')


class Message(list):
    """
    消息。
    本类是 ``list`` 的子类，同时重写了 ``__init__()`` 方法，可以直接处理 str, Mapping, Iterable[Mapping], T_MessageSegment, T_Message。
    其中 str 的支持需要适配器开发者重写 ``_construct()`` 方法实现，若开发者实现了 MessageSegment 的子类也需要重写 ``_construct()`` 方法。
    本类重写了 ``+`` 和 ``+=`` 运算符，可以直接和 Message, MessageSegment 等类型的对象执行取和运算。
    """

    def __init__(self,
                 message: Union[str, None, Mapping, Iterable[Mapping], T_MessageSegment, T_Message, Any] = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        if message is None:
            return
        elif isinstance(message, Message):
            self.extend(message)
        elif isinstance(message, MessageSegment):
            self.append(message)
        else:
            self.extend(self._construct(message))

    @classmethod
    def __get_validators__(cls):
        """pydantic自定义校验器"""
        yield cls._validate

    @classmethod
    def _validate(cls, value):
        return cls(value)

    @staticmethod
    def _construct(msg: Union[str, Mapping, Iterable[Mapping], Any]) -> Iterable[T_MessageSegment]:
        """
        用于将 str, Mapping, Iterable[Mapping] 等类型转换为 MessageSegment。
        用于pydantic数据解析和方便用户使用，子类应重写此方法以支持 str 及支持新的消息字段。

        :param msg: 要解析为 MessageSegment 的数据。
        :return: MessageSegment 生成器。
        :rtype: Iterable[T_MessageSegment]
        """
        if isinstance(msg, Mapping):
            yield MessageSegment(msg['type'], msg.get('data') or {})
        elif isinstance(msg, Iterable) and not isinstance(msg, str):
            for seg in msg:
                yield MessageSegment(seg['type'], seg.get('data') or {})
        elif isinstance(msg, str):
            raise NotImplementedError
        return

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
        if isinstance(other, MessageSegment):
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

    def startswith(self, prefix: str, start=None, end=None) -> bool:
        """
        实现类似字符串的 ``startswith()`` 方法。

        :param prefix: 前缀。
        :param start: 开始检查位置。
        :param end: 停止检查位置。
        :return: 检查结果。
        :rtype: bool
        """
        return str(self).startswith(prefix, start, end)

    def endswith(self, suffix: str, start=None, end=None) -> bool:
        """
        实现类似字符串的 ``endswith()`` 方法。

        :param suffix: 后缀。
        :param start: 开始检查位置。
        :param end: 停止检查位置。
        :return: 检查结果。
        :rtype: bool
        """
        return str(self).endswith(suffix, start, end)

    def replace(self,
                old: Union[str, T_MessageSegment],
                new: Union[str, T_MessageSegment, None],
                count: int = -1) -> T_Message:
        """
        实现类似字符串的 ``replace()`` 方法。
        当 ``old`` 为 str 类型时，``new`` 也必须是 str ，本方法将仅对 ``type`` 为 ``text`` 的消息字段进行处理。
        当 ``old`` 为 MessageSegment 类型时，``new`` 可以是 MessageSegment 或 None，本方法将对所有消息字段进行处理，并替换符合条件的消息字段。None 表示删除匹配到的消息字段。

        :param old: 被匹配的字符串或消息字段。
        :param new: 被替换为的字符串或消息字段。
        :param count: 替换的次数。
        :return:
        """
        temp_msg = self.deepcopy()
        if not (type(old) == type(new) == str) and \
                not (type(old) == MessageSegment and (type(new) == MessageSegment or new is None)):
            raise ValueError()
        if type(old) == str:
            for index, item in enumerate(temp_msg):
                if count == 0:
                    break
                if item.type == 'text' and old in item.data['text']:
                    if count == -1:
                        temp_msg[index].data['text'] = item.data['text'].replace(old, new)
                    else:
                        temp = item.data['text'].count(old)
                        temp_msg[index].data['text'] = item.data['text'].replace(old, new, min(temp, count))
                        if count <= temp:
                            count = 0
                        else:
                            count -= temp
        else:
            if new is None:
                temp_msg = Message(filter(lambda x: x != old, temp_msg))
            for index, item in enumerate(temp_msg):
                if count == 0:
                    break
                if item == old:
                    temp_msg[index] = new
        return temp_msg


@dataclass
class MessageSegment(Mapping):
    """
    消息字段。
    本类实现了所有映射类型的方法，这些方法全部是对 ``data`` 属性的操作。
    本类重写了 ``+`` 和 ``+=`` 运算符，可以直接和 Message, MessageSegment 等类型的对象执行取和运算，返回 Message 对象。
    """
    type: str
    """
    消息字段类型。
    """
    data: Dict[str, Any] = field(default_factory=lambda: {})
    """
    消息字段内容。
    """

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

    def __add__(self, other):
        return Message(self) + other

    def __radd__(self, other):
        return Message(other) + self

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
            return dataclasses.asdict(o)
        return super().default(o)
