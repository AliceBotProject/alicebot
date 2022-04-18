# alicebot.adapter.dingtalk

DingTalk 协议适配器。

本适配器适配了钉钉企业自建机器人协议。
协议详情请参考: [钉钉开放平台](https://developers.dingtalk.com/document/robots/robot-overview) 。

## *class* `DingTalkAdapter`(self, bot) {#DingTalkAdapter}

Bases: `alicebot.adapter.Adapter`

钉钉协议适配器。

- **Arguments**

  - **bot** (*Bot*)

- **Attributes**

  - **name** (*str*)

  - **app** (*aiohttp.web_app.Application*)

  - **runner** (*aiohttp.web_runner.AppRunner*)

  - **site** (*aiohttp.web_runner.TCPSite*)

  - **session** (*aiohttp.client.ClientSession*)

### *readonly property* `config` {#DingTalkAdapter.config}

本适配器的配置。

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

  - **request** (*aiohttp.web_request.Request*) - aiohttp 服务器的 Request 对象。

### *async method* `run(self)` {#DingTalkAdapter.run}

运行 aiohttp 服务器。

### *async method* `send(self, webhook, conversation_type, msg, at = None)` {#DingTalkAdapter.send}

发送消息。

- **Arguments**

  - **webhook** (*str*) - Webhook 网址。

  - **conversation_type** (*Literal['1', '2']*) - 聊天类型，'1' 表示单聊，'2' 表示群聊。

  - **msg** (*Union[str, Dict, alicebot.adapter.dingtalk.message.DingTalkMessage]*) - 消息。

  - **at** (*Union[NoneType, Dict, alicebot.adapter.dingtalk.message.DingTalkMessage]*) - At 对象，仅在群聊时生效，默认为空。

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