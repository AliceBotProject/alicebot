"""AliceBot 依赖注入。

实现依赖注入相关功能。
"""
import asyncio
import inspect
from typing import Any, Dict, Type, Union, TypeVar, Callable, Optional, Coroutine, cast

from alicebot.event import Event
from alicebot.utils import get_annotations, sync_func_wrapper

T = TypeVar("T")
T_Dependency = Union[Type[T], Callable[..., T], Callable[..., Coroutine[None, None, T]]]


__all__ = ["Depends"]


class InnerDepends:
    """子依赖的内部实现。

    用户无需关注此内部实现。

    Attributes:
        dependency: 依赖类。如果不指定则根据字段的类型注释自动判断。
        use_cache: 是否使用缓存。默认为 `True`。
    """

    dependency: Optional[T_Dependency[Any]]
    use_cache: bool

    def __init__(
        self, dependency: Optional[T_Dependency[Any]] = None, *, use_cache: bool = True
    ):
        self.dependency = dependency
        self.use_cache = use_cache

    def __repr__(self) -> str:
        attr = getattr(self.dependency, "__name__", type(self.dependency).__name__)
        cache = "" if self.use_cache else ", use_cache=False"
        return f"InnerDepends({attr}{cache})"


def Depends(
    dependency: Optional[T_Dependency[T]] = None, *, use_cache: bool = True
) -> T:
    """子依赖装饰器。

    Args:
        dependency: 依赖类。如果不指定则根据字段的类型注释自动判断。
        use_cache: 是否使用缓存。默认为 `True`。

    Returns:
        返回内部子依赖对象。
    """
    return InnerDepends(dependency=dependency, use_cache=use_cache)  # type: ignore


async def solve_dependencies(
    dependent: T_Dependency[T],
    *,
    event: Event,
    use_cache: bool = True,
    dependency_cache: Optional[Dict[T_Dependency[Any], Any]] = None,
) -> T:
    """解析子依赖。

    Args:
        dependent: 依赖类。
        use_cache: 是否使用缓存。默认为 `True`。
        dependency_cache: 依赖缓存。默认为 `None`。

    Raises:
        TypeError: 解析错误。

    Returns:
        解析完成子依赖的对象。
    """
    dependency_cache = {} if dependency_cache is None else dependency_cache

    # 对于 Event 的特殊处理
    if isinstance(dependent, type) and issubclass(event.__class__, dependent):
        return cast(T, event)

    # 使用缓存
    if use_cache and dependent in dependency_cache:
        return dependency_cache[dependent]

    if isinstance(dependent, type):
        values = {}
        ann = get_annotations(dependent)
        for name, sub_dependent in inspect.getmembers(
            dependent, lambda x: isinstance(x, InnerDepends)
        ):
            assert isinstance(sub_dependent, InnerDepends)
            if sub_dependent.dependency is None:
                dependent_ann = ann.get(name, None)
                if dependent_ann is None:
                    raise TypeError("can not solve dependent")
                else:
                    sub_dependent.dependency = dependent_ann
            values[name] = await solve_dependencies(
                sub_dependent.dependency,
                event=event,
                use_cache=sub_dependent.use_cache,
                dependency_cache=dependency_cache,
            )
        depend = cast(T, dependent.__new__(dependent))  # type: ignore
        for key, value in values.items():
            setattr(depend, key, value)
        depend.__init__()
    elif callable(dependent):
        if asyncio.iscoroutinefunction(dependent):
            depend = cast(T, await dependent())
        else:
            depend = cast(T, await sync_func_wrapper(dependent)())
    else:
        raise TypeError("dependent is not callable")

    dependency_cache[dependent] = depend
    return depend
