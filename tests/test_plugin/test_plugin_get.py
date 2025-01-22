from typing import Any
from typing_extensions import override

import anyio
import pytest
from fake_adapter import FakeAdapter, FakeMessageEvent
from pytest_mock import MockerFixture

from alicebot import Bot, MessageEvent, Plugin
from alicebot.exceptions import GetEventTimeout


def test_plugin_get(bot: Bot) -> None:
    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        @override
        async def handle(self) -> None:
            assert self.event.get_plain_text() == "test_0"
            assert (await self.event.get()).get_plain_text() == "test_1"

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message", message="test_0"),
        lambda self: FakeMessageEvent(adapter=self, type="message", message="test_1"),
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_ask(bot: Bot, mocker: MockerFixture) -> None:
    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        @override
        async def handle(self) -> None:
            assert self.event.get_plain_text() == "test_0"
            assert (await self.event.ask("Hello")).get_plain_text() == "test_1"

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    spy = mocker.spy(FakeMessageEvent, "reply")
    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message", message="test_0"),
        lambda self: FakeMessageEvent(adapter=self, type="message", message="test_1"),
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()
    spy.assert_awaited_once_with(mocker.ANY, "Hello")


def test_plugin_get_timeout(bot: Bot) -> None:
    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        @override
        async def handle(self) -> None:
            assert self.event.get_plain_text() == "test_0"
            assert (await self.event.get(timeout=0.1)).get_plain_text() == "test_1"

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message", message="test_0"),
        lambda self: FakeMessageEvent(adapter=self, type="message", message="test_1"),
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_get_timeout_error(bot: Bot) -> None:
    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        @override
        async def handle(self) -> None:
            assert self.event.get_plain_text() == "test_0"
            with pytest.raises(GetEventTimeout):
                await self.event.get(timeout=0.1)

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    async def wait_half_sec(_: Any) -> None:
        await anyio.sleep(0.5)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message", message="test_0"),
        wait_half_sec,
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_get_timeout_zero(bot: Bot) -> None:
    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        @override
        async def handle(self) -> None:
            assert self.event.get_plain_text() == "test_0"
            with pytest.raises(GetEventTimeout):
                await self.event.get(timeout=0)

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    async def wait_half_sec(_: Any) -> None:
        await anyio.sleep(0.5)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message", message="test_0"),
        wait_half_sec,
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_get_try_times(bot: Bot) -> None:
    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        @override
        async def handle(self) -> None:
            assert self.event.get_plain_text() == "test_0"
            assert (await self.event.get(max_try_times=1)).get_plain_text() == "test_1"

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message", message="test_0"),
        lambda self: FakeMessageEvent(adapter=self, type="message", message="test_1"),
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_get_try_times_error(bot: Bot) -> None:
    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        @override
        async def handle(self) -> None:
            with pytest.raises(GetEventTimeout):
                await self.bot.get(
                    lambda x: isinstance(x, MessageEvent)
                    and x.get_plain_text() == "test_3",
                    max_try_times=1,
                )

        @override
        async def rule(self) -> bool:
            return self.event.get_plain_text() == "test_0"

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message", message="test_0"),
        lambda self: FakeMessageEvent(adapter=self, type="message", message="test_1"),
        lambda self: FakeMessageEvent(adapter=self, type="message", message="test_2"),
        lambda self: FakeMessageEvent(adapter=self, type="message", message="test_3"),
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_get_no_handle(bot: Bot, mocker: MockerFixture) -> None:
    mock = mocker.AsyncMock()

    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        @override
        async def handle(self) -> None:
            await mock(self.event.get_plain_text())
            with pytest.raises(GetEventTimeout):
                await self.event.get()

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message", message="test_0"),
        lambda self: FakeMessageEvent(adapter=self, type="message", message="test_1"),
    )
    FakeAdapter.handle_get = False
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()
    assert mock.await_args_list == [mocker.call("test_0"), mocker.call("test_1")]
