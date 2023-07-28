# alicebot.message

AliceBot 消息。

实现了常用的基本消息 `Message` 和消息字段 `MessageSegment` 模型供适配器使用。
适配器开发者可以根据需要实现此模块中消息类的子类或定义与此不同的消息类型，但建议若可行的话应尽量使用此模块中消息类的子类。

## *class* `Message`(self, message = None) {#Message}

Bases: `list`, `typing.Generic`

消息。

本类是 `List` 的子类，并重写了 `__init__()` 方法，
可以直接处理 `str`, `Mapping`, `Iterable[Mapping]`, `MessageSegment`, `Message`。
其中 `str` 的支持需要适配器开发者重写 `_str_to_message_segment()` 方法实现。
本类重写了 `+` 和 `+=` 运算符，可以直接和 `Message`, `MessageSegment` 等类型的对象执行取和运算。
若开发者实现了 `MessageSegment` 的子类则需要重写 `_message_segment_class()` 方法，
并在 `MessageSegment` 的子类中重写 `_message_class()` 方法。

- **Arguments**

  - **message** (*Union[Self, ~T_MessageSegment, str, Mapping[str, Any], Iterable[Union[~T_MessageSegment, str, Mapping[str, Any]]], NoneType]*) - 可以被转化为消息的数据。

  - ***args** - 其他参数。

### *method* `copy(self)` {#Message.copy}

返回自身的浅复制。

- **Returns**

  Type: *Self*

  自身的浅复制。

### *method* `deepcopy(self)` {#Message.deepcopy}

返回自身的深复制。

- **Returns**

  Type: *Self*

  自身的深复制。

### *method* `endswith(self, suffix, start = None, end = None)` {#Message.endswith}

实现类似字符串的 `endswith()` 方法。

当 `suffix` 类型是 `str` 时，会将自身转换为 `str` 类型，再调用 `str` 类型的 `endswith()` 方法。
当 `suffix` 类型是 MessageSegment 时，`start` 和 `end` 参数将不其作用，
    会判断列表的最后一个消息字段是否和 `suffix` 相等。

- **Arguments**

  - **suffix** (*Union[str, ~T_MessageSegment]*) - 后缀。

  - **start** (*Optional[SupportsIndex]*) - 开始检查位置。

  - **end** (*Optional[SupportsIndex]*) - 停止检查位置。

- **Returns**

  Type: *bool*

  检查结果。

### *method* `get_plain_text(self)` {#Message.get_plain_text}

获取消息中的纯文本部分。

- **Returns**

  Type: *str*

  消息中的纯文本部分。

### *method* `is_text(self)` {#Message.is_text}

是否是纯文本消息。

- **Returns**

  Type: *bool*

### *method* `replace(self, old, new, count = -1)` {#Message.replace}

实现类似字符串的 `replace()` 方法。

当 `old` 为 `str` 类型时，`new` 也必须是 `str`，本方法将仅对 `is_text()` 为 `True` 的消息字段进行处理。
当 `old` 为 MessageSegment 类型时，`new` 可以是 `MessageSegment` 或 `None`，本方法将对所有消息字段进行处理，
    并替换符合条件的消息字段。`None` 表示删除匹配到的消息字段。

- **Arguments**

  - **old** (*Union[str, ~T_MessageSegment]*) - 被匹配的字符串或消息字段。

  - **new** (*Union[str, ~T_MessageSegment, NoneType]*) - 被替换为的字符串或消息字段。

  - **count** (*int*) - 替换的次数。

- **Returns**

  Type: *Self*

  替换后的消息对象。

### *method* `startswith(self, prefix, start = None, end = None)` {#Message.startswith}

实现类似字符串的 `startswith()` 方法。

当 `prefix` 类型是 `str` 时，会将自身转换为 `str` 类型，再调用 `str` 类型的 `startswith()` 方法。
当 `prefix` 类型是 `MessageSegment` 时，`start` 和 `end` 参数将不其作用，
    会判断列表的第一个消息字段是否和 `prefix` 相等。

- **Arguments**

  - **prefix** (*Union[str, ~T_MessageSegment]*) - 前缀。

  - **start** (*Optional[SupportsIndex]*) - 开始检查位置。

  - **end** (*Optional[SupportsIndex]*) - 停止检查位置。

- **Returns**

  Type: *bool*

  检查结果。

## *class* `MessageSegment`(self, type, data = \<factory\>) {#MessageSegment}

Bases: `collections.abc.Mapping`, `typing.Generic`

消息字段。

本类实现了所有映射类型的方法，这些方法全部是对 `data` 属性的操作。
本类重写了 `+` 和 `+=` 运算符，可以直接和 `Message`, `MessageSegment` 等类型的对象执行取和运算，返回 `Message` 对象。
若开发者实现了 `Message` 和 `MessageSegment` 的子类则需要重写 `_message_class()` 方法。

- **Arguments**

  - **type** (*str*)

  - **data** (*Dict[str, Any]*)

- **Attributes**

  - **type** (*str*) - 消息字段类型。

  - **data** (*Dict[str, Any]*) - 消息字段内容。

### *method* `as_dict(self)` {#MessageSegment.as_dict}

将当前对象解析为 `dict` 对象，开发者可重写本方法以适配特殊的解析方式。

- **Returns**

  Type: *Dict[str, Any]*

  `dict` 对象。

### *method* `copy(self)` {#MessageSegment.copy}

返回自身的浅复制。

- **Returns**

  Type: *Self*

  自身的浅复制。

### *method* `deepcopy(self)` {#MessageSegment.deepcopy}

返回自身的深复制。

- **Returns**

  Type: *Self*

  自身的深复制。

### *method* `get(self, key, default = None)` {#MessageSegment.get}

如果 `key` 存在于 `data` 字典中则返回 `key` 的值，否则返回 `default`。

- **Arguments**

  - **key** (*str*)

  - **default** (*Any*)

### *method* `is_text(self)` {#MessageSegment.is_text}

是否是纯文本消息字段。

- **Returns**

  Type: *bool*

  是否是纯文本消息字段。

### *method* `items(self)` {#MessageSegment.items}

返回由 `data` 字典项 (`(键, 值)` 对) 组成的一个新视图。

### *method* `keys(self)` {#MessageSegment.keys}

返回由 `data` 字典键组成的一个新视图。

### *method* `values(self)` {#MessageSegment.values}

返回由 `data` 字典值组成的一个新视图。