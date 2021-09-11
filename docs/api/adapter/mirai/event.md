# alicebot.adapter.mirai.event

## Mirai 事件


## _class_ `MiraiEvent`

基类：[`alicebot.event.Event`](../../event.md#alicebot.event.Event)

Mirai 事件基类


## _class_ `MateEvent`

基类：`alicebot.adapter.mirai.event.base.MiraiEvent`

默认不会被传播的特殊事件


## _class_ `BotEvent`

基类：`alicebot.adapter.mirai.event.mate.MateEvent`

Bot 自身事件


## _class_ `BotOnlineEvent`

基类：`alicebot.adapter.mirai.event.mate.BotEvent`

Bot 登录成功


## _class_ `BotOfflineEventActive`

基类：`alicebot.adapter.mirai.event.mate.BotEvent`

Bot 主动离线


## _class_ `BotOfflineEventForce`

基类：`alicebot.adapter.mirai.event.mate.BotEvent`

Bot 被挤下线


## _class_ `BotOfflineEventDropped`

基类：`alicebot.adapter.mirai.event.mate.BotEvent`

Bot 被服务器断开或因网络问题而掉线


## _class_ `BotReloginEvent`

基类：`alicebot.adapter.mirai.event.mate.BotEvent`

Bot 主动重新登录


## _class_ `CommandExecutedEvent`

基类：`alicebot.adapter.mirai.event.mate.MateEvent`

命令被执行


## _class_ `MessageEvent`

基类：`alicebot.adapter.mirai.event.base.MiraiEvent`

消息事件


### `get_plain_text()`


* **返回**

    消息的纯文本内容。



* **返回类型**

    str



### _async_ `reply(msg, quote=False)`

回复消息。


* **参数**

    
    * **msg** – 回复消息的内容，同 `call_api()` 方法。


    * **quote** – 引用消息，默认为 `False`。



* **返回**

    API 请求响应。



* **返回类型**

    Dict[str, Any]



## _class_ `FriendMessage`

基类：`alicebot.adapter.mirai.event.message.MessageEvent`

好友消息


## _class_ `GroupMessage`

基类：`alicebot.adapter.mirai.event.message.MessageEvent`

群消息


## _class_ `TempMessage`

基类：`alicebot.adapter.mirai.event.message.MessageEvent`

群临时消息


## _class_ `StrangerMessage`

基类：`alicebot.adapter.mirai.event.message.MessageEvent`

陌生人消息


## _class_ `OtherClientMessage`

基类：`alicebot.adapter.mirai.event.message.MessageEvent`

其他客户端消息


## _class_ `NoticeEvent`

基类：`alicebot.adapter.mirai.event.base.MiraiEvent`

通知事件


## _class_ `NudgeEvent`

基类：`alicebot.adapter.mirai.event.notice.NoticeEvent`

戳一戳事件


## _class_ `FriendEvent`

基类：`alicebot.adapter.mirai.event.notice.NoticeEvent`

好友事件


## _class_ `FriendInputStatusChangedEvent`

基类：`alicebot.adapter.mirai.event.notice.FriendEvent`

好友输入状态改变


## _class_ `FriendRecallEvent`

基类：`alicebot.adapter.mirai.event.notice.FriendEvent`

好友消息撤回


## _class_ `GroupEvent`

基类：`alicebot.adapter.mirai.event.notice.NoticeEvent`

群事件


## _class_ `GroupBotEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupEvent`

与 Bot 相关的群事件


## _class_ `BotGroupPermissionChangeEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 在群里的权限被改变. 操作人一定是群主


## _class_ `BotMuteEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 被禁言


## _class_ `BotUnmuteEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 被取消禁言


## _class_ `BotJoinGroupEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot加入了一个新群


## _class_ `BotLeaveEventActive`

基类：`alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 主动退出一个群


## _class_ `BotLeaveEventKick`

基类：`alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 被踢出一个群


## _class_ `GroupNoticeEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupEvent`

其他群事件


## _class_ `GroupRecallEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

群消息撤回


## _class_ `GroupNameChangeEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

某个群名改变


## _class_ `GroupEntranceAnnouncementChangeEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

某群入群公告改变


## _class_ `GroupMuteAllEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

全员禁言


## _class_ `GroupAllowAnonymousChatEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

匿名聊天


## _class_ `GroupAllowConfessTalkEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

坦白说


## _class_ `GroupAllowMemberInviteEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

允许群员邀请好友加群


## _class_ `GroupMemberEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupEvent`

群成员相关事件


## _class_ `MemberJoinEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupMemberEvent`

新人入群的事件


## _class_ `MemberLeaveEventKick`

基类：`alicebot.adapter.mirai.event.notice.GroupMemberEvent`

成员被踢出群（该成员不是Bot）


## _class_ `MemberLeaveEventQuit`

基类：`alicebot.adapter.mirai.event.notice.GroupMemberEvent`

成员主动离群（该成员不是Bot）


## _class_ `MemberCardChangeEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群名片改动


## _class_ `MemberSpecialTitleChangeEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群头衔改动（只有群主有操作限权）


## _class_ `MemberPermissionChangeEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupMemberEvent`

成员权限改变的事件（该成员不是Bot）


## _class_ `MemberMuteEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群成员被禁言事件（该成员不是Bot）


## _class_ `MemberUnmuteEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群成员被取消禁言事件（该成员不是Bot）


## _class_ `MemberHonorChangeEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群员称号改变


## _class_ `RequestEvent`

基类：`alicebot.adapter.mirai.event.base.MiraiEvent`

申请事件


### _async_ `approve(message='')`

同意请求。


* **参数**

    **message** – 回复的信息，默认为空。



* **返回**

    API 请求响应。



* **返回类型**

    Dict[str, Any]



### _async_ `refuse(message='')`

拒绝请求。


* **参数**

    **message** – 回复的信息，默认为空。



* **返回**

    API 请求响应。



* **返回类型**

    Dict[str, Any]



## _class_ `NewFriendRequestEvent`

基类：`alicebot.adapter.mirai.event.request.RequestEvent`

添加好友申请


### _async_ `refuse(message='', black_list=False)`

拒绝请求。


* **参数**

    
    * **message** – 回复的信息，默认为空。


    * **black_list** – 是否加入黑名单，默认为 `False`。



* **返回**

    API 请求响应。



* **返回类型**

    Dict[str, Any]



## _class_ `MemberJoinRequestEvent`

基类：`alicebot.adapter.mirai.event.request.RequestEvent`

用户入群申请（Bot需要有管理员权限）


### _async_ `refuse(message='', black_list=False)`

拒绝请求。


* **参数**

    
    * **message** – 回复的信息，默认为空。


    * **black_list** – 是否加入黑名单，默认为 `False`。



* **返回**

    API 请求响应。



* **返回类型**

    Dict[str, Any]



### _async_ `ignore(message='', black_list=False)`

忽略请求。


* **参数**

    
    * **message** – 回复的信息，默认为空。


    * **black_list** – 是否加入黑名单，默认为 `False`。



* **返回**

    API 请求响应。



* **返回类型**

    Dict[str, Any]



## _class_ `BotInvitedJoinGroupRequestEvent`

基类：`alicebot.adapter.mirai.event.request.RequestEvent`

Bot 被邀请入群申请


## `get_event_class(event_type)`

根据接收到的消息类型返回对应的事件类。


* **参数**

    **event_type** – 事件类型。



* **返回**

    对应的事件类。



* **返回类型**

    Type[T_MiraiEvent]


# alicebot.adapter.mirai.event.mate


## _class_ `MateEvent`

基类：`alicebot.adapter.mirai.event.base.MiraiEvent`

默认不会被传播的特殊事件


## _class_ `BotEvent`

基类：`alicebot.adapter.mirai.event.mate.MateEvent`

Bot 自身事件


## _class_ `BotOnlineEvent`

基类：`alicebot.adapter.mirai.event.mate.BotEvent`

Bot 登录成功


## _class_ `BotOfflineEventActive`

基类：`alicebot.adapter.mirai.event.mate.BotEvent`

Bot 主动离线


## _class_ `BotOfflineEventForce`

基类：`alicebot.adapter.mirai.event.mate.BotEvent`

Bot 被挤下线


## _class_ `BotOfflineEventDropped`

基类：`alicebot.adapter.mirai.event.mate.BotEvent`

Bot 被服务器断开或因网络问题而掉线


## _class_ `BotReloginEvent`

基类：`alicebot.adapter.mirai.event.mate.BotEvent`

Bot 主动重新登录


## _class_ `CommandExecutedEvent`

基类：`alicebot.adapter.mirai.event.mate.MateEvent`

命令被执行

# alicebot.adapter.mirai.event.base


## _class_ `MiraiEvent`

基类：[`alicebot.event.Event`](../../event.md#alicebot.event.Event)

Mirai 事件基类

# alicebot.adapter.mirai.event.request


## _class_ `RequestEvent`

基类：`alicebot.adapter.mirai.event.base.MiraiEvent`

申请事件


### _async_ `approve(message='')`

同意请求。


* **参数**

    **message** – 回复的信息，默认为空。



* **返回**

    API 请求响应。



* **返回类型**

    Dict[str, Any]



### _async_ `refuse(message='')`

拒绝请求。


* **参数**

    **message** – 回复的信息，默认为空。



* **返回**

    API 请求响应。



* **返回类型**

    Dict[str, Any]



## _class_ `NewFriendRequestEvent`

基类：`alicebot.adapter.mirai.event.request.RequestEvent`

添加好友申请


### _async_ `refuse(message='', black_list=False)`

拒绝请求。


* **参数**

    
    * **message** – 回复的信息，默认为空。


    * **black_list** – 是否加入黑名单，默认为 `False`。



* **返回**

    API 请求响应。



* **返回类型**

    Dict[str, Any]



## _class_ `MemberJoinRequestEvent`

基类：`alicebot.adapter.mirai.event.request.RequestEvent`

用户入群申请（Bot需要有管理员权限）


### _async_ `refuse(message='', black_list=False)`

拒绝请求。


* **参数**

    
    * **message** – 回复的信息，默认为空。


    * **black_list** – 是否加入黑名单，默认为 `False`。



* **返回**

    API 请求响应。



* **返回类型**

    Dict[str, Any]



### _async_ `ignore(message='', black_list=False)`

忽略请求。


* **参数**

    
    * **message** – 回复的信息，默认为空。


    * **black_list** – 是否加入黑名单，默认为 `False`。



* **返回**

    API 请求响应。



* **返回类型**

    Dict[str, Any]



## _class_ `BotInvitedJoinGroupRequestEvent`

基类：`alicebot.adapter.mirai.event.request.RequestEvent`

Bot 被邀请入群申请

# alicebot.adapter.mirai.event.message


## _class_ `MessageEvent`

基类：`alicebot.adapter.mirai.event.base.MiraiEvent`

消息事件


### `get_plain_text()`


* **返回**

    消息的纯文本内容。



* **返回类型**

    str



### _async_ `reply(msg, quote=False)`

回复消息。


* **参数**

    
    * **msg** – 回复消息的内容，同 `call_api()` 方法。


    * **quote** – 引用消息，默认为 `False`。



* **返回**

    API 请求响应。



* **返回类型**

    Dict[str, Any]



## _class_ `FriendMessage`

基类：`alicebot.adapter.mirai.event.message.MessageEvent`

好友消息


## _class_ `GroupMessage`

基类：`alicebot.adapter.mirai.event.message.MessageEvent`

群消息


## _class_ `TempMessage`

基类：`alicebot.adapter.mirai.event.message.MessageEvent`

群临时消息


## _class_ `StrangerMessage`

基类：`alicebot.adapter.mirai.event.message.MessageEvent`

陌生人消息


## _class_ `OtherClientMessage`

基类：`alicebot.adapter.mirai.event.message.MessageEvent`

其他客户端消息

# alicebot.adapter.mirai.event.notice


## _class_ `NoticeEvent`

基类：`alicebot.adapter.mirai.event.base.MiraiEvent`

通知事件


## _class_ `NudgeEvent`

基类：`alicebot.adapter.mirai.event.notice.NoticeEvent`

戳一戳事件


## _class_ `FriendEvent`

基类：`alicebot.adapter.mirai.event.notice.NoticeEvent`

好友事件


## _class_ `FriendInputStatusChangedEvent`

基类：`alicebot.adapter.mirai.event.notice.FriendEvent`

好友输入状态改变


## _class_ `FriendNickChangedEvent`

基类：`alicebot.adapter.mirai.event.notice.FriendEvent`


## _class_ `FriendRecallEvent`

基类：`alicebot.adapter.mirai.event.notice.FriendEvent`

好友消息撤回


## _class_ `GroupEvent`

基类：`alicebot.adapter.mirai.event.notice.NoticeEvent`

群事件


## _class_ `GroupBotEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupEvent`

与 Bot 相关的群事件


## _class_ `BotGroupPermissionChangeEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 在群里的权限被改变. 操作人一定是群主


## _class_ `BotMuteEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 被禁言


## _class_ `BotUnmuteEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 被取消禁言


## _class_ `BotJoinGroupEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot加入了一个新群


## _class_ `BotLeaveEventActive`

基类：`alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 主动退出一个群


## _class_ `BotLeaveEventKick`

基类：`alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 被踢出一个群


## _class_ `GroupNoticeEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupEvent`

其他群事件


## _class_ `GroupRecallEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

群消息撤回


## _class_ `GroupNameChangeEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

某个群名改变


## _class_ `GroupEntranceAnnouncementChangeEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

某群入群公告改变


## _class_ `GroupMuteAllEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

全员禁言


## _class_ `GroupAllowAnonymousChatEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

匿名聊天


## _class_ `GroupAllowConfessTalkEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

坦白说


## _class_ `GroupAllowMemberInviteEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

允许群员邀请好友加群


## _class_ `GroupMemberEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupEvent`

群成员相关事件


## _class_ `MemberJoinEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupMemberEvent`

新人入群的事件


## _class_ `MemberLeaveEventKick`

基类：`alicebot.adapter.mirai.event.notice.GroupMemberEvent`

成员被踢出群（该成员不是Bot）


## _class_ `MemberLeaveEventQuit`

基类：`alicebot.adapter.mirai.event.notice.GroupMemberEvent`

成员主动离群（该成员不是Bot）


## _class_ `MemberCardChangeEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群名片改动


## _class_ `MemberSpecialTitleChangeEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群头衔改动（只有群主有操作限权）


## _class_ `MemberPermissionChangeEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupMemberEvent`

成员权限改变的事件（该成员不是Bot）


## _class_ `MemberMuteEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群成员被禁言事件（该成员不是Bot）


## _class_ `MemberUnmuteEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群成员被取消禁言事件（该成员不是Bot）


## _class_ `MemberHonorChangeEvent`

基类：`alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群员称号改变
