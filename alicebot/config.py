"""
======
配置
======
AliceBot 使用 pydantic_ 来读取配置。

.. _pydantic: https://pydantic-docs.helpmanual.io/
"""
from typing import Set, Optional
from contextvars import ContextVar

from pydantic import BaseModel

config_file = 'config.json'


class MainConfig(BaseModel):
    """
    AliceBot 的主要配置。
    """
    plugins: Optional[Set[str]]
    """
    将被加载的插件列表，将依次被 ``Bot`` 类的 ``load_plugin()`` 方法加载。
    
    :type: Optional[Set[str]]
    """
    plugin_dir: Optional[Set[str]]
    """
    将被加载的插件目录列表，将被 ``Bot`` 类的 ``load_plugins_from_dir()`` 方法加载。
    
    :type: Optional[Set[str]]
    """
    adapters: Optional[Set[str]]
    """
    将被加载的适配器列表，将依次被 ``Bot`` 类的 ``load_adapter()`` 方法加载。
    
    :type: Optional[Set[str]]
    """

    dev_env: bool = False
    """
    当前是否处于开发环境，默认为 false，在使用时请勿设置为 true。
    
    :type: bool
    """

    class Config:
        extra = 'allow'


config = ContextVar('config', default=None)
