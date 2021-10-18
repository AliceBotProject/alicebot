# alicebot.config

## 配置

AliceBot 使用 [pydantic](https://pydantic-docs.helpmanual.io/) 来读取配置。


## _class_ `MainConfig`

基类：`pydantic.main.BaseModel`

AliceBot 的主要配置。


### `plugins`

将被加载的插件列表，将依次被 `Bot` 类的 `load_plugin()` 方法加载。


* **Type**

    Optional[Set[str]]



### `plugin_dir`

将被加载的插件目录列表，将被 `Bot` 类的 `load_plugins_from_dir()` 方法加载。


* **Type**

    Optional[Set[str]]



### `adapters`

将被加载的适配器列表，将依次被 `Bot` 类的 `load_adapter()` 方法加载。


* **Type**

    Optional[Set[str]]
