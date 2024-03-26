# alicebot.adapter.cqhttp.exceptions

CQHTTP 适配器异常。

## _class_ `CQHTTPException` {#CQHTTPException}

Bases: `alicebot.exceptions.AdapterException`

CQHTTP 异常基类。

### _method_ `__init__(self, /, *args, **kwargs)` {#Exception---init--}

Initialize self.  See help(type(self)) for accurate signature.

- **Arguments**

  - **args**

  - **kwargs**

## _class_ `NetworkError` {#NetworkError}

Bases: `alicebot.adapter.cqhttp.exceptions.CQHTTPException`

网络异常。

### _method_ `__init__(self, /, *args, **kwargs)` {#Exception---init--}

Initialize self.  See help(type(self)) for accurate signature.

- **Arguments**

  - **args**

  - **kwargs**

## _class_ `ActionFailed` {#ActionFailed}

Bases: `alicebot.adapter.cqhttp.exceptions.CQHTTPException`

API 请求成功响应，但响应表示 API 操作失败。

### _method_ `__init__(self, resp)` {#ActionFailed---init--}

初始化。

- **Arguments**

  - **resp** (_Dict\[str, Any\]_) - 返回的响应。

- **Returns**

  Type: _None_

## _class_ `ApiNotAvailable` {#ApiNotAvailable}

Bases: `alicebot.adapter.cqhttp.exceptions.ActionFailed`

API 请求返回 404，表示当前请求的 API 不可用或不存在。

- **Attributes**

  - **ERROR\_CODE** (_ClassVar\[int\]_)

### _method_ `__init__(self, resp)` {#ActionFailed---init--}

初始化。

- **Arguments**

  - **resp** (_Dict\[str, Any\]_) - 返回的响应。

- **Returns**

  Type: _None_

## _class_ `ApiTimeout` {#ApiTimeout}

Bases: `alicebot.adapter.cqhttp.exceptions.CQHTTPException`

API 请求响应超时。

### _method_ `__init__(self, /, *args, **kwargs)` {#Exception---init--}

Initialize self.  See help(type(self)) for accurate signature.

- **Arguments**

  - **args**

  - **kwargs**
