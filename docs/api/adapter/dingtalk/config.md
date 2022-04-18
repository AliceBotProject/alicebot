# alicebot.adapter.dingtalk.config

DingTalk 适配器配置。

## *class* `Config`(__pydantic_self__, **data) {#Config}

Bases: `pydantic.main.BaseModel`

DingTalk 配置类，将在适配器被加载时被混入到机器人主配置中。

- **Attributes**

  - **host** (*str*) - 本机域名。

  - **port** (*int*) - 监听的端口。

  - **url** (*str*) - 路径。

  - **api_timeout** (*int*) - 进行 API 调用时等待返回响应的超时时间。

  - **app_secret** (*str*) - 机器人的 appSecret。

  - **__config_name__** - 配置名称。