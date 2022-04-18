# alicebot.adapter.mirai.event.mate

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