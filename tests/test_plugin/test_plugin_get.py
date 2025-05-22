from typing import Any, Optional
from typing_extensions import override

import anyio
import pytest
from fake_adapter import (
    BaseTestPlugin,
    FakeAdapter,
    FakeMessageEvent,
    fake_adapter_class_factory,
    fake_message_event_factor,
)
from pytest_mock import MockerFixture

from alicebot import Bot
from alicebot.adapter import Adapter
from alicebot.event import Event
from alicebot.exceptions import GetEventTimeout
from alicebot.plugin import Plugin


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


def test_plugin_get_event_type(bot: Bot, mocker: MockerFixture) -> None:
    mock = mocker.AsyncMock()

    class FakeOtherEvent(Event[FakeAdapter]):
        type: Optional[str] = "other"

    class TestPlugin(Plugin):
        @override
        async def handle(self) -> None:
            await mock(self.event)
            assert (
                await self.bot.get(event_type=FakeMessageEvent)
            ).get_plain_text() == "test_1"

        @override
        async def rule(self) -> bool:
            return True

    bot.load_adapters(
        fake_adapter_class_factory(
            lambda self: fake_message_event_factor(adapter=self, message="test_0"),
            lambda self: FakeOtherEvent(adapter=self),
            lambda self: fake_message_event_factor(adapter=self, message="test_1"),
        )
    )
    bot.load_plugins(TestPlugin)
    bot.run()
    assert len(mock.await_args_list) == 2
    assert mock.await_args_list[0][0][0].get_plain_text() == "test_0"
    assert isinstance(mock.await_args_list[1][0][0], FakeOtherEvent)


def test_plugin_get_adapter_type(bot: Bot, mocker: MockerFixture) -> None:
    mock = mocker.AsyncMock()

    class OtherFakeAdapter(Adapter):
        @override
        async def run(self) -> None: ...

    class TestPlugin(Plugin):
        @override
        async def handle(self) -> None:
            await mock(self.event)
            assert (
                await self.bot.get(
                    adapter_type=FakeAdapter,
                    event_type=FakeMessageEvent,
                )
            ).get_plain_text() == "test_1"

        @override
        async def rule(self) -> bool:
            return True

    bot.load_adapters(
        fake_adapter_class_factory(
            lambda self: fake_message_event_factor(adapter=self, message="test_0"),
            lambda self: fake_message_event_factor(adapter=OtherFakeAdapter(self.bot)),  # type: ignore
            lambda self: fake_message_event_factor(adapter=self, message="test_1"),
        )
    )
    bot.load_plugins(TestPlugin)
    bot.run()
    assert len(mock.await_args_list) == 2
    assert mock.await_args_list[0][0][0].get_plain_text() == "test_0"
    assert isinstance(mock.await_args_list[1][0][0].adapter, OtherFakeAdapter)


def test_plugin_get_none_func(bot: Bot) -> None:
    class TestPlugin(BaseTestPlugin):
        @override
        async def handle(self) -> None:
            assert self.event.get_plain_text() == "test_0"
            event = await self.event.adapter.get()
            assert isinstance(event, FakeMessageEvent)
            assert event.get_plain_text() == "test_1"

    bot.load_adapters(
        fake_adapter_class_factory(
            lambda self: fake_message_event_factor(adapter=self, message="test_0"),
            lambda self: fake_message_event_factor(adapter=self, message="test_1"),
        )
    )
    bot.load_plugins(TestPlugin)
    bot.run()


def test_plugin_get_raise_error(bot: Bot) -> None:
    class TestPlugin(BaseTestPlugin):
        @override
        async def handle(self) -> None:
            assert self.event.get_plain_text() in {"test_0", "test_1"}
            with pytest.raises(ZeroDivisionError):
                await self.event.adapter.get(lambda _: 1 / 0 == 0)

    bot.load_adapters(
        fake_adapter_class_factory(
            lambda self: fake_message_event_factor(adapter=self, message="test_0"),
            lambda self: fake_message_event_factor(adapter=self, message="test_1"),
        )
    )
    bot.load_plugins(TestPlugin)
    bot.run()
