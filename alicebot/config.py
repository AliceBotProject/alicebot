"""AliceBot 配置。

AliceBot 使用 [pydantic](https://pydantic-docs.helpmanual.io/) 来读取配置。
"""
from typing import Set, Optional

from pydantic import BaseModel

__all__ = ["MainConfig"]


class MainConfig(BaseModel):
    """AliceBot 的主要配置。

    Attributes:
        plugins: 将被加载的插件列表，将依次被 `Bot` 类的 `load_plugin()` 方法加载。
        plugin_dir: 将被加载的插件目录列表，将被 `Bot` 类的 `load_plugins_from_dir()` 方法加载。
        adapters: 将被加载的适配器列表，将依次被 `Bot` 类的 `load_adapter()` 方法加载。
    """

    plugins: Optional[Set[str]]
    plugin_dir: Optional[Set[str]]
    adapters: Optional[Set[str]]

    class Config:
        extra = "allow"
