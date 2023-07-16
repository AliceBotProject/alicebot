# alicebot.adapter.mirai.exceptions

Mirai 适配器异常。

## *class* `MiraiException`(self, /, *args, **kwargs) {#MiraiException}

Bases: `alicebot.exceptions.AdapterException`

Mirai 异常基类。

- **Arguments**

  - **args**

  - **kwargs**

## *class* `NetworkError`(self, /, *args, **kwargs) {#NetworkError}

Bases: `alicebot.adapter.mirai.exceptions.MiraiException`

网络异常。

- **Arguments**

  - **args**

  - **kwargs**

## *class* `ActionFailed`(self, code, resp) {#ActionFailed}

Bases: `alicebot.adapter.mirai.exceptions.MiraiException`

API 请求成功响应，但响应表示 API 操作失败。

- **Arguments**

  - **code** (*int*) - 错误代码。

  - **resp** (*Dict[str, Any]*) - 返回的响应。

## *class* `ApiTimeout`(self, /, *args, **kwargs) {#ApiTimeout}

Bases: `alicebot.adapter.mirai.exceptions.MiraiException`

API 请求响应超时。

- **Arguments**

  - **args**

  - **kwargs**