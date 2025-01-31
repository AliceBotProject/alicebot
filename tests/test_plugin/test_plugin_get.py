from typing import Any
from typing_extensions import override

import anyio
import pytest
from fake_adapter import (
    BaseTestPlugin,
    FakeMessageEvent,
    fake_adapter_class_factory,
    fake_message_event_factor,
)
from pytest_mock import MockerFixture

from alicebot import Bot
from alicebot.exceptions import GetEventTimeout


def test_plugin_get(bot: Bot) -> None:
    class TestPlugin(BaseTestPlugin):
        @override
        async def handle(self) -> None:
            assert self.event.get_plain_text() == "test_0"
            assert (await self.event.get()).get_plain_text() == "test_1"

    bot.load_adapters(
        fake_adapter_class_factory(
            lambda self: fake_message_event_factor(adapter=self, message="test_0"),
            lambda self: fake_message_event_factor(adapter=self, message="test_1"),
        )
    )
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_ask(bot: Bot, mocker: MockerFixture) -> None:
    class TestPlugin(BaseTestPlugin):
        @override
        async def handle(self) -> None:
            assert self.event.get_plain_text() == "test_0"
            assert (await self.event.ask("Hello")).get_plain_text() == "test_1"

    spy = mocker.spy(FakeMessageEvent, "reply")
    bot.load_adapters(
        fake_adapter_class_factory(
            lambda self: fake_message_event_factor(adapter=self, message="test_0"),
            lambda self: fake_message_event_factor(adapter=self, message="test_1"),
        )
    )
    bot.load_plugins(TestPlugin)
    bot.run()
    spy.assert_awaited_once_with(mocker.ANY, "Hello")


def test_plugin_get_timeout(bot: Bot) -> None:
    class TestPlugin(BaseTestPlugin):
        @override
        async def handle(self) -> None:
            assert self.event.get_plain_text() == "test_0"
            assert (await self.event.get(timeout=0.1)).get_plain_text() == "test_1"

    bot.load_adapters(
        fake_adapter_class_factory(
            lambda self: fake_message_event_factor(adapter=self, message="test_0"),
            lambda self: fake_message_event_factor(adapter=self, message="test_1"),
        )
    )
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_get_timeout_error(bot: Bot) -> None:
    class TestPlugin(BaseTestPlugin):
        @override
        async def handle(self) -> None:
            assert self.event.get_plain_text() == "test"
            with pytest.raises(GetEventTimeout):
                await self.event.get(timeout=0.1)

    async def wait_half_sec(_: Any) -> None:
        await anyio.sleep(0.5)

    bot.load_adapters(
        fake_adapter_class_factory(fake_message_event_factor, wait_half_sec)
    )
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_get_timeout_zero(bot: Bot) -> None:
    class TestPlugin(BaseTestPlugin):
        @override
        async def handle(self) -> None:
            assert self.event.get_plain_text() == "test"
            with pytest.raises(GetEventTimeout):
                await self.event.get(timeout=0)

    async def wait_half_sec(_: Any) -> None:
        await anyio.sleep(0.5)

    bot.load_adapters(
        fake_adapter_class_factory(fake_message_event_factor, wait_half_sec)
    )
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_get_try_times(bot: Bot) -> None:
    class TestPlugin(BaseTestPlugin):
        @override
        async def handle(self) -> None:
            assert self.event.get_plain_text() == "test_0"
            assert (await self.event.get(max_try_times=1)).get_plain_text() == "test_1"

    bot.load_adapters(
        fake_adapter_class_factory(
            lambda self: fake_message_event_factor(adapter=self, message="test_0"),
            lambda self: fake_message_event_factor(adapter=self, message="test_1"),
        )
    )
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_get_try_times_error(bot: Bot) -> None:
    class TestPlugin(BaseTestPlugin):
        @override
        async def handle(self) -> None:
            with pytest.raises(GetEventTimeout):
                await self.bot.get(
                    lambda x: isinstance(x, FakeMessageEvent)
                    and x.get_plain_text() == "test_3",
                    max_try_times=1,
                )

        @override
        async def rule(self) -> bool:
            return await super().rule() and self.event.get_plain_text() == "test_0"

    bot.load_adapters(
        fake_adapter_class_factory(
            lambda self: fake_message_event_factor(adapter=self, message="test_0"),
            lambda self: fake_message_event_factor(adapter=self, message="test_1"),
            lambda self: fake_message_event_factor(adapter=self, message="test_2"),
            lambda self: fake_message_event_factor(adapter=self, message="test_3"),
        )
    )
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_get_no_handle(bot: Bot, mocker: MockerFixture) -> None:
    mock = mocker.AsyncMock()

    class TestPlugin(BaseTestPlugin):
        @override
        async def handle(self) -> None:
            await mock(self.event.get_plain_text())
            with pytest.raises(GetEventTimeout):
                await self.event.get()

    bot.load_adapters(
        fake_adapter_class_factory(
            lambda self: fake_message_event_factor(adapter=self, message="test_0"),
            lambda self: fake_message_event_factor(adapter=self, message="test_1"),
            handle_get=False,
        )
    )
    bot.load_plugins(TestPlugin)
    bot.run()
    assert mock.await_args_list == [mocker.call("test_0"), mocker.call("test_1")]
