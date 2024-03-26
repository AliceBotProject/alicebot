# alicebot.adapter.mirai.event.message

消息事件。

## _abstract class_ `MiraiBaseMessageEvent` {#MiraiBaseMessageEvent}

Bases: `alicebot.adapter.mirai.event.base.MiraiEvent`, `alicebot.event.MessageEvent[MiraiAdapter]`

Mirai 消息事件基类

- **Attributes**

  - **messageChain** (_alicebot.adapter.mirai.message.MiraiMessage_)

### _method_ `get_plain_text(self)` {#MiraiBaseMessageEvent-get-plain-text}

获取消息的纯文本内容。

- **Returns**

  Type: _str_

  消息的纯文本内容。

### _readonly property_ `message` {#MiraiBaseMessageEvent-message}

Type: _alicebot.adapter.mirai.message.MiraiMessage_

与 messageChain 相同。

### _async method_ `reply(self, message, quote = False)` {#MiraiBaseMessageEvent-reply}

回复消息。

- **Arguments**

  - **message** (_Union\[List\[alicebot.adapter.mirai.message.MiraiMessageSegment\], alicebot.adapter.mirai.message.MiraiMessageSegment, str, Mapping\[str, Any\]\]_) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (_bool_) - 引用消息，默认为 `False`。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。

## _class_ `MessageEvent` {#MessageEvent}

Bases: `alicebot.adapter.mirai.event.message.MiraiBaseMessageEvent`

消息事件

- **Attributes**

  - **sender** (_Union\[alicebot.adapter.mirai.event.base.FriendInfo, alicebot.adapter.mirai.event.base.GroupMemberInfo, alicebot.adapter.mirai.event.base.OtherClientSender\]_)

### _method_ `get_sender_id(self)` {#MessageEvent-get-sender-id}

获取消息的发送者的唯一标识符。

- **Returns**

  Type: _int_

  消息的发送者的唯一标识符。

### _async method_ `reply(self, message, quote = False)` {#MessageEvent-reply}

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

### _async method_ `reply(self, message, quote = False)` {#FriendMessage-reply}

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

### _async method_ `reply(self, message, quote = False)` {#GroupMessage-reply}

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

### _async method_ `reply(self, message, quote = False)` {#TempMessage-reply}

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

### _async method_ `reply(self, message, quote = False)` {#StrangerMessage-reply}

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

### _async method_ `reply(self, message, quote = False)` {#OtherClientMessage-reply}

回复消息。

- **Arguments**

  - **message** (_Union\[List\[alicebot.adapter.mirai.message.MiraiMessageSegment\], alicebot.adapter.mirai.message.MiraiMessageSegment, str, Mapping\[str, Any\]\]_) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (_bool_) - 引用消息，默认为 `False`。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。

## _class_ `SyncMessage` {#SyncMessage}

Bases: `alicebot.adapter.mirai.event.message.MiraiBaseMessageEvent`

同步消息

- **Attributes**

  - **subject** (_Union\[alicebot.adapter.mirai.event.base.FriendInfo, alicebot.adapter.mirai.event.base.GroupMemberInfo\]_)

### _method_ `get_sender_id(self)` {#SyncMessage-get-sender-id}

获取消息的发送者的唯一标识符。

- **Returns**

  Type: _None_

  消息的发送者的唯一标识符。

### _async method_ `reply(self, message, quote = False)` {#SyncMessage-reply}

回复消息。

- **Arguments**

  - **message** (_Union\[List\[alicebot.adapter.mirai.message.MiraiMessageSegment\], alicebot.adapter.mirai.message.MiraiMessageSegment, str, Mapping\[str, Any\]\]_) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (_bool_) - 引用消息，默认为 `False`。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。

## _class_ `FriendSyncMessage` {#FriendSyncMessage}

Bases: `alicebot.adapter.mirai.event.message.SyncMessage`

同步好友消息

- **Attributes**

  - **type** (_Literal\['FriendSyncMessage'\]_)

  - **subject** (_alicebot.adapter.mirai.event.base.FriendInfo_)

### _async method_ `reply(self, message, quote = False)` {#FriendSyncMessage-reply}

回复消息。

- **Arguments**

  - **message** (_Union\[List\[alicebot.adapter.mirai.message.MiraiMessageSegment\], alicebot.adapter.mirai.message.MiraiMessageSegment, str, Mapping\[str, Any\]\]_) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (_bool_) - 引用消息，默认为 `False`。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。

## _class_ `GroupSyncMessage` {#GroupSyncMessage}

Bases: `alicebot.adapter.mirai.event.message.SyncMessage`

同步群消息

- **Attributes**

  - **type** (_Literal\['GroupSyncMessage'\]_)

  - **subject** (_alicebot.adapter.mirai.event.base.GroupMemberInfo_)

### _async method_ `reply(self, message, quote = False)` {#GroupSyncMessage-reply}

回复消息。

- **Arguments**

  - **message** (_Union\[List\[alicebot.adapter.mirai.message.MiraiMessageSegment\], alicebot.adapter.mirai.message.MiraiMessageSegment, str, Mapping\[str, Any\]\]_) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (_bool_) - 引用消息，默认为 `False`。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。

## _class_ `TempSyncMessage` {#TempSyncMessage}

Bases: `alicebot.adapter.mirai.event.message.SyncMessage`

同步群临时消息

- **Attributes**

  - **type** (_Literal\['TempSyncMessage'\]_)

  - **subject** (_alicebot.adapter.mirai.event.base.GroupMemberInfo_)

### _async method_ `reply(self, message, quote = False)` {#TempSyncMessage-reply}

回复消息。

- **Arguments**

  - **message** (_Union\[List\[alicebot.adapter.mirai.message.MiraiMessageSegment\], alicebot.adapter.mirai.message.MiraiMessageSegment, str, Mapping\[str, Any\]\]_) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (_bool_) - 引用消息，默认为 `False`。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。

## _class_ `StrangerSyncMessage` {#StrangerSyncMessage}

Bases: `alicebot.adapter.mirai.event.message.SyncMessage`

同步陌生人消息

- **Attributes**

  - **type** (_Literal\['StrangerSyncMessage'\]_)

  - **subject** (_alicebot.adapter.mirai.event.base.FriendInfo_)

### _async method_ `reply(self, message, quote = False)` {#StrangerSyncMessage-reply}

回复消息。

- **Arguments**

  - **message** (_Union\[List\[alicebot.adapter.mirai.message.MiraiMessageSegment\], alicebot.adapter.mirai.message.MiraiMessageSegment, str, Mapping\[str, Any\]\]_) - 回复消息的内容，同 `call_api()` 方法。

  - **quote** (_bool_) - 引用消息，默认为 `False`。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。
