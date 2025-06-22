from typing import Any
from typing_extensions import override

import pytest

from alicebot import Adapter, Bot, Event


def test_adapter_startup_error(bot: Bot) -> None:
    class TestAdapter(Adapter[Any, None]):
        @override
        async def startup(self) -> None:
            raise RuntimeError

        @override
        async def run(self) -> None:
            self.bot.exit()

    bot.load_adapters(TestAdapter)
    with pytest.raises(ExceptionGroup) as exc_info:
        bot.run()
    assert exc_info.group_contains(RuntimeError)


def test_adapter_raise_error(bot: Bot) -> None:
    class TestAdapter(Adapter[Event[Any], None]):
        @override
        async def run(self) -> None:
            self.bot.exit()
            raise RuntimeError

    bot.load_adapters(TestAdapter)
    with pytest.raises(ExceptionGroup) as exc_info:
        bot.run()
    assert exc_info.group_contains(RuntimeError)
