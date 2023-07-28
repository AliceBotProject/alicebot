# alicebot.event

AliceBot 事件。

事件类的基类。适配器开发者应实现此事件类基类的子类。

## *class* `Event`(self, adapter, **data) {#Event}

Bases: `abc.ABC`, `pydantic.main.BaseModel`, `typing.Generic`

事件类的基类。

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **adapter** (*~T_Adapter*) - 产生当前事件的适配器对象。

  - **type** (*Optional[str]*) - 事件类型。

  - **__handled__** - 表示事件是否被处理过了，用于适配器处理。警告：请勿手动更改此属性的值。

### *class* `Config`(self, /, *args, **kwargs) {#Event.Config}

Bases: `object`

- **Arguments**

  - **args**

  - **kwargs**

### *readonly property* `adapter` {#Event.adapter}

Type: *~T_Adapter*

产生当前事件的适配器对象。

## *abstract class* `MessageEvent`(self, adapter, **data) {#MessageEvent}

Bases: `alicebot.event.Event`

通用的消息事件类的基类。

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

### *async method* `ask(self, message, max_try_times = None, timeout = None)` {#MessageEvent.ask}

询问消息。

表示回复一个消息后获取用户的回复。
相当于 `reply()` 后执行 `get()`。

- **Arguments**

  - **message** (*str*) - 回复消息的内容。

  - **max_try_times** (*Optional[int]*) - 最大事件数。

  - **timeout** (*Union[int, float, NoneType]*) - 超时时间。

- **Returns**

  Type: *Self*

  用户回复的消息事件。

### *async method* `get(self, *, max_try_times = None, timeout = None)` {#MessageEvent.get}

获取用户回复消息。

相当于 `Bot` 的 `get()`，条件为适配器、事件类型、发送人相同。

- **Arguments**

  - **max_try_times** (*Optional[int]*) - 最大事件数。

  - **timeout** (*Union[int, float, NoneType]*) - 超时时间。

- **Returns**

  Type: *Self*

  用户回复的消息事件。

- **Raises**

  - **GetEventTimeout** - 超过最大事件数或超时。

### *method* `get_plain_text(self)` {#MessageEvent.get_plain_text}

获取消息的纯文本内容。

- **Returns**

  Type: *str*

  消息的纯文本内容。

### *async method* `is_same_sender(self, other)` {#MessageEvent.is_same_sender}

判断自身和另一个事件是否是同一个发送者。

- **Arguments**

  - **other** (*Self*) - 另一个事件。

- **Returns**

  Type: *bool*

  是否是同一个发送者。

### *async method* `reply(self, message, *args, **kwargs)` {#MessageEvent.reply}

回复消息。

- **Arguments**

  - **message** (*str*) - 回复消息的内容。

  - **args** (*Any*)

  - **kwargs** (*Any*)

- **Returns**

  Type: *Any*

  回复消息动作的响应。