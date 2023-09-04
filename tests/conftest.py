import asyncio
import os
from pathlib import Path
from typing import Any, Dict, Union

import pytest

from alicebot import Bot


@pytest.fixture(scope="session", autouse=True)
def change_test_dir() -> None:  # noqa: PT004
    os.chdir(Path(__file__).parent)


@pytest.fixture()
def bot(monkeypatch: pytest.MonkeyPatch) -> Bot:
    def error_or_exception(_self: Bot, _message: str, exception: Exception) -> None:
        raise exception

    monkeypatch.setattr(Bot, "error_or_exception", error_or_exception)

    bot = Bot(config_file=None)
    exception: Union[BaseException, None] = None

    async def set_exception_handler(_bot: Bot) -> None:
        def async_loop_exception_handler(
            loop: asyncio.AbstractEventLoop, context: Dict[str, Any]
        ) -> None:
            nonlocal exception
            exception = context.get("exception", RuntimeError(context["message"]))
            loop.set_exception_handler(None)
            bot.should_exit.set()

        loop = asyncio.get_running_loop()
        loop.set_exception_handler(async_loop_exception_handler)

    async def bot_exit_hook(_bot: Bot) -> None:
        if exception is not None:
            raise exception

    bot.bot_run_hook(set_exception_handler)
    bot.bot_exit_hook(bot_exit_hook)

    return bot
