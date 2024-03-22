# alicebot.adapter.dingtalk.config

DingTalk 适配器配置。

## _class_ `Config` {#Config}

Bases: `alicebot.config.ConfigModel`

DingTalk 配置类，将在适配器被加载时被混入到机器人主配置中。

- **Attributes**

  - **host** (_str_) - 本机域名。

  - **port** (_int_) - 监听的端口。

  - **url** (_str_) - 路径。

  - **api\_timeout** (_int_) - 进行 API 调用时等待返回响应的超时时间。

  - **app\_secret** (_str_) - 机器人的 `appSecret`。

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_
