from typing import Any

import pytest
from fake_adapter import FakeAdapter, FakeMessageEvent

from alicebot import Bot, MessageEvent, Plugin


def test_plugin_rule(bot: Bot) -> None:
    class HandleFlag(BaseException):
        pass

    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        async def handle(self) -> None:
            raise HandleFlag

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
    with pytest.raises(HandleFlag):
        bot.run()


def test_plugin_reply(bot: Bot) -> None:
    class TestEvent(FakeMessageEvent):
        async def reply(self, message: str) -> None:
            assert message == "Hello"

    class TestPlugin(Plugin[MessageEvent[Any], None, None]):
        async def handle(self) -> None:
            await self.event.reply("Hello")

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
        async def handle(self) -> None:
            nonlocal flag
            assert flag == self.priority
            flag += 1

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
        async def handle(self) -> None:
            assert self.name == "TestPlugin"

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

        async def handle(self) -> None:
            nonlocal test_plugin_1_flag
            await self.do_something()
            test_plugin_1_flag = True

        async def do_something(self) -> None:
            self.skip()

        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    class TestPlugin2(Plugin[MessageEvent[Any], None, None]):
        priority = 1

        async def handle(self) -> None:
            nonlocal test_plugin_2_flag
            test_plugin_2_flag = True

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

        async def handle(self) -> None:
            nonlocal test_plugin_1_flag
            await self.do_something()
            test_plugin_1_flag = True

        async def do_something(self) -> None:
            self.stop()

        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    class TestPlugin2(Plugin[MessageEvent[Any], None, None]):
        priority = 0

        async def handle(self) -> None:
            nonlocal test_plugin_2_flag
            test_plugin_2_flag = True

        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    class TestPlugin3(Plugin[MessageEvent[Any], None, None]):
        priority = 1

        async def handle(self) -> None:
            nonlocal test_plugin_3_flag
            test_plugin_3_flag = True

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

        async def handle(self) -> None:
            nonlocal test_plugin_1_flag
            test_plugin_1_flag = True

        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    class TestPlugin2(Plugin[MessageEvent[Any], None, None]):
        priority = 1

        async def handle(self) -> None:
            nonlocal test_plugin_2_flag
            test_plugin_2_flag = True

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
        async def handle(self) -> None:
            raise HandleError

        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message")
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    with pytest.raises(HandleError):
        bot.run()
