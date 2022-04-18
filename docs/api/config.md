# alicebot.config

AliceBot 配置。

AliceBot 使用 [pydantic](https://pydantic-docs.helpmanual.io/) 来读取配置。

## *class* `MainConfig`(__pydantic_self__, **data) {#MainConfig}

Bases: `pydantic.main.BaseModel`

AliceBot 的主要配置。

- **Attributes**

  - **plugins** (*Optional[Set[str]]*) - 将被加载的插件列表，将依次被 `Bot` 类的 `load_plugin()` 方法加载。

  - **plugin_dir** (*Optional[Set[str]]*) - 将被加载的插件目录列表，将被 `Bot` 类的 `load_plugins_from_dir()` 方法加载。

  - **adapters** (*Optional[Set[str]]*) - 将被加载的适配器列表，将依次被 `Bot` 类的 `load_adapter()` 方法加载。

### *class* `Config`(self, /, *args, **kwargs) {#MainConfig.Config}

Bases: `object`