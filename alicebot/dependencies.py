"""AliceBot 依赖注入。

实现依赖注入相关功能。
"""

import inspect
from collections.abc import AsyncGenerator, Callable, Generator
from contextlib import (
    AbstractAsyncContextManager,
    AbstractContextManager,
    AsyncExitStack,
    asynccontextmanager,
    contextmanager,
)
from typing import Any, TypeVar, cast, get_type_hints
from typing_extensions import override

from typing_inspection.introspection import (
    UNKNOWN,
    AnnotationSource,
    inspect_annotation,
)

from alicebot.utils import sync_ctx_manager_wrapper

_T = TypeVar("_T")
Dependency = (
    # Class
    type[_T | AbstractAsyncContextManager[_T] | AbstractContextManager[_T]]
    # GeneratorContextManager
    | Callable[[], AsyncGenerator[_T, None]]
    | Callable[[], Generator[_T, None, None]]
)


__all__ = ["Depends"]


class _InnerDepends:
    """子依赖的内部实现。

    Attributes:
        dependency: 依赖类。如果不指定则根据字段的类型注释自动判断。
        use_cache: 是否使用缓存。默认为 `True`。
    """

    dependency: Dependency[Any] | None
    use_cache: bool

    def __init__(
        self, dependency: Dependency[Any] | None = None, *, use_cache: bool = True
    ) -> None:
        self.dependency = dependency
        self.use_cache = use_cache

    @override
    def __repr__(self) -> str:
        attr = getattr(self.dependency, "__name__", type(self.dependency).__name__)
        cache = "" if self.use_cache else ", use_cache=False"
        return f"InnerDepends({attr}{cache})"


def Depends(  # noqa: N802 # pylint: disable=invalid-name
    dependency: Dependency[_T] | None = None, *, use_cache: bool = True
) -> _T:
    """子依赖装饰器。

    Args:
        dependency: 依赖类。如果不指定则根据字段的类型注释自动判断。
        use_cache: 是否使用缓存。默认为 `True`。

    Returns:
        返回内部子依赖对象。
    """
    return _InnerDepends(dependency=dependency, use_cache=use_cache)  # type: ignore


async def solve_dependencies(
    dependent: Dependency[_T],
    *,
    use_cache: bool,
    stack: AsyncExitStack,
    dependency_cache: dict[Dependency[Any], Any],
) -> _T:
    """解析子依赖。

    Args:
        dependent: 依赖类。
        use_cache: 是否使用缓存。
        stack: `AsyncExitStack` 对象。
        dependency_cache: 依赖缓存。

    Raises:
        TypeError: 解析错误。

    Returns:
        解析完成子依赖的对象。
    """
    if use_cache and dependent in dependency_cache:
        return dependency_cache[dependent]

    if isinstance(dependent, type):
        # type of dependent is Type[T]
        values: dict[str, Any] = {}
        ann = get_type_hints(dependent)
        for name, sub_dependent in inspect.getmembers(
            dependent, lambda x: isinstance(x, _InnerDepends)
        ):
            assert isinstance(sub_dependent, _InnerDepends)
            if sub_dependent.dependency is None:
                dependent_ann = ann.get(name)
                if dependent_ann is None:
                    raise TypeError("can not solve dependent")
                inspected_ann = inspect_annotation(
                    dependent_ann,
                    annotation_source=AnnotationSource.CLASS,
                )
                if inspected_ann.type == UNKNOWN:
                    raise TypeError("can not solve dependent")
                sub_dependent.dependency = inspected_ann.type  # type: ignore
            assert sub_dependent.dependency is not None
            values[name] = await solve_dependencies(
                sub_dependent.dependency,
                use_cache=sub_dependent.use_cache,
                stack=stack,
                dependency_cache=dependency_cache,
            )

        depend_obj = cast(
            "_T | AbstractAsyncContextManager[_T] | AbstractContextManager[_T]",
            dependent.__new__(dependent),  # type: ignore
        )
        for key, value in values.items():
            setattr(depend_obj, key, value)
        depend_obj.__init__()  # type: ignore[misc] # pylint: disable=unnecessary-dunder-call

        if isinstance(depend_obj, AbstractAsyncContextManager):
            depend = await stack.enter_async_context(
                cast("AbstractAsyncContextManager[_T]", depend_obj)
            )
        elif isinstance(depend_obj, AbstractContextManager):
            depend = await stack.enter_async_context(
                sync_ctx_manager_wrapper(cast("AbstractContextManager[_T]", depend_obj))
            )
        else:
            depend = depend_obj
    elif inspect.isasyncgenfunction(dependent):
        # type of dependent is Callable[[], AsyncGenerator[T, None]]
        cm = asynccontextmanager(dependent)()
        depend = cast("_T", await stack.enter_async_context(cm))
    elif inspect.isgeneratorfunction(dependent):
        # type of dependent is Callable[[], Generator[T, None, None]]
        cm = sync_ctx_manager_wrapper(contextmanager(dependent)())
        depend = cast("_T", await stack.enter_async_context(cm))
    else:
        raise TypeError("dependent is not a class or generator function")

    dependency_cache[dependent] = depend
    return depend
