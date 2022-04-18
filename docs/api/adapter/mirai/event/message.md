# alicebot.adapter.mirai.event.message

## *class* `MessageEvent`(__pydantic_self__, **data) {#MessageEvent}

Bases: `alicebot.adapter.mirai.event.base.MiraiEvent`

消息事件

- **Attributes**

  - **messageChain** (*alicebot.adapter.mirai.message.MiraiMessage*)

### *method* `get_plain_text(self)` {#MessageEvent.get_plain_text}

- **Returns**

  Type: *str*

### *readonly property* `message` {#MessageEvent.message}

### *async method* `reply(self, msg, quote = False)` {#MessageEvent.reply}

回复消息。

- **Arguments**

  - **msg** (*Union[str, Mapping, Iterable[Mapping], MiraiMessageSegment, MiraiMessage]*) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (*bool*) - 引用消息，默认为 `False`。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `FriendMessage`(__pydantic_self__, **data) {#FriendMessage}

Bases: `alicebot.adapter.mirai.event.message.MessageEvent`

好友消息

- **Attributes**

  - **type** (*Literal['FriendMessage']*)

  - **sender** (*alicebot.adapter.mirai.event.base.FriendInfo*)

### *async method* `reply(self, msg, quote = False)` {#FriendMessage.reply}

回复消息。

- **Arguments**

  - **msg** (*Union[str, Mapping, Iterable[Mapping], MiraiMessageSegment, MiraiMessage]*) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (*bool*) - 引用消息，默认为 `False`。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `GroupMessage`(__pydantic_self__, **data) {#GroupMessage}

Bases: `alicebot.adapter.mirai.event.message.MessageEvent`

群消息

- **Attributes**

  - **type** (*Literal['GroupMessage']*)

  - **sender** (*alicebot.adapter.mirai.event.base.GroupMemberInfo*)

### *async method* `reply(self, msg, quote = False)` {#GroupMessage.reply}

回复消息。

- **Arguments**

  - **msg** (*Union[str, Mapping, Iterable[Mapping], MiraiMessageSegment, MiraiMessage]*) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (*bool*) - 引用消息，默认为 `False`。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `TempMessage`(__pydantic_self__, **data) {#TempMessage}

Bases: `alicebot.adapter.mirai.event.message.MessageEvent`

群临时消息

- **Attributes**

  - **type** (*Literal['TempMessage']*)

  - **sender** (*alicebot.adapter.mirai.event.base.GroupMemberInfo*)

### *async method* `reply(self, msg, quote = False)` {#TempMessage.reply}

回复消息。

- **Arguments**

  - **msg** (*Union[str, Mapping, Iterable[Mapping], MiraiMessageSegment, MiraiMessage]*) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (*bool*) - 引用消息，默认为 `False`。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `StrangerMessage`(__pydantic_self__, **data) {#StrangerMessage}

Bases: `alicebot.adapter.mirai.event.message.MessageEvent`

陌生人消息

- **Attributes**

  - **type** (*Literal['StrangerMessage']*)

  - **sender** (*alicebot.adapter.mirai.event.base.FriendInfo*)

### *async method* `reply(self, msg, quote = False)` {#StrangerMessage.reply}

回复消息。

- **Arguments**

  - **msg** (*Union[str, Mapping, Iterable[Mapping], MiraiMessageSegment, MiraiMessage]*) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (*bool*) - 引用消息，默认为 `False`。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `OtherClientMessage`(__pydantic_self__, **data) {#OtherClientMessage}

Bases: `alicebot.adapter.mirai.event.message.MessageEvent`

其他客户端消息

- **Attributes**

  - **type** (*Literal['OtherClientMessage']*)

  - **sender** (*alicebot.adapter.mirai.event.base.OtherClientSender*)

### *async method* `reply(self, msg, quote = False)` {#OtherClientMessage.reply}

回复消息。

- **Arguments**

  - **msg** (*Union[str, Mapping, Iterable[Mapping], MiraiMessageSegment, MiraiMessage]*) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (*bool*) - 引用消息，默认为 `False`。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。