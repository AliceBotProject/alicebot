# alicebot.adapter.telegram.exceptions

Telegram 适配器异常。

## _class_ `TelegramException` {#TelegramException}

Bases: `alicebot.exceptions.AdapterException`

Telegram 异常基类。

## _class_ `NetworkError` {#NetworkError}

Bases: `alicebot.adapter.telegram.exceptions.TelegramException`

网络异常。

## _class_ `ActionFailed` {#ActionFailed}

Bases: `alicebot.adapter.telegram.exceptions.TelegramException`

API 请求成功响应，但响应表示 API 操作失败。

### _method_ `__init__(self, resp)` {#ActionFailed---init--}

初始化。

- **Arguments**

  - **resp** (_Any_) - 返回的响应。

- **Returns**

  Type: _None_
