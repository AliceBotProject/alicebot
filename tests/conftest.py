import asyncio
import os
import sys
from pathlib import Path
from typing import Any, Dict, Union

import pytest
import structlog

from alicebot import Bot


@pytest.fixture(scope="session", autouse=True)
def change_test_dir() -> None:  # noqa: PT004
    os.chdir(Path(__file__).parent)


@pytest.fixture(autouse=True)
def fixture_configure_structlog() -> None:  # noqa: PT004
    class PrintLogger:
        def msg(self, **kwargs: Any) -> None:
            print(kwargs)  # noqa: T201

        def exception_msg(self, **kwargs: Any) -> None:
            exc = sys.exc_info()[1]
            if exc is not None:
                raise exc
            self.msg(**kwargs)

        log = debug = info = warn = warning = msg
        fatal = failure = err = error = critical = exception = exception_msg

    structlog.configure(logger_factory=PrintLogger, processors=[])


@pytest.fixture()
def bot() -> Bot:
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
