from typing import Annotated, Any
from typing_extensions import override

from fake_adapter import FakeAdapter, FakeMessageEvent

from alicebot import Bot, MessageEvent, Plugin


def test_plugin_state(bot: Bot) -> None:
    class TestEvent(FakeMessageEvent):
        count: int

        @override
        async def reply(self, message: str) -> None:
            assert message == str(self.count)

    class TestPlugin(Plugin[MessageEvent[Any], int, None]):
        @override
        async def handle(self) -> None:
            if self.state is None:  # pyright: ignore[reportUnnecessaryComparison]
                self.state = 0
            self.state += 1
            await self.event.reply(str(self.state))

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, MessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: TestEvent(adapter=self, type="message", count=1),
        lambda self: TestEvent(adapter=self, type="message", count=2),
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_init_state(bot: Bot) -> None:
    class TestEvent(FakeMessageEvent):
        count: int

        @override
        async def reply(self, message: str) -> None:
            assert message == str(self.count)

    class TestPlugin(Plugin[MessageEvent[Any], int, None]):
        @override
        def __init_state__(self) -> int:
            return 0

        @override
        async def handle(self) -> None:
            self.state += 1
            await self.event.reply(str(self.state))

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, MessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: TestEvent(adapter=self, type="message", count=1),
        lambda self: TestEvent(adapter=self, type="message", count=2),
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_init_state_subclass(bot: Bot) -> None:
    class TestEvent(FakeMessageEvent):
        count: int

        @override
        async def reply(self, message: str) -> None:
            assert message == str(self.count)

    class TestPlugin(Plugin[MessageEvent[Any], int, None], init_state=0):
        @override
        async def handle(self) -> None:
            self.state += 1
            await self.event.reply(str(self.state))

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, MessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: TestEvent(adapter=self, type="message", count=1),
        lambda self: TestEvent(adapter=self, type="message", count=2),
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_init_state_annotated(bot: Bot) -> None:
    class TestEvent(FakeMessageEvent):
        count: int

        @override
        async def reply(self, message: str) -> None:
            assert message == str(self.count)

    class TestPlugin(Plugin[MessageEvent[Any], Annotated[int, 0], None]):
        @override
        async def handle(self) -> None:
            self.state += 1
            await self.event.reply(str(self.state))

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, MessageEvent)

    FakeAdapter.set_event_factories(
        lambda self: TestEvent(adapter=self, type="message", count=1),
        lambda self: TestEvent(adapter=self, type="message", count=2),
    )
    bot.load_adapters(FakeAdapter)
    bot.load_plugins(TestPlugin)
    bot.run()
