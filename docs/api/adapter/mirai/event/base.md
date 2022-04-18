# alicebot.adapter.mirai.event.base

## *class* `Subject`(__pydantic_self__, **data) {#Subject}

Bases: `pydantic.main.BaseModel`

- **Attributes**

  - **id** (*int*)

  - **kind** (*Literal['Friend', 'Group']*)

## *class* `FriendInfo`(__pydantic_self__, **data) {#FriendInfo}

Bases: `pydantic.main.BaseModel`

- **Attributes**

  - **id** (*int*)

  - **nickname** (*str*)

  - **remark** (*str*)

## *class* `GroupInfo`(__pydantic_self__, **data) {#GroupInfo}

Bases: `pydantic.main.BaseModel`

- **Attributes**

  - **id** (*int*)

  - **name** (*str*)

  - **permission** (*Literal['OWNER', 'ADMINISTRATOR', 'MEMBER']*)

## *class* `GroupMemberInfo`(__pydantic_self__, **data) {#GroupMemberInfo}

Bases: `pydantic.main.BaseModel`

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

- **Attributes**

  - **id** (*int*)

  - **platform** (*str*)

## *class* `MiraiEvent`(__pydantic_self__, **data) {#MiraiEvent}

Bases: `alicebot.event.Event`

Mirai 事件基类

- **Attributes**

  - **type** (*str*)