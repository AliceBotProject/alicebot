# alicebot.config

AliceBot 配置。

AliceBot 使用 [pydantic](https://pydantic-docs.helpmanual.io/) 来读取配置。

## _class_ `ConfigModel` {#ConfigModel}

Bases: `pydantic.main.BaseModel`

AliceBot 配置模型。

- **Attributes**

  - **\_\_config\_name\_\_** - 配置名称。

## _class_ `LogConfig` {#LogConfig}

Bases: `alicebot.config.ConfigModel`

AliceBot 日志相关设置。

- **Attributes**

  - **level** (_Union\[str, int\]_) - 日志级别。

  - **verbose\_exception** (_bool_) - 详细的异常记录，设置为 `True` 时会在日志中添加异常的 Traceback。

## _class_ `BotConfig` {#BotConfig}

Bases: `alicebot.config.ConfigModel`

Bot 配置。

- **Attributes**

  - **plugins** (_Set\[str\]_) - 将被加载的插件列表，将被 `Bot` 类的 `load_plugins()` 方法加载。

  - **plugin\_dirs** (_Set\[Annotated\[pathlib.Path, PathType\(path\_type='dir'\)\]\]_) - 将被加载的插件目录列表，将被 `Bot` 类的 `load_plugins_from_dirs()` 方法加载。

  - **adapters** (_Set\[str\]_) - 将被加载的适配器列表，将依次被 `Bot` 类的 `load_adapters()` 方法加载。

  - **log** (_Optional\[alicebot.config.LogConfig\]_) - AliceBot 日志相关设置。

## _class_ `PluginConfig` {#PluginConfig}

Bases: `alicebot.config.ConfigModel`

插件配置。

## _class_ `AdapterConfig` {#AdapterConfig}

Bases: `alicebot.config.ConfigModel`

适配器配置。

## _class_ `MainConfig` {#MainConfig}

Bases: `alicebot.config.ConfigModel`

AliceBot 配置。

- **Attributes**

  - **bot** (_BotConfig_) - AliceBot 的主要配置。

  - **plugin** (_PluginConfig_)

  - **adapter** (_AdapterConfig_)
