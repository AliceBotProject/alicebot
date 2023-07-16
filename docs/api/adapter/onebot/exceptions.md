# alicebot.adapter.onebot.exceptions

OneBot 适配器异常。

## *class* `OneBotException`(self, /, *args, **kwargs) {#OneBotException}

Bases: `alicebot.exceptions.AdapterException`

OneBot 异常基类。

- **Arguments**

  - **args**

  - **kwargs**

## *class* `NetworkError`(self, /, *args, **kwargs) {#NetworkError}

Bases: `alicebot.adapter.onebot.exceptions.OneBotException`

网络异常。

- **Arguments**

  - **args**

  - **kwargs**

## *class* `ActionFailed`(self, resp) {#ActionFailed}

Bases: `alicebot.adapter.onebot.exceptions.OneBotException`

API 请求成功响应，但响应表示 API 操作失败。

- **Arguments**

  - **resp** (*Any*) - 返回的响应。

## *class* `ApiTimeout`(self, /, *args, **kwargs) {#ApiTimeout}

Bases: `alicebot.adapter.onebot.exceptions.OneBotException`

API 请求响应超时。

- **Arguments**

  - **args**

  - **kwargs**