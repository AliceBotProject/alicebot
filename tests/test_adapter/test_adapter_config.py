# pyright: reportPrivateUsage=false
# ruff: noqa: SLF001

from typing import Any
from typing_extensions import override

from alicebot import Adapter, Bot, ConfigModel, Event


def test_adapter_config(bot: Bot) -> None:
    class TestAdapter(Adapter[Event[Any], Any]):
        class Config(ConfigModel):
            __config_name__ = "test_adapter"
            a: int = 0
            b: str = ""

        @override
        async def run(self) -> None:
            self.bot.should_exit.set()
            assert self.config.a == 1
            assert self.config.b == "test"

    bot._config_dict = {
        "adapter": {
            "test_adapter": {
                "a": 1,
                "b": "test",
            },
        },
    }
    bot.load_adapters(TestAdapter)
    bot.run()


def test_adapter_no_config(bot: Bot) -> None:
    class TestAdapter(Adapter[Event[Any], None]):
        @override
        async def run(self) -> None:
            self.bot.should_exit.set()
            assert self.config is None

    bot.load_adapters(TestAdapter)
    bot.run()
