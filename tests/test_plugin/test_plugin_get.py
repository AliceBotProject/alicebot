import asyncio
from typing import Any

import pytest
from fake_adapter import FakeAdapter, FakeMessageEvent

from alicebot import Bot, MessageEvent, Plugin
from alicebot.exceptions import GetEventTimeout


def test_plugin_get(bot: Bot) -> None:
    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        async def handle(self) -> None:
            assert self.event.get_plain_text() == "test_0"
            assert (await self.event.get()).get_plain_text() == "test_1"

        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message", message="test_0"),
        lambda self: FakeMessageEvent(adapter=self, type="message", message="test_1"),
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_ask(bot: Bot) -> None:
    class TestEvent(FakeMessageEvent):
        async def reply(self, message: str) -> None:
            assert message == "Hello"

    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        async def handle(self) -> None:
            assert self.event.get_plain_text() == "test_0"
            assert (await self.event.ask("Hello")).get_plain_text() == "test_1"

        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: TestEvent(adapter=self, type="message", message="test_0"),
        lambda self: TestEvent(adapter=self, type="message", message="test_1"),
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_get_timeout(bot: Bot) -> None:
    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        async def handle(self) -> None:
            assert self.event.get_plain_text() == "test_0"
            assert (await self.event.get(timeout=0.1)).get_plain_text() == "test_1"

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
        async def handle(self) -> None:
            assert self.event.get_plain_text() == "test_0"
            with pytest.raises(GetEventTimeout):
                await self.event.get(timeout=0.1)

        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    async def wait_half_sec(_: Any) -> None:
        await asyncio.sleep(0.5)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message", message="test_0"),
        wait_half_sec,
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_get_timeout_zero(bot: Bot) -> None:
    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        async def handle(self) -> None:
            assert self.event.get_plain_text() == "test_0"
            with pytest.raises(GetEventTimeout):
                await self.event.get(timeout=0)

        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    async def wait_half_sec(_: Any) -> None:
        await asyncio.sleep(0.5)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message", message="test_0"),
        wait_half_sec,
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_get_try_times(bot: Bot) -> None:
    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        async def handle(self) -> None:
            assert self.event.get_plain_text() == "test_0"
            assert (await self.event.get(max_try_times=1)).get_plain_text() == "test_1"

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
        async def handle(self) -> None:
            with pytest.raises(GetEventTimeout):
                await self.bot.get(
                    lambda x: isinstance(x, MessageEvent)
                    and x.get_plain_text() == "test_3",
                    max_try_times=1,
                )

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


def test_plugin_get_no_handle(bot: Bot) -> None:
    flag = 0

    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        async def handle(self) -> None:
            nonlocal flag
            flag += 1
            with pytest.raises(GetEventTimeout):
                await self.event.get()

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
    assert flag == 2
