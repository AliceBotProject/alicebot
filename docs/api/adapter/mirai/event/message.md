# alicebot.adapter.mirai.event.message

消息事件。

## _class_ `MessageEvent` {#MessageEvent}

Bases: `alicebot.adapter.mirai.event.base.MiraiEvent`, `alicebot.event.MessageEvent[MiraiAdapter]`

消息事件

- **Attributes**

  - **sender** (_Union\[alicebot.adapter.mirai.event.base.FriendInfo, alicebot.adapter.mirai.event.base.GroupMemberInfo, alicebot.adapter.mirai.event.base.OtherClientSender\]_)

  - **messageChain** (_alicebot.adapter.mirai.message.MiraiMessage_)

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

### _method_ `get_plain_text(self)` {#MessageEvent.get\_plain\_text}

获取消息的纯文本内容。

- **Returns**

  Type: _str_

  消息的纯文本内容。

### _async method_ `is_same_sender(self, other)` {#MessageEvent.is\_same\_sender}

判断自身和另一个事件是否是同一个发送者。

- **Arguments**

  - **other** (_typing\_extensions.Self_) - 另一个事件。

- **Returns**

  Type: _bool_

  是否是同一个发送者。

### _readonly property_ `message` {#MessageEvent.message}

Type: _alicebot.adapter.mirai.message.MiraiMessage_

与 messageChain 相同。

### _async method_ `reply(self, message, quote = False)` {#MessageEvent.reply}

回复消息。

- **Arguments**

  - **message** (_Union\[List\[alicebot.adapter.mirai.message.MiraiMessageSegment\], alicebot.adapter.mirai.message.MiraiMessageSegment, str, Mapping\[str, Any\]\]_) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (_bool_) - 引用消息，默认为 `False`。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。

## _class_ `FriendMessage` {#FriendMessage}

Bases: `alicebot.adapter.mirai.event.message.MessageEvent`

好友消息

- **Attributes**

  - **type** (_Literal\['FriendMessage'\]_)

  - **sender** (_alicebot.adapter.mirai.event.base.FriendInfo_)

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

### _async method_ `reply(self, message, quote = False)` {#FriendMessage.reply}

回复消息。

- **Arguments**

  - **message** (_Union\[List\[alicebot.adapter.mirai.message.MiraiMessageSegment\], alicebot.adapter.mirai.message.MiraiMessageSegment, str, Mapping\[str, Any\]\]_) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (_bool_) - 引用消息，默认为 `False`。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。

## _class_ `GroupMessage` {#GroupMessage}

Bases: `alicebot.adapter.mirai.event.message.MessageEvent`

群消息

- **Attributes**

  - **type** (_Literal\['GroupMessage'\]_)

  - **sender** (_alicebot.adapter.mirai.event.base.GroupMemberInfo_)

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

### _async method_ `reply(self, message, quote = False)` {#GroupMessage.reply}

回复消息。

- **Arguments**

  - **message** (_Union\[List\[alicebot.adapter.mirai.message.MiraiMessageSegment\], alicebot.adapter.mirai.message.MiraiMessageSegment, str, Mapping\[str, Any\]\]_) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (_bool_) - 引用消息，默认为 `False`。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。

## _class_ `TempMessage` {#TempMessage}

Bases: `alicebot.adapter.mirai.event.message.MessageEvent`

群临时消息

- **Attributes**

  - **type** (_Literal\['TempMessage'\]_)

  - **sender** (_alicebot.adapter.mirai.event.base.GroupMemberInfo_)

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

### _async method_ `reply(self, message, quote = False)` {#TempMessage.reply}

回复消息。

- **Arguments**

  - **message** (_Union\[List\[alicebot.adapter.mirai.message.MiraiMessageSegment\], alicebot.adapter.mirai.message.MiraiMessageSegment, str, Mapping\[str, Any\]\]_) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (_bool_) - 引用消息，默认为 `False`。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。

## _class_ `StrangerMessage` {#StrangerMessage}

Bases: `alicebot.adapter.mirai.event.message.MessageEvent`

陌生人消息

- **Attributes**

  - **type** (_Literal\['StrangerMessage'\]_)

  - **sender** (_alicebot.adapter.mirai.event.base.FriendInfo_)

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

### _async method_ `reply(self, message, quote = False)` {#StrangerMessage.reply}

回复消息。

- **Arguments**

  - **message** (_Union\[List\[alicebot.adapter.mirai.message.MiraiMessageSegment\], alicebot.adapter.mirai.message.MiraiMessageSegment, str, Mapping\[str, Any\]\]_) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (_bool_) - 引用消息，默认为 `False`。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。

## _class_ `OtherClientMessage` {#OtherClientMessage}

Bases: `alicebot.adapter.mirai.event.message.MessageEvent`

其他客户端消息

- **Attributes**

  - **type** (_Literal\['OtherClientMessage'\]_)

  - **sender** (_alicebot.adapter.mirai.event.base.OtherClientSender_)

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

### _async method_ `reply(self, message, quote = False)` {#OtherClientMessage.reply}

回复消息。

- **Arguments**

  - **message** (_Union\[List\[alicebot.adapter.mirai.message.MiraiMessageSegment\], alicebot.adapter.mirai.message.MiraiMessageSegment, str, Mapping\[str, Any\]\]_) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (_bool_) - 引用消息，默认为 `False`。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。
