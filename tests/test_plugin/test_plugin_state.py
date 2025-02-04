from typing import Annotated
from typing_extensions import override

from fake_adapter import (
    BaseTestPlugin,
    FakeMessageEvent,
    fake_adapter_class_factory,
    fake_message_event_factor,
)
from pytest_mock import MockerFixture

from alicebot import Bot, Plugin


def test_plugin_state(bot: Bot, mocker: MockerFixture) -> None:
    class TestPlugin(BaseTestPlugin[int]):
        @override
        async def handle(self) -> None:
            if self.state is None:  # pyright: ignore[reportUnnecessaryComparison]
                self.state = 0
            self.state += 1
            await self.event.reply(str(self.state))

    spy = mocker.spy(FakeMessageEvent, "reply")
    bot.load_adapters(
        fake_adapter_class_factory(fake_message_event_factor, fake_message_event_factor)
    )
    bot.load_plugins(TestPlugin)
    bot.run()
    assert spy.await_args_list == [
        mocker.call(mocker.ANY, "1"),
        mocker.call(mocker.ANY, "2"),
    ]


def test_plugin_init_state(bot: Bot, mocker: MockerFixture) -> None:
    class TestPlugin(BaseTestPlugin[int]):
        @override
        def __init_state__(self) -> int:
            return 0

        @override
        async def handle(self) -> None:
            self.state += 1
            await self.event.reply(str(self.state))

    spy = mocker.spy(FakeMessageEvent, "reply")
    bot.load_adapters(
        fake_adapter_class_factory(fake_message_event_factor, fake_message_event_factor)
    )
    bot.load_plugins(TestPlugin)
    bot.run()
    assert spy.await_args_list == [
        mocker.call(mocker.ANY, "1"),
        mocker.call(mocker.ANY, "2"),
    ]


def test_plugin_init_state_subclass(bot: Bot, mocker: MockerFixture) -> None:
    class TestPlugin(BaseTestPlugin[int], init_state=0):
        @override
        async def handle(self) -> None:
            self.state += 1
            await self.event.reply(str(self.state))

    spy = mocker.spy(FakeMessageEvent, "reply")
    bot.load_adapters(
        fake_adapter_class_factory(fake_message_event_factor, fake_message_event_factor)
    )
    bot.load_plugins(TestPlugin)
    bot.run()
    assert spy.await_args_list == [
        mocker.call(mocker.ANY, "1"),
        mocker.call(mocker.ANY, "2"),
    ]


def test_plugin_init_state_annotated(bot: Bot, mocker: MockerFixture) -> None:
    class TestPlugin(Plugin[FakeMessageEvent, Annotated[int, 0], None]):
        @override
        async def handle(self) -> None:
            self.state += 1
            await self.event.reply(str(self.state))

        @override
        async def rule(self) -> bool:
            return isinstance(self.event, FakeMessageEvent)

    spy = mocker.spy(FakeMessageEvent, "reply")
    bot.load_adapters(
        fake_adapter_class_factory(fake_message_event_factor, fake_message_event_factor)
    )
    bot.load_plugins(TestPlugin)
    bot.run()
    assert spy.await_args_list == [
        mocker.call(mocker.ANY, "1"),
        mocker.call(mocker.ANY, "2"),
    ]
