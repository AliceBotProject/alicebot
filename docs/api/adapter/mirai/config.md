# alicebot.adapter.mirai.config

## Mirai 配置


## _class_ `Config`

基类：`pydantic.main.BaseModel`

Mirai 配置类，将在适配器被加载时被混入到机器人主配置中。


### `adapter_type`

适配器类型，需要和 mirai-api-http 配置相同。


* **Type**

    str



### `host`

本机域名。


* **Type**

    str



### `port`

监听的端口。


* **Type**

    int



### `url`

WebSocket 路径，需要和 mirai-api-http 配置相同。


* **Type**

    str



### `api_timeout`

进行 API 调用时等待返回响应的超时时间。


* **Type**

    int



### `verify_key`

建立连接时的认证密钥，需要和 mirai-api-http 配置中的 verifyKey 相同，如果关闭验证则留空。


* **Type**

    str



### `qq`

机器人的 QQ 号码，必须指定。


* **Type**

    int
