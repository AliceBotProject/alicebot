# alicebot.adapter.mirai.event.base

事件基类。

## *class* `Subject`(__pydantic_self__, **data) {#Subject}

Bases: `pydantic.main.BaseModel`

来源

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **id** (*int*)

  - **kind** (*Literal['Friend', 'Group']*)

## *class* `FriendInfo`(__pydantic_self__, **data) {#FriendInfo}

Bases: `pydantic.main.BaseModel`

好友信息

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **id** (*int*)

  - **nickname** (*str*)

  - **remark** (*str*)

## *class* `GroupInfo`(__pydantic_self__, **data) {#GroupInfo}

Bases: `pydantic.main.BaseModel`

群聊信息

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **id** (*int*)

  - **name** (*str*)

  - **permission** (*Literal['OWNER', 'ADMINISTRATOR', 'MEMBER']*)

## *class* `GroupMemberInfo`(__pydantic_self__, **data) {#GroupMemberInfo}

Bases: `pydantic.main.BaseModel`

群成员信息

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **id** (*int*)

  - **memberName** (*str*)

  - **permission** (*Literal['OWNER', 'ADMINISTRATOR', 'MEMBER']*)

  - **specialTitle** (*str*)

  - **joinTimestamp** (*int*)

  - **lastSpeakTimestamp** (*int*)

  - **muteTimeRemaining** (*int*)

  - **group** (*alicebot.adapter.mirai.event.base.GroupInfo*)

## *class* `OtherClientSender`(__pydantic_self__, **data) {#OtherClientSender}

Bases: `pydantic.main.BaseModel`

其他客户端信息

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **id** (*int*)

  - **platform** (*str*)

## *class* `MiraiEvent`(self, adapter, **data) {#MiraiEvent}

Bases: `alicebot.event.Event`

Mirai 事件基类

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*str*)