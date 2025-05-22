import json
from abc import ABC
from collections.abc import Generator
from contextlib import contextmanager

import get_classes_test_module
import pytest
from get_classes_test_module import SubClass1, SubClass2, SuperClass
from pydantic import BaseModel

from alicebot.config import ConfigModel
from alicebot.utils import (
    get_classes_from_module,
    get_classes_from_module_name,
    is_config_class,
    samefile,
    sync_ctx_manager_wrapper,
)


def test_is_config_class() -> None:
    class ConfigClass(ConfigModel):
        __config_name__ = "test_config_model"

    class NotConfigClass:
        pass

    class AbstractConfigClass(ABC, BaseModel):
        __config_name__ = "test_config_model"

    class PydanticModel(BaseModel):
        __config_name__ = "test_config_model"

    assert is_config_class(ConfigClass)
    assert not is_config_class(NotConfigClass)
    assert not is_config_class(AbstractConfigClass)
    assert not is_config_class(PydanticModel)


def test_get_classes_from_module() -> None:
    classes = get_classes_from_module(get_classes_test_module, SuperClass)
    assert classes == [SubClass1, SubClass2]


def test_get_classes_from_module_name() -> None:
    classes = get_classes_from_module_name(
        "get_classes_test_module", SuperClass, reload=False
    )
    assert len(classes) == 2

    classes = get_classes_from_module_name(
        "get_classes_test_module", SuperClass, reload=True
    )
    assert len(classes) == 0

    with pytest.raises(ImportError):
        classes = get_classes_from_module_name(
            "raise_value_error", SuperClass, reload=False
        )
    with pytest.raises(KeyboardInterrupt):
        classes = get_classes_from_module_name(
            "raise_keyboard_interrupt_error", SuperClass, reload=False
        )


def test_json_encoder_default() -> None:
    from alicebot.utils import PydanticEncoder

    class User(BaseModel):
        id: int
        name: str

    assert (
        json.dumps(User(id=1, name="test"), cls=PydanticEncoder)
        == '{"id": 1, "name": "test"}'
    )

    with pytest.raises(TypeError):
        json.dumps(object, cls=PydanticEncoder)


def test_samefile() -> None:
    file1 = "/path/to/file"
    file2 = "/path/to/another/file"
    assert samefile(__file__, __file__)
    assert samefile(file1, file1)
    assert not samefile(file1, file2)


@pytest.mark.anyio
async def test_sync_ctx_manager_wrapper() -> None:
    @contextmanager
    def sync_context_manager() -> Generator[str, None, None]:
        yield "test"

    @contextmanager
    def error_context_manager() -> Generator[str, None, None]:
        raise TypeError
        yield "test"

    async with sync_ctx_manager_wrapper(sync_context_manager()) as result:
        assert result == "test"

    with pytest.raises(TypeError):
        async with sync_ctx_manager_wrapper(error_context_manager()) as result:
            assert result == "test"
