# alicebot.adapter.apscheduler.config

APScheduler 适配器配置。

## _class_ `Config` {#Config}

Bases: `alicebot.config.ConfigModel`

APScheduler 配置类，将在适配器被加载时被混入到机器人主配置中。

- **Attributes**

  - **scheduler\_config** (_Dict\[str, Any\]_) - 调度器配置。

### _method_ `__init__(__pydantic_self__, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`__init__` uses `__pydantic_self__` instead of the more common `self` for the first arg to
allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_
