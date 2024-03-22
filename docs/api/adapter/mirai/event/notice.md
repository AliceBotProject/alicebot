# alicebot.adapter.mirai.event.notice

通知事件。

## _class_ `NoticeEvent` {#NoticeEvent}

Bases: `alicebot.adapter.mirai.event.base.MiraiEvent`

通知事件

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `NudgeEvent` {#NudgeEvent}

Bases: `alicebot.adapter.mirai.event.notice.NoticeEvent`

戳一戳事件

- **Attributes**

  - **type** (_Literal\['NudgeEvent'\]_)

  - **fromId** (_int_)

  - **subject** (_alicebot.adapter.mirai.event.base.Subject_)

  - **action** (_str_)

  - **suffix** (_str_)

  - **target** (_int_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `FriendEvent` {#FriendEvent}

Bases: `alicebot.adapter.mirai.event.notice.NoticeEvent`

好友事件

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `FriendInputStatusChangedEvent` {#FriendInputStatusChangedEvent}

Bases: `alicebot.adapter.mirai.event.notice.FriendEvent`

好友输入状态改变

- **Attributes**

  - **type** (_Literal\['FriendInputStatusChangedEvent'\]_)

  - **friend** (_alicebot.adapter.mirai.event.base.FriendInfo_)

  - **inputting** (_bool_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `FriendNickChangedEvent` {#FriendNickChangedEvent}

Bases: `alicebot.adapter.mirai.event.notice.FriendEvent`

好友事件

- **Attributes**

  - **type** (_Literal\['FriendNickChangedEvent'\]_)

  - **friend** (_alicebot.adapter.mirai.event.base.FriendInfo_)

  - **from** (_str_)

  - **to** (_str_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `FriendRecallEvent` {#FriendRecallEvent}

Bases: `alicebot.adapter.mirai.event.notice.FriendEvent`

好友消息撤回

- **Attributes**

  - **type** (_Literal\['FriendRecallEvent'\]_)

  - **authorId** (_int_)

  - **messageId** (_int_)

  - **time** (_int_)

  - **operator** (_int_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `GroupEvent` {#GroupEvent}

Bases: `alicebot.adapter.mirai.event.notice.NoticeEvent`

群事件

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `GroupBotEvent` {#GroupBotEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupEvent`

与 Bot 相关的群事件

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `BotGroupPermissionChangeEvent` {#BotGroupPermissionChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 在群里的权限被改变. 操作人一定是群主

- **Attributes**

  - **type** (_Literal\['BotGroupPermissionChangeEvent'\]_)

  - **origin** (_Literal\['OWNER', 'ADMINISTRATOR', 'MEMBER'\]_)

  - **current** (_Literal\['OWNER', 'ADMINISTRATOR', 'MEMBER'\]_)

  - **group** (_alicebot.adapter.mirai.event.base.GroupInfo_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `BotMuteEvent` {#BotMuteEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 被禁言

- **Attributes**

  - **type** (_Literal\['BotMuteEvent'\]_)

  - **operator** (_alicebot.adapter.mirai.event.base.GroupMemberInfo_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `BotUnmuteEvent` {#BotUnmuteEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 被取消禁言

- **Attributes**

  - **type** (_Literal\['BotUnmuteEvent'\]_)

  - **operator** (_alicebot.adapter.mirai.event.base.GroupMemberInfo_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `BotJoinGroupEvent` {#BotJoinGroupEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot加入了一个新群

- **Attributes**

  - **type** (_Literal\['BotJoinGroupEvent'\]_)

  - **group** (_alicebot.adapter.mirai.event.base.GroupInfo_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `BotLeaveEventActive` {#BotLeaveEventActive}

Bases: `alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 主动退出一个群

- **Attributes**

  - **type** (_Literal\['BotLeaveEventActive'\]_)

  - **group** (_alicebot.adapter.mirai.event.base.GroupInfo_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `BotLeaveEventKick` {#BotLeaveEventKick}

Bases: `alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 被踢出一个群

- **Attributes**

  - **type** (_Literal\['BotLeaveEventKick'\]_)

  - **group** (_alicebot.adapter.mirai.event.base.GroupInfo_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `BotLeaveEventDisband` {#BotLeaveEventDisband}

Bases: `alicebot.adapter.mirai.event.notice.GroupBotEvent`

Bot 所在的群被解散

- **Attributes**

  - **type** (_Literal\['BotLeaveEventDisband'\]_)

  - **group** (_alicebot.adapter.mirai.event.base.GroupInfo_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `GroupNoticeEvent` {#GroupNoticeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupEvent`

其他群事件

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `GroupRecallEvent` {#GroupRecallEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

群消息撤回

- **Attributes**

  - **type** (_Literal\['GroupRecallEvent'\]_)

  - **authorId** (_int_)

  - **messageId** (_int_)

  - **time** (_int_)

  - **group** (_alicebot.adapter.mirai.event.base.GroupInfo_)

  - **operator** (_Optional\[alicebot.adapter.mirai.event.base.GroupMemberInfo\]_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `GroupNameChangeEvent` {#GroupNameChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

某个群名改变

- **Attributes**

  - **type** (_Literal\['GroupNameChangeEvent'\]_)

  - **origin** (_str_)

  - **current** (_str_)

  - **group** (_alicebot.adapter.mirai.event.base.GroupInfo_)

  - **operator** (_Optional\[alicebot.adapter.mirai.event.base.GroupMemberInfo\]_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `GroupEntranceAnnouncementChangeEvent` {#GroupEntranceAnnouncementChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

某群入群公告改变

- **Attributes**

  - **type** (_Literal\['GroupEntranceAnnouncementChangeEvent'\]_)

  - **origin** (_str_)

  - **current** (_str_)

  - **group** (_alicebot.adapter.mirai.event.base.GroupInfo_)

  - **operator** (_Optional\[alicebot.adapter.mirai.event.base.GroupMemberInfo\]_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `GroupMuteAllEvent` {#GroupMuteAllEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

全员禁言

- **Attributes**

  - **type** (_Literal\['GroupMuteAllEvent'\]_)

  - **origin** (_bool_)

  - **current** (_bool_)

  - **group** (_alicebot.adapter.mirai.event.base.GroupInfo_)

  - **operator** (_Optional\[alicebot.adapter.mirai.event.base.GroupMemberInfo\]_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `GroupAllowAnonymousChatEvent` {#GroupAllowAnonymousChatEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

匿名聊天

- **Attributes**

  - **type** (_Literal\['GroupAllowAnonymousChatEvent'\]_)

  - **origin** (_bool_)

  - **current** (_bool_)

  - **group** (_alicebot.adapter.mirai.event.base.GroupInfo_)

  - **operator** (_Optional\[alicebot.adapter.mirai.event.base.GroupMemberInfo\]_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `GroupAllowConfessTalkEvent` {#GroupAllowConfessTalkEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

坦白说

- **Attributes**

  - **type** (_Literal\['GroupAllowAnonymousChatEvent'\]_)

  - **origin** (_bool_)

  - **current** (_bool_)

  - **group** (_alicebot.adapter.mirai.event.base.GroupInfo_)

  - **isByBot** (_bool_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `GroupAllowMemberInviteEvent` {#GroupAllowMemberInviteEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupNoticeEvent`

允许群员邀请好友加群

- **Attributes**

  - **type** (_Literal\['GroupAllowMemberInviteEvent'\]_)

  - **origin** (_bool_)

  - **current** (_bool_)

  - **group** (_alicebot.adapter.mirai.event.base.GroupInfo_)

  - **operator** (_Optional\[alicebot.adapter.mirai.event.base.GroupMemberInfo\]_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `GroupMemberEvent` {#GroupMemberEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupEvent`

群成员相关事件

- **Attributes**

  - **member** (_alicebot.adapter.mirai.event.base.GroupMemberInfo_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `MemberJoinEvent` {#MemberJoinEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

新人入群的事件

- **Attributes**

  - **type** (_Literal\['MemberJoinEvent'\]_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `MemberLeaveEventKick` {#MemberLeaveEventKick}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

成员被踢出群 (该成员不是Bot)

- **Attributes**

  - **type** (_Literal\['MemberLeaveEventKick'\]_)

  - **operator** (_Optional\[alicebot.adapter.mirai.event.base.GroupMemberInfo\]_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `MemberLeaveEventQuit` {#MemberLeaveEventQuit}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

成员主动离群 (该成员不是Bot)

- **Attributes**

  - **type** (_Literal\['MemberLeaveEventQuit'\]_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `MemberCardChangeEvent` {#MemberCardChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群名片改动

- **Attributes**

  - **type** (_Literal\['MemberCardChangeEvent'\]_)

  - **origin** (_str_)

  - **current** (_str_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `MemberSpecialTitleChangeEvent` {#MemberSpecialTitleChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群头衔改动 (只有群主有操作限权)

- **Attributes**

  - **type** (_Literal\['MemberSpecialTitleChangeEvent'\]_)

  - **origin** (_str_)

  - **current** (_str_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `MemberPermissionChangeEvent` {#MemberPermissionChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

成员权限改变的事件 (该成员不是Bot)

- **Attributes**

  - **type** (_Literal\['MemberPermissionChangeEvent'\]_)

  - **origin** (_Literal\['OWNER', 'ADMINISTRATOR', 'MEMBER'\]_)

  - **current** (_Literal\['OWNER', 'ADMINISTRATOR', 'MEMBER'\]_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `MemberMuteEvent` {#MemberMuteEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群成员被禁言事件 (该成员不是Bot)

- **Attributes**

  - **type** (_Literal\['MemberMuteEvent'\]_)

  - **durationSeconds** (_int_)

  - **operator** (_Optional\[alicebot.adapter.mirai.event.base.GroupMemberInfo\]_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `MemberUnmuteEvent` {#MemberUnmuteEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群成员被取消禁言事件 (该成员不是Bot)

- **Attributes**

  - **type** (_Literal\['MemberUnmuteEvent'\]_)

  - **operator** (_Optional\[alicebot.adapter.mirai.event.base.GroupMemberInfo\]_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `MemberHonorChangeEvent` {#MemberHonorChangeEvent}

Bases: `alicebot.adapter.mirai.event.notice.GroupMemberEvent`

群员称号改变

- **Attributes**

  - **type** (_Literal\['MemberHonorChangeEvent'\]_)

  - **action** (_Literal\['achieve', 'lose'\]_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `OtherClientEvent` {#OtherClientEvent}

Bases: `alicebot.adapter.mirai.event.notice.NoticeEvent`

其他客户端事件

- **Attributes**

  - **client** (_alicebot.adapter.mirai.event.base.OtherClientSender_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `OtherClientOnlineEvent` {#OtherClientOnlineEvent}

Bases: `alicebot.adapter.mirai.event.notice.OtherClientEvent`

其他客户端上线

- **Attributes**

  - **type** (_Literal\['OtherClientOnlineEvent'\]_)

  - **kind** (_Optional\[int\]_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `OtherClientOfflineEvent` {#OtherClientOfflineEvent}

Bases: `alicebot.adapter.mirai.event.notice.OtherClientEvent`

其他客户端下线

- **Attributes**

  - **type** (_Literal\['OtherClientOfflineEvent'\]_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_
