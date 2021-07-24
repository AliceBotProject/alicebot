# alicebot.adapter.cqhttp.config

## CQHTTP 配置


## _class_ `Config`

基类：`pydantic.main.BaseModel`

CQHTTP 配置类，将在适配器被加载时被混入到机器人主配置中。


### `host`

本机域名。


### `port`

监听的端口。


### `url`

WebSockets 路径，需和客户端配置相同。


### `api_timeout`

进行 API 调用时等待返回响应的超时时间。
