# alicebot.adapter.dingtalk.exceptions

DingTalk 适配器异常。

## *class* `DingTalkException`(self, /, *args, **kwargs) {#DingTalkException}

Bases: `alicebot.exceptions.AdapterException`

DingTalk 异常基类。

- **Arguments**

  - **args**

  - **kwargs**

## *class* `NetworkError`(self, /, *args, **kwargs) {#NetworkError}

Bases: `alicebot.adapter.dingtalk.exceptions.DingTalkException`

网络异常。

- **Arguments**

  - **args**

  - **kwargs**

## *class* `WebhookExpiredError`(self, /, *args, **kwargs) {#WebhookExpiredError}

Bases: `alicebot.adapter.dingtalk.exceptions.DingTalkException`

Webhook 地址已到期。

- **Arguments**

  - **args**

  - **kwargs**