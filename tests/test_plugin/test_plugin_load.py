from pathlib import Path
from typing import Any, NoReturn

import pytest
from structlog.testing import capture_logs

from alicebot import Bot, Plugin
from alicebot.exceptions import LoadModuleError


def test_plugin_load() -> None:
    from plugins.plugin1 import Plugin1
    from plugins.plugin2 import Plugin2

    bot = Bot()
    bot.load_plugins(Plugin1, Plugin2)

    assert bot.get_plugin("Plugin1")
    assert bot.get_plugin("Plugin2")

    with pytest.raises(LookupError):
        bot.get_plugin("NoSuchPlugin")


def test_plugin_load_error(bot: Bot) -> None:
    class TestPlugin(Plugin[Any, None, None]):
        priority = -1

    bot = Bot()

    with capture_logs() as cap_logs:
        bot.load_plugins(TestPlugin)
    assert cap_logs[0] == {
        "event": "Load plugin from class failed: Plugin priority incorrect in the class",
        "plugin_class": TestPlugin,
        "log_level": "error",
    }


def test_plugin_load_error_type(bot: Bot) -> None:
    with pytest.raises(TypeError):
        bot.load_plugins(type)  # type: ignore

    with pytest.raises(TypeError):
        bot.load_plugins(object)  # type: ignore


def test_plugin_load_from_module_name() -> None:
    bot = Bot()
    bot.load_plugins("plugins.plugin1", "plugins.plugin2")

    assert bot.get_plugin("Plugin1")
    assert bot.get_plugin("Plugin2")

    with pytest.raises(LookupError):
        bot.get_plugin("NoSuchPlugin")


def test_plugin_load_from_module_name_error(bot: Bot) -> None:
    with pytest.raises(ImportError):
        bot.load_plugins("bad_plugins.plugin_raise_error")


def test_plugin_load_from_file() -> None:
    bot = Bot()
    bot.load_plugins(
        Path("plugins/plugin1.py"),
        Path("plugins/plugin2/__init__.py"),
    )

    assert bot.get_plugin("Plugin1")
    assert bot.get_plugin("Plugin2")

    with pytest.raises(LookupError):
        bot.get_plugin("NoSuchPlugin")


def test_plugin_load_from_file_error(bot: Bot) -> None:
    with pytest.raises(LoadModuleError):
        bot.load_plugins(Path("plugins/plugin3.py"))

    with pytest.raises(LoadModuleError):
        bot.load_plugins(Path("bad_plugins/plugin_error_ext.txt"))


def test_plugin_load_from_dir() -> None:
    bot = Bot()
    bot.load_plugins_from_dirs(Path("plugins"))

    assert bot.get_plugin("Plugin1")
    assert bot.get_plugin("Plugin2")

    with pytest.raises(LookupError):
        bot.get_plugin("NoSuchPlugin")


def test_plugin_load_from_dir_then_from_file() -> None:
    bot = Bot()
    bot.load_plugins_from_dirs(Path("plugins"))

    assert bot.get_plugin("Plugin1")
    assert bot.get_plugin("Plugin2")

    with pytest.raises(LookupError):
        bot.get_plugin("NoSuchPlugin")

    bot.load_plugins(
        Path("plugins/plugin1.py"),
        Path("plugins/plugin2/__init__.py"),
    )

    assert bot.get_plugin("Plugin1")
    assert bot.get_plugin("Plugin2")

    with pytest.raises(LookupError):
        bot.get_plugin("NoSuchPlugin")


def test_plugin_load_from_dir_then_from_file_error(
    bot: Bot, monkeypatch: pytest.MonkeyPatch
) -> None:
    bot.load_plugins_from_dirs(Path("plugins"))

    def raise_oserror(*_args: Any) -> NoReturn:
        raise OSError

    with monkeypatch.context() as m:
        m.setattr(Path, "resolve", raise_oserror)
        with pytest.raises(OSError):  # noqa: PT011
            bot.load_plugins(Path("plugins/plugin1.py"))


def test_reload_plugin() -> None:
    bot = Bot()
    bot.load_plugins("plugins.plugin1", "plugins.plugin2")

    plugin_1 = bot.get_plugin("Plugin1")
    plugin_2 = bot.get_plugin("Plugin2")
    assert plugin_1
    assert plugin_2

    bot.reload_plugins()

    new_plugin_1 = bot.get_plugin("Plugin1")
    new_plugin_2 = bot.get_plugin("Plugin2")
    assert new_plugin_1
    assert new_plugin_2
