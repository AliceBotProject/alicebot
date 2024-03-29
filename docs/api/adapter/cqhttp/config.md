# alicebot.adapter.cqhttp.config

CQHTTP 适配器配置。

## _class_ `Config` {#Config}

Bases: `alicebot.config.ConfigModel`

CQHTTP 配置类，将在适配器被加载时被混入到机器人主配置中。

- **Attributes**

  - **adapter\_type** (_Literal\['ws', 'reverse-ws', 'ws-reverse'\]_) - 适配器类型，需要和协议端配置相同。

  - **host** (_str_) - 本机域名。

  - **port** (_int_) - 监听的端口。

  - **url** (_str_) - WebSocket 路径，需和协议端配置相同。

  - **reconnect\_interval** (_int_) - 重连等待时间。

  - **api\_timeout** (_int_) - 进行 API 调用时等待返回响应的超时时间。

  - **access\_token** (_str_) - 鉴权。
