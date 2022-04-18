import inspect
import pkgutil
import importlib
from abc import ABC
from importlib.abc import MetaPathFinder
from typing import Iterable, List, Tuple, Type, TypeVar, Optional, Union, TYPE_CHECKING
from importlib.machinery import PathFinder

from pydantic import BaseModel

from alicebot.exceptions import LoadModuleError

if TYPE_CHECKING:
    from pkgutil import ModuleInfo

_T = TypeVar('_T')


class ModulePathFinder(MetaPathFinder):
    """用于查找 AliceBot 组件的元路径查找器。"""
    path: List[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if path is None:
            path = []
        return PathFinder.find_spec(fullname, self.path + list(path), target)


def load_module(name: str,
                module_class_type: Type[_T],
                try_instantiate_class: bool = False,
                *args, **kwargs) -> Tuple[Union[Type[_T], _T], Optional[Type[BaseModel]]]:
    """从模块中查找指定类型的类和 `Config` 。若模块中存在多个符合条件的类，则抛出错误。

    Args:
        name: 模块名称，格式和 Python `import` 语句相同。
        module_class_type: 要查找的类型。
        try_instantiate_class: 是否尝试实例化类，当为 True 时，查找到指定的类后会尝试使用指定参数示例化类，仅返回成功被实例化的对象。
        *args: 实例化类时使用的参数，仅当 `try_instantiate_class` 为 True 时生效。
        **kwargs: 实例化类时使用的参数，仅当 `try_instantiate_class` 为 True 时生效。

    Returns:
        `(class, config)` 返回符合条件的类和配置类组成的元组，当 `try_instantiate_class` 为 True 时，返回 `(object, config)` 。

    Raises:
        LoadModuleError: 当找不到符合条件的类或者模块中存在多个符合条件的类。
    """

    def _instantiate_class(_module_class: type) -> Union[_T, Exception]:
        try:
            return _module_class(*args, **kwargs)
        except Exception as e:
            return e

    importlib.invalidate_caches()
    module = importlib.import_module(name)
    module_class = []
    for module_attr in dir(module):
        module_attr = getattr(module, module_attr)
        if inspect.isclass(module_attr) and \
                issubclass(module_attr, module_class_type) and \
                module_attr != module_class_type and \
                ABC not in module_attr.__bases__:
            module_class.append(module_attr)

    if try_instantiate_class:
        module_class = list(filter(lambda x: not isinstance(x, Exception), map(_instantiate_class, module_class)))

    if not module_class:
        raise LoadModuleError(f'Can not find {module_class_type!r} class in the {name!r} module')
    elif len(module_class) > 1:
        raise LoadModuleError(f'More then one {module_class_type!r} class in the {name!r} module')

    if 'Config' in dir(module):
        module_attr = getattr(module, 'Config')
        if inspect.isclass(module_attr) and issubclass(module_attr, BaseModel) and '__config_name__' in dir(
                module_attr):
            return module_class[0], getattr(module, 'Config')
    return module_class[0], None


def load_modules_from_dir(
        _module_path_finder: ModulePathFinder,
        path: Iterable[str],
        module_class_type: Type[_T]) -> List[Tuple[Type[_T], Optional[Type[BaseModel]], 'ModuleInfo']]:
    """从指定路径列表中的所有模块中查找指定类型的类和 `Config` ，以 `_` 开头的插件不会被导入。路径可以是相对路径或绝对路径。

    Args:
        _module_path_finder: 用于查找 AliceBot 组件的元路径查找器。
        path: 由储存模块的路径文本组成的列表。 例如 `['path/of/plugins/', '/home/xxx/alicebot/plugins']` 。
        module_class_type: 要查找的类型。

    Returns:
        `[(class, config, module_info), ...]` 返回由符合条件的类、配置类和 `ModuleInfo` 组成的元组组成的列表。
    """
    modules = []
    _module_path_finder.path = list(path)
    for module_info in pkgutil.iter_modules(path):
        try:
            module_class, config_class = load_module(module_info.name, module_class_type)
            if not module_info.name.startswith('_'):
                modules.append((module_class, config_class, module_info))
        except LoadModuleError:
            continue
    return modules
