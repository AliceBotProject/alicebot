# alicebot.adapter.dingtalk.exceptions

DingTalk 适配器异常。

## _class_ `DingTalkException` {#DingTalkException}

Bases: `alicebot.exceptions.AdapterException`

DingTalk 异常基类。

### _method_ `__init__(self, /, *args, **kwargs)` {#Exception.\_\_init\_\_}

Initialize self.  See help(type(self)) for accurate signature.

- **Arguments**

  - **args**

  - **kwargs**

## _class_ `NetworkError` {#NetworkError}

Bases: `alicebot.adapter.dingtalk.exceptions.DingTalkException`

网络异常。

### _method_ `__init__(self, /, *args, **kwargs)` {#Exception.\_\_init\_\_}

Initialize self.  See help(type(self)) for accurate signature.

- **Arguments**

  - **args**

  - **kwargs**

## _class_ `WebhookExpiredError` {#WebhookExpiredError}

Bases: `alicebot.adapter.dingtalk.exceptions.DingTalkException`

Webhook 地址已到期。

### _method_ `__init__(self, /, *args, **kwargs)` {#Exception.\_\_init\_\_}

Initialize self.  See help(type(self)) for accurate signature.

- **Arguments**

  - **args**

  - **kwargs**
