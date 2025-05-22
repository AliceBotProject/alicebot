"""AliceBot 内部使用的实用工具。"""

import importlib
import inspect
import json
import os
import os.path
import sys
import traceback
from abc import ABC
from collections.abc import AsyncGenerator, Awaitable, Iterable, Sequence
from contextlib import AbstractContextManager, asynccontextmanager
from importlib.abc import MetaPathFinder
from importlib.machinery import ModuleSpec, PathFinder
from os import PathLike
from types import GetSetDescriptorType, ModuleType
from typing import Any, Callable, ClassVar, Optional, TypeVar, Union, cast
from typing_extensions import TypeAlias, TypeIs, override

import anyio
import anyio.to_thread
from anyio.abc import TaskGroup
from pydantic import BaseModel

from alicebot.config import ConfigModel

__all__ = [
    "ModulePathFinder",
    "PydanticEncoder",
    "async_map",
    "get_annotations",
    "get_classes_from_module",
    "get_classes_from_module_name",
    "is_config_class",
    "samefile",
    "sync_ctx_manager_wrapper",
]

_T = TypeVar("_T")
_R = TypeVar("_R")
_TypeT = TypeVar("_TypeT", bound=type[Any])

StrOrBytesPath: TypeAlias = Union[str, bytes, PathLike[str], PathLike[bytes]]


class ModulePathFinder(MetaPathFinder):
    """用于查找 AliceBot 组件的元路径查找器。"""

    path: ClassVar[list[str]] = []

    @override
    def find_spec(
        self,
        fullname: str,
        path: Optional[Sequence[str]] = None,
        target: Optional[ModuleType] = None,
    ) -> Union[ModuleSpec, None]:
        """用于查找指定模块的 `spec`。"""
        if path is None:
            path = []
        return PathFinder.find_spec(fullname, self.path + list(path), target)


def is_config_class(config_class: Any) -> TypeIs[type[ConfigModel]]:
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


def get_classes_from_module(module: ModuleType, super_class: _TypeT) -> list[_TypeT]:
    """从模块中查找指定类型的类。

    Args:
        module: Python 模块。
        super_class: 要查找的类的超类。

    Returns:
        返回符合条件的类的列表。
    """
    classes: list[_TypeT] = []
    for _, module_attr in inspect.getmembers(module, inspect.isclass):
        if (
            (inspect.getmodule(module_attr) or module) is module
            and issubclass(module_attr, super_class)
            and module_attr != super_class
            and ABC not in module_attr.__bases__
            and not inspect.isabstract(module_attr)
        ):
            classes.append(cast("_TypeT", module_attr))
    return classes


def get_classes_from_module_name(
    name: str, super_class: _TypeT, *, reload: bool = False
) -> list[tuple[_TypeT, ModuleType]]:
    """从指定名称的模块中查找指定类型的类。

    Args:
        name: 模块名称，格式和 Python `import` 语句相同。
        super_class: 要查找的类的超类。
        reload: 是否重新加载模块。

    Returns:
        返回由符合条件的类和模块组成的元组的列表。

    Raises:
        ImportError: 当导入模块过程中出现错误。
    """
    try:
        importlib.invalidate_caches()
        module = importlib.import_module(name)
        if reload:
            importlib.reload(module)
        return [(x, module) for x in get_classes_from_module(module, super_class)]
    except KeyboardInterrupt:
        # 不捕获 KeyboardInterrupt
        # 捕获 KeyboardInterrupt 会阻止用户关闭 Python 当正在导入的模块陷入死循环时
        raise
    except BaseException as e:
        raise ImportError(e, traceback.format_exc()) from e


class PydanticEncoder(json.JSONEncoder):
    """用于解析 `pydantic.BaseModel` 的 `JSONEncoder` 类。"""

    @override
    def default(self, o: Any) -> Any:
        if isinstance(o, BaseModel):
            return o.model_dump(mode="json")
        return super().default(o)


def samefile(path1: StrOrBytesPath, path2: StrOrBytesPath) -> bool:
    """一个 `os.path.samefile` 的简单包装。

    Args:
        path1: 路径 1。
        path2: 路径 2。

    Returns:
        如果两个路径是否指向相同的文件或目录。
    """
    try:
        return path1 == path2 or os.path.samefile(path1, path2)  # noqa: PTH121
    except OSError:
        return False


@asynccontextmanager
async def sync_ctx_manager_wrapper(
    cm: AbstractContextManager[_T],
) -> AsyncGenerator[_T, None]:
    """将同步上下文管理器包装为异步上下文管理器。

    Args:
        cm: 待包装的同步上下文管理器。
        to_thread: 是否在独立的线程中运行同步函数。默认为 `False`。

    Returns:
        异步上下文管理器。
    """
    try:
        yield await anyio.to_thread.run_sync(cm.__enter__)
    except Exception as e:
        if not await anyio.to_thread.run_sync(cm.__exit__, type(e), e, e.__traceback__):
            raise
    else:
        await anyio.to_thread.run_sync(cm.__exit__, None, None, None)


async def async_map(
    tg: TaskGroup,
    func: Callable[[_T], Awaitable[_R]],
    iterable: Iterable[_T],
) -> AsyncGenerator[tuple[_T, _R]]:
    """在 TaskGroup 中并行运行多个任务并且获取其结果。

    注意：结果将不会按照参数给出的顺序返回，而是按照实际执行结束的顺序返回。
    为了将结果和参数对应起来，这个函数返回的生成器的每一项将是一个由参数和结果组成的元组。

    Args:
        tg: 运行任务的 TaskGroup。
        func: 并行运行的函数。
        iterable: 并行运行的函数的参数。

    Returns:
        由参数和结果组成元组的生成器。
    """
    send_stream, receive_stream = anyio.create_memory_object_stream[tuple[_T, _R]]()

    async def _run_wrapper(item: _T) -> None:
        result = await func(item)
        await send_stream.send((item, result))

    count = 0
    for item in iterable:
        count += 1
        tg.start_soon(_run_wrapper, item)

    for _ in range(count):
        yield await receive_stream.receive()

    await send_stream.aclose()


if sys.version_info >= (3, 10):  # pragma: no cover
    from inspect import get_annotations
else:  # pragma: no cover

    def get_annotations(
        obj: Union[Callable[..., object], type[Any], ModuleType],
    ) -> dict[str, Any]:
        """计算一个对象的标注字典。

        Args:
            obj: 一个可调用对象、类或模块。

        Raises:
            TypeError: `obj` 不是一个可调用对象、类或模块。
            ValueError: 对象的 `__annotations__` 不是一个字典或 `None`。

        Returns:
            对象的标注字典。
        """
        ann: Union[dict[str, Any], None]

        if isinstance(obj, type):
            # class
            obj_dict = getattr(obj, "__dict__", None)
            if obj_dict and hasattr(obj_dict, "get"):
                ann = obj_dict.get("__annotations__")
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
            raise ValueError(  # noqa: TRY004
                f"{obj!r}.__annotations__ is neither a dict nor None"
            )

        if not ann:
            return {}

        return dict(ann)
