# alicebot.adapter.mirai.config

Mirai 适配器配置。

## *class* `Config`(__pydantic_self__, **data) {#Config}

Bases: `alicebot.config.ConfigModel`

Mirai 配置类，将在适配器被加载时被混入到机器人主配置中。

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **adapter_type** (*Literal['ws', 'reverse-ws']*) - 适配器类型，需要和协议端配置相同。

  - **host** (*str*) - 本机域名。

  - **port** (*int*) - 监听的端口。

  - **url** (*str*) - WebSocket 路径，需要和协议端配置相同。

  - **reconnect_interval** (*int*) - 重连等待时间。

  - **api_timeout** (*int*) - 进行 API 调用时等待返回响应的超时时间。

  - **verify_key** (*str*) - 建立连接时的认证密钥，需要和 mirai-api-http 配置中的 `verifyKey` 相同，如果关闭验证则留空。

  - **qq** (*int*) - 机器人的 QQ 号码，必须指定。