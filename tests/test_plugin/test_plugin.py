import sys
from typing_extensions import override

import pytest
from fake_adapter import (
    BaseTestPlugin,
    FakeMessageEvent,
    fake_adapter_class_factory,
    fake_message_event_factor,
)
from pytest_mock import MockerFixture

from alicebot import Bot, Plugin

if sys.version_info < (3, 11):
    from exceptiongroup import ExceptionGroup


def test_plugin_rule(bot: Bot, mocker: MockerFixture) -> None:
    mock = mocker.AsyncMock()

    class TestPlugin(Plugin[FakeMessageEvent, None, None]):
        @override
        async def handle(self) -> None:
            await mock(self.name)

        @override
        async def rule(self) -> bool:
            return (
                isinstance(self.event, FakeMessageEvent)
                and self.event.get_plain_text() == "test"
            )

    bot.load_adapters(fake_adapter_class_factory(fake_message_event_factor))
    bot.load_plugins(TestPlugin)
    bot.run()
    mock.assert_awaited_once()


def test_plugin_reply(bot: Bot, mocker: MockerFixture) -> None:
    class TestPlugin(BaseTestPlugin):
        @override
        async def handle(self) -> None:
            await self.event.reply("Hello")

    spy = mocker.spy(FakeMessageEvent, "reply")
    bot.load_adapters(fake_adapter_class_factory(fake_message_event_factor))
    bot.load_plugins(TestPlugin)
    bot.run()
    spy.assert_awaited_once_with(mocker.ANY, "Hello")


def test_plugin_priority(bot: Bot, mocker: MockerFixture) -> None:
    mock = mocker.AsyncMock()

    class TestPriorityPlugin(BaseTestPlugin):
        @override
        async def handle(self) -> None:
            await mock(self.name)

    class TestPlugin0(TestPriorityPlugin):
        pass

    class TestPlugin1(TestPriorityPlugin):
        priority = 1

    class TestPlugin2(TestPriorityPlugin):
        priority = 2

    bot.load_adapters(fake_adapter_class_factory(fake_message_event_factor))
    bot.load_plugins(TestPlugin0, TestPlugin1, TestPlugin2)
    bot.run()
    assert mock.await_args_list == [
        mocker.call("TestPlugin0"),
        mocker.call("TestPlugin1"),
        mocker.call("TestPlugin2"),
    ]


def test_plugin_name(bot: Bot) -> None:
    class TestPlugin(BaseTestPlugin):
        @override
        async def handle(self) -> None:
            assert self.name == "TestPlugin"

    bot.load_adapters(fake_adapter_class_factory(fake_message_event_factor))
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_skip(bot: Bot, mocker: MockerFixture) -> None:
    mock = mocker.AsyncMock()

    class TestPlugin1(BaseTestPlugin):
        priority = 0

        @override
        async def handle(self) -> None:
            await self.do_something()
            await mock(self.name)

        async def do_something(self) -> None:
            self.skip()

    class TestPlugin2(BaseTestPlugin):
        priority = 1

        @override
        async def handle(self) -> None:
            await mock(self.name)

    bot.load_adapters(fake_adapter_class_factory(fake_message_event_factor))
    bot.load_plugins(TestPlugin1, TestPlugin2)
    bot.run()
    mock.assert_awaited_once_with("TestPlugin2")


def test_plugin_stop(bot: Bot, mocker: MockerFixture) -> None:
    mock = mocker.AsyncMock()

    class TestPlugin1(BaseTestPlugin):
        priority = 0

        @override
        async def handle(self) -> None:
            await self.do_something()
            await mock(self.name)

        async def do_something(self) -> None:
            self.stop()

    class TestPlugin2(BaseTestPlugin):
        priority = 0

        @override
        async def handle(self) -> None:
            await mock(self.name)

    class TestPlugin3(BaseTestPlugin):
        priority = 1

        @override
        async def handle(self) -> None:
            await mock(self.name)

    bot.load_adapters(fake_adapter_class_factory(fake_message_event_factor))
    bot.load_plugins(TestPlugin1, TestPlugin2, TestPlugin3)
    bot.run()
    mock.assert_awaited_once_with("TestPlugin2")


def test_plugin_block(bot: Bot, mocker: MockerFixture) -> None:
    mock = mocker.AsyncMock()

    class TestPlugin1(BaseTestPlugin):
        priority = 0
        block = True

        @override
        async def handle(self) -> None:
            await mock(self.name)

    class TestPlugin2(BaseTestPlugin):
        priority = 1

        @override
        async def handle(self) -> None:
            await mock(self.name)

    bot.load_adapters(fake_adapter_class_factory(fake_message_event_factor))
    bot.load_plugins(TestPlugin1, TestPlugin2)
    bot.run()
    mock.assert_awaited_once_with("TestPlugin1")


def test_plugin_error(bot: Bot) -> None:
    class HandleError(Exception):
        pass

    class TestPlugin(BaseTestPlugin):
        @override
        async def handle(self) -> None:
            raise HandleError

    bot.load_adapters(fake_adapter_class_factory(fake_message_event_factor))
    bot.load_plugins(TestPlugin)
    with pytest.raises(ExceptionGroup) as exc_info:  # pyright: ignore[reportUnknownVariableType]
        bot.run()
    assert exc_info.group_contains(HandleError)
