"""测试加载配置文件。"""

# ruff: noqa: SLF001
# pyright: reportPrivateUsage=false
import json
from pathlib import Path
from typing import Any, Dict

import pytest
import structlog
from pydantic import ValidationError
from structlog.testing import capture_logs

from alicebot import Bot


@pytest.fixture(scope="module")
def raw_config() -> Dict[str, Any]:
    with Path("config_files/raw_config.json").open(encoding="utf-8") as f:
        return json.load(f)


def test_load_config(raw_config: Dict[str, Any]) -> None:
    bot = Bot()
    bot._reload_config_dict()
    assert bot.config.model_dump(mode="json") == raw_config


def test_load_config_toml(raw_config: Dict[str, Any]) -> None:
    bot = Bot(config_file="config_files/config.toml")
    bot._reload_config_dict()
    assert bot.config.model_dump(mode="json") == raw_config


def test_load_config_json(raw_config: Dict[str, Any]) -> None:
    bot = Bot(config_file="config_files/config.json")
    bot._reload_config_dict()
    assert bot.config.model_dump(mode="json") == raw_config


def test_load_config_dict(raw_config: Dict[str, Any]) -> None:
    with Path("config_files/config.json").open(encoding="utf-8") as f:
        config_dict = json.load(f)
    bot = Bot(config_dict=config_dict)
    bot._reload_config_dict()
    assert bot.config.model_dump(mode="json") == raw_config


def test_load_config_file_not_exist() -> None:
    bot = Bot(config_file="config_files/no_such_file.toml")
    with pytest.raises(FileNotFoundError):
        bot._reload_config_dict()


def test_load_config_error() -> None:
    bot = Bot(config_file="config_files/error_config.toml")
    with pytest.raises(ValidationError):
        bot._reload_config_dict()


def test_load_config_error_ext() -> None:
    bot = Bot(config_file="config_files/error_ext.txt")
    with capture_logs() as cap_logs:
        bot._reload_config_dict()
    assert cap_logs[0] == {
        "event": "Read config file failed: Unable to determine config file type",
        "log_level": "error",
    }


def test_load_config_error_format() -> None:
    bot = Bot(config_file="config_files/error_format.json")
    with pytest.raises(json.JSONDecodeError):
        bot._reload_config_dict()


def test_load_config_with_log() -> None:
    bot = Bot(
        config_dict={
            "bot": {
                "log": {
                    "level": 10,
                    "verbose_exception": False,
                },
            },
        }
    )
    bot._reload_config_dict()
    wrapper_class = structlog.get_config()["wrapper_class"]
    assert issubclass(wrapper_class, structlog.make_filtering_bound_logger(10))  # pyright: ignore
    assert wrapper_class.exception == wrapper_class.error
    assert wrapper_class.aexception == wrapper_class.aexception
