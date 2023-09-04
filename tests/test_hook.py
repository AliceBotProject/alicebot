from typing import Any

from fake_adapter import FakeAdapter, FakeMessageEvent

from alicebot import Adapter, Bot, Event


def test_bot_run_hook() -> None:  # noqa: PLR0915
    bot_run_hook_flag = False
    bot_exit_hook_flag = False
    adapter_startup_hook_flag = False
    adapter_run_hook_flag = False
    adapter_shutdown_hook_flag = False
    event_preprocessor_hook_flag = False
    event_postprocessor_hook_flag = False

    async def bot_run_hook(_bot: Bot) -> None:
        nonlocal bot_run_hook_flag
        bot_run_hook_flag = True

        assert bot_run_hook_flag
        assert not bot_exit_hook_flag
        assert not adapter_startup_hook_flag
        assert not adapter_run_hook_flag
        assert not adapter_shutdown_hook_flag
        assert not event_preprocessor_hook_flag
        assert not event_postprocessor_hook_flag

    async def bot_exit_hook(_bot: Bot) -> None:
        nonlocal bot_exit_hook_flag
        bot_exit_hook_flag = True

        assert bot_run_hook_flag
        assert bot_exit_hook_flag
        assert adapter_startup_hook_flag
        assert adapter_run_hook_flag
        assert adapter_shutdown_hook_flag
        assert event_preprocessor_hook_flag
        assert event_postprocessor_hook_flag

    async def adapter_startup_hook(_adapter: Adapter[Any, Any]) -> None:
        nonlocal adapter_startup_hook_flag
        adapter_startup_hook_flag = True

        assert bot_run_hook_flag
        assert not bot_exit_hook_flag
        assert adapter_startup_hook_flag
        assert not adapter_run_hook_flag
        assert not adapter_shutdown_hook_flag
        assert not event_preprocessor_hook_flag
        assert not event_postprocessor_hook_flag

    async def adapter_run_hook(_adapter: Adapter[Any, Any]) -> None:
        nonlocal adapter_run_hook_flag
        adapter_run_hook_flag = True

        assert bot_run_hook_flag
        assert not bot_exit_hook_flag
        assert adapter_startup_hook_flag
        assert adapter_run_hook_flag
        assert not adapter_shutdown_hook_flag
        assert not event_preprocessor_hook_flag
        assert not event_postprocessor_hook_flag

    async def adapter_shutdown_hook(_adapter: Adapter[Any, Any]) -> None:
        nonlocal adapter_shutdown_hook_flag
        adapter_shutdown_hook_flag = True

        assert bot_run_hook_flag
        assert not bot_exit_hook_flag
        assert adapter_startup_hook_flag
        assert adapter_run_hook_flag
        assert adapter_shutdown_hook_flag
        assert event_preprocessor_hook_flag
        assert event_postprocessor_hook_flag

    async def event_preprocessor_hook(_event: Event[Any]) -> None:
        nonlocal event_preprocessor_hook_flag
        event_preprocessor_hook_flag = True

        assert bot_run_hook_flag
        assert not bot_exit_hook_flag
        assert adapter_startup_hook_flag
        assert adapter_run_hook_flag
        assert not adapter_shutdown_hook_flag
        assert event_preprocessor_hook_flag
        assert not event_postprocessor_hook_flag

    async def event_postprocessor_hook(_event: Event[Any]) -> None:
        nonlocal event_postprocessor_hook_flag
        event_postprocessor_hook_flag = True

        assert bot_run_hook_flag
        assert not bot_exit_hook_flag
        assert adapter_startup_hook_flag
        assert adapter_run_hook_flag
        assert not adapter_shutdown_hook_flag
        assert event_preprocessor_hook_flag
        assert event_postprocessor_hook_flag

    bot = Bot()

    bot.bot_run_hook(bot_run_hook)
    bot.bot_exit_hook(bot_exit_hook)
    bot.adapter_startup_hook(adapter_startup_hook)
    bot.adapter_run_hook(adapter_run_hook)
    bot.adapter_shutdown_hook(adapter_shutdown_hook)
    bot.event_preprocessor_hook(event_preprocessor_hook)
    bot.event_postprocessor_hook(event_postprocessor_hook)

    FakeAdapter.set_event_factories(
        lambda self: FakeMessageEvent(adapter=self, type="message")
    )
    bot.load_adapters(FakeAdapter)
    bot.run()

    assert bot_run_hook_flag
    assert bot_exit_hook_flag
    assert adapter_startup_hook_flag
    assert adapter_run_hook_flag
    assert adapter_shutdown_hook_flag
    assert event_preprocessor_hook_flag
    assert event_postprocessor_hook_flag
