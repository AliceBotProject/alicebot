# pyright: reportPrivateUsage=false
# ruff: noqa: SLF001

from typing import Any
from typing_extensions import override

import pytest
from fake_adapter import (
    BaseTestPlugin,
    FakeMessageEvent,
    fake_adapter_class_factory,
    fake_message_event_factor,
)
from pydantic import ValidationError

from alicebot import Bot, ConfigModel, Plugin


def test_plugin_config(bot: Bot) -> None:
    class TestPlugin(BaseTestPlugin[None, Any]):
        class Config(ConfigModel):
            __config_name__ = "test_plugin"
            a: int = 0
            b: str = ""

        @override
        async def handle(self) -> None:
            assert self.config.a == 1
            assert self.config.b == "test"

    bot._config_dict = {
        "plugin": {
            "test_plugin": {
                "a": 1,
                "b": "test",
            },
        },
    }
    bot.load_adapters(fake_adapter_class_factory(fake_message_event_factor))
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_no_config(bot: Bot) -> None:
    class TestPlugin(BaseTestPlugin):
        @override
        async def handle(self) -> None:
            assert self.config is None

    bot.load_adapters(fake_adapter_class_factory(fake_message_event_factor))
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_config_subclass(bot: Bot) -> None:
    class Config(ConfigModel):
        __config_name__ = "test_plugin"
        a: int = 0
        b: str = ""

    class TestPlugin(BaseTestPlugin[None, Config], config=Config):
        @override
        async def handle(self) -> None:
            assert self.config.a == 1
            assert self.config.b == "test"

    bot._config_dict = {
        "plugin": {
            "test_plugin": {
                "a": 1,
                "b": "test",
            },
        },
    }
    bot.load_adapters(fake_adapter_class_factory(fake_message_event_factor))
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_config_error(bot: Bot) -> None:
    class TestPlugin(BaseTestPlugin[None, Any]):
        class Config(ConfigModel):
            __config_name__ = "test_plugin"
            a: int
            b: str

        @override
        async def handle(self) -> None:
            assert self.config.a == 1
            assert self.config.b == "test"

    bot.load_adapters(fake_adapter_class_factory(fake_message_event_factor))
    bot.load_plugins(TestPlugin)
    with pytest.raises(ValidationError):
        bot.run()


def test_plugin_config_subclass_generic(bot: Bot) -> None:
    class Config(ConfigModel):
        __config_name__ = "test_plugin"
        a: int = 0
        b: str = ""

    class TestPlugin(Plugin[FakeMessageEvent, int, Config]):
        @override
        async def handle(self) -> None:
            assert self.config.a == 1
            assert self.config.b == "test"

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    bot._config_dict = {
        "plugin": {
            "test_plugin": {
                "a": 1,
                "b": "test",
            },
        },
    }
    bot.load_adapters(fake_adapter_class_factory(fake_message_event_factor))
    bot.load_plugins(TestPlugin)
    bot.run()
