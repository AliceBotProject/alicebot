"""AliceBot 内部使用的实用工具。"""
from abc import ABC
import asyncio
from contextlib import asynccontextmanager
from functools import partial
import importlib
from importlib.abc import MetaPathFinder
from importlib.machinery import PathFinder
import inspect
import json
import os
import os.path
import sys
import traceback
from types import GetSetDescriptorType, ModuleType
from typing import (
    Any,
    AsyncGenerator,
    Awaitable,
    Callable,
    ClassVar,
    ContextManager,
    Coroutine,
    Dict,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
)
from typing_extensions import ParamSpec, TypeGuard

from pydantic import BaseModel

from alicebot.config import ConfigModel
from alicebot.typing import T_Event

__all__ = [
    "ModulePathFinder",
    "is_config_class",
    "get_classes_from_module",
    "get_classes_from_module_name",
    "PydanticEncoder",
    "samefile",
    "sync_func_wrapper",
    "sync_ctx_manager_wrapper",
    "wrap_get_func",
    "get_annotations",
]

_T = TypeVar("_T")
_P = ParamSpec("_P")
_R = TypeVar("_R")


class ModulePathFinder(MetaPathFinder):
    """用于查找 AliceBot 组件的元路径查找器。"""

    path: ClassVar[List[str]] = []

    def find_spec(
        self,
        fullname: str,
        path: Optional[Sequence[str]] = None,
        target: Optional[ModuleType] = None,
    ):
        """用于查找指定模块的 `spec`。"""
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
        return [(x, module) for x in get_classes_from_module(module, super_class)]
    except BaseException as e:
        # 不捕获 KeyboardInterrupt
        # 捕获 KeyboardInterrupt 会阻止用户关闭 Python 当正在导入的模块陷入死循环时
        if isinstance(e, KeyboardInterrupt):
            raise e
        raise ImportError(e, traceback.format_exc()) from e


class PydanticEncoder(json.JSONEncoder):
    """用于解析 `pydantic.BaseModel` 的 `JSONEncoder` 类。"""

    def default(self, o: Any) -> Any:
        """返回 `o` 的可序列化对象。"""
        if isinstance(o, BaseModel):
            return o.model_dump(mode="json")
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
    func: Callable[_P, _R], *, to_thread: bool = False
) -> Callable[_P, Coroutine[None, None, _R]]:
    """包装一个同步函数为异步函数。

    Args:
        func: 待包装的同步函数。
        to_thread: 是否在独立的线程中运行同步函数。默认为 `False`。

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


@asynccontextmanager
async def sync_ctx_manager_wrapper(
    cm: ContextManager[_T], *, to_thread: bool = False
) -> AsyncGenerator[_T, None]:
    """将同步上下文管理器包装为异步上下文管理器。

    Args:
        cm: 待包装的同步上下文管理器。
        to_thread: 是否在独立的线程中运行同步函数。默认为 `False`。

    Returns:
        异步上下文管理器。
    """
    try:
        yield await sync_func_wrapper(cm.__enter__, to_thread=to_thread)()
    except Exception as e:
        if not await sync_func_wrapper(cm.__exit__, to_thread=to_thread)(
            type(e), e, e.__traceback__
        ):
            raise e
    else:
        await sync_func_wrapper(cm.__exit__, to_thread=to_thread)(None, None, None)


def wrap_get_func(
    func: Optional[Callable[[T_Event], Union[bool, Awaitable[bool]]]]
) -> Callable[[T_Event], Awaitable[bool]]:
    """将 `get()` 函数接受的参数包装为一个异步函数。

    Args:
        func: `get()` 函数接受的参数。

    Returns:
        异步函数。
    """
    if func is None:
        return sync_func_wrapper(lambda _: True)
    if not asyncio.iscoroutinefunction(func):
        return sync_func_wrapper(func)  # type: ignore
    return func


if sys.version_info >= (3, 10):
    from inspect import get_annotations
else:

    def get_annotations(
        obj: Union[Callable[..., object], Type[Any], ModuleType]
    ) -> Dict[str, Any]:
        """计算一个对象的标注字典。

        Args:
            obj: 一个可调用对象、类或模块。

        Raises:
            TypeError: `obj` 不是一个可调用对象、类或模块。
            ValueError: 对象的 `__annotations__` 不是一个字典或 `None`。

        Returns:
            对象的标注字典。
        """
        if isinstance(obj, type):
            # class
            obj_dict = getattr(obj, "__dict__", None)
            if obj_dict and hasattr(obj_dict, "get"):
                ann = obj_dict.get("__annotations__", None)
                if isinstance(ann, GetSetDescriptorType):
                    ann = None
            else:
                ann = None
        elif isinstance(obj, ModuleType) or callable(obj):
            # this includes types.ModuleType, types.Function, types.BuiltinFunctionType,
            # types.BuiltinMethodType, functools.partial, functools.singledispatch,
            # "class funclike" from Lib/test/test_inspect... on and on it goes.
            ann = getattr(obj, "__annotations__", None)
        else:
            raise TypeError(f"{obj!r} is not a module, class, or callable.")

        if ann is None:
            return {}

        if not isinstance(ann, dict):
            raise ValueError(f"{obj!r}.__annotations__ is neither a dict nor None")

        if not ann:
            return {}

        return dict(ann)
