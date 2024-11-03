# alicebot.adapter.dingtalk

DingTalk 协议适配器。

本适配器适配了钉钉企业自建机器人协议。
协议详情请参考：[钉钉开放平台](https://open.dingtalk.com/document/robots/robot-overview)。

## _class_ `DingTalkAdapter` {#DingTalkAdapter}

Bases: `alicebot.adapter.Adapter`

钉钉协议适配器。

- **Attributes**

  - **name** (_str_)

  - **app** (_aiohttp.web\_app.Application_)

  - **runner** (_aiohttp.web\_runner.AppRunner_)

  - **site** (_aiohttp.web\_runner.TCPSite_)

  - **session** (_aiohttp.client.ClientSession_)

### _class_ `Config` {#Config}

Bases: `alicebot.config.ConfigModel`

DingTalk 配置类，将在适配器被加载时被混入到机器人主配置中。

- **Attributes**

  - **host** (_str_) - 本机域名。

  - **port** (_int_) - 监听的端口。

  - **url** (_str_) - 路径。

  - **api\_timeout** (_int_) - 进行 API 调用时等待返回响应的超时时间。

  - **app\_secret** (_str_) - 机器人的 `appSecret`。

### _method_ `get_sign(self, timestamp)` {#DingTalkAdapter-get-sign}

计算签名。

- **Arguments**

  - **timestamp** (_str_) - 时间戳。

- **Returns**

  Type: _str_

  签名。

### _async method_ `handler(self, request)` {#DingTalkAdapter-handler}

处理 aiohttp 服务器的接收。

- **Arguments**

  - **request** (_aiohttp.web\_request.Request_) - aiohttp 服务器的 `Request` 对象。

- **Returns**

  Type: _aiohttp.web\_response.Response_

### _async method_ `run(self)` {#DingTalkAdapter-run}

适配器运行方法，适配器开发者必须实现该方法。

适配器运行过程中保持保持运行，当此方法结束后， AliceBot 不会自动重新启动适配器。

- **Returns**

  Type: _None_

### _async method_ `send(self, webhook, conversation_type, msg, at = None)` {#DingTalkAdapter-send}

发送消息。

- **Arguments**

  - **webhook** (_str_) - Webhook 网址。

  - **conversation\_type** (_Literal\['1', '2'\]_) - 聊天类型，"1" 表示单聊，"2" 表示群聊。

  - **msg** (_Union\[str, dict\[str, Any\], alicebot.adapter.dingtalk.message.DingTalkMessage\]_) - 消息。

  - **at** (_Union\[NoneType, dict\[str, Any\], alicebot.adapter.dingtalk.message.DingTalkMessage\]_) - At 对象，仅在群聊时生效，默认为空。

- **Returns**

  Type: _dict\[str, typing.Any\]_

  钉钉服务器的响应。

- **Raises**

  - **TypeError** - 传入参数类型错误。

  - **ValueError** - 传入参数值错误。

  - **NetworkError** - 调用 Webhook 地址时网络错误。

### _async method_ `shutdown(self)` {#DingTalkAdapter-shutdown}

在适配器结束运行时运行的方法，用于安全地关闭适配器。

AliceBot 在接收到系统的结束信号后先发送 cancel 请求给 run 任务。
在所有适配器都停止运行后，会依次运行并等待所有适配器的 `shutdown()` 方法。
当强制退出时此方法可能未被执行。

- **Returns**

  Type: _None_

### _async method_ `startup(self)` {#DingTalkAdapter-startup}

在适配器开始运行前运行的方法，用于初始化适配器。

AliceBot 依次运行并等待所有适配器的 `startup()` 方法，待运行完毕后再创建 `run()` 任务。

- **Returns**

  Type: _None_
