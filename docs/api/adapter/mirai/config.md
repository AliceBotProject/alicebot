# alicebot.adapter.mirai.config

Mirai 适配器配置。

## _class_ `Config` {#Config}

Bases: `alicebot.config.ConfigModel`

Mirai 配置类，将在适配器被加载时被混入到机器人主配置中。

- **Attributes**

  - **adapter\_type** (_Literal\['ws', 'reverse-ws'\]_) - 适配器类型，需要和协议端配置相同。

  - **host** (_str_) - 本机域名。

  - **port** (_int_) - 监听的端口。

  - **url** (_str_) - WebSocket 路径，需要和协议端配置相同。

  - **reconnect\_interval** (_int_) - 重连等待时间。

  - **api\_timeout** (_int_) - 进行 API 调用时等待返回响应的超时时间。

  - **verify\_key** (_str_) - 建立连接时的认证密钥，需要和 mirai-api-http 配置中的 `verifyKey` 相同，如果关闭验证则留空。

  - **qq** (_int_) - 机器人的 QQ 号码，必须指定。

### _method_ `__init__(self, /, **data)` {#BaseModel---init--}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_
