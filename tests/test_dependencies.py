from contextlib import AsyncExitStack
from types import TracebackType
from typing import AsyncGenerator, Generator, Optional, Type
from typing_extensions import Self

import pytest

from alicebot.dependencies import Depends, solve_dependencies


def test_repr_inner_depends() -> None:
    from alicebot import Bot

    assert repr(Depends()) == "InnerDepends(NoneType)"
    assert repr(Depends(use_cache=False)) == "InnerDepends(NoneType, use_cache=False)"
    assert repr(Depends(Bot)) == "InnerDepends(Bot)"


@pytest.mark.asyncio()
async def test_depends() -> None:
    class DepA: ...

    class DepB: ...

    class Dependent:
        a: DepA = Depends()
        b: DepB = Depends()

    obj = None

    async with AsyncExitStack() as stack:
        obj = await solve_dependencies(
            Dependent,
            use_cache=True,
            stack=stack,
            dependency_cache={},
        )

    assert obj is not None
    assert isinstance(obj.a, DepA)
    assert isinstance(obj.b, DepB)


@pytest.mark.asyncio()
async def test_sub_depends() -> None:
    class DepA: ...

    class DepB:
        a: DepA = Depends()

    class Dependent:
        a: DepA = Depends()
        b: DepB = Depends()

    obj = None

    async with AsyncExitStack() as stack:
        obj = await solve_dependencies(
            Dependent,
            use_cache=True,
            stack=stack,
            dependency_cache={},
        )

    assert obj is not None
    assert isinstance(obj.a, DepA)
    assert isinstance(obj.b, DepB)
    assert obj.b.a is obj.a


@pytest.mark.asyncio()
async def test_depends_context_manager() -> None:
    enter_flag = False
    exit_flag = False

    class DepA:
        def __enter__(self) -> Self:
            nonlocal enter_flag
            enter_flag = True
            return self

        def __exit__(
            self,
            __exc_type: Optional[Type[BaseException]],
            __exc_value: Optional[BaseException],
            __traceback: Optional[TracebackType],
        ) -> None:
            nonlocal exit_flag
            exit_flag = True

    class DepB:
        a: DepA = Depends()

    class Dependent:
        a: DepA = Depends()
        b: DepB = Depends()

    obj = None

    async with AsyncExitStack() as stack:
        obj = await solve_dependencies(
            Dependent,
            use_cache=True,
            stack=stack,
            dependency_cache={},
        )

    assert obj is not None
    assert isinstance(obj.a, DepA)
    assert isinstance(obj.b, DepB)
    assert obj.b.a is obj.a


@pytest.mark.asyncio()
async def test_depends_async_context_manager() -> None:
    enter_flag = False
    exit_flag = False

    class DepA:
        async def __aenter__(self) -> Self:
            nonlocal enter_flag
            enter_flag = True
            return self

        async def __aexit__(
            self,
            __exc_type: Optional[Type[BaseException]],
            __exc_value: Optional[BaseException],
            __traceback: Optional[TracebackType],
        ) -> None:
            nonlocal exit_flag
            exit_flag = True

    class DepB:
        a: DepA = Depends()

    class Dependent:
        a: DepA = Depends()
        b: DepB = Depends()

    obj = None

    async with AsyncExitStack() as stack:
        obj = await solve_dependencies(
            Dependent,
            use_cache=True,
            stack=stack,
            dependency_cache={},
        )

    assert obj is not None
    assert isinstance(obj.a, DepA)
    assert isinstance(obj.b, DepB)
    assert obj.b.a is obj.a

    assert enter_flag
    assert exit_flag


@pytest.mark.asyncio()
async def test_depends_generator() -> None:
    enter_flag = False
    exit_flag = False

    class DepA: ...

    def dep_a() -> Generator[DepA, None, None]:
        nonlocal enter_flag, exit_flag
        enter_flag = True
        yield DepA()
        exit_flag = True

    class DepB:
        a = Depends(dep_a)

    class Dependent:
        a = Depends(dep_a)
        b: DepB = Depends()

    obj = None

    async with AsyncExitStack() as stack:
        obj = await solve_dependencies(
            Dependent,
            use_cache=True,
            stack=stack,
            dependency_cache={},
        )

    assert obj is not None
    assert isinstance(obj.a, DepA)
    assert isinstance(obj.b, DepB)
    assert obj.b.a is obj.a

    assert enter_flag
    assert exit_flag


@pytest.mark.asyncio()
async def test_depends_async_generator() -> None:
    enter_flag = False
    exit_flag = False

    class DepA: ...

    async def dep_a() -> AsyncGenerator[DepA, None]:
        nonlocal enter_flag, exit_flag
        enter_flag = True
        yield DepA()
        exit_flag = True

    class DepB:
        a = Depends(dep_a)

    class Dependent:
        a = Depends(dep_a)
        b: DepB = Depends()

    obj = None

    async with AsyncExitStack() as stack:
        obj = await solve_dependencies(
            Dependent,
            use_cache=True,
            stack=stack,
            dependency_cache={},
        )

    assert obj is not None
    assert isinstance(obj.a, DepA)
    assert isinstance(obj.b, DepB)
    assert obj.b.a is obj.a

    assert enter_flag
    assert exit_flag


@pytest.mark.asyncio()
async def test_depends_solve_error() -> None:
    class Dependent:
        a = Depends()  # type: ignore

    with pytest.raises(TypeError):
        async with AsyncExitStack() as stack:
            await solve_dependencies(
                Dependent,
                use_cache=True,
                stack=stack,
                dependency_cache={},
            )


@pytest.mark.asyncio()
async def test_depends_type_error() -> None:
    class Dependent:
        a = Depends(1)  # type: ignore

    with pytest.raises(TypeError):
        async with AsyncExitStack() as stack:
            await solve_dependencies(
                Dependent,
                use_cache=True,
                stack=stack,
                dependency_cache={},
            )
