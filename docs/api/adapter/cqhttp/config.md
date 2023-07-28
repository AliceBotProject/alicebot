# alicebot.adapter.cqhttp.config

CQHTTP 适配器配置。

## *class* `Config`(__pydantic_self__, **data) {#Config}

Bases: `alicebot.config.ConfigModel`

CQHTTP 配置类，将在适配器被加载时被混入到机器人主配置中。

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **adapter_type** (*Literal['ws', 'reverse-ws', 'ws-reverse']*) - 适配器类型，需要和协议端配置相同。

  - **host** (*str*) - 本机域名。

  - **port** (*int*) - 监听的端口。

  - **url** (*str*) - WebSocket 路径，需和协议端配置相同。

  - **reconnect_interval** (*int*) - 重连等待时间。

  - **api_timeout** (*int*) - 进行 API 调用时等待返回响应的超时时间。

  - **access_token** (*str*) - 鉴权。