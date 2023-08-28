# alicebot.adapter.mirai.event.base

事件基类。

## _class_ `Subject` {#Subject}

Bases: `pydantic.main.BaseModel`

来源

- **Attributes**

  - **id** (_int_)

  - **kind** (_Literal\['Friend', 'Group'\]_)

### _method_ `__init__(__pydantic_self__, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`__init__` uses `__pydantic_self__` instead of the more common `self` for the first arg to
allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `FriendInfo` {#FriendInfo}

Bases: `pydantic.main.BaseModel`

好友信息

- **Attributes**

  - **id** (_int_)

  - **nickname** (_str_)

  - **remark** (_str_)

### _method_ `__init__(__pydantic_self__, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`__init__` uses `__pydantic_self__` instead of the more common `self` for the first arg to
allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `GroupInfo` {#GroupInfo}

Bases: `pydantic.main.BaseModel`

群聊信息

- **Attributes**

  - **id** (_int_)

  - **name** (_str_)

  - **permission** (_Literal\['OWNER', 'ADMINISTRATOR', 'MEMBER'\]_)

### _method_ `__init__(__pydantic_self__, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`__init__` uses `__pydantic_self__` instead of the more common `self` for the first arg to
allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `GroupMemberInfo` {#GroupMemberInfo}

Bases: `pydantic.main.BaseModel`

群成员信息

- **Attributes**

  - **id** (_int_)

  - **memberName** (_str_)

  - **permission** (_Literal\['OWNER', 'ADMINISTRATOR', 'MEMBER'\]_)

  - **specialTitle** (_str_)

  - **joinTimestamp** (_int_)

  - **lastSpeakTimestamp** (_int_)

  - **muteTimeRemaining** (_int_)

  - **group** (_GroupInfo_)

### _method_ `__init__(__pydantic_self__, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`__init__` uses `__pydantic_self__` instead of the more common `self` for the first arg to
allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `OtherClientSender` {#OtherClientSender}

Bases: `pydantic.main.BaseModel`

其他客户端信息

- **Attributes**

  - **id** (_int_)

  - **platform** (_str_)

### _method_ `__init__(__pydantic_self__, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`__init__` uses `__pydantic_self__` instead of the more common `self` for the first arg to
allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

## _class_ `MiraiEvent` {#MiraiEvent}

Bases: `alicebot.event.Event[MiraiAdapter]`

Mirai 事件基类

- **Attributes**

  - **type** (_str_)

### _method_ `__init__(__pydantic_self__, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`__init__` uses `__pydantic_self__` instead of the more common `self` for the first arg to
allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_
