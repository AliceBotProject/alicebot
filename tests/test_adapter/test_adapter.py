from typing import Any

import pytest

from alicebot import Adapter, Bot, Event


def test_adapter_startup_error(bot: Bot) -> None:
    bot.load_adapters("bad_adapters.adapter_startup_error")
    with pytest.raises(RuntimeError):
        bot.run()


def test_adapter_raise_error(bot: Bot) -> None:
    class TestAdapter(Adapter[Event[Any], None]):
        async def run(self) -> None:
            """运行适配器。"""
            self.bot.should_exit.set()
            raise TypeError

    bot.load_adapters(TestAdapter)
    bot.run()
