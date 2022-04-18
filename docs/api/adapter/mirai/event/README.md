# alicebot.adapter.mirai.event

Mirai 适配器事件。

## *class* `MiraiEvent`(__pydantic_self__, **data) {#MiraiEvent}

Bases: `alicebot.event.Event`

Mirai 事件基类

- **Attributes**

  - **type** (*str*)

## *class* `MateEvent`(__pydantic_self__, **data) {#MateEvent}

Bases: `alicebot.adapter.mirai.event.base.MiraiEvent`

默认不会被传播的特殊事件

## *class* `BotEvent`(__pydantic_self__, **data) {#BotEvent}

Bases: `alicebot.adapter.mirai.event.mate.MateEvent`

Bot 自身事件

- **Attributes**

  - **qq** (*int*)

## *class* `BotOnlineEvent`(__pydantic_self__, **data) {#BotOnlineEvent}

Bases: `alicebot.adapter.mirai.event.mate.BotEvent`

Bot 登录成功

- **Attributes**

  - **type** (*Literal['BotOnlineEvent']*)

## *class* `BotOfflineEventActive`(__pydantic_self__, **data) {#BotOfflineEventActive}

Bases: `alicebot.adapter.mirai.event.mate.BotEvent`

Bot 主动离线

- **Attributes**

  - **type** (*Literal['BotOfflineEventActive']*)

## *class* `BotOfflineEventForce`(__pydantic_self__, **data) {#BotOfflineEventForce}

Bases: `alicebot.adapter.mirai.event.mate.BotEvent`

Bot 被挤下线

- **Attributes**

  - **type** (*Literal['BotOfflineEventForce']*)

## *class* `BotOfflineEventDropped`(__pydantic_self__, **data) {#BotOfflineEventDropped}

Bases: `alicebot.adapter.mirai.event.mate.BotEvent`

Bot 被服务器断开或因网络问题而掉线

- **Attributes**

  - **type** (*Literal['BotOfflineEventDropped']*)

## *class* `BotReloginEvent`(__pydantic_self__, **data) {#BotReloginEvent}

Bases: `alicebot.adapter.mirai.event.mate.BotEvent`

Bot 主动重新登录

- **Attributes**

  - **type** (*Literal['BotReloginEvent']*)

## *class* `CommandExecutedEvent`(__pydantic_self__, **data) {#CommandExecutedEvent}

Bases: `alicebot.adapter.mirai.event.mate.MateEvent`

命令被执行

- **Attributes**

  - **type** (*Literal['CommandExecutedEvent']*)

  - **name** (*str*)

  - **friend** (*Optional[alicebot.adapter.mirai.event.base.FriendInfo]*)

  - **member** (*Optional[alicebot.adapter.mirai.event.base.GroupMemberInfo]*)

  - **args** (*List[Any]*)

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

## *class* `NoticeEvent`(__pydantic_self__, **data) {#NoticeEvent}

Bases: `alicebot.adapter.mirai.event.base.MiraiEvent`

通知事件

## *class* `NudgeEvent`(__pydantic_self__, **data) {#NudgeEvent}

Bases: `alicebot.adapter.mirai.event.notice.NoticeEvent`

戳一戳事件

- **Attributes**

  - **type** (*Literal['NudgeEvent']*)

  - **fromId** (*int*)

  - **subject** (*alicebot.adapter.mirai.event.base.Subject*)

  - **action** (*str*)

  - **suffix** (*str*)

  - **target** (*int*)

## *class* `FriendEvent`(__pydantic_self__, **data) {#FriendEvent}

Bases: `alicebot.adapter.mirai.event.notice.NoticeEvent`

好友事件

- **Attributes**

  - **friend** (*alicebot.adapter.mirai.event.base.FriendInfo*)

## *class* `FriendInputStatusChangedEvent`(__pydantic_self__, **data) {#FriendInputStatusChangedEvent}

Bases: `alicebot.adapter.mirai.event.notice.FriendEvent`

好友输入状态改变

- **Attributes**

  - **type** (*Literal['FriendInputStatusChangedEvent']*)

  - **inputting** (*bool*)

## *class* `FriendNickChangedEvent`(__pydantic_self__, **data) {#FriendNickChangedEvent}

Bases: `alicebot.adapter.mirai.event.notice.FriendEvent`

- **Attributes**

  - **type** (*Literal['FriendNickChangedEvent']*)

  - **from** (*str*)

  - **to** (*str*)

## *class* `FriendRecallEvent`(__pydantic_self__, **data) {#FriendRecallEvent}

Bases: `alicebot.adapter.mirai.event.notice.FriendEvent`

好友消息撤回

- **Attributes**

  - **type** (*Literal['FriendRecallEvent']*)

  - **authorId** (*int*)

  - **messageId** (*int*)

  - **time** (*int*)

  - **operator** (*int*)

## *class* `GroupEvent`(__pydantic_self__, **data) {#GroupEvent}

Bases: `alicebot.adapter.mirai.event.notice.NoticeEvent`

群事件

## *class* `GroupBotEvent`(__pydantic_self__, **data) {#GroupBotEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupEvent`

与 Bot 相关的群事件

## *class* `BotGroupPermissionChangeEvent`(__pydantic_self__, **data) {#BotGroupPermissionChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 在群里的权限被改变. 操作人一定是群主

- **Attributes**

  - **type** (*Literal['BotGroupPermissionChangeEvent']*)

  - **origin** (*Literal['OWNER', 'ADMINISTRATOR', 'MEMBER']*)

  - **current** (*Literal['OWNER', 'ADMINISTRATOR', 'MEMBER']*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

## *class* `BotMuteEvent`(__pydantic_self__, **data) {#BotMuteEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 被禁言

- **Attributes**

  - **type** (*Literal['BotMuteEvent']*)

  - **operator** (*alicebot.adapter.mirai.event.base.GroupMemberInfo*)

## *class* `BotUnmuteEvent`(__pydantic_self__, **data) {#BotUnmuteEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 被取消禁言

- **Attributes**

  - **type** (*Literal['BotUnmuteEvent']*)

  - **operator** (*alicebot.adapter.mirai.event.base.GroupMemberInfo*)

## *class* `BotJoinGroupEvent`(__pydantic_self__, **data) {#BotJoinGroupEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot加入了一个新群

- **Attributes**

  - **type** (*Literal['BotJoinGroupEvent']*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

## *class* `BotLeaveEventActive`(__pydantic_self__, **data) {#BotLeaveEventActive}

Bases: `alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 主动退出一个群

- **Attributes**

  - **type** (*Literal['BotLeaveEventActive']*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

## *class* `BotLeaveEventKick`(__pydantic_self__, **data) {#BotLeaveEventKick}

Bases: `alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 被踢出一个群

- **Attributes**

  - **type** (*Literal['BotLeaveEventKick']*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

## *class* `GroupNoticeEvent`(__pydantic_self__, **data) {#GroupNoticeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupEvent`

其他群事件

## *class* `GroupRecallEvent`(__pydantic_self__, **data) {#GroupRecallEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

群消息撤回

- **Attributes**

  - **type** (*Literal['GroupRecallEvent']*)

  - **authorId** (*int*)

  - **messageId** (*int*)

  - **time** (*int*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

  - **operator** (*alicebot.adapter.mirai.event.base.GroupMemberInfo*)

## *class* `GroupNameChangeEvent`(__pydantic_self__, **data) {#GroupNameChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

某个群名改变

- **Attributes**

  - **type** (*Literal['GroupNameChangeEvent']*)

  - **origin** (*str*)

  - **current** (*str*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

  - **operator** (*alicebot.adapter.mirai.event.base.GroupMemberInfo*)

## *class* `GroupEntranceAnnouncementChangeEvent`(__pydantic_self__, **data) {#GroupEntranceAnnouncementChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

某群入群公告改变

- **Attributes**

  - **type** (*Literal['GroupEntranceAnnouncementChangeEvent']*)

  - **origin** (*str*)

  - **current** (*str*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

  - **operator** (*alicebot.adapter.mirai.event.base.GroupMemberInfo*)

## *class* `GroupMuteAllEvent`(__pydantic_self__, **data) {#GroupMuteAllEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

全员禁言

- **Attributes**

  - **type** (*Literal['GroupMuteAllEvent']*)

  - **origin** (*bool*)

  - **current** (*bool*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

  - **operator** (*alicebot.adapter.mirai.event.base.GroupMemberInfo*)

## *class* `GroupAllowAnonymousChatEvent`(__pydantic_self__, **data) {#GroupAllowAnonymousChatEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

匿名聊天

- **Attributes**

  - **type** (*Literal['GroupAllowAnonymousChatEvent']*)

  - **origin** (*bool*)

  - **current** (*bool*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

  - **operator** (*alicebot.adapter.mirai.event.base.GroupMemberInfo*)

## *class* `GroupAllowConfessTalkEvent`(__pydantic_self__, **data) {#GroupAllowConfessTalkEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

坦白说

- **Attributes**

  - **type** (*Literal['GroupAllowAnonymousChatEvent']*)

  - **origin** (*bool*)

  - **current** (*bool*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

  - **isByBot** (*bool*)

## *class* `GroupAllowMemberInviteEvent`(__pydantic_self__, **data) {#GroupAllowMemberInviteEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

允许群员邀请好友加群

- **Attributes**

  - **type** (*Literal['GroupAllowMemberInviteEvent']*)

  - **origin** (*bool*)

  - **current** (*bool*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

  - **operator** (*alicebot.adapter.mirai.event.base.GroupMemberInfo*)

## *class* `GroupMemberEvent`(__pydantic_self__, **data) {#GroupMemberEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupEvent`

群成员相关事件

- **Attributes**

  - **member** (*alicebot.adapter.mirai.event.base.GroupMemberInfo*)

## *class* `MemberJoinEvent`(__pydantic_self__, **data) {#MemberJoinEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

新人入群的事件

- **Attributes**

  - **type** (*Literal['MemberJoinEvent']*)

## *class* `MemberLeaveEventKick`(__pydantic_self__, **data) {#MemberLeaveEventKick}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

成员被踢出群（该成员不是Bot）

- **Attributes**

  - **type** (*Literal['MemberLeaveEventKick']*)

  - **operator** (*alicebot.adapter.mirai.event.base.GroupMemberInfo*)

## *class* `MemberLeaveEventQuit`(__pydantic_self__, **data) {#MemberLeaveEventQuit}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

成员主动离群（该成员不是Bot）

- **Attributes**

  - **type** (*Literal['MemberLeaveEventQuit']*)

## *class* `MemberCardChangeEvent`(__pydantic_self__, **data) {#MemberCardChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群名片改动

- **Attributes**

  - **type** (*Literal['MemberCardChangeEvent']*)

  - **origin** (*str*)

  - **current** (*str*)

## *class* `MemberSpecialTitleChangeEvent`(__pydantic_self__, **data) {#MemberSpecialTitleChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群头衔改动（只有群主有操作限权）

- **Attributes**

  - **type** (*Literal['MemberSpecialTitleChangeEvent']*)

  - **origin** (*str*)

  - **current** (*str*)

## *class* `MemberPermissionChangeEvent`(__pydantic_self__, **data) {#MemberPermissionChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

成员权限改变的事件（该成员不是Bot）

- **Attributes**

  - **type** (*Literal['MemberPermissionChangeEvent']*)

  - **origin** (*Literal['OWNER', 'ADMINISTRATOR', 'MEMBER']*)

  - **current** (*Literal['OWNER', 'ADMINISTRATOR', 'MEMBER']*)

## *class* `MemberMuteEvent`(__pydantic_self__, **data) {#MemberMuteEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群成员被禁言事件（该成员不是Bot）

- **Attributes**

  - **type** (*Literal['MemberMuteEvent']*)

  - **durationSeconds** (*int*)

  - **operator** (*alicebot.adapter.mirai.event.base.GroupMemberInfo*)

## *class* `MemberUnmuteEvent`(__pydantic_self__, **data) {#MemberUnmuteEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群成员被取消禁言事件（该成员不是Bot）

- **Attributes**

  - **type** (*Literal['MemberUnmuteEvent']*)

  - **operator** (*alicebot.adapter.mirai.event.base.GroupMemberInfo*)

## *class* `MemberHonorChangeEvent`(__pydantic_self__, **data) {#MemberHonorChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群员称号改变

- **Attributes**

  - **type** (*Literal['MemberHonorChangeEvent']*)

  - **action** (*Literal['achieve', 'lose']*)

## *class* `RequestEvent`(__pydantic_self__, **data) {#RequestEvent}

Bases: `alicebot.adapter.mirai.event.base.MiraiEvent`

申请事件

### *async method* `approve(self, message = '')` {#RequestEvent.approve}

同意请求。

- **Arguments**

  - **message** (*str*) - 回复的信息，默认为空。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

### *async method* `refuse(self, message = '')` {#RequestEvent.refuse}

拒绝请求。

- **Arguments**

  - **message** (*str*) - 回复的信息，默认为空。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `NewFriendRequestEvent`(__pydantic_self__, **data) {#NewFriendRequestEvent}

Bases: `alicebot.adapter.mirai.event.request.RequestEvent`

添加好友申请

- **Attributes**

  - **type** (*Literal['NewFriendRequestEvent']*)

  - **eventId** (*int*)

  - **fromId** (*int*)

  - **groupId** (*int*)

  - **nick** (*str*)

  - **message** (*str*)

### *async method* `approve(self, message = '')` {#NewFriendRequestEvent.approve}

同意请求。

- **Arguments**

  - **message** (*str*) - 回复的信息，默认为空。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

### *async method* `refuse(self, message = '', black_list = False)` {#NewFriendRequestEvent.refuse}

拒绝请求。

- **Arguments**

  - **message** (*str*) - 回复的信息，默认为空。

  - **black_list** (*bool*) - 是否加入黑名单，默认为 `False`。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `MemberJoinRequestEvent`(__pydantic_self__, **data) {#MemberJoinRequestEvent}

Bases: `alicebot.adapter.mirai.event.request.RequestEvent`

用户入群申请（Bot需要有管理员权限）

- **Attributes**

  - **type** (*Literal['MemberJoinRequestEvent']*)

  - **eventId** (*int*)

  - **fromId** (*int*)

  - **groupId** (*int*)

  - **groupName** (*str*)

  - **nick** (*str*)

  - **message** (*str*)

### *async method* `approve(self, message = '')` {#MemberJoinRequestEvent.approve}

同意请求。

- **Arguments**

  - **message** (*str*) - 回复的信息，默认为空。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

### *async method* `ignore(self, message = '', black_list = False)` {#MemberJoinRequestEvent.ignore}

忽略请求。

- **Arguments**

  - **message** (*str*) - 回复的信息，默认为空。

  - **black_list** (*bool*) - 是否加入黑名单，默认为 `False`。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

### *async method* `refuse(self, message = '', black_list = False)` {#MemberJoinRequestEvent.refuse}

拒绝请求。

- **Arguments**

  - **message** (*str*) - 回复的信息，默认为空。

  - **black_list** (*bool*) - 是否加入黑名单，默认为 `False`。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *class* `BotInvitedJoinGroupRequestEvent`(__pydantic_self__, **data) {#BotInvitedJoinGroupRequestEvent}

Bases: `alicebot.adapter.mirai.event.request.RequestEvent`

Bot 被邀请入群申请

- **Attributes**

  - **type** (*Literal['BotInvitedJoinGroupRequestEvent']*)

  - **eventId** (*int*)

  - **fromId** (*int*)

  - **groupId** (*int*)

  - **groupName** (*str*)

  - **nick** (*str*)

  - **message** (*str*)

### *async method* `approve(self, message = '')` {#BotInvitedJoinGroupRequestEvent.approve}

同意请求。

- **Arguments**

  - **message** (*str*) - 回复的信息，默认为空。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

### *async method* `refuse(self, message = '')` {#BotInvitedJoinGroupRequestEvent.refuse}

拒绝请求。

- **Arguments**

  - **message** (*str*) - 回复的信息，默认为空。

- **Returns**

  Type: *Dict[str, Any]*

  API 请求响应。

## *function* `get_event_class(event_type)` {#get_event_class}

根据接收到的消息类型返回对应的事件类。

- **Arguments**

  - **event_type** (*str*) - 事件类型。

- **Returns**

  Type: *Type[~T_MiraiEvent]*

  对应的事件类。