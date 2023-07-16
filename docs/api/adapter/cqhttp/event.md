# alicebot.adapter.cqhttp.event

CQHTTP 适配器事件。

## *class* `Sender`(__pydantic_self__, **data) {#Sender}

Bases: `pydantic.main.BaseModel`

发送人信息

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **user_id** (*Optional[int]*)

  - **nickname** (*Optional[str]*)

  - **card** (*Optional[str]*)

  - **sex** (*Optional[Literal['male', 'female', 'unknown']]*)

  - **age** (*Optional[int]*)

  - **area** (*Optional[str]*)

  - **level** (*Optional[str]*)

  - **role** (*Optional[str]*)

  - **title** (*Optional[str]*)

## *class* `Anonymous`(__pydantic_self__, **data) {#Anonymous}

Bases: `pydantic.main.BaseModel`

匿名信息

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **id** (*int*)

  - **name** (*str*)

  - **flag** (*str*)

## *class* `File`(__pydantic_self__, **data) {#File}

Bases: `pydantic.main.BaseModel`

文件信息

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **id** (*str*)

  - **name** (*str*)

  - **size** (*int*)

  - **busid** (*int*)

## *class* `Status`(__pydantic_self__, **data) {#Status}

Bases: `pydantic.main.BaseModel`

状态信息

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **online** (*bool*)

  - **good** (*bool*)

### *class* `Config`(self, /, *args, **kwargs) {#Status.Config}

Bases: `object`

- **Arguments**

  - **args**

  - **kwargs**

## *class* `CQHTTPEvent`(self, adapter, **data) {#CQHTTPEvent}

Bases: `alicebot.event.Event`

CQHTTP 事件基类

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Optional[str]*)

  - **time** (*int*)

  - **self_id** (*int*)

  - **post_type** (*str*)

### *class method* `get_event_type(cls)` {#CQHTTPEvent.get_event_type}

获取事件类型。

- **Returns**

  Type: *Tuple[Optional[str], Optional[str], Optional[str]]*

  事件类型。

### *readonly property* `to_me` {#CQHTTPEvent.to_me}

Type: *bool*

当前事件的 `user_id` 是否等于 `self_id`。

## *class* `MessageEvent`(self, adapter, **data) {#MessageEvent}

Bases: `alicebot.adapter.cqhttp.event.CQHTTPEvent`, `alicebot.event.MessageEvent`

消息事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **post_type** (*Literal['message']*)

  - **message_type** (*Literal['private', 'group']*)

  - **sub_type** (*str*)

  - **message_id** (*int*)

  - **user_id** (*int*)

  - **message** (*alicebot.adapter.cqhttp.message.CQHTTPMessage*)

  - **raw_message** (*str*)

  - **font** (*int*)

  - **sender** (*alicebot.adapter.cqhttp.event.Sender*)

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

  - **message** (*T_CQMSG*) - 回复消息的内容，同 `call_api()` 方法。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `PrivateMessageEvent`(self, adapter, **data) {#PrivateMessageEvent}

Bases: `alicebot.adapter.cqhttp.event.MessageEvent`

私聊消息

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **message_type** (*Literal['private']*)

  - **sub_type** (*Literal['friend', 'group', 'other']*)

### *async method* `reply(self, message)` {#PrivateMessageEvent.reply}

回复消息。

- **Arguments**

  - **message** (*T_CQMSG*) - 回复消息的内容，同 `call_api()` 方法。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `GroupMessageEvent`(self, adapter, **data) {#GroupMessageEvent}

Bases: `alicebot.adapter.cqhttp.event.MessageEvent`

群消息

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **message_type** (*Literal['group']*)

  - **sub_type** (*Literal['normal', 'anonymous', 'notice']*)

  - **group_id** (*int*)

  - **anonymous** (*Optional[alicebot.adapter.cqhttp.event.Anonymous]*)

### *async method* `reply(self, message)` {#GroupMessageEvent.reply}

回复消息。

- **Arguments**

  - **message** (*T_CQMSG*) - 回复消息的内容，同 `call_api()` 方法。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `NoticeEvent`(self, adapter, **data) {#NoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.CQHTTPEvent`

通知事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **post_type** (*Literal['notice']*)

  - **notice_type** (*str*)

## *class* `GroupUploadNoticeEvent`(self, adapter, **data) {#GroupUploadNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

群文件上传

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **notice_type** (*Literal['group_upload']*)

  - **user_id** (*int*)

  - **group_id** (*int*)

  - **file** (*alicebot.adapter.cqhttp.event.File*)

## *class* `GroupAdminNoticeEvent`(self, adapter, **data) {#GroupAdminNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

群管理员变动

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **notice_type** (*Literal['group_admin']*)

  - **sub_type** (*Literal['set', 'unset']*)

  - **user_id** (*int*)

  - **group_id** (*int*)

## *class* `GroupDecreaseNoticeEvent`(self, adapter, **data) {#GroupDecreaseNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

群成员减少

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **notice_type** (*Literal['group_decrease']*)

  - **sub_type** (*Literal['leave', 'kick', 'kick_me']*)

  - **group_id** (*int*)

  - **operator_id** (*int*)

  - **user_id** (*int*)

## *class* `GroupIncreaseNoticeEvent`(self, adapter, **data) {#GroupIncreaseNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

群成员增加

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **notice_type** (*Literal['group_increase']*)

  - **sub_type** (*Literal['approve', 'invite']*)

  - **group_id** (*int*)

  - **operator_id** (*int*)

  - **user_id** (*int*)

## *class* `GroupBanNoticeEvent`(self, adapter, **data) {#GroupBanNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

群禁言

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **notice_type** (*Literal['group_ban']*)

  - **sub_type** (*Literal['ban', 'lift_ban']*)

  - **group_id** (*int*)

  - **operator_id** (*int*)

  - **user_id** (*int*)

  - **duration** (*int*)

## *class* `FriendAddNoticeEvent`(self, adapter, **data) {#FriendAddNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

好友添加

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **notice_type** (*Literal['friend_add']*)

  - **user_id** (*int*)

## *class* `GroupRecallNoticeEvent`(self, adapter, **data) {#GroupRecallNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

群消息撤回

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **notice_type** (*Literal['group_recall']*)

  - **group_id** (*int*)

  - **operator_id** (*int*)

  - **user_id** (*int*)

  - **message_id** (*int*)

## *class* `FriendRecallNoticeEvent`(self, adapter, **data) {#FriendRecallNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

好友消息撤回

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **notice_type** (*Literal['friend_recall']*)

  - **user_id** (*int*)

  - **message_id** (*int*)

## *class* `NotifyEvent`(self, adapter, **data) {#NotifyEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

提醒事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **notice_type** (*Literal['notify']*)

  - **sub_type** (*str*)

  - **group_id** (*Optional[int]*)

  - **user_id** (*int*)

## *class* `PokeNotifyEvent`(self, adapter, **data) {#PokeNotifyEvent}

Bases: `alicebot.adapter.cqhttp.event.NotifyEvent`

戳一戳

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **sub_type** (*Literal['poke']*)

  - **target_id** (*int*)

  - **group_id** (*Optional[int]*)

## *class* `GroupLuckyKingNotifyEvent`(self, adapter, **data) {#GroupLuckyKingNotifyEvent}

Bases: `alicebot.adapter.cqhttp.event.NotifyEvent`

群红包运气王

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **sub_type** (*Literal['lucky_king']*)

  - **group_id** (*int*)

  - **target_id** (*int*)

## *class* `GroupHonorNotifyEvent`(self, adapter, **data) {#GroupHonorNotifyEvent}

Bases: `alicebot.adapter.cqhttp.event.NotifyEvent`

群成员荣誉变更

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **sub_type** (*Literal['honor']*)

  - **group_id** (*int*)

  - **honor_type** (*Literal['talkative', 'performer', 'emotion']*)

## *class* `RequestEvent`(self, adapter, **data) {#RequestEvent}

Bases: `alicebot.adapter.cqhttp.event.CQHTTPEvent`

请求事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **post_type** (*Literal['request']*)

  - **request_type** (*str*)

### *async method* `approve(self)` {#RequestEvent.approve}

同意请求。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

### *async method* `refuse(self)` {#RequestEvent.refuse}

拒绝请求。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `FriendRequestEvent`(self, adapter, **data) {#FriendRequestEvent}

Bases: `alicebot.adapter.cqhttp.event.RequestEvent`

加好友请求

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **request_type** (*Literal['friend']*)

  - **user_id** (*int*)

  - **comment** (*str*)

  - **flag** (*str*)

### *async method* `approve(self, remark = '')` {#FriendRequestEvent.approve}

同意请求。

- **Arguments**

  - **remark** (*str*) - 好友备注。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

### *async method* `refuse(self)` {#FriendRequestEvent.refuse}

拒绝请求。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `GroupRequestEvent`(self, adapter, **data) {#GroupRequestEvent}

Bases: `alicebot.adapter.cqhttp.event.RequestEvent`

加群请求／邀请

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **request_type** (*Literal['group']*)

  - **sub_type** (*Literal['add', 'invite']*)

  - **group_id** (*int*)

  - **user_id** (*int*)

  - **comment** (*str*)

  - **flag** (*str*)

### *async method* `approve(self)` {#GroupRequestEvent.approve}

同意请求。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

### *async method* `refuse(self, reason = '')` {#GroupRequestEvent.refuse}

拒绝请求。

- **Arguments**

  - **reason** (*str*) - 拒绝原因。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `MetaEvent`(self, adapter, **data) {#MetaEvent}

Bases: `alicebot.adapter.cqhttp.event.CQHTTPEvent`

元事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **post_type** (*Literal['meta_event']*)

  - **meta_event_type** (*str*)

## *class* `LifecycleMetaEvent`(self, adapter, **data) {#LifecycleMetaEvent}

Bases: `alicebot.adapter.cqhttp.event.MetaEvent`

生命周期

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **meta_event_type** (*Literal['lifecycle']*)

  - **sub_type** (*Literal['enable', 'disable', 'connect']*)

## *class* `HeartbeatMetaEvent`(self, adapter, **data) {#HeartbeatMetaEvent}

Bases: `alicebot.adapter.cqhttp.event.MetaEvent`

心跳

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **meta_event_type** (*Literal['heartbeat']*)

  - **status** (*alicebot.adapter.cqhttp.event.Status*)

  - **interval** (*int*)