# alicebot.adapter.dingtalk.config

## DingTalk 配置


## _class_ `Config`

基类：`pydantic.main.BaseModel`

DingTalk 配置类，将在适配器被加载时被混入到机器人主配置中。


### `host`

本机域名。


* **Type**

    str



### `port`

监听的端口。


* **Type**

    int



### `url`

路径。


* **Type**

    str



### `api_timeout`

进行 API 调用时等待返回响应的超时时间。


* **Type**

    int



### `app_secret`

机器人的 appSecret。


* **Type**

    str
