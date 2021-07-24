# alicebot.adapter.cqhttp.event

## CQHTTP 事件


## _class_ `CQHTTPEvent`

基类：[`alicebot.event.Event`](../../event.md#alicebot.event.Event)

CQHTTP 事件基类


### _property_ `to_me`


* **返回**

    当前事件的 user_id 是否等于 self_id。



* **返回类型**

    bool



## _class_ `MessageEvent`

基类：`alicebot.adapter.cqhttp.event.CQHTTPEvent`

消息事件


### `get_plain_text()`


* **返回**

    消息的纯文本内容。



* **返回类型**

    str



### _async_ `replay(msg)`

回复消息。


* **参数**

    **msg** – 回复消息的内容，同 `call_api()` 方法。



* **返回**

    API 请求响应。



## _class_ `PrivateMessageEvent`

基类：`alicebot.adapter.cqhttp.event.MessageEvent`

私聊消息


## _class_ `GroupMessageEvent`

基类：`alicebot.adapter.cqhttp.event.MessageEvent`

群消息


## _class_ `NoticeEvent`

基类：`alicebot.adapter.cqhttp.event.CQHTTPEvent`

通知事件


## _class_ `GroupUploadNoticeEvent`

基类：`alicebot.adapter.cqhttp.event.NoticeEvent`

群文件上传


## _class_ `GroupAdminNoticeEvent`

基类：`alicebot.adapter.cqhttp.event.NoticeEvent`

群管理员变动


## _class_ `GroupDecreaseNoticeEvent`

基类：`alicebot.adapter.cqhttp.event.NoticeEvent`

群成员减少


## _class_ `GroupIncreaseNoticeEvent`

基类：`alicebot.adapter.cqhttp.event.NoticeEvent`

群成员增加


## _class_ `GroupBanNoticeEvent`

基类：`alicebot.adapter.cqhttp.event.NoticeEvent`

群禁言


## _class_ `FriendAddNoticeEvent`

基类：`alicebot.adapter.cqhttp.event.NoticeEvent`

好友添加


## _class_ `GroupRecallNoticeEvent`

基类：`alicebot.adapter.cqhttp.event.NoticeEvent`

群消息撤回


## _class_ `FriendRecallNoticeEvent`

基类：`alicebot.adapter.cqhttp.event.NoticeEvent`

好友消息撤回


## _class_ `NotifyEvent`

基类：`alicebot.adapter.cqhttp.event.NoticeEvent`

提醒事件


## _class_ `PokeNotifyEvent`

基类：`alicebot.adapter.cqhttp.event.NotifyEvent`

戳一戳


## _class_ `GroupLuckyKingNotifyEvent`

基类：`alicebot.adapter.cqhttp.event.NotifyEvent`

群红包运气王


## _class_ `GroupHonorNotifyEvent`

基类：`alicebot.adapter.cqhttp.event.NotifyEvent`

群成员荣誉变更


## _class_ `RequestEvent`

基类：`alicebot.adapter.cqhttp.event.CQHTTPEvent`

请求事件


## _class_ `FriendRequestEvent`

基类：`alicebot.adapter.cqhttp.event.RequestEvent`

加好友请求


### _async_ `approve(remark='')`

同意请求。


* **参数**

    **remark** – (optional) 好友备注。



* **返回**

    API 请求响应。



### _async_ `refuse()`

拒绝请求。


* **返回**

    API 请求响应。



## _class_ `GroupRequestEvent`

基类：`alicebot.adapter.cqhttp.event.RequestEvent`

加群请求／邀请


### _async_ `approve()`

同意请求。


* **返回**

    API 请求响应。



### _async_ `refuse(reason='')`

拒绝请求。


* **参数**

    **reason** – (optional) 拒绝原因。



* **返回**

    API 请求响应。



## _class_ `MetaEvent`

基类：`alicebot.adapter.cqhttp.event.CQHTTPEvent`

元事件


## _class_ `LifecycleMetaEvent`

基类：`alicebot.adapter.cqhttp.event.MetaEvent`

生命周期


## _class_ `HeartbeatMetaEvent`

基类：`alicebot.adapter.cqhttp.event.MetaEvent`

心跳


## `get_event_class(post_type, event_type, sub_type=None)`

根据接收到的消息类型返回对应的事件类。
:param post_type: 请求类型。
:param event_type: 事件类型。
:param sub_type: (optional) 子类型。
:return: 返回事件类。
:rtype: Type[T_CQHTTPEvent]
