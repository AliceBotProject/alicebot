# alicebot.adapter.mirai.exceptions

Mirai 适配器异常。

## _class_ `MiraiException` {#MiraiException}

Bases: `alicebot.exceptions.AdapterException`

Mirai 异常基类。

## _class_ `NetworkError` {#NetworkError}

Bases: `alicebot.adapter.mirai.exceptions.MiraiException`

网络异常。

## _class_ `ActionFailed` {#ActionFailed}

Bases: `alicebot.adapter.mirai.exceptions.MiraiException`

API 请求成功响应，但响应表示 API 操作失败。

### _method_ `__init__(self, code, resp)` {#ActionFailed---init--}

初始化。

- **Arguments**

  - **code** (_int_) - 错误代码。

  - **resp** (_dict\[str, typing.Any\]_) - 返回的响应。

- **Returns**

  Type: _None_

## _class_ `ApiTimeout` {#ApiTimeout}

Bases: `alicebot.adapter.mirai.exceptions.MiraiException`

API 请求响应超时。
