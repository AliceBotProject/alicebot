# alicebot.adapter.mirai.exceptions

Mirai 适配器异常。

## *class* `MiraiException`(self, /, *args, **kwargs) {#MiraiException}

Bases: `alicebot.exceptions.AdapterException`

Mirai 异常基类。

## *class* `NetworkError`(self, /, *args, **kwargs) {#NetworkError}

Bases: `alicebot.adapter.mirai.exceptions.MiraiException`

网络异常。

## *class* `ActionFailed`(self, code, resp) {#ActionFailed}

Bases: `alicebot.adapter.mirai.exceptions.MiraiException`

API 请求成功响应，但响应表示 API 操作失败。

- **Arguments**

  - **code**

  - **resp**

## *class* `ApiTimeout`(self, /, *args, **kwargs) {#ApiTimeout}

Bases: `alicebot.adapter.mirai.exceptions.MiraiException`, `alicebot.exceptions.AdapterTimeout`

API 请求响应超时。