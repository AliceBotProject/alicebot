# alicebot.adapter.mirai.exceptions

Mirai 适配器异常。

## _class_ `MiraiException` {#MiraiException}

Bases: `alicebot.exceptions.AdapterException`

Mirai 异常基类。

### _method_ `__init__(self, /, *args, **kwargs)` {#Exception.\_\_init\_\_}

Initialize self.  See help(type(self)) for accurate signature.

- **Arguments**

  - **args**

  - **kwargs**

## _class_ `NetworkError` {#NetworkError}

Bases: `alicebot.adapter.mirai.exceptions.MiraiException`

网络异常。

### _method_ `__init__(self, /, *args, **kwargs)` {#Exception.\_\_init\_\_}

Initialize self.  See help(type(self)) for accurate signature.

- **Arguments**

  - **args**

  - **kwargs**

## _class_ `ActionFailed` {#ActionFailed}

Bases: `alicebot.adapter.mirai.exceptions.MiraiException`

API 请求成功响应，但响应表示 API 操作失败。

### _method_ `__init__(self, code, resp)` {#ActionFailed.\_\_init\_\_}

初始化。

- **Arguments**

  - **code** (_int_) - 错误代码。

  - **resp** (_Dict\[str, Any\]_) - 返回的响应。

- **Returns**

  Type: _None_

## _class_ `ApiTimeout` {#ApiTimeout}

Bases: `alicebot.adapter.mirai.exceptions.MiraiException`

API 请求响应超时。

### _method_ `__init__(self, /, *args, **kwargs)` {#Exception.\_\_init\_\_}

Initialize self.  See help(type(self)) for accurate signature.

- **Arguments**

  - **args**

  - **kwargs**
