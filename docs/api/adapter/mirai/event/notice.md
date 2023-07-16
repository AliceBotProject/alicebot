# alicebot.adapter.mirai.event.notice

通知事件。

## *class* `NoticeEvent`(self, adapter, **data) {#NoticeEvent}

Bases: `alicebot.adapter.mirai.event.base.MiraiEvent`

通知事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

## *class* `NudgeEvent`(self, adapter, **data) {#NudgeEvent}

Bases: `alicebot.adapter.mirai.event.notice.NoticeEvent`

戳一戳事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['NudgeEvent']*)

  - **fromId** (*int*)

  - **subject** (*alicebot.adapter.mirai.event.base.Subject*)

  - **action** (*str*)

  - **suffix** (*str*)

  - **target** (*int*)

## *class* `FriendEvent`(self, adapter, **data) {#FriendEvent}

Bases: `alicebot.adapter.mirai.event.notice.NoticeEvent`

好友事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **friend** (*alicebot.adapter.mirai.event.base.FriendInfo*)

## *class* `FriendInputStatusChangedEvent`(self, adapter, **data) {#FriendInputStatusChangedEvent}

Bases: `alicebot.adapter.mirai.event.notice.FriendEvent`

好友输入状态改变

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['FriendInputStatusChangedEvent']*)

  - **inputting** (*bool*)

## *class* `FriendRecallEvent`(self, adapter, **data) {#FriendRecallEvent}

Bases: `alicebot.adapter.mirai.event.notice.FriendEvent`

好友消息撤回

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['FriendRecallEvent']*)

  - **authorId** (*int*)

  - **messageId** (*int*)

  - **time** (*int*)

  - **operator** (*int*)

## *class* `GroupEvent`(self, adapter, **data) {#GroupEvent}

Bases: `alicebot.adapter.mirai.event.notice.NoticeEvent`

群事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

## *class* `GroupBotEvent`(self, adapter, **data) {#GroupBotEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupEvent`

与 Bot 相关的群事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

## *class* `BotGroupPermissionChangeEvent`(self, adapter, **data) {#BotGroupPermissionChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 在群里的权限被改变. 操作人一定是群主

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['BotGroupPermissionChangeEvent']*)

  - **origin** (*Literal['OWNER', 'ADMINISTRATOR', 'MEMBER']*)

  - **current** (*Literal['OWNER', 'ADMINISTRATOR', 'MEMBER']*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

## *class* `BotMuteEvent`(self, adapter, **data) {#BotMuteEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 被禁言

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['BotMuteEvent']*)

  - **operator** (*alicebot.adapter.mirai.event.base.GroupMemberInfo*)

## *class* `BotUnmuteEvent`(self, adapter, **data) {#BotUnmuteEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 被取消禁言

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['BotUnmuteEvent']*)

  - **operator** (*alicebot.adapter.mirai.event.base.GroupMemberInfo*)

## *class* `BotJoinGroupEvent`(self, adapter, **data) {#BotJoinGroupEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot加入了一个新群

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['BotJoinGroupEvent']*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

## *class* `BotLeaveEventActive`(self, adapter, **data) {#BotLeaveEventActive}

Bases: `alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 主动退出一个群

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['BotLeaveEventActive']*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

## *class* `BotLeaveEventKick`(self, adapter, **data) {#BotLeaveEventKick}

Bases: `alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 被踢出一个群

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['BotLeaveEventKick']*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

## *class* `BotLeaveEventDisband`(self, adapter, **data) {#BotLeaveEventDisband}

Bases: `alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 所在的群被解散

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['BotLeaveEventDisband']*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

## *class* `GroupNoticeEvent`(self, adapter, **data) {#GroupNoticeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupEvent`

其他群事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

## *class* `GroupRecallEvent`(self, adapter, **data) {#GroupRecallEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

群消息撤回

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['GroupRecallEvent']*)

  - **authorId** (*int*)

  - **messageId** (*int*)

  - **time** (*int*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

  - **operator** (*Optional[alicebot.adapter.mirai.event.base.GroupMemberInfo]*)

## *class* `GroupNameChangeEvent`(self, adapter, **data) {#GroupNameChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

某个群名改变

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['GroupNameChangeEvent']*)

  - **origin** (*str*)

  - **current** (*str*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

  - **operator** (*Optional[alicebot.adapter.mirai.event.base.GroupMemberInfo]*)

## *class* `GroupEntranceAnnouncementChangeEvent`(self, adapter, **data) {#GroupEntranceAnnouncementChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

某群入群公告改变

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['GroupEntranceAnnouncementChangeEvent']*)

  - **origin** (*str*)

  - **current** (*str*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

  - **operator** (*Optional[alicebot.adapter.mirai.event.base.GroupMemberInfo]*)

## *class* `GroupMuteAllEvent`(self, adapter, **data) {#GroupMuteAllEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

全员禁言

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['GroupMuteAllEvent']*)

  - **origin** (*bool*)

  - **current** (*bool*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

  - **operator** (*Optional[alicebot.adapter.mirai.event.base.GroupMemberInfo]*)

## *class* `GroupAllowAnonymousChatEvent`(self, adapter, **data) {#GroupAllowAnonymousChatEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

匿名聊天

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['GroupAllowAnonymousChatEvent']*)

  - **origin** (*bool*)

  - **current** (*bool*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

  - **operator** (*Optional[alicebot.adapter.mirai.event.base.GroupMemberInfo]*)

## *class* `GroupAllowConfessTalkEvent`(self, adapter, **data) {#GroupAllowConfessTalkEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

坦白说

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['GroupAllowAnonymousChatEvent']*)

  - **origin** (*bool*)

  - **current** (*bool*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

  - **isByBot** (*bool*)

## *class* `GroupAllowMemberInviteEvent`(self, adapter, **data) {#GroupAllowMemberInviteEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

允许群员邀请好友加群

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['GroupAllowMemberInviteEvent']*)

  - **origin** (*bool*)

  - **current** (*bool*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

  - **operator** (*Optional[alicebot.adapter.mirai.event.base.GroupMemberInfo]*)

## *class* `GroupMemberEvent`(self, adapter, **data) {#GroupMemberEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupEvent`

群成员相关事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **member** (*alicebot.adapter.mirai.event.base.GroupMemberInfo*)

## *class* `MemberJoinEvent`(self, adapter, **data) {#MemberJoinEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

新人入群的事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['MemberJoinEvent']*)

## *class* `MemberLeaveEventKick`(self, adapter, **data) {#MemberLeaveEventKick}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

成员被踢出群（该成员不是Bot）

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['MemberLeaveEventKick']*)

  - **operator** (*Optional[alicebot.adapter.mirai.event.base.GroupMemberInfo]*)

## *class* `MemberLeaveEventQuit`(self, adapter, **data) {#MemberLeaveEventQuit}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

成员主动离群（该成员不是Bot）

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['MemberLeaveEventQuit']*)

## *class* `MemberCardChangeEvent`(self, adapter, **data) {#MemberCardChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群名片改动

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['MemberCardChangeEvent']*)

  - **origin** (*str*)

  - **current** (*str*)

## *class* `MemberSpecialTitleChangeEvent`(self, adapter, **data) {#MemberSpecialTitleChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群头衔改动（只有群主有操作限权）

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['MemberSpecialTitleChangeEvent']*)

  - **origin** (*str*)

  - **current** (*str*)

## *class* `MemberPermissionChangeEvent`(self, adapter, **data) {#MemberPermissionChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

成员权限改变的事件（该成员不是Bot）

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['MemberPermissionChangeEvent']*)

  - **origin** (*Literal['OWNER', 'ADMINISTRATOR', 'MEMBER']*)

  - **current** (*Literal['OWNER', 'ADMINISTRATOR', 'MEMBER']*)

## *class* `MemberMuteEvent`(self, adapter, **data) {#MemberMuteEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群成员被禁言事件（该成员不是Bot）

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['MemberMuteEvent']*)

  - **durationSeconds** (*int*)

  - **operator** (*Optional[alicebot.adapter.mirai.event.base.GroupMemberInfo]*)

## *class* `MemberUnmuteEvent`(self, adapter, **data) {#MemberUnmuteEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群成员被取消禁言事件（该成员不是Bot）

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['MemberUnmuteEvent']*)

  - **operator** (*Optional[alicebot.adapter.mirai.event.base.GroupMemberInfo]*)

## *class* `MemberHonorChangeEvent`(self, adapter, **data) {#MemberHonorChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群员称号改变

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['MemberHonorChangeEvent']*)

  - **action** (*Literal['achieve', 'lose']*)

## *class* `OtherClientEvent`(self, adapter, **data) {#OtherClientEvent}

Bases: `alicebot.adapter.mirai.event.notice.NoticeEvent`

其他客户端事件

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **client** (*alicebot.adapter.mirai.event.base.OtherClientSender*)

## *class* `OtherClientOnlineEvent`(self, adapter, **data) {#OtherClientOnlineEvent}

Bases: `alicebot.adapter.mirai.event.notice.OtherClientEvent`

其他客户端上线

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['OtherClientOnlineEvent']*)

  - **kind** (*Optional[int]*)

## *class* `OtherClientOfflineEvent`(self, adapter, **data) {#OtherClientOfflineEvent}

Bases: `alicebot.adapter.mirai.event.notice.OtherClientEvent`

其他客户端下线

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Literal['OtherClientOfflineEvent']*)