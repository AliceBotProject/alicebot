import json
import asyncio
import inspect
import pkgutil
import importlib
import collections
import dataclasses
from abc import ABC
from importlib.abc import MetaPathFinder
from importlib.machinery import PathFinder
from typing import (
    TYPE_CHECKING,
    List,
    Type,
    Tuple,
    Union,
    Generic,
    TypeVar,
    Callable,
    Iterable,
    Optional,
)

from pydantic import BaseModel

from alicebot.exceptions import LoadModuleError

if TYPE_CHECKING:
    from pkgutil import ModuleInfo

__all__ = [
    "Condition",
    "ModulePathFinder",
    "load_module",
    "load_modules_from_dir",
    "DataclassEncoder",
]

_T = TypeVar("_T")


class Condition(Generic[_T]):
    """类似于 asyncio.Condition ，但允许在 notify() 时传递值，并由 wait() 返回。"""

    def __init__(self):
        self._loop = asyncio.get_running_loop()
        lock = asyncio.Lock()
        self._lock = lock
        # Export the lock's locked(), acquire() and release() methods.
        self.locked = lock.locked
        self.acquire = lock.acquire
        self.release = lock.release

        self._waiters = collections.deque()

    async def __aenter__(self):
        await self.acquire()
        # We have no use for the "as ..."  clause in the with
        # statement for locks.
        return None

    async def __aexit__(self, exc_type, exc, tb):
        self.release()

    def __repr__(self):
        res = super().__repr__()
        extra = "locked" if self.locked() else "unlocked"
        if self._waiters:
            extra = f"{extra}, waiters:{len(self._waiters)}"
        return f"<{res[1:-1]} [{extra}]>"

    async def wait(self) -> _T:
        if not self.locked():
            raise RuntimeError("cannot wait on un-acquired lock")

        self.release()
        try:
            fut = self._loop.create_future()
            self._waiters.append(fut)
            try:
                return await fut
            finally:
                self._waiters.remove(fut)

        finally:
            # Must reacquire lock even if wait is cancelled
            cancelled = False
            while True:
                try:
                    await self.acquire()
                    break
                except asyncio.CancelledError:
                    cancelled = True

            if cancelled:
                raise asyncio.CancelledError

    async def wait_for(self, predicate: Callable[..., bool]) -> bool:
        result = predicate()
        while not result:
            await self.wait()
            result = predicate()
        return result

    def notify(self, value: _T = None, n: int = 1):
        if not self.locked():
            raise RuntimeError("cannot notify on un-acquired lock")

        idx = 0
        for fut in self._waiters:
            if idx >= n:
                break

            if not fut.done():
                idx += 1
                fut.set_result(value)

    def notify_all(self, value: _T = None):
        self.notify(value, len(self._waiters))


class ModulePathFinder(MetaPathFinder):
    """用于查找 AliceBot 组件的元路径查找器。"""

    path: List[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if path is None:
            path = []
        return PathFinder.find_spec(fullname, self.path + list(path), target)


def load_module(
    name: str,
    module_class_type: Type[_T],
    try_instantiate_class: bool = False,
    *args,
    **kwargs,
) -> Tuple[Union[Type[_T], _T], Optional[Type[BaseModel]]]:
    """从模块中查找指定类型的类和 `Config` 。若模块中存在多个符合条件的类，则抛出错误。

    Args:
        name: 模块名称，格式和 Python `import` 语句相同。
        module_class_type: 要查找的类型。
        try_instantiate_class: 是否尝试实例化类。
            当为 True 时，查找到指定的类后会尝试使用指定参数示例化类，仅返回成功被实例化的对象。
        *args: 实例化类时使用的参数，仅当 `try_instantiate_class` 为 True 时生效。
        **kwargs: 实例化类时使用的参数，仅当 `try_instantiate_class` 为 True 时生效。

    Returns:
        `(class, config)` 返回符合条件的类和配置类组成的元组。
        当 `try_instantiate_class` 为 True 时，返回 `(object, config)` 。

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
        if (
            inspect.isclass(module_attr)
            and issubclass(module_attr, module_class_type)
            and module_attr != module_class_type
            and ABC not in module_attr.__bases__
        ):
            module_class.append(module_attr)

    if try_instantiate_class:
        module_class = list(
            filter(
                lambda x: not isinstance(x, Exception),
                map(_instantiate_class, module_class),
            )
        )

    if not module_class:
        raise LoadModuleError(
            f"Can not find {module_class_type!r} class in the {name!r} module"
        )
    elif len(module_class) > 1:
        raise LoadModuleError(
            f"More then one {module_class_type!r} class in the {name!r} module"
        )

    if "Config" in dir(module):
        module_attr = getattr(module, "Config")
        if (
            inspect.isclass(module_attr)
            and issubclass(module_attr, BaseModel)
            and "__config_name__" in dir(module_attr)
        ):
            return module_class[0], getattr(module, "Config")
    return module_class[0], None


def load_modules_from_dir(
    _module_path_finder: ModulePathFinder,
    path: Iterable[str],
    module_class_type: Type[_T],
) -> List[Tuple[Type[_T], Optional[Type[BaseModel]], "ModuleInfo"]]:
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
            module_class, config_class = load_module(
                module_info.name, module_class_type
            )
            if not module_info.name.startswith("_"):
                modules.append((module_class, config_class, module_info))
        except LoadModuleError:
            continue
    return modules


class DataclassEncoder(json.JSONEncoder):
    """用于解析 MessageSegment 的 JSONEncoder 类。"""

    def default(self, o):
        if dataclasses.is_dataclass(o):
            return o.as_dict()
        return super().default(o)
