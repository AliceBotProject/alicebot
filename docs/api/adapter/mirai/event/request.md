# alicebot.adapter.mirai.event.request

申请事件。

## _class_ `RequestEvent` {#RequestEvent}

Bases: `alicebot.adapter.mirai.event.base.MiraiEvent`

申请事件

### _async method_ `approve(self, message = '')` {#RequestEvent-approve}

同意请求。

- **Arguments**

  - **message** (_str_) - 回复的信息，默认为空。

- **Returns**

  Type: _dict\[str, typing.Any\]_

  API 请求响应。

### _async method_ `refuse(self, message = '')` {#RequestEvent-refuse}

拒绝请求。

- **Arguments**

  - **message** (_str_) - 回复的信息，默认为空。

- **Returns**

  Type: _dict\[str, typing.Any\]_

  API 请求响应。

## _class_ `NewFriendRequestEvent` {#NewFriendRequestEvent}

Bases: `alicebot.adapter.mirai.event.request.RequestEvent`

添加好友申请

- **Attributes**

  - **type** (_Literal\['NewFriendRequestEvent'\]_)

  - **eventId** (_int_)

  - **fromId** (_int_)

  - **groupId** (_int_)

  - **nick** (_str_)

  - **message** (_str_)

### _async method_ `approve(self, message = '')` {#NewFriendRequestEvent-approve}

同意请求。

- **Arguments**

  - **message** (_str_) - 回复的信息，默认为空。

- **Returns**

  Type: _dict\[str, typing.Any\]_

  API 请求响应。

### _async method_ `refuse(self, message = '', black_list = False)` {#NewFriendRequestEvent-refuse}

拒绝请求。

- **Arguments**

  - **message** (_str_) - 回复的信息，默认为空。

  - **black\_list** (_bool_) - 是否加入黑名单，默认为 `False`。

- **Returns**

  Type: _dict\[str, typing.Any\]_

  API 请求响应。

## _class_ `MemberJoinRequestEvent` {#MemberJoinRequestEvent}

Bases: `alicebot.adapter.mirai.event.request.RequestEvent`

用户入群申请 (Bot 需要有管理员权限)

- **Attributes**

  - **type** (_Literal\['MemberJoinRequestEvent'\]_)

  - **eventId** (_int_)

  - **fromId** (_int_)

  - **groupId** (_int_)

  - **groupName** (_str_)

  - **nick** (_str_)

  - **message** (_str_)

### _async method_ `approve(self, message = '')` {#MemberJoinRequestEvent-approve}

同意请求。

- **Arguments**

  - **message** (_str_) - 回复的信息，默认为空。

- **Returns**

  Type: _dict\[str, typing.Any\]_

  API 请求响应。

### _async method_ `ignore(self, message = '', black_list = False)` {#MemberJoinRequestEvent-ignore}

忽略请求。

- **Arguments**

  - **message** (_str_) - 回复的信息，默认为空。

  - **black\_list** (_bool_) - 是否加入黑名单，默认为 `False`。

- **Returns**

  Type: _dict\[str, typing.Any\]_

  API 请求响应。

### _async method_ `refuse(self, message = '', black_list = False)` {#MemberJoinRequestEvent-refuse}

拒绝请求。

- **Arguments**

  - **message** (_str_) - 回复的信息，默认为空。

  - **black\_list** (_bool_) - 是否加入黑名单，默认为 `False`。

- **Returns**

  Type: _dict\[str, typing.Any\]_

  API 请求响应。

## _class_ `BotInvitedJoinGroupRequestEvent` {#BotInvitedJoinGroupRequestEvent}

Bases: `alicebot.adapter.mirai.event.request.RequestEvent`

Bot 被邀请入群申请

- **Attributes**

  - **type** (_Literal\['BotInvitedJoinGroupRequestEvent'\]_)

  - **eventId** (_int_)

  - **fromId** (_int_)

  - **groupId** (_int_)

  - **groupName** (_str_)

  - **nick** (_str_)

  - **message** (_str_)

### _async method_ `approve(self, message = '')` {#BotInvitedJoinGroupRequestEvent-approve}

同意请求。

- **Arguments**

  - **message** (_str_) - 回复的信息，默认为空。

- **Returns**

  Type: _dict\[str, typing.Any\]_

  API 请求响应。

### _async method_ `refuse(self, message = '')` {#BotInvitedJoinGroupRequestEvent-refuse}

拒绝请求。

- **Arguments**

  - **message** (_str_) - 回复的信息，默认为空。

- **Returns**

  Type: _dict\[str, typing.Any\]_

  API 请求响应。
