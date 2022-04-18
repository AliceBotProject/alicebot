# alicebot.adapter.cqhttp.exceptions

CQHTTP 适配器异常。

## *class* `CQHTTPException`(self, /, *args, **kwargs) {#CQHTTPException}

Bases: `alicebot.exceptions.AdapterException`

CQHTTP 异常基类。

## *class* `NetworkError`(self, /, *args, **kwargs) {#NetworkError}

Bases: `alicebot.adapter.cqhttp.exceptions.CQHTTPException`

网络异常。

## *class* `ActionFailed`(self, resp) {#ActionFailed}

Bases: `alicebot.adapter.cqhttp.exceptions.CQHTTPException`

API 请求成功响应，但响应表示 API 操作失败。

- **Arguments**

  - **resp**

## *class* `ApiNotAvailable`(self, resp) {#ApiNotAvailable}

Bases: `alicebot.adapter.cqhttp.exceptions.ActionFailed`

API 请求返回 404，表示当前请求的 API 不可用或不存在。

- **Arguments**

  - **resp**

## *class* `ApiTimeout`(self, /, *args, **kwargs) {#ApiTimeout}

Bases: `alicebot.adapter.cqhttp.exceptions.CQHTTPException`, `alicebot.exceptions.AdapterTimeout`

API 请求响应超时。