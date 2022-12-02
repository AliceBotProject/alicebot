"""AliceBot 机器人对象。

AliceBot 的基础模块，每一个 AliceBot 机器人即是一个 `Bot` 实例。
"""
import os
import sys
import json
import time
import signal
import asyncio
import threading
from pathlib import Path
from itertools import chain
from collections import defaultdict
from typing import Any, Dict, List, Type, Union, Callable, Optional, Awaitable

from pydantic import ValidationError, create_model

from alicebot.adapter import Adapter
from alicebot.plugin import Plugin, PluginLoadType
from alicebot.log import logger, error_or_exception
from alicebot.config import MainConfig, ConfigModel, PluginConfig, AdapterConfig
from alicebot.typing import (
    T_Event,
    T_BotHook,
    T_EventHook,
    T_AdapterHook,
    T_BotExitHook,
)
from alicebot.exceptions import (
    SkipException,
    StopException,
    GetEventTimeout,
    LoadModuleError,
)
from alicebot.utils import (
    ModulePathFinder,
    samefile,
    is_config_class,
    sync_func_wrapper,
    get_classes_from_dir,
    get_classes_from_module_name,
)

try:
    import tomllib  # noqa
except ModuleNotFoundError:
    import tomli as tomllib

__all__ = ["Bot"]

HANDLED_SIGNALS = (
    signal.SIGINT,  # Unix signal 2. Sent by Ctrl+C.
    signal.SIGTERM,  # Unix signal 15. Sent by `kill <pid>`.
)


class Bot:
    """AliceBot 机器人对象，定义了机器人的基本方法。
        读取并储存配置 `Config`，加载适配器 `Adapter` 和插件 `Plugin`，并进行事件分发。

    Attributes:
        config: 机器人配置。
        should_exit: 机器人是否应该进入准备退出状态。
        adapters: 当前已经加载的适配器的列表。
        plugins_priority_dict: 插件优先级字典。
        plugin_state: 插件状态。
        global_state: 全局状态。
    """

    config: MainConfig
    should_exit: asyncio.Event
    adapters: List[Adapter]
    plugins_priority_dict: Dict[int, List[Type[Plugin]]]
    plugin_state: Dict[str, Any]
    global_state: Dict[Any, Any]

    _condition: asyncio.Condition  # 用于处理 get 的 Condition
    _current_event: T_Event  # 当前待处理的 Event

    _restart_flag: bool  # 重新启动标志
    _module_path_finder: ModulePathFinder  # 用于查找 plugins 的模块元路径查找器
    _raw_config_dict: Dict[str, Any]  # 原始配置字典

    # 以下属性不会在重启时清除
    _config_file: Optional[str]  # 配置文件
    _config_dict: Optional[Dict[str, Any]]  # 配置字典
    _hot_reload: bool  # 热重载

    _extend_plugins: List[
        Union[Type[Plugin], str, Path]
    ]  # 使用 load_plugins() 方法程序化加载的插件列表
    _extend_plugin_dirs: List[Path]  # 使用 load_plugins_from_dirs() 方法程序化加载的插件路径列表
    _extend_adapters: List[str]  # 使用 load_adapter() 方法程序化加载的适配器列表
    _bot_run_hooks: List[T_BotHook]
    _bot_exit_hooks: List[T_BotExitHook]
    _adapter_startup_hooks: List[T_AdapterHook]
    _adapter_run_hooks: List[T_AdapterHook]
    _adapter_shutdown_hooks: List[T_AdapterHook]
    _event_preprocessor_hooks: List[T_EventHook]
    _event_postprocessor_hooks: List[T_EventHook]

    def __init__(
        self,
        *,
        config_file: Optional[str] = "config.toml",
        config_dict: Optional[Dict] = None,
        hot_reload: bool = False,
    ):
        """初始化 AliceBot ，读取配置文件，创建配置，加载适配器和插件。

        Args:
            config_file: 配置文件，如不指定则使用默认的 `config.toml`。
                若指定为 None，则不加载配置文件。
            config_dict: 配置字典，默认为 None。
                若指定字典，则会忽略 config_file 配置，不再读取配置文件。
            hot_reload: 热重载。
                启用后将自动检查 `plugin_dir` 中的插件文件更新，并在更新时自动重新加载。
        """
        self.config = MainConfig()
        self.plugins_priority_dict = defaultdict(list)
        self.plugin_state = defaultdict(type(None))
        self.global_state = {}

        self.adapters = []
        self._restart_flag = False
        self._module_path_finder = ModulePathFinder()
        self._raw_config_dict = {}

        self._config_file = config_file
        self._config_dict = config_dict
        self._hot_reload = hot_reload

        self._extend_plugins = []
        self._extend_plugin_dirs = []
        self._extend_adapters = []
        self._bot_run_hooks = []
        self._bot_exit_hooks = []
        self._adapter_startup_hooks = []
        self._adapter_run_hooks = []
        self._adapter_shutdown_hooks = []
        self._event_preprocessor_hooks = []
        self._event_postprocessor_hooks = []

        sys.meta_path.insert(0, self._module_path_finder)

    @property
    def plugins(self) -> List[Type[Plugin]]:
        """当前已经加载的插件的列表。"""
        return list(chain(*self.plugins_priority_dict.values()))

    def run(self):
        """运行 AliceBot，监听并拦截系统退出信号，更新机器人配置。"""
        self._restart_flag = True
        while self._restart_flag:
            self._restart_flag = False
            asyncio.run(self._run())
            if self._restart_flag:
                self._load_plugins_from_dirs(*self._extend_plugin_dirs)
                self._load_plugins(*self._extend_plugins)
                self._load_adapters(*self._extend_adapters)

    def restart(self):
        """退出并重新运行 AliceBot。"""
        logger.info("Restarting AliceBot...")
        self._restart_flag = True
        self.should_exit.set()

    async def _run(self):
        """运行 AliceBot。"""
        self.should_exit = asyncio.Event()
        self._condition = asyncio.Condition()

        # 监听并拦截系统退出信号，从而完成一些善后工作后再关闭程序
        if threading.current_thread() is threading.main_thread():
            # Signal 仅能在主线程中被处理。
            try:
                loop = asyncio.get_running_loop()
                for sig in HANDLED_SIGNALS:
                    loop.add_signal_handler(sig, self._handle_exit)
            except NotImplementedError:
                # add_signal_handler 仅在 Unix 下可用，以下对于 Windows。
                for sig in HANDLED_SIGNALS:
                    signal.signal(sig, self._handle_exit)

        # 加载配置文件
        self._reload_config_dict()

        # 加载插件和适配器
        self._load_plugins_from_dirs(*self.config.bot.plugin_dirs)
        self._load_plugins(*self.config.bot.plugins)
        self._load_adapters(*self.config.bot.adapters)
        self._update_config()

        # 启动 AliceBot
        logger.info("Running AliceBot...")

        hot_reload_task = None
        if self._hot_reload:
            hot_reload_task = asyncio.create_task(self._run_hot_reload())

        for _hook_func in self._bot_run_hooks:
            await _hook_func(self)

        try:
            for _adapter in self.adapters:
                for _hook_func in self._adapter_startup_hooks:
                    await _hook_func(_adapter)
                try:
                    await _adapter.startup()
                except Exception as e:
                    error_or_exception(
                        f"Startup adapter {_adapter!r} failed:",
                        e,
                        self.config.bot.log.verbose_exception,
                    )

            for _adapter in self.adapters:
                for _hook_func in self._adapter_run_hooks:
                    await _hook_func(_adapter)
                asyncio.create_task(_adapter.safe_run())

            await self.should_exit.wait()

            if hot_reload_task is not None:
                await hot_reload_task
        finally:
            for _adapter in self.adapters:
                for _hook_func in self._adapter_shutdown_hooks:
                    await _hook_func(_adapter)
                await _adapter.shutdown()
            for _hook_func in self._bot_exit_hooks:
                _hook_func(self)

            self.adapters.clear()
            self.plugins_priority_dict.clear()
            self._module_path_finder.path.clear()

    def _remove_plugin_by_path(self, file: str) -> List[Type[Plugin]]:
        """根据路径删除已加载的插件。"""
        removed_plugins: List[Type[Plugin]] = []
        for plugins in self.plugins_priority_dict.values():
            _removed_plugins = list(
                filter(
                    lambda x: x.__plugin_load_type__ != PluginLoadType.CLASS
                    and x.__plugin_file_path__ is not None
                    and samefile(x.__plugin_file_path__, file),
                    plugins,
                )
            )
            removed_plugins.extend(_removed_plugins)
            for plugin_ in _removed_plugins:
                plugins.remove(plugin_)
                logger.info(
                    "Succeeded to remove plugin "
                    f'"{plugin_.__name__}" from file "{file}"'
                )
        return removed_plugins

    async def _run_hot_reload(self):
        """热重载。"""
        try:
            from watchfiles import Change, PythonFilter, DefaultFilter, awatch
        except ImportError:
            logger.warning(
                'Hot reload needs to install "watchfiles", '
                'try "pip install watchfiles"'
            )
            return

        logger.info("Hot reload is working!")
        async for changes in awatch(
            *map(
                lambda x: x.resolve(),
                set(self._extend_plugin_dirs)
                .union(self.config.bot.plugin_dirs)
                .union(
                    {Path(self._config_file)}
                    if self._config_dict is None and self._config_file is not None
                    else set()
                ),
            ),
            stop_event=self.should_exit,
        ):
            # 按照 Change.deleted, Change.modified, Change.added 的顺序处理
            # 以确保发生重命名时先处理删除再处理新增
            for change_type, file in sorted(changes, key=lambda x: x[0], reverse=True):
                # 更改配置文件
                if (
                    samefile(self._config_file, file)
                    and change_type == change_type.modified
                ):
                    logger.info(f'Reload config file "{self._config_file}"')
                    old_config = self.config
                    self._reload_config_dict()
                    if self.config.bot != old_config.bot:
                        self.restart()
                    continue

                # 更改插件文件夹
                if change_type == Change.deleted:
                    # 针对删除操作特殊处理
                    if not file.endswith(".py"):
                        file = os.path.join(file, "__init__.py")
                else:
                    if os.path.isdir(file) and os.path.isfile(
                        os.path.join(file, "__init__.py")
                    ):
                        # 当新增一个目录，且此目录中包含 __init__.py 文件
                        # 说明此时发生的是添加一个 Python 包，则视为添加了此包的 __init__.py 文件
                        file = os.path.join(file, "__init__.py")
                    if not (os.path.isfile(file) and file.endswith(".py")):
                        continue

                if change_type == Change.added:
                    logger.info(f"Hot reload: added file: {file}")
                    self._load_plugins(Path(file), plugin_load_type=PluginLoadType.DIR)
                    self._update_config()
                    continue
                elif change_type == Change.deleted:
                    logger.info(f"Hot reload: Deleted file: {file}")
                    self._remove_plugin_by_path(file)
                    self._update_config()
                elif change_type == Change.modified:
                    logger.info(f"Hot reload: Modified file: {file}")
                    self._remove_plugin_by_path(file)
                    self._load_plugins(Path(file), plugin_load_type=PluginLoadType.DIR)
                    self._update_config()

    def _update_config(self):
        """更新 config，合并入来自 Plugin 和 Adapter 的 Config。"""

        def update_config(
            source: List, name: str, base: Type[ConfigModel]
        ) -> ConfigModel:
            config_update_dict = {}
            for i in source:
                config_class = getattr(i, "Config", None)
                if is_config_class(config_class):
                    try:
                        default_value = config_class()
                    except ValidationError:
                        default_value = ...
                    config_update_dict[getattr(config_class, "__config_name__")] = (
                        config_class,
                        default_value,
                    )
            return create_model(name, **config_update_dict, __base__=base)(
                **self._raw_config_dict
            )

        self.config = create_model(
            "Config",
            plugin=update_config(self.plugins, "PluginConfig", PluginConfig),
            adapter=update_config(self.adapters, "AdapterConfig", AdapterConfig),
            __base__=MainConfig,
        )(**self._raw_config_dict)
        # 更新 log 级别
        logger.remove()
        logger.add(sys.stderr, level=self.config.bot.log.level)

    def _reload_config_dict(self):
        """重新加载配置文件。"""
        self._raw_config_dict = {}
        if self._config_dict is not None:
            self._raw_config_dict = self._config_dict
        elif self._config_file is not None:
            try:
                with open(self._config_file, "rb") as f:
                    if self._config_file.endswith(".json"):
                        self._raw_config_dict = json.load(f)
                    elif self._config_file.endswith(".toml"):
                        self._raw_config_dict = tomllib.load(f)
                    else:
                        logger.error("Unable to determine config file type")
            except OSError as e:
                error_or_exception(
                    "Can not open config file:",
                    e,
                    self.config.bot.log.verbose_exception,
                )
            except (ValueError, json.JSONDecodeError, tomllib.TOMLDecodeError) as e:
                error_or_exception(
                    "Read config file failed:", e, self.config.bot.log.verbose_exception
                )

        try:
            self.config = MainConfig(**self._raw_config_dict)
        except ValidationError as e:
            self.config = MainConfig()
            error_or_exception(
                "Config dict parse error:", e, self.config.bot.log.verbose_exception
            )
        self._update_config()

    def reload_plugins(self):
        """手动重新加载所有插件。"""
        self.plugins_priority_dict.clear()
        self._load_plugins(*self.config.bot.plugins)
        self._load_plugins_from_dirs(*self.config.bot.plugin_dirs)
        self._load_plugins(*self._extend_plugins)
        self._load_plugins_from_dirs(*self._extend_plugin_dirs)
        self._update_config()

    def _handle_exit(self, *args):  # noqa
        """当机器人收到退出信号时，根据情况进行处理。"""
        logger.info("Stopping AliceBot...")
        if self.should_exit.is_set():
            logger.warning("Force Exit AliceBot...")
            sys.exit()
        else:
            self.should_exit.set()

    async def handle_event(
        self, current_event: T_Event, *, handle_get: bool = True, show_log: bool = True
    ):
        """被适配器对象调用，根据优先级分发事件给所有插件，并处理插件的 `stop` 、 `skip` 等信号。

        此方法不应该被用户手动调用。

        Args:
            current_event: 当前待处理的 `Event`。
            handle_get: 当前事件是否可以被 get 方法捕获，默认为 True。
            show_log: 是否在日志中显示，默认为 True。
        """
        if show_log:
            logger.info(
                f"Adapter {current_event.adapter.name} received: {current_event!r}"
            )

        if handle_get:
            asyncio.create_task(self._handle_event())
            await asyncio.sleep(0)
            async with self._condition:
                self._current_event = current_event
                self._condition.notify_all()
        else:
            asyncio.create_task(self._handle_event(current_event))

    async def _handle_event(self, current_event: Optional[T_Event] = None):
        if current_event is None:
            async with self._condition:
                await self._condition.wait()
                current_event = self._current_event
            if current_event.__handled__:
                return

        for _hook_func in self._event_preprocessor_hooks:
            await _hook_func(current_event)

        for plugin_priority in sorted(self.plugins_priority_dict.keys()):
            try:
                logger.debug(
                    f"Checking for matching plugins with priority {plugin_priority!r}"
                )
                stop = False
                for _plugin in self.plugins_priority_dict[plugin_priority]:
                    try:
                        _plugin = _plugin(current_event)
                        if await _plugin.rule():
                            logger.info(f"Event will be handled by {_plugin!r}")
                            try:
                                await _plugin.handle()
                            finally:
                                if _plugin.block:
                                    stop = True
                    except SkipException:
                        # 插件要求跳过自身继续当前事件传播
                        continue
                    except StopException:
                        # 插件要求停止当前事件传播
                        stop = True
                    except Exception as e:
                        error_or_exception(
                            f'Exception in plugin "{_plugin}":',
                            e,
                            self.config.bot.log.verbose_exception,
                        )
                if stop:
                    break
            except Exception as e:
                error_or_exception(
                    f"Exception in handling event {current_event!r}:",
                    e,
                    self.config.bot.log.verbose_exception,
                )

        for _hook_func in self._event_postprocessor_hooks:
            await _hook_func(current_event)

        logger.info("Event Finished")

    async def get(
        self,
        func: Optional[Callable[[T_Event], Union[bool, Awaitable[bool]]]] = None,
        *,
        max_try_times: Optional[int] = None,
        timeout: Optional[Union[int, float]] = None,
    ) -> T_Event:
        """获取满足指定条件的的事件，协程会等待直到适配器接收到满足条件的事件、超过最大事件数或超时。

        Args:
            func: 协程或者函数，函数会被自动包装为协程执行。
                要求接受一个事件作为参数，返回布尔值。当协程返回 `True` 时返回当前事件。
                当为 `None` 时相当于输入对于任何事件均返回真的协程，即返回适配器接收到的下一个事件。
            max_try_times: 最大事件数。
            timeout: 超时时间。

        Returns:
            返回满足 func 条件的事件。

        Raises:
            GetEventTimeout: 超过最大事件数或超时。
        """
        if func is None:
            func = sync_func_wrapper(lambda x: True)
        elif not asyncio.iscoroutinefunction(func):
            func = sync_func_wrapper(func)

        try_times = 0
        start_time = time.time()
        while not self.should_exit.is_set():
            if max_try_times is not None and try_times > max_try_times:
                break
            if timeout is not None and time.time() - start_time > timeout:
                break

            async with self._condition:
                if timeout is None:
                    await self._condition.wait()
                else:
                    try:
                        await asyncio.wait_for(
                            self._condition.wait(),
                            timeout=start_time + timeout - time.time(),
                        )
                    except asyncio.TimeoutError:
                        break

                if not self._current_event.__handled__:
                    if await func(self._current_event):
                        self._current_event.__handled__ = True
                        return self._current_event

                try_times += 1

        if not self.should_exit.is_set():
            raise GetEventTimeout

    def _load_plugin_class(
        self,
        plugin_class: Type[Plugin],
        plugin_load_type: PluginLoadType,
        plugin_file_path: Optional[str],
    ):
        """加载插件类。"""
        priority = getattr(plugin_class, "priority", None)
        if type(priority) is int and priority >= 0:
            for _plugin in self.plugins:
                if _plugin.__name__ == plugin_class.__name__:
                    logger.warning(
                        f'Already have a same name plugin "{_plugin.__name__}"'
                    )
            plugin_class.__plugin_load_type__ = plugin_load_type
            plugin_class.__plugin_file_path__ = plugin_file_path
            self.plugins_priority_dict[priority].append(plugin_class)
            logger.info(
                f'Succeeded to load plugin "{plugin_class.__name__}" '
                f'from class "{plugin_class!r}"'
            )
        else:
            error_or_exception(
                f'Load plugin from class "{plugin_class!r}" failed:',
                LoadModuleError(
                    f'Plugin priority incorrect in the class "{plugin_class!r}"'
                ),
                self.config.bot.log.verbose_exception,
            )

    def _load_plugins_from_module_name(
        self, module_name: str, plugin_load_type: PluginLoadType
    ):
        """从模块名称中插件模块。"""
        try:
            plugin_classes = get_classes_from_module_name(module_name, Plugin)
        except ImportError as e:
            error_or_exception(
                f'Import module "{module_name}" failed:',
                e,
                self.config.bot.log.verbose_exception,
            )
        else:
            for plugin_class, module in plugin_classes:
                self._load_plugin_class(
                    plugin_class,
                    plugin_load_type,
                    module.__file__,
                )

    def _load_plugins(
        self,
        *plugins: Union[Type[Plugin], str, Path],
        plugin_load_type: Optional[PluginLoadType] = None,
    ):
        """加载插件。

        Args:
            *plugins: 插件类、插件模块名称或者插件模块文件路径。类型可以是 `Type[Plugin]`, `str` 或 `pathlib.Path`。
                如果为 `Type[Plugin]` 类型时，将作为插件类进行加载。
                如果为 `str` 类型时，将作为插件模块名称进行加载，格式和 Python `import` 语句相同。
                    例如：`path.of.plugin`。
                如果为 `pathlib.Path` 类型时，将作为插件模块文件路径进行加载。
                    例如：`pathlib.Path("path/of/plugin")`。
            plugin_load_type: 插件加载类型，如果为 None 则自动判断，否则使用指定的类型。
        """
        for plugin_ in plugins:
            if isinstance(plugin_, type):
                if issubclass(plugin_, Plugin):
                    self._load_plugin_class(
                        plugin_, plugin_load_type or PluginLoadType.CLASS, None
                    )
                else:
                    logger.error(
                        f'The plugin class "{plugin_!r}" must be a subclass of Plugin'
                    )
            elif isinstance(plugin_, str):
                logger.info(f'Loading plugins from module "{plugin_}"')
                self._load_plugins_from_module_name(
                    plugin_, plugin_load_type or PluginLoadType.NAME
                )
            elif isinstance(plugin_, Path):
                logger.info(f'Loading plugins from path "{plugin_}"')
                if plugin_.is_file():
                    if plugin_.suffix != ".py":
                        logger.error(f'The path "{plugin_}" must endswith ".py"')
                        return

                    plugin_module_name = None
                    for path in self._module_path_finder.path:
                        try:
                            if plugin_.stem == "__init__":
                                if plugin_.resolve().parent.parent.samefile(Path(path)):
                                    plugin_module_name = plugin_.resolve().parent.name
                                    break
                            elif plugin_.resolve().parent.samefile(Path(path)):
                                plugin_module_name = plugin_.stem
                                break
                        except OSError:
                            continue
                    if plugin_module_name is None:
                        rel_path = plugin_.resolve().relative_to(Path(".").resolve())
                        if rel_path.stem == "__init__":
                            plugin_module_name = ".".join(rel_path.parts[:-1])
                        else:
                            plugin_module_name = ".".join(
                                rel_path.parts[:-1] + (rel_path.stem,)
                            )

                    self._load_plugins_from_module_name(
                        plugin_module_name, plugin_load_type or PluginLoadType.FILE
                    )
                else:
                    logger.error(f'The plugin path "{plugin_}" must be a file')
            else:
                logger.error(f"Type error: {plugin_} can not be loaded as plugin")

    def load_plugins(self, *plugins: Union[Type[Plugin], str, Path]):
        """加载插件。

        Args:
            *plugins: 插件类、插件模块名称或者插件模块文件路径。类型可以是 `Type[Plugin]`, `str` 或 `pathlib.Path`。
                如果为 `Type[Plugin]` 类型时，将作为插件类进行加载。
                如果为 `str` 类型时，将作为插件模块名称进行加载，格式和 Python `import` 语句相同。
                    例如：`path.of.plugin`。
                如果为 `pathlib.Path` 类型时，将作为插件模块文件路径进行加载。
                    例如：`pathlib.Path("path/of/plugin")`。
        """
        self._extend_plugins.extend(plugins)
        return self._load_plugins(*plugins)

    def _load_plugins_from_dirs(self, *dirs: Path):
        """从目录中加载插件，以 `_` 开头的模块中的插件不会被导入。路径可以是相对路径或绝对路径。

        Args:
            *dirs: 储存包含插件的模块的模块路径。
                例如：`pathlib.Path("path/of/plugins/")` 。
        """
        dirs = list(map(lambda x: str(x.resolve()), dirs))
        logger.info(f'Loading plugins from dirs "{", ".join(map(str, dirs))}"')
        self._module_path_finder.path.extend(dirs)
        for plugin_class, module in get_classes_from_dir(dirs, Plugin):
            self._load_plugin_class(plugin_class, PluginLoadType.DIR, module.__file__)

    def load_plugins_from_dirs(self, *dirs: Path):
        """从目录中加载插件，以 `_` 开头的模块中的插件不会被导入。路径可以是相对路径或绝对路径。

        Args:
            *dirs: 储存包含插件的模块的模块路径。
                例如：`pathlib.Path("path/of/plugins/")` 。
        """
        self._extend_plugin_dirs.extend(dirs)
        self._load_plugins_from_dirs(*dirs)

    def _load_adapters(self, *adapters: Union[Type[Adapter], str]):
        """加载适配器。

        Args:
            *adapters: 适配器类或适配器名称，类型可以是 `Type[Adapter]` 或 `str`。
                如果为 `Type[Adapter]` 类型时，将作为适配器类进行加载。
                如果为 `str` 类型时，将作为适配器模块名称进行加载，格式和 Python `import` 语句相同。
                    例如：`path.of.adapter`。
        """
        for adapter_ in adapters:
            try:
                if isinstance(adapter_, type):
                    if issubclass(adapter_, Adapter):
                        adapter_object = adapter_(self)
                    else:
                        raise LoadModuleError(
                            f'The Adapter class "{adapter_!r}" '
                            "must be a subclass of Adapter"
                        )
                elif isinstance(adapter_, str):
                    adapter_classes = get_classes_from_module_name(adapter_, Adapter)
                    if not adapter_classes:
                        raise LoadModuleError(
                            f"Can not find Adapter class in the {adapter_} module"
                        )
                    elif len(adapter_classes) > 1:
                        raise LoadModuleError(
                            f"More then one Adapter class in the {adapter_} module"
                        )
                    adapter_object = adapter_classes[0][0](self)
                else:
                    raise LoadModuleError(
                        f"Type error: {adapter_} can not be loaded as adapter"
                    )
            except Exception as e:
                error_or_exception(
                    f'Load adapter "{adapter_}" failed:',
                    e,
                    self.config.bot.log.verbose_exception,
                )
            else:
                self.adapters.append(adapter_object)
                logger.info(
                    f'Succeeded to load adapter "{adapter_object.__class__.__name__}" '
                    f'from "{adapter_}"'
                )

    def load_adapters(self, *adapters: Union[Type[Adapter], str]):
        """加载适配器。

        Args:
            *adapters: 适配器类或适配器名称，类型可以是 `Type[Adapter]` 或 `str`。
                如果为 `Type[Adapter]` 类型时，将作为适配器类进行加载。
                如果为 `str` 类型时，将作为适配器模块名称进行加载，格式和 Python `import` 语句相同。
                    例如：`path.of.adapter`。
        """
        self._extend_adapters.extend(adapters)
        return self._load_adapters(*adapters)

    def get_adapter(self, name: str) -> Adapter:
        """按照名称获取已经加载的适配器。

        Args:
            name: 适配器名称。

        Returns:
            获取到的适配器对象。

        Raises:
            LookupError: 找不到此名称的适配器对象。
        """
        for _adapter in self.adapters:
            if _adapter.name == name:
                return _adapter
        raise LookupError(f'Can not find adapter named "{name}"')

    def get_plugin(self, name: str) -> Type[Plugin]:
        """按照名称获取已经加载的插件类。

        Args:
            name: 插件名称

        Returns:
            获取到的插件类。

        Raises:
            LookupError: 找不到此名称的插件类。
        """
        for _plugin in self.plugins:
            if _plugin.name == name:
                return _plugin
        raise LookupError(f'Can not find plugin named "{name}"')

    def bot_run_hook(self, func: T_BotHook) -> T_BotHook:
        """注册一个 Bot 启动时的函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._bot_run_hooks.append(func)
        return func

    def bot_exit_hook(self, func: T_BotExitHook) -> T_BotExitHook:
        """注册一个 Bot 退出时的函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._bot_exit_hooks.append(func)
        return func

    def adapter_startup_hook(self, func: T_AdapterHook) -> T_AdapterHook:
        """注册一个适配器初始化时的函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._adapter_startup_hooks.append(func)
        return func

    def adapter_run_hook(self, func: T_AdapterHook) -> T_AdapterHook:
        """注册一个适配器运行时的函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._adapter_run_hooks.append(func)
        return func

    def adapter_shutdown_hook(self, func: T_AdapterHook) -> T_AdapterHook:
        """注册一个适配器关闭时的函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._adapter_shutdown_hooks.append(func)
        return func

    def event_preprocessor_hook(self, func: T_EventHook) -> T_EventHook:
        """注册一个事件预处理函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._event_preprocessor_hooks.append(func)
        return func

    def event_postprocessor_hook(self, func: T_EventHook) -> T_EventHook:
        """注册一个事件后处理函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._event_postprocessor_hooks.append(func)
        return func
