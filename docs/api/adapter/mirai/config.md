# alicebot.adapter.mirai.config

Mirai 适配器配置。

## *class* `Config`(__pydantic_self__, **data) {#Config}

Bases: `pydantic.main.BaseModel`

Mirai 配置类，将在适配器被加载时被混入到机器人主配置中。

- **Attributes**

  - **adapter_type** (*str*) - 适配器类型，需要和 mirai-api-http 配置相同。

  - **host** (*str*) - 本机域名。

  - **port** (*int*) - 监听的端口。

  - **url** (*str*) - WebSocket 路径，需要和 mirai-api-http 配置相同。

  - **api_timeout** (*int*) - 进行 API 调用时等待返回响应的超时时间。

  - **verify_key** (*str*) - 建立连接时的认证密钥，需要和 mirai-api-http 配置中的 verifyKey 相同，如果关闭验证则留空。

  - **qq** (*int*) - 机器人的 QQ 号码，必须指定。

  - **__config_name__** - 配置名称。