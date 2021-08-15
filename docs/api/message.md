# alicebot.message

## 消息

实现了常用的基本消息 `Message` 和消息字段 `MessageSegment` 模型供适配器使用。
适配器开发者可以根据需要实现此模块中消息类的子类或定义与此不同的消息类型，但建议若可行的话应尽量使用此模块中消息类的子类。


## _class_ `Message`

基类：`list`

消息。
本类是 `list` 的子类，同时重写了 `__init__()` 方法，可以直接处理 str, Mapping, Iterable[Mapping], T_MessageSegment, T_Message。
其中 str 的支持需要适配器开发者重写 `_str_to_message_segment()` 方法实现。
本类重写了 `+` 和 `+=` 运算符，可以直接和 Message, MessageSegment 等类型的对象执行取和运算。
若开发者实现了 MessageSegment 的子类则需要重写 `_set_message_segment_class()` 方法，
并在 MessageSegment 的子类中重写 `_set_message_class()` 方法。


### `copy()`

返回自身的浅复制。


* **返回**

    自身的浅复制。



* **返回类型**

    T_Message



### `deepcopy()`

返回自身的深复制。


* **返回**

    自身的深复制。



* **返回类型**

    T_Message



### `startswith(prefix, start=None, end=None)`

实现类似字符串的 `startswith()` 方法。
当 `prefix` 类型是 str 时，会将自身转换为 str 类型，再调用 str 类型的 `startswith()` 方法。
当 `prefix` 类型是 T_MessageSegment 时，`start` 和 `end` 参数将不其作用，会判断列表的第一个消息字段是否和 `prefix` 相等。


* **参数**

    
    * **prefix** – 前缀。


    * **start** – 开始检查位置。


    * **end** – 停止检查位置。



* **返回**

    检查结果。



* **返回类型**

    bool



### `endswith(suffix, start=None, end=None)`

实现类似字符串的 `endswith()` 方法。
当 `suffix` 类型是 str 时，会将自身转换为 str 类型，再调用 str 类型的 `endswith()` 方法。
当 `suffix` 类型是 T_MessageSegment 时，`start` 和 `end` 参数将不其作用，会判断列表的最后一个消息字段是否和 `suffix` 相等。


* **参数**

    
    * **suffix** – 后缀。


    * **start** – 开始检查位置。


    * **end** – 停止检查位置。



* **返回**

    检查结果。



* **返回类型**

    bool



### `replace(old, new, count=- 1)`

实现类似字符串的 `replace()` 方法。
当 `old` 为 str 类型时，`new` 也必须是 str ，本方法将仅对 `type` 为 `text` 的消息字段进行处理。
当 `old` 为 MessageSegment 类型时，`new` 可以是 MessageSegment 或 None，本方法将对所有消息字段进行处理，并替换符合条件的消息字段。None 表示删除匹配到的消息字段。


* **参数**

    
    * **old** – 被匹配的字符串或消息字段。


    * **new** – 被替换为的字符串或消息字段。


    * **count** – 替换的次数。



* **返回**

    


## _class_ `MessageSegment`

基类：`collections.abc.Mapping`, `typing.Generic`

消息字段。
本类实现了所有映射类型的方法，这些方法全部是对 `data` 属性的操作。
本类重写了 `+` 和 `+=` 运算符，可以直接和 Message, MessageSegment 等类型的对象执行取和运算，返回 Message 对象。
若开发者实现了 Message 和 MessageSegment 的子类则需要重写 `_set_message_class()` 方法。


### `type`

消息字段类型。


### `data`

消息字段内容。


### `copy()`

返回自身的浅复制。


* **返回**

    自身的浅复制。



* **返回类型**

    T_MessageSegment



### `deepcopy()`

返回自身的深复制。


* **返回**

    自身的深复制。



* **返回类型**

    T_MessageSegment



## _class_ `DataclassEncoder`

基类：`json.encoder.JSONEncoder`

用于解析 MessageSegment 的 JSONEncoder 类。
