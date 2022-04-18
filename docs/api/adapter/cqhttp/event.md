# alicebot.adapter.cqhttp.event

CQHTTP 适配器事件。

## *class* `Sender`(__pydantic_self__, **data) {#Sender}

Bases: `pydantic.main.BaseModel`

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

- **Attributes**

  - **id** (*int*)

  - **name** (*str*)

  - **flag** (*str*)

## *class* `File`(__pydantic_self__, **data) {#File}

Bases: `pydantic.main.BaseModel`

- **Attributes**

  - **id** (*str*)

  - **name** (*str*)

  - **size** (*int*)

  - **busid** (*int*)

## *class* `Status`(__pydantic_self__, **data) {#Status}

Bases: `pydantic.main.BaseModel`

- **Attributes**

  - **online** (*bool*)

  - **good** (*bool*)

### *class* `Config`(self, /, *args, **kwargs) {#Status.Config}

Bases: `object`

## *class* `CQHTTPEvent`(__pydantic_self__, **data) {#CQHTTPEvent}

Bases: `alicebot.event.Event`

CQHTTP 事件基类

- **Attributes**

  - **type** (*Optional[str]*)

  - **time** (*int*)

  - **self_id** (*int*)

  - **post_type** (*Literal['message', 'notice', 'request', 'meta_event']*)

### *readonly property* `to_me` {#CQHTTPEvent.to_me}

Type: *bool*

当前事件的 user_id 是否等于 self_id。

## *class* `MessageEvent`(__pydantic_self__, **data) {#MessageEvent}

Bases: `alicebot.adapter.cqhttp.event.CQHTTPEvent`

消息事件

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

### *async method* `reply(self, msg)` {#MessageEvent.reply}

回复消息。

- **Arguments**

  - **msg** (*Union[str, Mapping, Iterable[Mapping], CQHTTPMessageSegment, CQHTTPMessage]*) - 回复消息的内容，同 `call_api()` 方法。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `PrivateMessageEvent`(__pydantic_self__, **data) {#PrivateMessageEvent}

Bases: `alicebot.adapter.cqhttp.event.MessageEvent`

私聊消息

- **Attributes**

  - **message_type** (*Literal['private']*)

  - **sub_type** (*Literal['friend', 'group', 'other']*)

### *async method* `reply(self, msg)` {#PrivateMessageEvent.reply}

回复消息。

- **Arguments**

  - **msg** (*Union[str, Mapping, Iterable[Mapping], CQHTTPMessageSegment, CQHTTPMessage]*) - 回复消息的内容，同 `call_api()` 方法。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `GroupMessageEvent`(__pydantic_self__, **data) {#GroupMessageEvent}

Bases: `alicebot.adapter.cqhttp.event.MessageEvent`

群消息

- **Attributes**

  - **message_type** (*Literal['group']*)

  - **sub_type** (*Literal['normal', 'anonymous', 'notice']*)

  - **group_id** (*int*)

  - **anonymous** (*Optional[alicebot.adapter.cqhttp.event.Anonymous]*)

### *async method* `reply(self, msg)` {#GroupMessageEvent.reply}

回复消息。

- **Arguments**

  - **msg** (*Union[str, Mapping, Iterable[Mapping], CQHTTPMessageSegment, CQHTTPMessage]*) - 回复消息的内容，同 `call_api()` 方法。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `NoticeEvent`(__pydantic_self__, **data) {#NoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.CQHTTPEvent`

通知事件

- **Attributes**

  - **post_type** (*Literal['notice']*)

  - **notice_type** (*str*)

## *class* `GroupUploadNoticeEvent`(__pydantic_self__, **data) {#GroupUploadNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

群文件上传

- **Attributes**

  - **notice_type** (*Literal['group_upload']*)

  - **user_id** (*int*)

  - **group_id** (*int*)

  - **file** (*alicebot.adapter.cqhttp.event.File*)

## *class* `GroupAdminNoticeEvent`(__pydantic_self__, **data) {#GroupAdminNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

群管理员变动

- **Attributes**

  - **notice_type** (*Literal['group_admin']*)

  - **sub_type** (*Literal['set', 'unset']*)

  - **user_id** (*int*)

  - **group_id** (*int*)

## *class* `GroupDecreaseNoticeEvent`(__pydantic_self__, **data) {#GroupDecreaseNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

群成员减少

- **Attributes**

  - **notice_type** (*Literal['group_decrease']*)

  - **sub_type** (*Literal['leave', 'kick', 'kick_me']*)

  - **group_id** (*int*)

  - **operator_id** (*int*)

  - **user_id** (*int*)

## *class* `GroupIncreaseNoticeEvent`(__pydantic_self__, **data) {#GroupIncreaseNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

群成员增加

- **Attributes**

  - **notice_type** (*Literal['group_increase']*)

  - **sub_type** (*Literal['approve', 'invite']*)

  - **group_id** (*int*)

  - **operator_id** (*int*)

  - **user_id** (*int*)

## *class* `GroupBanNoticeEvent`(__pydantic_self__, **data) {#GroupBanNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

群禁言

- **Attributes**

  - **notice_type** (*Literal['group_ban']*)

  - **sub_type** (*Literal['ban', 'lift_ban']*)

  - **group_id** (*int*)

  - **operator_id** (*int*)

  - **user_id** (*int*)

  - **duration** (*int*)

## *class* `FriendAddNoticeEvent`(__pydantic_self__, **data) {#FriendAddNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

好友添加

- **Attributes**

  - **notice_type** (*Literal['friend_add']*)

  - **user_id** (*int*)

## *class* `GroupRecallNoticeEvent`(__pydantic_self__, **data) {#GroupRecallNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

群消息撤回

- **Attributes**

  - **notice_type** (*Literal['group_recall']*)

  - **group_id** (*int*)

  - **operator_id** (*int*)

  - **user_id** (*int*)

  - **message_id** (*int*)

## *class* `FriendRecallNoticeEvent`(__pydantic_self__, **data) {#FriendRecallNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

好友消息撤回

- **Attributes**

  - **notice_type** (*Literal['friend_recall']*)

  - **user_id** (*int*)

  - **message_id** (*int*)

## *class* `NotifyEvent`(__pydantic_self__, **data) {#NotifyEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

提醒事件

- **Attributes**

  - **notice_type** (*Literal['notify']*)

  - **sub_type** (*str*)

  - **group_id** (*int*)

  - **user_id** (*int*)

## *class* `PokeNotifyEvent`(__pydantic_self__, **data) {#PokeNotifyEvent}

Bases: `alicebot.adapter.cqhttp.event.NotifyEvent`

戳一戳

- **Attributes**

  - **sub_type** (*Literal['poke']*)

  - **target_id** (*int*)

  - **group_id** (*Optional[int]*)

## *class* `GroupLuckyKingNotifyEvent`(__pydantic_self__, **data) {#GroupLuckyKingNotifyEvent}

Bases: `alicebot.adapter.cqhttp.event.NotifyEvent`

群红包运气王

- **Attributes**

  - **sub_type** (*Literal['lucky_king']*)

  - **target_id** (*int*)

## *class* `GroupHonorNotifyEvent`(__pydantic_self__, **data) {#GroupHonorNotifyEvent}

Bases: `alicebot.adapter.cqhttp.event.NotifyEvent`

群成员荣誉变更

- **Attributes**

  - **sub_type** (*Literal['honor']*)

  - **honor_type** (*Literal['talkative', 'performer', 'emotion']*)

## *class* `RequestEvent`(__pydantic_self__, **data) {#RequestEvent}

Bases: `alicebot.adapter.cqhttp.event.CQHTTPEvent`

请求事件

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

## *class* `FriendRequestEvent`(__pydantic_self__, **data) {#FriendRequestEvent}

Bases: `alicebot.adapter.cqhttp.event.RequestEvent`

加好友请求

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

## *class* `GroupRequestEvent`(__pydantic_self__, **data) {#GroupRequestEvent}

Bases: `alicebot.adapter.cqhttp.event.RequestEvent`

加群请求／邀请

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

## *class* `MetaEvent`(__pydantic_self__, **data) {#MetaEvent}

Bases: `alicebot.adapter.cqhttp.event.CQHTTPEvent`

元事件

- **Attributes**

  - **post_type** (*Literal['meta_event']*)

  - **meta_event_type** (*str*)

## *class* `LifecycleMetaEvent`(__pydantic_self__, **data) {#LifecycleMetaEvent}

Bases: `alicebot.adapter.cqhttp.event.MetaEvent`

生命周期

- **Attributes**

  - **meta_event_type** (*Literal['lifecycle']*)

  - **sub_type** (*Literal['enable', 'disable', 'connect']*)

## *class* `HeartbeatMetaEvent`(__pydantic_self__, **data) {#HeartbeatMetaEvent}

Bases: `alicebot.adapter.cqhttp.event.MetaEvent`

心跳

- **Attributes**

  - **meta_event_type** (*Literal['heartbeat']*)

  - **status** (*alicebot.adapter.cqhttp.event.Status*)

  - **interval** (*int*)

## *function* `get_event_class(post_type, event_type, sub_type = None)` {#get_event_class}

根据接收到的消息类型返回对应的事件类。

- **Arguments**

  - **post_type** (*str*) - 请求类型。

  - **event_type** (*str*) - 事件类型。

  - **sub_type** (*Optional[str]*) - 子类型。

- **Returns**

  Type: *Type[~T_CQHTTPEvent]*

  对应的事件类。