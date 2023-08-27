# alicebot.adapter.cqhttp.event

CQHTTP 适配器事件。

## _class_ `Sender` {#Sender}

Bases: `pydantic.main.BaseModel`

发送人信息

- **Attributes**

  - **user\_id** (_Optional\[int\]_)

  - **nickname** (_Optional\[str\]_)

  - **card** (_Optional\[str\]_)

  - **sex** (_Optional\[Literal\['male', 'female', 'unknown'\]\]_)

  - **age** (_Optional\[int\]_)

  - **area** (_Optional\[str\]_)

  - **level** (_Optional\[str\]_)

  - **role** (_Optional\[str\]_)

  - **title** (_Optional\[str\]_)

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

## _class_ `Anonymous` {#Anonymous}

Bases: `pydantic.main.BaseModel`

匿名信息

- **Attributes**

  - **id** (_int_)

  - **name** (_str_)

  - **flag** (_str_)

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

## _class_ `File` {#File}

Bases: `pydantic.main.BaseModel`

文件信息

- **Attributes**

  - **id** (_str_)

  - **name** (_str_)

  - **size** (_int_)

  - **busid** (_int_)

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

## _class_ `Status` {#Status}

Bases: `pydantic.main.BaseModel`

状态信息

- **Attributes**

  - **online** (_bool_)

  - **good** (_bool_)

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

## _class_ `CQHTTPEvent` {#CQHTTPEvent}

Bases: `alicebot.event.Event[CQHTTPAdapter]`

CQHTTP 事件基类

- **Attributes**

  - **type** (_Optional\[str\]_)

  - **time** (_int_)

  - **self\_id** (_int_)

  - **post\_type** (_str_)

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

### _method_ `get_event_type()` {#CQHTTPEvent.get\_event\_type}

获取事件类型。

- **Returns**

  Type: _Tuple\[Optional\[str\], Optional\[str\], Optional\[str\]\]_

  事件类型。

### _readonly property_ `to_me` {#CQHTTPEvent.to\_me}

Type: _bool_

当前事件的 `user_id` 是否等于 `self_id`。

## _class_ `MessageEvent` {#MessageEvent}

Bases: `alicebot.adapter.cqhttp.event.CQHTTPEvent`, `alicebot.event.MessageEvent[CQHTTPAdapter]`

消息事件

- **Attributes**

  - **post\_type** (_Literal\['message'\]_)

  - **message\_type** (_Literal\['private', 'group'\]_)

  - **sub\_type** (_str_)

  - **message\_id** (_int_)

  - **user\_id** (_int_)

  - **message** (_alicebot.adapter.cqhttp.message.CQHTTPMessage_)

  - **raw\_message** (_str_)

  - **font** (_int_)

  - **sender** (_Sender_)

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

### _async method_ `reply(self, message)` {#MessageEvent.reply}

回复消息。

- **Arguments**

  - **message** (_Union\[List\[alicebot.adapter.cqhttp.message.CQHTTPMessageSegment\], alicebot.adapter.cqhttp.message.CQHTTPMessageSegment, str, Mapping\[str, Any\]\]_) - 回复消息的内容，同 `call_api()` 方法。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。

## _class_ `PrivateMessageEvent` {#PrivateMessageEvent}

Bases: `alicebot.adapter.cqhttp.event.MessageEvent`

私聊消息

- **Attributes**

  - **message\_type** (_Literal\['private'\]_)

  - **sub\_type** (_Literal\['friend', 'group', 'other'\]_)

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

### _async method_ `reply(self, message)` {#PrivateMessageEvent.reply}

回复消息。

- **Arguments**

  - **message** (_Union\[List\[alicebot.adapter.cqhttp.message.CQHTTPMessageSegment\], alicebot.adapter.cqhttp.message.CQHTTPMessageSegment, str, Mapping\[str, Any\]\]_) - 回复消息的内容，同 `call_api()` 方法。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。

## _class_ `GroupMessageEvent` {#GroupMessageEvent}

Bases: `alicebot.adapter.cqhttp.event.MessageEvent`

群消息

- **Attributes**

  - **message\_type** (_Literal\['group'\]_)

  - **sub\_type** (_Literal\['normal', 'anonymous', 'notice'\]_)

  - **group\_id** (_int_)

  - **anonymous** (_Optional\[alicebot.adapter.cqhttp.event.Anonymous\]_)

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

### _async method_ `reply(self, message)` {#GroupMessageEvent.reply}

回复消息。

- **Arguments**

  - **message** (_Union\[List\[alicebot.adapter.cqhttp.message.CQHTTPMessageSegment\], alicebot.adapter.cqhttp.message.CQHTTPMessageSegment, str, Mapping\[str, Any\]\]_) - 回复消息的内容，同 `call_api()` 方法。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。

## _class_ `NoticeEvent` {#NoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.CQHTTPEvent`

通知事件

- **Attributes**

  - **post\_type** (_Literal\['notice'\]_)

  - **notice\_type** (_str_)

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

## _class_ `GroupUploadNoticeEvent` {#GroupUploadNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

群文件上传

- **Attributes**

  - **notice\_type** (_Literal\['group\_upload'\]_)

  - **user\_id** (_int_)

  - **group\_id** (_int_)

  - **file** (_File_)

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

## _class_ `GroupAdminNoticeEvent` {#GroupAdminNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

群管理员变动

- **Attributes**

  - **notice\_type** (_Literal\['group\_admin'\]_)

  - **sub\_type** (_Literal\['set', 'unset'\]_)

  - **user\_id** (_int_)

  - **group\_id** (_int_)

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

## _class_ `GroupDecreaseNoticeEvent` {#GroupDecreaseNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

群成员减少

- **Attributes**

  - **notice\_type** (_Literal\['group\_decrease'\]_)

  - **sub\_type** (_Literal\['leave', 'kick', 'kick\_me'\]_)

  - **group\_id** (_int_)

  - **operator\_id** (_int_)

  - **user\_id** (_int_)

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

## _class_ `GroupIncreaseNoticeEvent` {#GroupIncreaseNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

群成员增加

- **Attributes**

  - **notice\_type** (_Literal\['group\_increase'\]_)

  - **sub\_type** (_Literal\['approve', 'invite'\]_)

  - **group\_id** (_int_)

  - **operator\_id** (_int_)

  - **user\_id** (_int_)

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

## _class_ `GroupBanNoticeEvent` {#GroupBanNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

群禁言

- **Attributes**

  - **notice\_type** (_Literal\['group\_ban'\]_)

  - **sub\_type** (_Literal\['ban', 'lift\_ban'\]_)

  - **group\_id** (_int_)

  - **operator\_id** (_int_)

  - **user\_id** (_int_)

  - **duration** (_int_)

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

## _class_ `FriendAddNoticeEvent` {#FriendAddNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

好友添加

- **Attributes**

  - **notice\_type** (_Literal\['friend\_add'\]_)

  - **user\_id** (_int_)

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

## _class_ `GroupRecallNoticeEvent` {#GroupRecallNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

群消息撤回

- **Attributes**

  - **notice\_type** (_Literal\['group\_recall'\]_)

  - **group\_id** (_int_)

  - **operator\_id** (_int_)

  - **user\_id** (_int_)

  - **message\_id** (_int_)

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

## _class_ `FriendRecallNoticeEvent` {#FriendRecallNoticeEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

好友消息撤回

- **Attributes**

  - **notice\_type** (_Literal\['friend\_recall'\]_)

  - **user\_id** (_int_)

  - **message\_id** (_int_)

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

## _class_ `NotifyEvent` {#NotifyEvent}

Bases: `alicebot.adapter.cqhttp.event.NoticeEvent`

提醒事件

- **Attributes**

  - **notice\_type** (_Literal\['notify'\]_)

  - **sub\_type** (_str_)

  - **group\_id** (_Optional\[int\]_)

  - **user\_id** (_int_)

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

## _class_ `PokeNotifyEvent` {#PokeNotifyEvent}

Bases: `alicebot.adapter.cqhttp.event.NotifyEvent`

戳一戳

- **Attributes**

  - **sub\_type** (_Literal\['poke'\]_)

  - **target\_id** (_int_)

  - **group\_id** (_Optional\[int\]_)

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

## _class_ `GroupLuckyKingNotifyEvent` {#GroupLuckyKingNotifyEvent}

Bases: `alicebot.adapter.cqhttp.event.NotifyEvent`

群红包运气王

- **Attributes**

  - **sub\_type** (_Literal\['lucky\_king'\]_)

  - **group\_id** (_int_)

  - **target\_id** (_int_)

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

## _class_ `GroupHonorNotifyEvent` {#GroupHonorNotifyEvent}

Bases: `alicebot.adapter.cqhttp.event.NotifyEvent`

群成员荣誉变更

- **Attributes**

  - **sub\_type** (_Literal\['honor'\]_)

  - **group\_id** (_int_)

  - **honor\_type** (_Literal\['talkative', 'performer', 'emotion'\]_)

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

## _class_ `RequestEvent` {#RequestEvent}

Bases: `alicebot.adapter.cqhttp.event.CQHTTPEvent`

请求事件

- **Attributes**

  - **post\_type** (_Literal\['request'\]_)

  - **request\_type** (_str_)

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

### _async method_ `approve(self)` {#RequestEvent.approve}

同意请求。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。

### _async method_ `refuse(self)` {#RequestEvent.refuse}

拒绝请求。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。

## _class_ `FriendRequestEvent` {#FriendRequestEvent}

Bases: `alicebot.adapter.cqhttp.event.RequestEvent`

加好友请求

- **Attributes**

  - **request\_type** (_Literal\['friend'\]_)

  - **user\_id** (_int_)

  - **comment** (_str_)

  - **flag** (_str_)

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

### _async method_ `approve(self, remark = '')` {#FriendRequestEvent.approve}

同意请求。

- **Arguments**

  - **remark** (_str_) - 好友备注。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。

### _async method_ `refuse(self)` {#FriendRequestEvent.refuse}

拒绝请求。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。

## _class_ `GroupRequestEvent` {#GroupRequestEvent}

Bases: `alicebot.adapter.cqhttp.event.RequestEvent`

加群请求 / 邀请

- **Attributes**

  - **request\_type** (_Literal\['group'\]_)

  - **sub\_type** (_Literal\['add', 'invite'\]_)

  - **group\_id** (_int_)

  - **user\_id** (_int_)

  - **comment** (_str_)

  - **flag** (_str_)

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

### _async method_ `approve(self)` {#GroupRequestEvent.approve}

同意请求。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。

### _async method_ `refuse(self, reason = '')` {#GroupRequestEvent.refuse}

拒绝请求。

- **Arguments**

  - **reason** (_str_) - 拒绝原因。

- **Returns**

  Type: _Dict\[str, Any\]_

  API 请求响应。

## _class_ `MetaEvent` {#MetaEvent}

Bases: `alicebot.adapter.cqhttp.event.CQHTTPEvent`

元事件

- **Attributes**

  - **post\_type** (_Literal\['meta\_event'\]_)

  - **meta\_event\_type** (_str_)

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

## _class_ `LifecycleMetaEvent` {#LifecycleMetaEvent}

Bases: `alicebot.adapter.cqhttp.event.MetaEvent`

生命周期

- **Attributes**

  - **meta\_event\_type** (_Literal\['lifecycle'\]_)

  - **sub\_type** (_Literal\['enable', 'disable', 'connect'\]_)

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

## _class_ `HeartbeatMetaEvent` {#HeartbeatMetaEvent}

Bases: `alicebot.adapter.cqhttp.event.MetaEvent`

心跳

- **Attributes**

  - **meta\_event\_type** (_Literal\['heartbeat'\]_)

  - **status** (_Status_)

  - **interval** (_int_)

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
