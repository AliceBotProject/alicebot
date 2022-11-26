"""AliceBot 配置。

AliceBot 使用 [pydantic](https://pydantic-docs.helpmanual.io/) 来读取配置。
"""
from typing import Set, Union

from pydantic import Extra, Field, BaseModel, DirectoryPath

__all__ = [
    "ConfigModel",
    "LogConfig",
    "BotConfig",
    "PluginConfig",
    "AdapterConfig",
    "MainConfig",
]


class ConfigModel(BaseModel):
    """AliceBot 配置模型。

    Attributes:
        __config_name__: 配置名称。
    """

    __config_name__: str

    class Config:
        extra = Extra.allow


class LogConfig(ConfigModel):
    """AliceBot 日志相关设置。

    Attributes:
        level: 日志级别。
        verbose_exception: 详细的异常记录，设置为 True 时会在日志中添加异常的 Traceback。
    """

    level: Union[str, int] = "DEBUG"
    verbose_exception: bool = False


class BotConfig(ConfigModel):
    """Bot 配置。

    Attributes:
        plugins: 将被加载的插件列表，将被 `Bot` 类的 `load_plugins()` 方法加载。
        plugin_dirs: 将被加载的插件目录列表，将被 `Bot` 类的 `load_plugins_from_dirs()` 方法加载。
        adapters: 将被加载的适配器列表，将依次被 `Bot` 类的 `load_adapters()` 方法加载。
        log: AliceBot 日志相关设置。
    """

    plugins: Set[str] = Field(default_factory=set)
    plugin_dirs: Set[DirectoryPath] = Field(default_factory=set)
    adapters: Set[str] = Field(default_factory=set)
    log: LogConfig = LogConfig()


class PluginConfig(ConfigModel):
    """插件配置。"""


class AdapterConfig(ConfigModel):
    """适配器配置。"""


class MainConfig(ConfigModel):
    """AliceBot 配置。

    Attributes:
        bot: AliceBot 的主要配置。
    """

    bot: BotConfig = BotConfig()
    plugin: PluginConfig = PluginConfig()
    adapter: AdapterConfig = AdapterConfig()

    class Config:
        extra = Extra.allow
