import os
import json
import inspect
import os.path
import pkgutil
import importlib
import dataclasses
from abc import ABC
from types import ModuleType
from importlib.abc import MetaPathFinder
from importlib.machinery import PathFinder
from typing import List, Type, Generic, TypeVar, Iterable, Optional

from pydantic import BaseModel

from alicebot.exceptions import LoadModuleError

__all__ = [
    "ModulePathFinder",
    "ModuleInfo",
    "load_module",
    "load_module_from_name",
    "load_modules_from_dir",
    "DataclassEncoder",
    "samefile",
    "get_module_name",
]

_T = TypeVar("_T")


class ModulePathFinder(MetaPathFinder):
    """用于查找 AliceBot 组件的元路径查找器。"""

    path: List[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if path is None:
            path = []
        return PathFinder.find_spec(fullname, self.path + list(path), target)


class ModuleInfo(Generic[_T]):
    """模块信息。

    Attributes
        module_class: 模块类。
        config_class: 配置类。
        module: 模块。
    """

    __slots__ = ("module_class", "config_class", "module")

    def __init__(
        self,
        module_class: Type[_T],
        config_class: Optional[Type[BaseModel]],
        module: ModuleType,
    ):
        self.module_class = module_class
        self.config_class = config_class
        self.module = module


def load_module(module: ModuleType, class_type: Type[_T]) -> ModuleInfo[_T]:
    """从模块中查找指定类型的类和 `Config` 。若模块中存在多个符合条件的类，则抛出错误。

    Args:
        module: Python 模块。
        class_type: 要查找的类型。

    Returns:
        返回符合条件的类和配置类组成的元组。

    Raises:
        LoadModuleError: 当找不到符合条件的类或者模块中存在多个符合条件的类。
    """

    module_class: Optional[Type[_T]] = None
    for _, module_attr in inspect.getmembers(module, inspect.isclass):
        module_attr: type
        if (
            (inspect.getmodule(module_attr) or module) is module
            and issubclass(module_attr, class_type)
            and module_attr != class_type
            and ABC not in module_attr.__bases__
            and not inspect.isabstract(module_attr)
        ):
            if module_class is None:
                module_class = module_attr
            else:
                raise LoadModuleError(
                    f"More then one {class_type!r} class "
                    f"in the {module.__name__} module"
                )
    if module_class is None:
        raise LoadModuleError(
            f"Can not find {class_type!r} class in the {module.__name__} module"
        )

    config_class: Optional[Type[BaseModel]] = None
    for name, module_attr in inspect.getmembers(module, inspect.isclass):
        module_attr: type
        if (
            name == "Config"
            and issubclass(module_attr, BaseModel)
            and isinstance(getattr(module_attr, "__config_name__", None), str)
        ):
            config_class = module_attr

    return ModuleInfo(module_class, config_class, module)


def load_module_from_name(name: str, class_type: Type[_T]) -> ModuleInfo[_T]:
    """从模块中查找指定类型的类和 `Config` 。若模块中存在多个符合条件的类，则抛出错误。

    Args:
        name: 模块名称，格式和 Python `import` 语句相同。
        class_type: 要查找的类型。

    Returns:
        返回符合条件的 `ModuleInfo`。

    Raises:
        LoadModuleError: 当找不到符合条件的类或者模块中存在多个符合条件的类。
    """
    importlib.invalidate_caches()
    module = importlib.import_module(name)
    importlib.reload(module)
    return load_module(module, class_type)


def load_modules_from_dir(
    path: Iterable[str], class_type: Type[_T]
) -> List[ModuleInfo[_T]]:
    """从指定路径列表中的所有模块中查找指定类型的类和 `Config` ，以 `_` 开头的插件不会被导入。路径可以是相对路径或绝对路径。

    Args:
        path: 由储存模块的路径文本组成的列表。 例如 `['path/of/plugins/', '/home/xxx/alicebot/plugins']` 。
        class_type: 要查找的类型。

    Returns:
        返回符合条件的 `ModuleInfo` 的列表。
    """
    modules = []
    for module_info in pkgutil.iter_modules(path):
        if not module_info.name.startswith("_"):
            try:
                modules.append(load_module_from_name(module_info.name, class_type))
            except LoadModuleError:
                continue
    return modules


class DataclassEncoder(json.JSONEncoder):
    """用于解析 MessageSegment 的 JSONEncoder 类。"""

    def default(self, o):
        if dataclasses.is_dataclass(o):
            return o.as_dict()
        return super().default(o)


def samefile(path1: str, path2: str) -> bool:
    """一个 `os.path.samefile` 的简单包装。

    Args:
        path1: 路径1。
        path2: 路径2。

    Returns:
        如果两个路径是否指向相同的文件或目录。
    """
    try:
        return path1 == path2 or os.path.samefile(path1, path2)
    except OSError:
        return False


def get_module_name(path: str) -> str:
    """
    从路径中获取合法的 Python 模块名称，与 `inspect.getmodulename()` 函数不同。

    Args:
        path: 路径。

    Returns:
        Python 模块名称。

    Raises:
        ValueError: 当路径不以 ".py" 结尾时。
    """
    basename = os.path.basename(path)
    if not basename.endswith(".py"):
        raise ValueError('path must endswith ".py"')
    if basename == "__init__.py":
        return os.path.basename(os.path.dirname(path))
    return basename[:-3]
