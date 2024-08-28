import os
import sys
from pathlib import Path
from typing import Any

import pytest
import structlog

from alicebot import Bot


@pytest.fixture(scope="session", autouse=True)
def change_test_dir() -> None:
    os.chdir(Path(__file__).parent)


@pytest.fixture(autouse=True)
def fixture_configure_structlog() -> None:
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


@pytest.fixture
def bot() -> Bot:
    return Bot(config_file=None, handle_signals=False)
