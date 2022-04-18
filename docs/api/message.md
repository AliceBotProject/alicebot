# alicebot.message

AliceBot 消息。

实现了常用的基本消息 `Message` 和消息字段 `MessageSegment` 模型供适配器使用。
适配器开发者可以根据需要实现此模块中消息类的子类或定义与此不同的消息类型，但建议若可行的话应尽量使用此模块中消息类的子类。

## *class* `Message`(self, message = None, *args, **kwargs) {#Message}

Bases: `list`, `<class 'Generic'>`

消息。

本类是 `List` 的子类，并重写了 `__init__()` 方法，可以直接处理 str, Mapping, Iterable[Mapping], T_MessageSegment, T_Message。
其中 str 的支持需要适配器开发者重写 `_str_to_message_segment()` 方法实现。
本类重写了 `+` 和 `+=` 运算符，可以直接和 Message, MessageSegment 等类型的对象执行取和运算。
若开发者实现了 MessageSegment 的子类则需要重写 `_message_segment_class()` 方法，
并在 MessageSegment 的子类中重写 `_message_class()` 方法。

- **Arguments**

  - **message** (*Union[NoneType, ~T_Message, ~T_MessageSegment, str, Mapping, Iterable[Union[~T_MessageSegment, str, Mapping]]]*)

### *method* `copy(self)` {#Message.copy}

返回自身的浅复制。

- **Returns**

  Type: *~T_Message*

  自身的浅复制。

### *method* `deepcopy(self)` {#Message.deepcopy}

返回自身的深复制。

- **Returns**

  Type: *~T_Message*

  自身的深复制。

### *method* `endswith(self, suffix, start=None, end=None)` {#Message.endswith}

实现类似字符串的 `endswith()` 方法。

当 `suffix` 类型是 str 时，会将自身转换为 str 类型，再调用 str 类型的 `endswith()` 方法。
当 `suffix` 类型是 T_MessageSegment 时，`start` 和 `end` 参数将不其作用，会判断列表的最后一个消息字段是否和 `suffix` 相等。

- **Arguments**

  - **suffix** (*Union[str, ~T_MessageSegment]*) - 后缀。

  - **start** - 开始检查位置。

  - **end** - 停止检查位置。

- **Returns**

  Type: *bool*

  检查结果。

### *method* `startswith(self, prefix, start=None, end=None)` {#Message.startswith}

实现类似字符串的 `startswith()` 方法。

当 `prefix` 类型是 str 时，会将自身转换为 str 类型，再调用 str 类型的 `startswith()` 方法。
当 `prefix` 类型是 T_MessageSegment 时，`start` 和 `end` 参数将不其作用，会判断列表的第一个消息字段是否和 `prefix` 相等。

- **Arguments**

  - **prefix** (*Union[str, ~T_MessageSegment]*) - 前缀。

  - **start** - 开始检查位置。

  - **end** - 停止检查位置。

- **Returns**

  Type: *bool*

  检查结果。

## *class* `MessageSegment`(self, type, data = <factory>) {#MessageSegment}

Bases: `collections.abc.Mapping`, `<class 'Generic'>`

消息字段。

本类实现了所有映射类型的方法，这些方法全部是对 `data` 属性的操作。
本类重写了 `+` 和 `+=` 运算符，可以直接和 Message, MessageSegment 等类型的对象执行取和运算，返回 Message 对象。
若开发者实现了 Message 和 MessageSegment 的子类则需要重写 `_message_class()` 方法。

- **Arguments**

  - **type** (*str*)

  - **data** (*Dict[str, Any]*)

- **Attributes**

  - **type** (*str*) - 消息字段类型。

  - **data** (*Dict[str, Any]*) - 消息字段内容。

### *method* `as_dict(self)` {#MessageSegment.as_dict}

将当前对象解析为 Dict 对象，开发者可重写本方法以适配特殊的解析方式。

- **Returns**

  Type: *Dict[str, Any]*

  Dict 对象。

### *method* `copy(self)` {#MessageSegment.copy}

返回自身的浅复制。

- **Returns**

  Type: *~T_MessageSegment*

  自身的浅复制。

### *method* `deepcopy(self)` {#MessageSegment.deepcopy}

返回自身的深复制。

- **Returns**

  Type: *~T_MessageSegment*

  自身的深复制。

### *method* `get(self, key, default=None)` {#MessageSegment.get}

D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.

- **Arguments**

  - **key** (*str*)

  - **default**

### *method* `items(self)` {#MessageSegment.items}

D.items() -> a set-like object providing a view on D's items

### *method* `keys(self)` {#MessageSegment.keys}

D.keys() -> a set-like object providing a view on D's keys

### *method* `values(self)` {#MessageSegment.values}

D.values() -> an object providing a view on D's values

## *class* `DataclassEncoder`(self, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None) {#DataclassEncoder}

Bases: `json.encoder.JSONEncoder`

用于解析 MessageSegment 的 JSONEncoder 类。

- **Arguments**

  - **skipkeys**

  - **ensure_ascii**

  - **check_circular**

  - **allow_nan**

  - **sort_keys**

  - **indent**

  - **separators**

  - **default**

### *method* `default(self, o)` {#DataclassEncoder.default}

Implement this method in a subclass such that it returns

a serializable object for ``o``, or calls the base implementation
(to raise a ``TypeError``).

For example, to support arbitrary iterators, you could
implement default like this::

    def default(self, o):
        try:
            iterable = iter(o)
        except TypeError:
            pass
        else:
            return list(iterable)
        # Let the base class default method raise the TypeError
        return JSONEncoder.default(self, o)

- **Arguments**

  - **o**