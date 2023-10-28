# pyright: reportPrivateUsage=false
# ruff: noqa: SLF001

from typing import Any

import pytest
from fake_adapter import FakeAdapter, FakeMessageEvent
from pydantic import ValidationError

from alicebot import Bot, ConfigModel, MessageEvent, Plugin


def test_plugin_config(bot: Bot) -> None:
    class TestPlugin(Plugin[MessageEvent[Any], int, Any]):
        class Config(ConfigModel):
            __config_name__ = "test_plugin"
            a: int = 0
            b: str = ""

        async def handle(self) -> None:
            assert self.config.a == 1
            assert self.config.b == "test"

        async def rule(self) -> bool:
            return isinstance(self.event, MessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message")
    )
    bot._config_dict = {
        "plugin": {
            "test_plugin": {
                "a": 1,
                "b": "test",
            },
        },
    }
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_no_config(bot: Bot) -> None:
    class TestPlugin(Plugin[MessageEvent[Any], int, None]):
        async def handle(self) -> None:
            assert self.config is None

        async def rule(self) -> bool:
            return isinstance(self.event, MessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message")
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_config_subclass(bot: Bot) -> None:
    class Config(ConfigModel):
        __config_name__ = "test_plugin"
        a: int = 0
        b: str = ""

    class TestPlugin(Plugin[MessageEvent[Any], int, Config], config=Config):
        async def handle(self) -> None:
            assert self.config.a == 1
            assert self.config.b == "test"

        async def rule(self) -> bool:
            return isinstance(self.event, MessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message")
    )
    bot._config_dict = {
        "plugin": {
            "test_plugin": {
                "a": 1,
                "b": "test",
            },
        },
    }
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_config_error(bot: Bot) -> None:
    class TestPlugin(Plugin[MessageEvent[Any], int, Any]):
        class Config(ConfigModel):
            __config_name__ = "test_plugin"
            a: int
            b: str

        async def handle(self) -> None:
            assert self.config.a == 1
            assert self.config.b == "test"

        async def rule(self) -> bool:
            return isinstance(self.event, MessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message")
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    with pytest.raises(ValidationError):
        bot.run()


def test_plugin_config_subclass_generic(bot: Bot) -> None:
    class Config(ConfigModel):
        __config_name__ = "test_plugin"
        a: int = 0
        b: str = ""

    class TestPlugin(Plugin[MessageEvent[Any], int, Config]):
        async def handle(self) -> None:
            assert self.config.a == 1
            assert self.config.b == "test"

        async def rule(self) -> bool:
            return isinstance(self.event, MessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message")
    )
    bot._config_dict = {
        "plugin": {
            "test_plugin": {
                "a": 1,
                "b": "test",
            },
        },
    }
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()
