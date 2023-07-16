# alicebot.adapter.onebot.event

OntBot 适配器事件。

## *class* `BotSelf`(__pydantic_self__, **data) {#BotSelf}

Bases: `pydantic.main.BaseModel`

机器人自身标识

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **platform** (*str*)

  - **user_id** (*str*)

## *class* `ImplVersion`(__pydantic_self__, **data) {#ImplVersion}

Bases: `pydantic.main.BaseModel`

实现版本

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **impl** (*str*)

  - **version** (*str*)

  - **onebot_version** (*str*)

## *class* `BotStatus`(__pydantic_self__, **data) {#BotStatus}

Bases: `pydantic.main.BaseModel`

机器人状态

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **self** (*alicebot.adapter.onebot.event.BotSelf*)

  - **online** (*bool*)

## *class* `Status`(__pydantic_self__, **data) {#Status}

Bases: `pydantic.main.BaseModel`

运行状态

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **good** (*bool*)

  - **bots** (*List[alicebot.adapter.onebot.event.BotStatus]*)

## *class* `OntBotEvent`(self, adapter, **data) {#OntBotEvent}

Bases: `alicebot.event.Event`

CQHTTP 事件基类

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **id** (*str*)

  - **time** (*float*)

  - **type** (*Literal['meta', 'message', 'notice', 'request']*)

  - **detail_type** (*str*)

  - **sub_type** (*str*)

### *class method* `get_event_type(cls)` {#OntBotEvent.get_event_type}

获取事件类型。

- **Returns**

  Type: *Tuple[Optional[str], Optional[str], Optional[str]]*

  事件类型。

## *class* `BotEvent`(self, adapter, **data) {#BotEvent}

Bases: `alicebot.adapter.onebot.event.OntBotEvent`

包含 self 字段的机器人事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **self** (*alicebot.adapter.onebot.event.BotSelf*)

### *readonly property* `to_me` {#BotEvent.to_me}

Type: *bool*

是否是发给自己的。

## *class* `MetaEvent`(self, adapter, **data) {#MetaEvent}

Bases: `alicebot.adapter.onebot.event.OntBotEvent`

元事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['meta']*)

## *class* `ConnectMetaEvent`(self, adapter, **data) {#ConnectMetaEvent}

Bases: `alicebot.adapter.onebot.event.MetaEvent`

连接事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **detail_type** (*Literal['connect']*)

  - **version** (*alicebot.adapter.onebot.event.ImplVersion*)

## *class* `HeartbeatMetaEvent`(self, adapter, **data) {#HeartbeatMetaEvent}

Bases: `alicebot.adapter.onebot.event.MetaEvent`

心跳事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **detail_type** (*Literal['heartbeat']*)

  - **interval** (*int*)

## *class* `StatusUpdateMetaEvent`(self, adapter, **data) {#StatusUpdateMetaEvent}

Bases: `alicebot.adapter.onebot.event.MetaEvent`

状态更新事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **detail_type** (*Literal['status_update']*)

  - **status** (*alicebot.adapter.onebot.event.Status*)

## *class* `MessageEvent`(self, adapter, **data) {#MessageEvent}

Bases: `alicebot.adapter.onebot.event.BotEvent`, `alicebot.event.MessageEvent`

消息事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['message']*)

  - **message_id** (*str*)

  - **message** (*alicebot.adapter.onebot.message.OneBotMessage*)

  - **alt_message** (*str*)

  - **user_id** (*str*)

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

### *async method* `reply(self, message)` {#MessageEvent.reply}

回复消息。

- **Arguments**

  - **message** (*T_OBMSG*) - 回复消息的内容，同 `call_api()` 方法。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `PrivateMessageEvent`(self, adapter, **data) {#PrivateMessageEvent}

Bases: `alicebot.adapter.onebot.event.MessageEvent`

私聊消息事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **detail_type** (*Literal['private']*)

### *async method* `reply(self, message)` {#PrivateMessageEvent.reply}

回复消息。

- **Arguments**

  - **message** (*T_OBMSG*) - 回复消息的内容，同 `call_api()` 方法。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `GroupMessageEvent`(self, adapter, **data) {#GroupMessageEvent}

Bases: `alicebot.adapter.onebot.event.MessageEvent`

群消息事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **detail_type** (*Literal['group']*)

  - **group_id** (*str*)

### *async method* `reply(self, message)` {#GroupMessageEvent.reply}

回复消息。

- **Arguments**

  - **message** (*T_OBMSG*) - 回复消息的内容，同 `call_api()` 方法。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `ChannelMessageEvent`(self, adapter, **data) {#ChannelMessageEvent}

Bases: `alicebot.adapter.onebot.event.MessageEvent`

频道消息事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **detail_type** (*Literal['channel']*)

  - **guild_id** (*str*)

  - **channel_id** (*str*)

### *async method* `reply(self, message)` {#ChannelMessageEvent.reply}

回复消息。

- **Arguments**

  - **message** (*T_OBMSG*) - 回复消息的内容，同 `call_api()` 方法。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `NoticeEvent`(self, adapter, **data) {#NoticeEvent}

Bases: `alicebot.adapter.onebot.event.BotEvent`

通知事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['notice']*)

## *class* `FriendIncreaseEvent`(self, adapter, **data) {#FriendIncreaseEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

好友增加事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **detail_type** (*Literal['friend_increase']*)

  - **user_id** (*str*)

## *class* `FriendDecreaseEvent`(self, adapter, **data) {#FriendDecreaseEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

好友减少事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **detail_type** (*Literal['friend_decrease']*)

  - **user_id** (*str*)

## *class* `PrivateMessageDeleteEvent`(self, adapter, **data) {#PrivateMessageDeleteEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

私聊消息删除

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **detail_type** (*Literal['private_message_delete']*)

  - **message_id** (*str*)

  - **user_id** (*str*)

## *class* `GroupMemberIncreaseEvent`(self, adapter, **data) {#GroupMemberIncreaseEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

群成员增加事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **detail_type** (*Literal['group_member_increase']*)

  - **group_id** (*str*)

  - **user_id** (*str*)

  - **operator_id** (*str*)

## *class* `GroupMemberDecreaseEvent`(self, adapter, **data) {#GroupMemberDecreaseEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

群成员减少事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **detail_type** (*Literal['group_member_decrease']*)

  - **group_id** (*str*)

  - **user_id** (*str*)

  - **operator_id** (*str*)

## *class* `GroupMessageDeleteEvent`(self, adapter, **data) {#GroupMessageDeleteEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

群消息删除事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **detail_type** (*Literal['group_message_delete']*)

  - **group_id** (*str*)

  - **message_id** (*str*)

  - **user_id** (*str*)

  - **operator_id** (*str*)

## *class* `GuildMemberIncreaseEvent`(self, adapter, **data) {#GuildMemberIncreaseEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

群组成员增加事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **detail_type** (*Literal['guild_member_increase']*)

  - **guild_id** (*str*)

  - **user_id** (*str*)

  - **operator_id** (*str*)

## *class* `GuildMemberDecreaseEvent`(self, adapter, **data) {#GuildMemberDecreaseEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

群组成员减少事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **detail_type** (*Literal['guild_member_decrease']*)

  - **guild_id** (*str*)

  - **user_id** (*str*)

  - **operator_id** (*str*)

## *class* `ChannelMemberIncreaseEvent`(self, adapter, **data) {#ChannelMemberIncreaseEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

频道成员增加事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **detail_type** (*Literal['channel_member_increase']*)

  - **guild_id** (*str*)

  - **channel_id** (*str*)

  - **user_id** (*str*)

  - **operator_id** (*str*)

## *class* `ChannelMemberDecreaseEvent`(self, adapter, **data) {#ChannelMemberDecreaseEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

频道成员减少事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **detail_type** (*Literal['channel_member_decrease']*)

  - **guild_id** (*str*)

  - **channel_id** (*str*)

  - **user_id** (*str*)

  - **operator_id** (*str*)

## *class* `ChannelMessageDeleteEvent`(self, adapter, **data) {#ChannelMessageDeleteEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

频道消息删除事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **detail_type** (*Literal['channel_message_delete']*)

  - **guild_id** (*str*)

  - **channel_id** (*str*)

  - **message_id** (*str*)

  - **user_id** (*str*)

  - **operator_id** (*str*)

## *class* `ChannelCreateEvent`(self, adapter, **data) {#ChannelCreateEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

频道新建事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **detail_type** (*Literal['channel_create']*)

  - **guild_id** (*str*)

  - **channel_id** (*str*)

  - **operator_id** (*str*)

## *class* `ChannelDeleteEvent`(self, adapter, **data) {#ChannelDeleteEvent}

Bases: `alicebot.adapter.onebot.event.NoticeEvent`

频道删除事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **detail_type** (*Literal['channel_delete']*)

  - **guild_id** (*str*)

  - **channel_id** (*str*)

  - **operator_id** (*str*)

## *class* `RequestEvent`(self, adapter, **data) {#RequestEvent}

Bases: `alicebot.adapter.onebot.event.BotEvent`

请求事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['request']*)