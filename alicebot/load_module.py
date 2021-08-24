import inspect
import pkgutil
import importlib
from importlib.abc import MetaPathFinder
from typing import Iterable, List, Tuple, Type, TypeVar, Optional, TYPE_CHECKING
from importlib.machinery import PathFinder

from pydantic import BaseModel

from alicebot.log import logger
from alicebot.exception import LoadModuleError

if TYPE_CHECKING:
    from pkgutil import ModuleInfo

_T = TypeVar('_T')


class ModulePathFinder(MetaPathFinder):
    """
    用于查找 AliceBot 组件的元路径查找器。
    """
    path: List[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if path is None:
            path = []
        return PathFinder.find_spec(fullname, self.path + path, target)


def load_module(name: str, module_class_type: Type[_T], ) -> Tuple[Type[_T], Optional[Type[BaseModel]]]:
    """
    从模块中查找指定类型的类和 ``Config`` 。
    查找到指定的类后会尝试使用指定参数示例化类，仅返回能被实例化的类。
    若模块中存在多个符合条件的类，则抛出错误。

    :param name: 模块名称，格式和 Python ``import`` 语句相同。
    :param module_class_type: 要查找的类型。
    :return: ``(class, config)`` 返回符合条件的类和配置类组成的元组。
    :rtype: Tuple[Type[_T], Optional[Type[BaseModel]]]
    :exception LoadModuleError: 当找不到符合条件的类或者模块中存在多个符合条件的类。
    """

    importlib.invalidate_caches()
    module = importlib.import_module(name)
    module_class = []
    for module_attr in dir(module):
        module_attr = getattr(module, module_attr)
        if inspect.isclass(module_attr) and \
                issubclass(module_attr, module_class_type) and \
                module_attr != module_class_type:
            module_class.append(module_attr)

    if not module_class:
        logger.error(f'Can not find {module_class_type!r} class in the {name!r} module')
    elif len(module_class) > 1:
        logger.error(f'More then one {module_class_type!r} class in the {name!r} module')
    else:
        if 'Config' in dir(module):
            module_attr = getattr(module, 'Config')
            if inspect.isclass(module_attr) and issubclass(module_attr, BaseModel) and '__config_name__' in dir(
                    module_attr):
                return module_class[0], getattr(module, 'Config')
        return module_class[0], None

    raise LoadModuleError


def load_module_with_instantiate(name: str,
                                 module_class_type: Type[_T],
                                 *args, **kwargs) -> Tuple[Type[_T], Optional[Type[BaseModel]]]:
    """
    从模块中查找指定类型的类和 ``Config`` 。
    查找到指定的类后会尝试使用指定参数示例化类，仅返回能被实例化的类。
    若模块中存在多个符合条件的类，则抛出错误。

    :param name: 模块名称，格式和 Python ``import`` 语句相同。
    :param module_class_type: 要查找的类型。
    :param args: 实例化类时使用的参数。
    :param kwargs: 实例化类时使用的参数。
    :return: ``(class, config)`` 返回符合条件的类和配置类组成的元组。
    :rtype: Tuple[Type[_T], Optional[Type[BaseModel]]]
    :exception LoadModuleError: 当找不到符合条件的类或者模块中存在多个符合条件的类。
    """

    def _is_instantiate_class(_module_class: type):
        try:
            _module_class = _module_class(*args, **kwargs)
        except TypeError:
            return False
        else:
            return True

    importlib.invalidate_caches()
    module = importlib.import_module(name)

    module_class = []
    for module_attr in dir(module):
        module_attr = getattr(module, module_attr)
        if inspect.isclass(module_attr) and issubclass(module_attr, module_class_type):
            module_class.append(module_attr)

    module_class = list(filter(_is_instantiate_class, module_class))

    if not module_class:
        logger.error(f'Can not find {module_class_type!r} class in the {name!r} module')
    elif len(module_class) > 1:
        logger.error(f'More then one {module_class_type!r} class in the {name!r} module')
    else:
        if 'Config' in dir(module):
            module_attr = getattr(module, 'Config')
            if inspect.isclass(module_attr) and issubclass(module_attr, BaseModel) and '__config_name__' in dir(
                    module_attr):
                return module_class[0], getattr(module, 'Config')
        return module_class[0], None

    raise LoadModuleError


def load_modules_from_dir(
        _module_path_finder: ModulePathFinder,
        path: Iterable[str],
        module_class_type: Type[_T]) -> List[Tuple[Type[_T], Optional[Type[BaseModel]], 'ModuleInfo']]:
    """
    从指定路径列表中的所有模块中查找指定类型的类和 ``Config`` ，以 ``_`` 开头的插件不会被导入。
    路径可以是相对路径或绝对路径。

    :param _module_path_finder: 用于查找 AliceBot 组件的元路径查找器。
    :param path: 由储存模块的路径文本组成的列表。 ``['path/of/plugins/', '/home/xxx/alicebot/plugins']``
    :param module_class_type: 要查找的类型。
    :return: ``[(class, config, module_info), ...]`` 返回由符合条件的类、配置类和 ``ModuleInfo`` 组成的元组组成的列表。
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
