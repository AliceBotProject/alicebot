# alicebot.message

AliceBot 消息。

实现了常用的基本消息 `Message` 和消息字段 `MessageSegment` 模型供适配器使用。
适配器开发者可以根据需要实现此模块中消息类的子类或定义与此不同的消息类型，但建议若可行的话应尽量使用此模块中消息类的子类。

## _abstract class_ `Message` {#Message}

Bases: `abc.ABC`, `list`, `typing.Generic`

消息。

本类是 `List` 的子类，并重写了 `__init__()` 方法，
可以直接处理 `str`, `Mapping`, `MessageSegment`, `List[MessageSegment]`。
本类重载了 `+` 和 `+=` 运算符，可以直接和 `Message`, `MessageSegment` 等类型的对象执行取和运算。
适配器开发者需要继承本类并重写 `get_segment_class()` 方法。

### _method_ `__init__(self, *messages)` {#Message.\_\_init\_\_}

初始化。

- **Arguments**

  - **\*messages** (_Union\[List\[~MessageSegmentT\], ~MessageSegmentT, str, Mapping\[str, Any\]\]_) - 可以被转化为消息的数据。

- **Returns**

  Type: _None_

### _method_ `copy(self)` {#Message.copy}

返回自身的浅复制。

- **Returns**

  Type: _Self_

  自身的浅复制。

### _method_ `endswith(self, suffix, start = None, end = None)` {#Message.endswith}

实现类似字符串的 `endswith()` 方法。

当 `suffix` 类型是 `str` 时，会将自身转换为 `str` 类型，再调用 `str` 类型的 `endswith()` 方法。
当 `suffix` 类型是 MessageSegment 时，`start` 和 `end` 参数将不其作用，
    会判断列表的最后一个消息字段是否和 `suffix` 相等。

- **Arguments**

  - **suffix** (_Union\[str, ~MessageSegmentT\]_) - 后缀。

  - **start** (_Optional\[SupportsIndex\]_) - 开始检查位置。

  - **end** (_Optional\[SupportsIndex\]_) - 停止检查位置。

- **Returns**

  Type: _bool_

  检查结果。

### _method_ `get_plain_text(self)` {#Message.get\_plain\_text}

获取消息中的纯文本部分。

- **Returns**

  Type: _str_

  消息中的纯文本部分。

### _method_ `get_segment_class()` {#Message.get\_segment\_class}

获取消息字段类。

- **Returns**

  Type: _Type\[~MessageSegmentT\]_

  消息字段类。

### _method_ `is_text(self)` {#Message.is\_text}

是否是纯文本消息。

- **Returns**

  Type: _bool_

### _method_ `replace(self, old, new, count = -1)` {#Message.replace}

实现类似字符串的 `replace()` 方法。

当 `old` 为 `str` 类型时，`new` 也必须是 `str`，本方法将仅对 `is_text()` 为 `True` 的消息字段进行处理。
当 `old` 为 MessageSegment 类型时，`new` 可以是 `MessageSegment` 或 `None`，本方法将对所有消息字段进行处理，
    并替换符合条件的消息字段。`None` 表示删除匹配到的消息字段。

- **Arguments**

  - **old** (_Union\[str, ~MessageSegmentT\]_) - 被匹配的字符串或消息字段。

  - **new** (_Union\[str, ~MessageSegmentT, NoneType\]_) - 被替换为的字符串或消息字段。

  - **count** (_int_) - 替换的次数。

- **Returns**

  Type: _Self_

  替换后的消息对象。

### _method_ `startswith(self, prefix, start = None, end = None)` {#Message.startswith}

实现类似字符串的 `startswith()` 方法。

当 `prefix` 类型是 `str` 时，会将自身转换为 `str` 类型，再调用 `str` 类型的 `startswith()` 方法。
当 `prefix` 类型是 `MessageSegment` 时，`start` 和 `end` 参数将不其作用，
    会判断列表的第一个消息字段是否和 `prefix` 相等。

- **Arguments**

  - **prefix** (_Union\[str, ~MessageSegmentT\]_) - 前缀。

  - **start** (_Optional\[SupportsIndex\]_) - 开始检查位置。

  - **end** (_Optional\[SupportsIndex\]_) - 停止检查位置。

- **Returns**

  Type: _bool_

  检查结果。

## _abstract class_ `MessageSegment` {#MessageSegment}

Bases: `abc.ABC`, `pydantic.main.BaseModel`, `collections.abc.Mapping`, `typing.Generic`

消息字段。

本类实现了所有 `Mapping` 类型的方法，这些方法全部是对 `data` 属性的操作。
本类重写了 `+` 和 `+=` 运算符，可以直接和 `Message`, `MessageSegment` 等类型的对象执行取和运算，返回 `Message` 对象。
适配器开发者需要继承本类并重写 `get_message_class()` 方法。

- **Attributes**

  - **type** (_str_) - 消息字段类型。

  - **data** (_Dict\[str, Any\]_) - 消息字段内容。

### _method_ `__init__(__pydantic_self__, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`__init__` uses `__pydantic_self__` instead of the more common `self` for the first arg to
allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

### _method_ `from_mapping(msg)` {#MessageSegment.from\_mapping}

用于将 `Mapping` 转换为消息字段。

如有需要，子类可重写此方法以更改对 `Mapping` 的默认行为。

- **Returns**

  Type: _Self_

  由 Mapping 转换的消息字段。

### _method_ `from_str(msg)` {#MessageSegment.from\_str}

用于将 `str` 转换为消息字段，子类应重写此方法。

- **Returns**

  Type: _Self_

  由 `str` 转换的消息字段。

### _method_ `get(self, key, default = None)` {#MessageSegment.get}

如果 `key` 存在于 `data` 字典中则返回 `key` 的值，否则返回 `default`。

- **Arguments**

  - **key** (_str_)

  - **default** (_Any_)

- **Returns**

  Type: _Any_

### _method_ `get_message_class()` {#MessageSegment.get\_message\_class}

获取消息类。

- **Returns**

  Type: _Type\[~MessageT\]_

  消息类。

### _method_ `is_text(self)` {#MessageSegment.is\_text}

是否是纯文本消息字段。

- **Returns**

  Type: _bool_

  是否是纯文本消息字段。

### _method_ `items(self)` {#MessageSegment.items}

返回由 `data` 字典项 (`(键, 值)` 对) 组成的一个新视图。

- **Returns**

  Type: _ItemsView\[str, Any\]_

### _method_ `keys(self)` {#MessageSegment.keys}

返回由 `data` 字典键组成的一个新视图。

- **Returns**

  Type: _KeysView\[str\]_

### _method_ `values(self)` {#MessageSegment.values}

返回由 `data` 字典值组成的一个新视图。

- **Returns**

  Type: _ValuesView\[Any\]_
