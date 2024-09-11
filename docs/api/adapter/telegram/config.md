# alicebot.adapter.telegram.config

Telegram 适配器配置

## _class_ `Config` {#Config}

Bases: `alicebot.config.ConfigModel`

Telegram 适配器配置

- **Attributes**

  - **adapter\_type** (_Literal\['polling', 'webhook'\]_) - 适配器运行模式

  - **bot\_token** (_str_) - 从 `BotFather` 获取的 token 值。
  参考：https://core.telegram.org/bots#how-do-i-create-a-bot

  - **api\_server** (_str_) - 自定义 API 服务器

  - **webhook\_host** (_Optional\[str\]_) - 自定义 Webhook 服务器地址

  - **webhook\_port** (_Optional\[int\]_) - 自定义 Webhook 服务器端口

  - **webhook\_url** (_Optional\[str\]_) - 自定义 Webhook 服务器路径

  - **proxy** (_Optional\[str\]_) - 代理服务器地址，为空时表示不使用代理

  - **api\_timeout** (_int_) - 进行 API 调用时等待返回响应的超时时间。
