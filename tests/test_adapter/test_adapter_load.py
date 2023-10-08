import pytest

from alicebot import Bot
from alicebot.exceptions import LoadModuleError


def test_adapter_load() -> None:
    from adapters.adapter1 import Adapter1
    from adapters.adapter2 import Adapter2

    bot = Bot()
    bot.load_adapters(Adapter1, Adapter2)
    assert isinstance(bot.get_adapter(Adapter1), Adapter1)
    assert isinstance(bot.get_adapter("adapter1"), Adapter1)
    assert isinstance(bot.get_adapter(Adapter2), Adapter2)
    assert isinstance(bot.get_adapter("adapter2"), Adapter2)

    with pytest.raises(LookupError):
        bot.get_adapter(adapter="NoSuchAdapter")


def test_adapter_load_error_type(bot: Bot) -> None:
    with pytest.raises(TypeError):
        bot.load_adapters(type)  # type: ignore

    with pytest.raises(TypeError):
        bot.load_adapters(object)  # type: ignore


def test_adapter_load_from_module_name() -> None:
    bot = Bot()
    bot.load_adapters("adapters.adapter1", "adapters.adapter2")
    assert bot.get_adapter("adapter1")
    assert bot.get_adapter("adapter2")


def test_adapter_load_empty(bot: Bot) -> None:
    with pytest.raises(LoadModuleError):
        bot.load_adapters("bad_adapters.adapter_empty")


def test_adapter_load_more_then_one(bot: Bot) -> None:
    with pytest.raises(LoadModuleError):
        bot.load_adapters("bad_adapters.adapter_more_then_one")
