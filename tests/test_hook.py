# pyright: reportUnusedFunction=false

from typing import Any

from fake_adapter import fake_adapter_class_factory, fake_message_event_factor

from alicebot import Adapter, Bot, Event


def test_bot_run_hook() -> None:
    hook_call_list: list[str] = []
    bot = Bot()

    @bot.bot_run_hook
    async def bot_run_hook(_bot: Bot) -> None:
        hook_call_list.append("bot_run_hook")

    @bot.bot_exit_hook
    async def bot_exit_hook(_bot: Bot) -> None:
        hook_call_list.append("bot_exit_hook")

    @bot.adapter_startup_hook
    async def adapter_startup_hook(_adapter: Adapter[Any, Any]) -> None:
        hook_call_list.append("adapter_startup_hook")

    @bot.adapter_run_hook
    async def adapter_run_hook(_adapter: Adapter[Any, Any]) -> None:
        hook_call_list.append("adapter_run_hook")

    @bot.adapter_shutdown_hook
    async def adapter_shutdown_hook(_adapter: Adapter[Any, Any]) -> None:
        hook_call_list.append("adapter_shutdown_hook")

    @bot.event_preprocessor_hook
    async def event_preprocessor_hook(_event: Event[Any]) -> None:
        hook_call_list.append("event_preprocessor_hook")

    @bot.event_postprocessor_hook
    async def event_postprocessor_hook(_event: Event[Any]) -> None:
        hook_call_list.append("event_postprocessor_hook")

    bot.load_adapters(fake_adapter_class_factory(fake_message_event_factor))
    bot.run()

    assert hook_call_list == [
        "bot_run_hook",
        "adapter_startup_hook",
        "adapter_run_hook",
        "event_preprocessor_hook",
        "event_postprocessor_hook",
        "adapter_shutdown_hook",
        "bot_exit_hook",
    ]
