from collections.abc import AsyncGenerator, Generator
from contextlib import AsyncExitStack
from types import TracebackType
from typing import Optional
from typing_extensions import Self

import pytest
from pytest_mock import MockerFixture

from alicebot.dependencies import Depends, solve_dependencies


def test_repr_inner_depends() -> None:
    from alicebot import Bot

    assert repr(Depends()) == "InnerDepends(NoneType)"
    assert repr(Depends(use_cache=False)) == "InnerDepends(NoneType, use_cache=False)"
    assert repr(Depends(Bot)) == "InnerDepends(Bot)"


@pytest.mark.anyio
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


@pytest.mark.anyio
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


@pytest.mark.anyio
async def test_depends_context_manager(mocker: MockerFixture) -> None:
    class DepA:
        def __enter__(self) -> Self:
            return self

        def __exit__(
            self,
            _exc_type: Optional[type[BaseException]],
            _exc_value: Optional[BaseException],
            _traceback: Optional[TracebackType],
        ) -> None:
            pass

    class DepB:
        a: DepA = Depends()

    class Dependent:
        a: DepA = Depends()
        b: DepB = Depends()

    enter_spy = mocker.spy(DepA, "__enter__")
    exit_spy = mocker.spy(DepA, "__exit__")

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
    enter_spy.assert_called_once()
    exit_spy.assert_called_once()


@pytest.mark.anyio
async def test_depends_async_context_manager(mocker: MockerFixture) -> None:
    class DepA:
        async def __aenter__(self) -> Self:
            return self

        async def __aexit__(
            self,
            _exc_type: Optional[type[BaseException]],
            _exc_value: Optional[BaseException],
            _traceback: Optional[TracebackType],
        ) -> None:
            pass

    class DepB:
        a: DepA = Depends()

    class Dependent:
        a: DepA = Depends()
        b: DepB = Depends()

    aenter_spy = mocker.spy(DepA, "__aenter__")
    aexit_spy = mocker.spy(DepA, "__aexit__")

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
    aenter_spy.assert_called_once()
    aexit_spy.assert_called_once()


@pytest.mark.anyio
async def test_depends_generator(mocker: MockerFixture) -> None:
    mock = mocker.MagicMock()

    class DepA: ...

    def dep_a() -> Generator[DepA, None, None]:
        mock("enter")
        yield DepA()
        mock("exit")

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
    assert mock.call_args_list == [mocker.call("enter"), mocker.call("exit")]


@pytest.mark.anyio
async def test_depends_async_generator(mocker: MockerFixture) -> None:
    mock = mocker.AsyncMock()

    class DepA: ...

    async def dep_a() -> AsyncGenerator[DepA, None]:
        await mock("enter")
        yield DepA()
        await mock("exit")

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
    assert mock.call_args_list == [mocker.call("enter"), mocker.call("exit")]


@pytest.mark.anyio
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


@pytest.mark.anyio
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
