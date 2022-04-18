# alicebot.adapter.mirai.event.notice

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