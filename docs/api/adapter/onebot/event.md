# alicebot.adapter.onebot.event

OneBot 适配器事件。

## _class_ `BotSelf` {#BotSelf}

Bases: `pydantic.main.BaseModel`

机器人自身标识

- **Attributes**

  - **platform** (_str_)

  - **user\_id** (_str_)

## _class_ `ImplVersion` {#ImplVersion}

Bases: `pydantic.main.BaseModel`

实现版本

- **Attributes**

  - **impl** (_str_)

  - **version** (_str_)

  - **onebot\_version** (_str_)

## _class_ `BotStatus` {#BotStatus}

Bases: `pydantic.main.BaseModel`

机器人状态

- **Attributes**

  - **self** (_BotSelf_)

  - **online** (_bool_)

## _class_ `Status` {#Status}

Bases: `pydantic.main.BaseModel`

运行状态

- **Attributes**

  - **good** (_bool_)

  - **bots** (_list\[alicebot.adapter.onebot.event.BotStatus\]_)

## _class_ `OneBotEvent` {#OneBotEvent}

Bases: `alicebot.event.Event[OneBotAdapter]`

OneBot 事件基类

- **Attributes**

  - **id** (_str_)

  - **time** (_float_)

  - **type** (_Literal\['meta', 'message', 'notice', 'request'\]_)

  - **detail\_type** (_str_)

  - **sub\_type** (_str_)

### _method_ `get_event_type()` {#OneBotEvent-get-event-type}

获取事件类型。

- **Returns**

  Type: _tuple\[typing.Optional\[str\], typing.Optional\[str\], typing.Optional\[str\]\]_

  事件类型。

## _class_ `BotEvent` {#BotEvent}

Bases: `alicebot.adapter.onebot.event.OneBotEvent`

包含 self 字段的机器人事件

- **Attributes**

  - **self** (_BotSelf_)

### _readonly property_ `to_me` {#BotEvent-to-me}

Type: _bool_

是否是发给自己的。

## _class_ `MetaEvent` {#MetaEvent}

Bases: `alicebot.adapter.onebot.event.OneBotEvent`

元事件

- **Attributes**

  - **type** (_Literal\['meta'\]_)

## _class_ `ConnectMetaEvent` {#ConnectMetaEvent}

Bases: `alicebot.adapter.onebot.event.MetaEvent`

连接事件

- **Attributes**

  - **detail\_type** (_Literal\['connect'\]_)

  - **version** (_ImplVersion_)

## _class_ `HeartbeatMetaEvent` {#HeartbeatMetaEvent}

Bases: `alicebot.adapter.onebot.event.MetaEvent`

心跳事件

- **Attributes**

  - **detail\_type** (_Literal\['heartbeat'\]_)

  - **interval** (_int_)

## _class_ `StatusUpdateMetaEvent` {#StatusUpdateMetaEvent}

Bases: `alicebot.adapter.onebot.event.MetaEvent`

状态更新事件

- **Attributes**

  - **detail\_type** (_Literal\['status\_update'\]_)

  - **status** (_Status_)

## _class_ `MessageEvent` {#MessageEvent}

Bases: `alicebot.adapter.onebot.event.BotEvent`, `alicebot.event.MessageEvent[OneBotAdapter]`

消息事件

- **Attributes**

  - **type** (_Literal\['message'\]_)

  - **message\_id** (_str_)

  - **message** (_alicebot.adapter.onebot.message.OneBotMessage_)

  - **alt\_message** (_str_)

  - **user\_id** (_str_)

### _method_ `get_plain_text(self)` {#MessageEvent-get-plain-text}

获取消息的纯文本内容。

- **Returns**

  Type: _str_

  消息的纯文本内容。

### _method_ `get_sender_id(self)` {#MessageEvent-get-sender-id}

获取消息的发送者的唯一标识符。

- **Returns**

  Type: _str_

  消息的发送者的唯一标识符。

### _async method_ `reply(self, message)` {#MessageEvent-reply}

回复消息。

- **Arguments**

  - **message** (_Union\[list\[alicebot.adapter.onebot.message.OneBotMessageSegment\], alicebot.adapter.onebot.message.OneBotMessageSegment, str, collections.abc.Mapping\[str, Any\]\]_) - 回复消息的内容，同 `call_api()` 方法。

- **Returns**

  Type: _dict\[str, typing.Any\]_

  API 请求响应。

## _class_ `PrivateMessageEvent` {#PrivateMessageEvent}

Bases: `alicebot.adapter.onebot.event.MessageEvent`

私聊消息事件

- **Attributes**

  - **detail\_type** (_Literal\['private'\]_)

### _async method_ `reply(self, message)` {#PrivateMessageEvent-reply}

回复消息。

- **Arguments**

  - **message** (_Union\[list\[alicebot.adapter.onebot.message.OneBotMessageSegment\], alicebot.adapter.onebot.message.OneBotMessageSegment, str, collections.abc.Mapping\[str, Any\]\]_) - 回复消息的内容，同 `call_api()` 方法。

- **Returns**

  Type: _dict\[str, typing.Any\]_

  API 请求响应。

## _class_ `GroupMessageEvent` {#GroupMessageEvent}

Bases: `alicebot.adapter.onebot.event.MessageEvent`

群消息事件

- **Attributes**

  - **detail\_type** (_Literal\['group'\]_)

  - **group\_id** (_str_)

### _async method_ `reply(self, message)` {#GroupMessageEvent-reply}

回复消息。

- **Arguments**

  - **message** (_Union\[list\[alicebot.adapter.onebot.message.OneBotMessageSegment\], alicebot.adapter.onebot.message.OneBotMessageSegment, str, collections.abc.Mapping\[str, Any\]\]_) - 回复消息的内容，同 `call_api()` 方法。

- **Returns**

  Type: _dict\[str, typing.Any\]_

  API 请求响应。

## _class_ `ChannelMessageEvent` {#ChannelMessageEvent}

Bases: `alicebot.adapter.onebot.event.MessageEvent`

频道消息事件

- **Attributes**

  - **detail\_type** (_Literal\['channel'\]_)

  - **guild\_id** (_str_)

  - **channel\_id** (_str_)

### _async method_ `reply(self, message)` {#ChannelMessageEvent-reply}

回复消息。

- **Arguments**

  - **message** (_Union\[list\[alicebot.adapter.onebot.message.OneBotMessageSegment\], alicebot.adapter.onebot.message.OneBotMessageSegment, str, collections.abc.Mapping\[str, Any\]\]_) - 回复消息的内容，同 `call_api()` 方法。

- **Returns**

  Type: _dict\[str, typing.Any\]_

  API 请求响应。

## _class_ `NoticeEvent` {#NoticeEvent}

Bases: `alicebot.adapter.onebot.event.BotEvent`

通知事件

- **Attributes**

  - **type** (_Literal\['notice'\]_)

## _class_ `FriendIncreaseEvent` {#FriendIncreaseEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

好友增加事件

- **Attributes**

  - **detail\_type** (_Literal\['friend\_increase'\]_)

  - **user\_id** (_str_)

## _class_ `FriendDecreaseEvent` {#FriendDecreaseEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

好友减少事件

- **Attributes**

  - **detail\_type** (_Literal\['friend\_decrease'\]_)

  - **user\_id** (_str_)

## _class_ `PrivateMessageDeleteEvent` {#PrivateMessageDeleteEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

私聊消息删除

- **Attributes**

  - **detail\_type** (_Literal\['private\_message\_delete'\]_)

  - **message\_id** (_str_)

  - **user\_id** (_str_)

## _class_ `GroupMemberIncreaseEvent` {#GroupMemberIncreaseEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

群成员增加事件

- **Attributes**

  - **detail\_type** (_Literal\['group\_member\_increase'\]_)

  - **group\_id** (_str_)

  - **user\_id** (_str_)

  - **operator\_id** (_str_)

## _class_ `GroupMemberDecreaseEvent` {#GroupMemberDecreaseEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

群成员减少事件

- **Attributes**

  - **detail\_type** (_Literal\['group\_member\_decrease'\]_)

  - **group\_id** (_str_)

  - **user\_id** (_str_)

  - **operator\_id** (_str_)

## _class_ `GroupMessageDeleteEvent` {#GroupMessageDeleteEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

群消息删除事件

- **Attributes**

  - **detail\_type** (_Literal\['group\_message\_delete'\]_)

  - **group\_id** (_str_)

  - **message\_id** (_str_)

  - **user\_id** (_str_)

  - **operator\_id** (_str_)

## _class_ `GuildMemberIncreaseEvent` {#GuildMemberIncreaseEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

群组成员增加事件

- **Attributes**

  - **detail\_type** (_Literal\['guild\_member\_increase'\]_)

  - **guild\_id** (_str_)

  - **user\_id** (_str_)

  - **operator\_id** (_str_)

## _class_ `GuildMemberDecreaseEvent` {#GuildMemberDecreaseEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

群组成员减少事件

- **Attributes**

  - **detail\_type** (_Literal\['guild\_member\_decrease'\]_)

  - **guild\_id** (_str_)

  - **user\_id** (_str_)

  - **operator\_id** (_str_)

## _class_ `ChannelMemberIncreaseEvent` {#ChannelMemberIncreaseEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

频道成员增加事件

- **Attributes**

  - **detail\_type** (_Literal\['channel\_member\_increase'\]_)

  - **guild\_id** (_str_)

  - **channel\_id** (_str_)

  - **user\_id** (_str_)

  - **operator\_id** (_str_)

## _class_ `ChannelMemberDecreaseEvent` {#ChannelMemberDecreaseEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

频道成员减少事件

- **Attributes**

  - **detail\_type** (_Literal\['channel\_member\_decrease'\]_)

  - **guild\_id** (_str_)

  - **channel\_id** (_str_)

  - **user\_id** (_str_)

  - **operator\_id** (_str_)

## _class_ `ChannelMessageDeleteEvent` {#ChannelMessageDeleteEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

频道消息删除事件

- **Attributes**

  - **detail\_type** (_Literal\['channel\_message\_delete'\]_)

  - **guild\_id** (_str_)

  - **channel\_id** (_str_)

  - **message\_id** (_str_)

  - **user\_id** (_str_)

  - **operator\_id** (_str_)

## _class_ `ChannelCreateEvent` {#ChannelCreateEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

频道新建事件

- **Attributes**

  - **detail\_type** (_Literal\['channel\_create'\]_)

  - **guild\_id** (_str_)

  - **channel\_id** (_str_)

  - **operator\_id** (_str_)

## _class_ `ChannelDeleteEvent` {#ChannelDeleteEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

频道删除事件

- **Attributes**

  - **detail\_type** (_Literal\['channel\_delete'\]_)

  - **guild\_id** (_str_)

  - **channel\_id** (_str_)

  - **operator\_id** (_str_)

## _class_ `RequestEvent` {#RequestEvent}

Bases: `alicebot.adapter.onebot.event.BotEvent`

请求事件

- **Attributes**

  - **type** (_Literal\['request'\]_)
