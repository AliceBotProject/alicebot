import os
import json
import asyncio
import inspect
import os.path
import importlib
import traceback
import dataclasses
from abc import ABC
from types import ModuleType
from functools import partial
from importlib.abc import MetaPathFinder
from importlib.machinery import PathFinder
from typing_extensions import ParamSpec, TypeGuard
from typing import (
    TYPE_CHECKING,
    Any,
    List,
    Type,
    Tuple,
    Union,
    TypeVar,
    Callable,
    Optional,
    Sequence,
    Awaitable,
    Coroutine,
)

from alicebot.config import ConfigModel

if TYPE_CHECKING:
    from alicebot.event import Event

__all__ = [
    "ModulePathFinder",
    "is_config_class",
    "get_classes_from_module",
    "get_classes_from_module_name",
    "DataclassEncoder",
    "samefile",
    "sync_func_wrapper",
    "wrap_get_func",
]

_T = TypeVar("_T")
_P = ParamSpec("_P")
_R = TypeVar("_R")


class ModulePathFinder(MetaPathFinder):
    """用于查找 AliceBot 组件的元路径查找器。"""

    path: List[str] = []

    def find_spec(
        self,
        fullname: str,
        path: Optional[Sequence[str]] = None,
        target: Optional[ModuleType] = None,
    ):
        if path is None:
            path = []
        return PathFinder.find_spec(fullname, self.path + list(path), target)


def is_config_class(config_class: Any) -> TypeGuard[Type[ConfigModel]]:
    """判断一个对象是否是配置类。

    Args:
        config_class: 待判断的对象。

    Returns:
        返回是否是配置类。
    """
    return (
        inspect.isclass(config_class)
        and issubclass(config_class, ConfigModel)
        and isinstance(getattr(config_class, "__config_name__", None), str)
        and ABC not in config_class.__bases__
        and not inspect.isabstract(config_class)
    )


def get_classes_from_module(
    module: ModuleType, super_class: Type[_T]
) -> List[Type[_T]]:
    """从模块中查找指定类型的类。

    Args:
        module: Python 模块。
        super_class: 要查找的类的超类。

    Returns:
        返回符合条件的类的列表。
    """
    classes: List[Type[_T]] = []
    for _, module_attr in inspect.getmembers(module, inspect.isclass):
        module_attr: type
        if (
            (inspect.getmodule(module_attr) or module) is module
            and issubclass(module_attr, super_class)
            and module_attr != super_class
            and ABC not in module_attr.__bases__
            and not inspect.isabstract(module_attr)
        ):
            classes.append(module_attr)
    return classes


def get_classes_from_module_name(
    name: str, super_class: Type[_T]
) -> List[Tuple[Type[_T], ModuleType]]:
    """从指定名称的模块中查找指定类型的类。

    Args:
        name: 模块名称，格式和 Python `import` 语句相同。
        super_class: 要查找的类的超类。

    Returns:
        返回由符合条件的类和模块组成的元组的列表。

    Raises:
        ImportError: 当导入模块过程中出现错误。
    """
    try:
        importlib.invalidate_caches()
        module = importlib.import_module(name)
        importlib.reload(module)
        return list(
            map(lambda x: (x, module), get_classes_from_module(module, super_class))
        )
    except BaseException as e:
        # 不捕获 KeyboardInterrupt
        # 捕获 KeyboardInterrupt 会阻止用户关闭 Python 当正在导入的模块陷入死循环时
        if isinstance(e, KeyboardInterrupt):
            raise e
        raise ImportError(e, traceback.format_exc()) from e


class DataclassEncoder(json.JSONEncoder):
    """用于解析 MessageSegment 的 JSONEncoder 类。"""

    def default(self, o: Any):
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


def sync_func_wrapper(
    func: Callable[_P, _R], to_thread: bool = False
) -> Callable[_P, Coroutine[None, None, _R]]:
    """包装一个同步函数为异步函数，当 func 为

    Args:
        func: 待包装的同步函数。
        to_thread: 在独立的线程中运行同步函数。

    Returns:
        异步函数。
    """
    if to_thread:

        async def _wrapper(*args: _P.args, **kwargs: _P.kwargs):
            loop = asyncio.get_running_loop()
            func_call = partial(func, *args, **kwargs)
            return await loop.run_in_executor(None, func_call)

    else:

        async def _wrapper(*args: _P.args, **kwargs: _P.kwargs):
            return func(*args, **kwargs)

    return _wrapper


def wrap_get_func(
    func: Optional[Callable[["Event"], Union[bool, Awaitable[bool]]]]
) -> Callable[["Event"], Awaitable[bool]]:
    """将 `get()` 函数接受的参数包装为一个异步函数。

    Args:
        func: `get()` 函数接受的参数。

    Returns:
        异步函数。
    """
    if func is None:
        return sync_func_wrapper(lambda _: True)
    elif not asyncio.iscoroutinefunction(func):
        return sync_func_wrapper(func)  # type: ignore
    else:
        return func
