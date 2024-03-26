# alicebot.event

AliceBot 事件。

事件类的基类。适配器开发者应实现此事件类基类的子类。

## _class_ `Event` {#Event}

Bases: `abc.ABC`, `pydantic.main.BaseModel`, `typing.Generic`

事件类的基类。

- **Attributes**

  - **adapter** (_Any_) - 产生当前事件的适配器对象。

  - **type** (_Optional\[str\]_) - 事件类型。

  - **\_\_handled\_\_** - 表示事件是否被处理过了，用于适配器处理。警告：请勿手动更改此属性的值。

### _method_ `__init__(self, /, **data)` {#BaseModel---init--}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _abstract class_ `MessageEvent` {#MessageEvent}

Bases: `alicebot.event.Event`, `typing.Generic`

通用的消息事件类的基类。

### _method_ `__init__(self, /, **data)` {#BaseModel---init--}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

### _async method_ `ask(self, message, max_try_times = None, timeout = None)` {#MessageEvent-ask}

询问消息。

表示回复一个消息后获取用户的回复。
相当于 `reply()` 后执行 `get()`。

- **Arguments**

  - **message** (_str_) - 回复消息的内容。

  - **max\_try\_times** (_Optional\[int\]_) - 最大事件数。

  - **timeout** (_Union\[int, float, NoneType\]_) - 超时时间。

- **Returns**

  Type: _Self_

  用户回复的消息事件。

### _async method_ `get(self, *, max_try_times = None, timeout = None)` {#MessageEvent-get}

获取用户回复消息。

相当于 `Bot` 的 `get()`，条件为适配器、事件类型、发送人相同。

- **Arguments**

  - **max\_try\_times** (_Optional\[int\]_) - 最大事件数。

  - **timeout** (_Union\[int, float, NoneType\]_) - 超时时间。

- **Returns**

  Type: _Self_

  用户回复的消息事件。

- **Raises**

  - **GetEventTimeout** - 超过最大事件数或超时。

### _method_ `get_plain_text(self)` {#MessageEvent-get-plain-text}

获取消息的纯文本内容。

- **Returns**

  Type: _str_

  消息的纯文本内容。

### _method_ `get_sender_id(self)` {#MessageEvent-get-sender-id}

获取消息的发送者的唯一标识符。

- **Returns**

  Type: _Union\[NoneType, int, str\]_

  消息的发送者的唯一标识符。

### _async method_ `is_same_sender(self, other)` {#MessageEvent-is-same-sender}

判断自身和另一个事件是否是同一个发送者。

- **Arguments**

  - **other** (_Self_) - 另一个事件。

- **Returns**

  Type: _bool_

  是否是同一个发送者。

### _async method_ `reply(self, message)` {#MessageEvent-reply}

回复消息。

- **Arguments**

  - **message** (_str_) - 回复消息的内容。

- **Returns**

  Type: _Any_

  回复消息动作的响应。
