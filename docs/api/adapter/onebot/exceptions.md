# alicebot.adapter.onebot.exceptions

OneBot 适配器异常。

## _class_ `OneBotException` {#OneBotException}

Bases: `alicebot.exceptions.AdapterException`

OneBot 异常基类。

## _class_ `NetworkError` {#NetworkError}

Bases: `alicebot.adapter.onebot.exceptions.OneBotException`

网络异常。

## _class_ `ActionFailed` {#ActionFailed}

Bases: `alicebot.adapter.onebot.exceptions.OneBotException`

API 请求成功响应，但响应表示 API 操作失败。

### _method_ `__init__(self, resp)` {#ActionFailed---init--}

初始化。

- **Arguments**

  - **resp** (_Any_) - 返回的响应。

- **Returns**

  Type: _None_

## _class_ `ApiTimeout` {#ApiTimeout}

Bases: `alicebot.adapter.onebot.exceptions.OneBotException`

API 请求响应超时。
