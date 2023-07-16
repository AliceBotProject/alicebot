# alicebot.adapter.dingtalk

DingTalk 协议适配器。

本适配器适配了钉钉企业自建机器人协议。
协议详情请参考: [钉钉开放平台](https://open.dingtalk.com/document/robots/robot-overview)。

## *class* `DingTalkAdapter`(self, bot) {#DingTalkAdapter}

Bases: `alicebot.adapter.Adapter`

钉钉协议适配器。

- **Arguments**

  - **bot** (*Bot*) - 当前机器人对象。

- **Attributes**

  - **name** (*str*)

  - **app** (*aiohttp.web_app.Application*)

  - **runner** (*aiohttp.web_runner.AppRunner*)

  - **site** (*aiohttp.web_runner.TCPSite*)

  - **session** (*aiohttp.client.ClientSession*)

### *class* `Config`(__pydantic_self__, **data) {#Config}

Bases: `alicebot.config.ConfigModel`

DingTalk 配置类，将在适配器被加载时被混入到机器人主配置中。

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **host** (*str*) - 本机域名。

  - **port** (*int*) - 监听的端口。

  - **url** (*str*) - 路径。

  - **api_timeout** (*int*) - 进行 API 调用时等待返回响应的超时时间。

  - **app_secret** (*str*) - 机器人的 `appSecret`。

### *method* `get_sign(self, timestamp)` {#DingTalkAdapter.get_sign}

计算签名。

- **Arguments**

  - **timestamp** (*str*) - 时间戳。

- **Returns**

  Type: *str*

  签名。

### *async method* `handler(self, request)` {#DingTalkAdapter.handler}

处理 aiohttp 服务器的接收。

- **Arguments**

  - **request** (*aiohttp.web_request.Request*) - aiohttp 服务器的 `Request` 对象。

### *async method* `run(self)` {#DingTalkAdapter.run}

运行 aiohttp 服务器。

### *async method* `send(self, webhook, conversation_type, msg, at = None)` {#DingTalkAdapter.send}

发送消息。

- **Arguments**

  - **webhook** (*str*) - Webhook 网址。

  - **conversation_type** (*Literal['1', '2']*) - 聊天类型，"1" 表示单聊，"2" 表示群聊。

  - **msg** (*Union[str, Dict[str, Any], alicebot.adapter.dingtalk.message.DingTalkMessage]*) - 消息。

  - **at** (*Union[NoneType, Dict[str, Any], alicebot.adapter.dingtalk.message.DingTalkMessage]*) - At 对象，仅在群聊时生效，默认为空。

- **Returns**

  Type: *Dict[str, Any]*

  钉钉服务器的响应。

- **Raises**

  - **TypeError** - 传入参数类型错误。

  - **ValueError** - 传入参数值错误。

  - **NetworkError** - 调用 Webhook 地址时网络错误。

### *async method* `shutdown(self)` {#DingTalkAdapter.shutdown}

清理 aiohttp AppRunner。

### *async method* `startup(self)` {#DingTalkAdapter.startup}

创建 aiohttp Application。