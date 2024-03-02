"""测试加载配置文件。"""

# ruff: noqa: SLF001
# pyright: reportPrivateUsage=false
import json
from pathlib import Path
from typing import Any, Dict, Type

import pytest
from pydantic import ValidationError

from alicebot import Bot


@pytest.fixture(scope="module")
def raw_config() -> Dict[str, Any]:
    with Path("config_files/raw_config.json").open(encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture()
def bot_type(monkeypatch: pytest.MonkeyPatch) -> Type[Bot]:
    def error_or_exception(_self: Bot, _message: str, exception: Exception) -> None:
        raise exception

    monkeypatch.setattr(Bot, "error_or_exception", error_or_exception)
    return Bot


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


def test_load_config_file_not_exist(bot_type: Type[Bot]) -> None:
    bot = bot_type(config_file="config_files/no_such_file.toml")
    with pytest.raises(FileNotFoundError):
        bot._reload_config_dict()


def test_load_config_error(bot_type: Type[Bot]) -> None:
    bot = bot_type(config_file="config_files/error_config.toml")
    with pytest.raises(ValidationError):
        bot._reload_config_dict()


def test_load_config_error_ext(bot_type: Type[Bot]) -> None:
    bot = bot_type(config_file="config_files/error_ext.txt")
    with pytest.raises(OSError):  # noqa: PT011
        bot._reload_config_dict()


def test_load_config_error_format(bot_type: Type[Bot]) -> None:
    bot = bot_type(config_file="config_files/error_format.json")
    with pytest.raises(json.JSONDecodeError):
        bot._reload_config_dict()
