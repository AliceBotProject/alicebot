# alicebot.adapter.mirai.event.message

消息事件。

## *class* `MessageEvent`(self, adapter, **data) {#MessageEvent}

Bases: `alicebot.adapter.mirai.event.base.MiraiEvent`, `alicebot.event.MessageEvent`

消息事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **sender** (*Union[alicebot.adapter.mirai.event.base.FriendInfo, alicebot.adapter.mirai.event.base.GroupMemberInfo, alicebot.adapter.mirai.event.base.OtherClientSender]*)

  - **messageChain** (*alicebot.adapter.mirai.message.MiraiMessage*)

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

### *readonly property* `message` {#MessageEvent.message}

Type: *alicebot.adapter.mirai.message.MiraiMessage*

与 messageChain 相同。

### *async method* `reply(self, message, quote = False)` {#MessageEvent.reply}

回复消息。

- **Arguments**

  - **message** (*T_MiraiMSG*) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (*bool*) - 引用消息，默认为 `False`。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `FriendMessage`(self, adapter, **data) {#FriendMessage}

Bases: `alicebot.adapter.mirai.event.message.MessageEvent`

好友消息

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['FriendMessage']*)

  - **sender** (*alicebot.adapter.mirai.event.base.FriendInfo*)

### *async method* `reply(self, message, quote = False)` {#FriendMessage.reply}

回复消息。

- **Arguments**

  - **message** (*T_MiraiMSG*) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (*bool*) - 引用消息，默认为 `False`。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `GroupMessage`(self, adapter, **data) {#GroupMessage}

Bases: `alicebot.adapter.mirai.event.message.MessageEvent`

群消息

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['GroupMessage']*)

  - **sender** (*alicebot.adapter.mirai.event.base.GroupMemberInfo*)

### *async method* `reply(self, message, quote = False)` {#GroupMessage.reply}

回复消息。

- **Arguments**

  - **message** (*T_MiraiMSG*) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (*bool*) - 引用消息，默认为 `False`。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `TempMessage`(self, adapter, **data) {#TempMessage}

Bases: `alicebot.adapter.mirai.event.message.MessageEvent`

群临时消息

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['TempMessage']*)

  - **sender** (*alicebot.adapter.mirai.event.base.GroupMemberInfo*)

### *async method* `reply(self, message, quote = False)` {#TempMessage.reply}

回复消息。

- **Arguments**

  - **message** (*T_MiraiMSG*) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (*bool*) - 引用消息，默认为 `False`。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `StrangerMessage`(self, adapter, **data) {#StrangerMessage}

Bases: `alicebot.adapter.mirai.event.message.MessageEvent`

陌生人消息

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['StrangerMessage']*)

  - **sender** (*alicebot.adapter.mirai.event.base.FriendInfo*)

### *async method* `reply(self, message, quote = False)` {#StrangerMessage.reply}

回复消息。

- **Arguments**

  - **message** (*T_MiraiMSG*) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (*bool*) - 引用消息，默认为 `False`。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `OtherClientMessage`(self, adapter, **data) {#OtherClientMessage}

Bases: `alicebot.adapter.mirai.event.message.MessageEvent`

其他客户端消息

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['OtherClientMessage']*)

  - **sender** (*alicebot.adapter.mirai.event.base.OtherClientSender*)

### *async method* `reply(self, message, quote = False)` {#OtherClientMessage.reply}

回复消息。

- **Arguments**

  - **message** (*T_MiraiMSG*) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (*bool*) - 引用消息，默认为 `False`。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。