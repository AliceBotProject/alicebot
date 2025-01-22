import sys
from typing import Any
from typing_extensions import override

import pytest
from fake_adapter import FakeAdapter, FakeMessageEvent
from pytest_mock import MockerFixture

from alicebot import Bot, MessageEvent, Plugin

if sys.version_info < (3, 11):
    from exceptiongroup import ExceptionGroup


def test_plugin_rule(bot: Bot, mocker: MockerFixture) -> None:
    mock = mocker.AsyncMock()

    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        handle = mock

        @override
        async def rule(self) -> bool:
            return (
                isinstance(self.event, MessageEvent)
                and self.event.get_plain_text().lower() == "test"
            )

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message")
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()
    mock.assert_awaited_once()


def test_plugin_reply(bot: Bot, mocker: MockerFixture) -> None:
    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        @override
        async def handle(self) -> None:
            await self.event.reply("Hello")

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    spy = mocker.spy(FakeMessageEvent, "reply")
    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message")
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()
    spy.assert_awaited_once_with(mocker.ANY, "Hello")


def test_plugin_priority(bot: Bot, mocker: MockerFixture) -> None:
    mock = mocker.AsyncMock()

    class TestPriorityPlugin(Plugin[MessageEvent[Any], None, None]):
        @override
        async def handle(self) -> None:
            await mock(self.name)

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    class TestPlugin0(TestPriorityPlugin):
        pass

    class TestPlugin1(TestPriorityPlugin):
        priority = 1

    class TestPlugin2(TestPriorityPlugin):
        priority = 2

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message")
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin0, TestPlugin1, TestPlugin2)
    bot.run()
    assert mock.await_args_list == [
        mocker.call("TestPlugin0"),
        mocker.call("TestPlugin1"),
        mocker.call("TestPlugin2"),
    ]


def test_plugin_name(bot: Bot) -> None:
    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        @override
        async def handle(self) -> None:
            assert self.name == "TestPlugin"

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message")
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_skip(bot: Bot, mocker: MockerFixture) -> None:
    mock = mocker.AsyncMock()

    class TestPlugin1(Plugin[MessageEvent[Any], None, None]):
        priority = 0

        @override
        async def handle(self) -> None:
            await self.do_something()
            await mock(self.name)

        async def do_something(self) -> None:
            self.skip()

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    class TestPlugin2(Plugin[MessageEvent[Any], None, None]):
        priority = 1

        @override
        async def handle(self) -> None:
            await mock(self.name)

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message")
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin1, TestPlugin2)
    bot.run()
    mock.assert_awaited_once_with("TestPlugin2")


def test_plugin_stop(bot: Bot, mocker: MockerFixture) -> None:
    mock = mocker.AsyncMock()

    class TestPlugin1(Plugin[MessageEvent[Any], None, None]):
        priority = 0

        @override
        async def handle(self) -> None:
            await self.do_something()
            await mock(self.name)

        async def do_something(self) -> None:
            self.stop()

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    class TestPlugin2(Plugin[MessageEvent[Any], None, None]):
        priority = 0

        @override
        async def handle(self) -> None:
            await mock(self.name)

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    class TestPlugin3(Plugin[MessageEvent[Any], None, None]):
        priority = 1

        @override
        async def handle(self) -> None:
            await mock(self.name)

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message")
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin1, TestPlugin2, TestPlugin3)
    bot.run()
    mock.assert_awaited_once_with("TestPlugin2")


def test_plugin_block(bot: Bot, mocker: MockerFixture) -> None:
    mock = mocker.AsyncMock()

    class TestPlugin1(Plugin[MessageEvent[Any], None, None]):
        priority = 0
        block = True

        @override
        async def handle(self) -> None:
            await mock(self.name)

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    class TestPlugin2(Plugin[MessageEvent[Any], None, None]):
        priority = 1

        @override
        async def handle(self) -> None:
            await mock(self.name)

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message")
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin1, TestPlugin2)
    bot.run()
    mock.assert_awaited_once_with("TestPlugin1")


def test_plugin_error(bot: Bot) -> None:
    class HandleError(Exception):
        pass

    class TestPlugin(Plugin[Any, None, None]):
        @override
        async def handle(self) -> None:
            raise HandleError

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message")
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    with pytest.raises(ExceptionGroup) as exc_info:  # pyright: ignore[reportUnknownVariableType]
        bot.run()
    assert exc_info.group_contains(HandleError)
