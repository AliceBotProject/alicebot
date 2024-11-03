# alicebot.adapter.mirai.event.meta

默认不会被传播的特殊事件。

## _class_ `MetaEvent` {#MetaEvent}

Bases: `alicebot.adapter.mirai.event.base.MiraiEvent`

默认不会被传播的特殊事件

## _class_ `BotEvent` {#BotEvent}

Bases: `alicebot.adapter.mirai.event.meta.MetaEvent`

Bot 自身事件

- **Attributes**

  - **qq** (_int_)

## _class_ `BotOnlineEvent` {#BotOnlineEvent}

Bases: `alicebot.adapter.mirai.event.meta.BotEvent`

Bot 登录成功

- **Attributes**

  - **type** (_Literal\['BotOnlineEvent'\]_)

## _class_ `BotOfflineEventActive` {#BotOfflineEventActive}

Bases: `alicebot.adapter.mirai.event.meta.BotEvent`

Bot 主动离线

- **Attributes**

  - **type** (_Literal\['BotOfflineEventActive'\]_)

## _class_ `BotOfflineEventForce` {#BotOfflineEventForce}

Bases: `alicebot.adapter.mirai.event.meta.BotEvent`

Bot 被挤下线

- **Attributes**

  - **type** (_Literal\['BotOfflineEventForce'\]_)

## _class_ `BotOfflineEventDropped` {#BotOfflineEventDropped}

Bases: `alicebot.adapter.mirai.event.meta.BotEvent`

Bot 被服务器断开或因网络问题而掉线

- **Attributes**

  - **type** (_Literal\['BotOfflineEventDropped'\]_)

## _class_ `BotReloginEvent` {#BotReloginEvent}

Bases: `alicebot.adapter.mirai.event.meta.BotEvent`

Bot 主动重新登录

- **Attributes**

  - **type** (_Literal\['BotReloginEvent'\]_)

## _class_ `CommandExecutedEvent` {#CommandExecutedEvent}

Bases: `alicebot.adapter.mirai.event.meta.MetaEvent`

命令被执行

- **Attributes**

  - **type** (_Literal\['CommandExecutedEvent'\]_)

  - **name** (_str_)

  - **friend** (_Optional\[alicebot.adapter.mirai.event.base.FriendInfo\]_)

  - **member** (_Optional\[alicebot.adapter.mirai.event.base.GroupMemberInfo\]_)

  - **args** (_list\[typing.Any\]_)
