import sys
from typing import Any
from typing_extensions import override

import pytest
from fake_adapter import FakeAdapter, FakeMessageEvent

from alicebot import Bot, MessageEvent, Plugin

if sys.version_info < (3, 11):
    from exceptiongroup import ExceptionGroup


def test_plugin_rule(bot: Bot) -> None:
    flag = False

    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        @override
        async def handle(self) -> None:
            nonlocal flag
            flag = True

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
    assert flag


def test_plugin_reply(bot: Bot) -> None:
    class TestEvent(FakeMessageEvent):
        @override
        async def reply(self, message: str) -> None:
            assert message == "Hello"

    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        @override
        async def handle(self) -> None:
            await self.event.reply("Hello")

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: TestEvent(adapter=self, type="message")
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_priority(bot: Bot) -> None:
    flag = 0

    class TestPriorityPlugin(Plugin[MessageEvent[Any], None, None]):
        @override
        async def handle(self) -> None:
            nonlocal flag
            assert flag == self.priority
            flag += 1

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


def test_plugin_skip(bot: Bot) -> None:
    test_plugin_1_flag = False
    test_plugin_2_flag = False

    class TestPlugin1(Plugin[MessageEvent[Any], None, None]):
        priority = 0

        @override
        async def handle(self) -> None:
            nonlocal test_plugin_1_flag
            await self.do_something()
            test_plugin_1_flag = True

        async def do_something(self) -> None:
            self.skip()

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    class TestPlugin2(Plugin[MessageEvent[Any], None, None]):
        priority = 1

        @override
        async def handle(self) -> None:
            nonlocal test_plugin_2_flag
            test_plugin_2_flag = True

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message")
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin1, TestPlugin2)
    bot.run()
    assert not test_plugin_1_flag
    assert test_plugin_2_flag


def test_plugin_stop(bot: Bot) -> None:
    test_plugin_1_flag = False
    test_plugin_2_flag = False
    test_plugin_3_flag = False

    class TestPlugin1(Plugin[MessageEvent[Any], None, None]):
        priority = 0

        @override
        async def handle(self) -> None:
            nonlocal test_plugin_1_flag
            await self.do_something()
            test_plugin_1_flag = True

        async def do_something(self) -> None:
            self.stop()

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    class TestPlugin2(Plugin[MessageEvent[Any], None, None]):
        priority = 0

        @override
        async def handle(self) -> None:
            nonlocal test_plugin_2_flag
            test_plugin_2_flag = True

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    class TestPlugin3(Plugin[MessageEvent[Any], None, None]):
        priority = 1

        @override
        async def handle(self) -> None:
            nonlocal test_plugin_3_flag
            test_plugin_3_flag = True

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message")
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin1, TestPlugin2, TestPlugin3)
    bot.run()
    assert not test_plugin_1_flag
    assert test_plugin_2_flag
    assert not test_plugin_3_flag


def test_plugin_block(bot: Bot) -> None:
    test_plugin_1_flag = False
    test_plugin_2_flag = False

    class TestPlugin1(Plugin[MessageEvent[Any], None, None]):
        priority = 0
        block = True

        @override
        async def handle(self) -> None:
            nonlocal test_plugin_1_flag
            test_plugin_1_flag = True

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    class TestPlugin2(Plugin[MessageEvent[Any], None, None]):
        priority = 1

        @override
        async def handle(self) -> None:
            nonlocal test_plugin_2_flag
            test_plugin_2_flag = True

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message")
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin1, TestPlugin2)
    bot.run()
    assert test_plugin_1_flag
    assert not test_plugin_2_flag


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
