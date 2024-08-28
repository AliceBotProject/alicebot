"""AliceBot 机器人对象。

AliceBot 的基础模块，每一个 AliceBot 机器人即是一个 `Bot` 实例。
"""

import json
import pkgutil
import signal
import sys
import threading
import time
from collections import defaultdict
from collections.abc import Awaitable
from contextlib import AsyncExitStack
from itertools import chain
from pathlib import Path
from typing import Any, Callable, Optional, Union, overload

import anyio
import structlog
from anyio.abc import TaskStatus
from anyio.streams.memory import MemoryObjectReceiveStream, MemoryObjectSendStream
from pydantic import ValidationError, create_model

from alicebot.adapter import Adapter
from alicebot.config import AdapterConfig, ConfigModel, MainConfig, PluginConfig
from alicebot.dependencies import solve_dependencies
from alicebot.event import Event, EventHandleOption
from alicebot.exceptions import (
    GetEventTimeout,
    LoadModuleError,
    SkipException,
    StopException,
)
from alicebot.plugin import Plugin, PluginLoadType
from alicebot.typing import AdapterHook, AdapterT, BotHook, EventHook, EventT
from alicebot.utils import (
    ModulePathFinder,
    get_classes_from_module_name,
    is_config_class,
    samefile,
    wrap_get_func,
)

if sys.version_info >= (3, 11):  # pragma: no cover
    import tomllib
else:  # pragma: no cover
    import tomli as tomllib


__all__ = ["Bot"]

HANDLED_SIGNALS = (
    signal.SIGINT,  # Unix signal 2. Sent by Ctrl+C.
    signal.SIGTERM,  # Unix signal 15. Sent by `kill <pid>`.
)

logger = structlog.stdlib.get_logger()


class Bot:
    """AliceBot 机器人对象，定义了机器人的基本方法。

    读取并储存配置 `Config`，加载适配器 `Adapter` 和插件 `Plugin`，并进行事件分发。

    Attributes:
        config: 机器人配置。
        adapters: 当前已经加载的适配器的列表。
        plugins_priority_dict: 插件优先级字典。
        plugin_state: 插件状态。
        global_state: 全局状态。
    """

    config: MainConfig
    adapters: list[Adapter[Any, Any]]
    plugins_priority_dict: dict[int, list[type[Plugin[Any, Any, Any]]]]
    plugin_state: dict[str, Any]
    global_state: dict[Any, Any]

    _event_send_stream: MemoryObjectSendStream[EventHandleOption]  # pyright: ignore[reportUninitializedInstanceVariable]
    _event_receive_stream: MemoryObjectReceiveStream[EventHandleOption]  # pyright: ignore[reportUninitializedInstanceVariable]
    _condition: anyio.Condition  # 用于处理 get 的 Condition # pyright: ignore[reportUninitializedInstanceVariable]
    _current_event: Optional[Event[Any]]  # 当前待处理的 Event

    _should_exit: anyio.Event  # 机器人是否应该进入准备退出状态 # pyright: ignore[reportUninitializedInstanceVariable]
    _restart_flag: bool  # 重新启动标志
    _module_path_finder: ModulePathFinder  # 用于查找 plugins 的模块元路径查找器
    _raw_config_dict: dict[str, Any]  # 原始配置字典

    # 以下属性不会在重启时清除
    _config_file: Optional[str]  # 配置文件
    _config_dict: Optional[dict[str, Any]]  # 配置字典
    _hot_reload: bool  # 热重载
    _handle_signals: bool  # 处理信号

    _extend_plugins: list[
        Union[type[Plugin[Any, Any, Any]], str, Path]
    ]  # 使用 load_plugins() 方法程序化加载的插件列表
    _extend_plugin_dirs: list[
        Path
    ]  # 使用 load_plugins_from_dirs() 方法程序化加载的插件路径列表
    _extend_adapters: list[
        Union[type[Adapter[Any, Any]], str]
    ]  # 使用 load_adapter() 方法程序化加载的适配器列表
    _bot_run_hooks: list[BotHook]
    _bot_exit_hooks: list[BotHook]
    _adapter_startup_hooks: list[AdapterHook]
    _adapter_run_hooks: list[AdapterHook]
    _adapter_shutdown_hooks: list[AdapterHook]
    _event_preprocessor_hooks: list[EventHook]
    _event_postprocessor_hooks: list[EventHook]

    def __init__(
        self,
        *,
        config_file: Optional[str] = "config.toml",
        config_dict: Optional[dict[str, Any]] = None,
        hot_reload: bool = False,
        handle_signals: bool = True,
    ) -> None:
        """初始化 AliceBot，读取配置文件，创建配置，加载适配器和插件。

        Args:
            config_file: 配置文件，如不指定则使用默认的 `config.toml`。
                若指定为 `None`，则不加载配置文件。
            config_dict: 配置字典，默认为 `None。`
                若指定字典，则会忽略 `config_file` 配置，不再读取配置文件。
            hot_reload: 热重载。
                启用后将自动检查 `plugin_dir` 中的插件文件更新，并在更新时自动重新加载。
            handle_signals: 是否处理系统信号，默认为 `True`。
        """
        self.config = MainConfig()
        self.plugins_priority_dict = defaultdict(list)
        self.plugin_state = defaultdict(lambda: None)
        self.global_state = {}

        self.adapters = []
        self._current_event = None
        self._restart_flag = False
        self._module_path_finder = ModulePathFinder()
        self._raw_config_dict = {}

        self._config_file = config_file
        self._config_dict = config_dict
        self._hot_reload = hot_reload
        self._handle_signals = handle_signals

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
    def plugins(self) -> list[type[Plugin[Any, Any, Any]]]:
        """当前已经加载的插件的列表。"""
        return list(chain(*self.plugins_priority_dict.values()))

    def run(self) -> None:
        """运行 AliceBot，监听并拦截系统退出信号，更新机器人配置。"""
        anyio.run(self.run_async)

    def restart(self) -> None:
        """退出并重新运行 AliceBot。"""
        logger.info("Restarting AliceBot...")
        self._restart_flag = True
        self._should_exit.set()

    def exit(self) -> None:
        """退出 AliceBot。"""
        logger.info("Exiting AliceBot...")
        self._should_exit.set()

    async def run_async(self) -> None:
        """异步运行 AliceBot。"""
        self._restart_flag = True
        while self._restart_flag:
            self._restart_flag = False
            await self._init()
            async with anyio.create_task_group() as tg:
                tg.start_soon(self._run)
                tg.start_soon(self._handle_event_receive)
                tg.start_soon(self._handle_should_exit, tg.cancel_scope)
                if self._handle_signals:  # pragma: no cover
                    tg.start_soon(self._handle_exit_signal)
                if self._hot_reload:  # pragma: no cover
                    tg.start_soon(self._run_hot_reload)
            if self._restart_flag:
                self._load_plugins_from_dirs(*self._extend_plugin_dirs)
                self._load_plugins(*self._extend_plugins)
                self._load_adapters(*self._extend_adapters)

    async def _init(self) -> None:
        """初始化 AliceBot。"""
        self._should_exit = anyio.Event()
        self._condition = anyio.Condition()
        self._event_send_stream, self._event_receive_stream = (
            anyio.create_memory_object_stream()
        )

        # 加载配置文件
        self._reload_config_dict()

        # 加载插件和适配器
        self._load_plugins_from_dirs(*self.config.bot.plugin_dirs)
        self._load_plugins(*self.config.bot.plugins)
        self._load_adapters(*self.config.bot.adapters)
        self._update_config()

    async def _run(self) -> None:
        """运行 AliceBot。"""
        logger.info("Running AliceBot...")

        for bot_run_hook_func in self._bot_run_hooks:
            await bot_run_hook_func(self)

        try:
            for _adapter in self.adapters:
                for adapter_startup_hook_func in self._adapter_startup_hooks:
                    await adapter_startup_hook_func(_adapter)
                try:
                    await _adapter.startup()
                except Exception:
                    logger.exception("Startup adapter failed", adapter=_adapter)

            async with anyio.create_task_group() as tg:
                for _adapter in self.adapters:
                    for adapter_run_hook_func in self._adapter_run_hooks:
                        await adapter_run_hook_func(_adapter)
                    tg.start_soon(_adapter.safe_run)

            await self._should_exit.wait()
        finally:
            for _adapter in self.adapters:
                for adapter_shutdown_hook_func in self._adapter_shutdown_hooks:
                    await adapter_shutdown_hook_func(_adapter)
                await _adapter.shutdown()

            for bot_exit_hook_func in self._bot_exit_hooks:
                await bot_exit_hook_func(self)

            self.adapters.clear()
            self.plugins_priority_dict.clear()
            self._module_path_finder.path.clear()

    def _remove_plugin_by_path(
        self, file: Path
    ) -> list[type[Plugin[Any, Any, Any]]]:  # pragma: no cover
        """根据路径删除已加载的插件。"""
        removed_plugins: list[type[Plugin[Any, Any, Any]]] = []
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
                    "Succeeded to remove plugin from file", plugin=plugin_, file=file
                )
        return removed_plugins

    async def _run_hot_reload(self) -> None:  # pragma: no cover
        """热重载。"""
        try:
            from watchfiles import Change, awatch
        except ImportError:
            logger.warning(
                'Hot reload needs to install "watchfiles", try "pip install watchfiles"'
            )
            return

        logger.info("Hot reload is working!")
        async for changes in awatch(
            *(
                x.resolve()
                for x in set(self._extend_plugin_dirs)
                .union(self.config.bot.plugin_dirs)
                .union(
                    {Path(self._config_file)}
                    if self._config_dict is None and self._config_file is not None
                    else set()
                )
            ),
            stop_event=self._should_exit,
        ):
            # 按照 Change.deleted, Change.modified, Change.added 的顺序处理
            # 以确保发生重命名时先处理删除再处理新增
            for change_type, file_ in sorted(changes, key=lambda x: x[0], reverse=True):
                file = Path(file_)
                # 更改配置文件
                if (
                    self._config_file is not None
                    and samefile(self._config_file, file)
                    and change_type == change_type.modified
                ):
                    logger.info("Reload config file", file=self._config_file)
                    old_config = self.config
                    self._reload_config_dict()
                    if (
                        self.config.bot != old_config.bot
                        or self.config.adapter != old_config.adapter
                    ):
                        self.restart()
                    continue

                # 更改插件文件夹
                if change_type == Change.deleted:
                    # 针对删除操作特殊处理
                    if file.suffix != ".py":
                        file = file / "__init__.py"
                else:
                    if file.is_dir() and (file / "__init__.py").is_file():
                        # 当新增一个目录，且此目录中包含 __init__.py 文件
                        # 说明此时发生的是添加一个 Python 包，则视为添加了此包的 __init__.py 文件
                        file = file / "__init__.py"
                    if not (file.is_file() and file.suffix == ".py"):
                        continue

                if change_type == Change.added:
                    logger.info("Hot reload: Added file", file=file)
                    self._load_plugins(
                        Path(file), plugin_load_type=PluginLoadType.DIR, reload=True
                    )
                    self._update_config()
                    continue
                if change_type == Change.deleted:
                    logger.info("Hot reload: Deleted file", file=file)
                    self._remove_plugin_by_path(file)
                    self._update_config()
                elif change_type == Change.modified:
                    logger.info("Hot reload: Modified file", file=file)
                    self._remove_plugin_by_path(file)
                    self._load_plugins(
                        Path(file), plugin_load_type=PluginLoadType.DIR, reload=True
                    )
                    self._update_config()

    def _update_config(self) -> None:
        """更新 config，合并入来自 Plugin 和 Adapter 的 Config。"""

        def update_config(
            source: Union[list[type[Plugin[Any, Any, Any]]], list[Adapter[Any, Any]]],
            name: str,
            base: type[ConfigModel],
        ) -> tuple[type[ConfigModel], ConfigModel]:
            config_update_dict: dict[str, Any] = {}
            for i in source:
                config_class = getattr(i, "Config", None)
                if is_config_class(config_class):
                    default_value: Any
                    try:
                        default_value = config_class()
                    except ValidationError:
                        default_value = ...
                    config_update_dict[config_class.__config_name__] = (
                        config_class,
                        default_value,
                    )
            config_model = create_model(name, **config_update_dict, __base__=base)
            return config_model, config_model()

        self.config = create_model(
            "Config",
            plugin=update_config(self.plugins, "PluginConfig", PluginConfig),
            adapter=update_config(self.adapters, "AdapterConfig", AdapterConfig),
            __base__=MainConfig,
        )(**self._raw_config_dict)

        if self.config.bot.log is not None:
            log_level = 0
            if isinstance(self.config.bot.log.level, int):
                log_level = self.config.bot.log.level
            elif isinstance(self.config.bot.log.level, str):
                log_level = structlog.processors.NAME_TO_LEVEL[
                    self.config.bot.log.level.lower()
                ]

            wrapper_class = structlog.make_filtering_bound_logger(log_level)

            if not self.config.bot.log.verbose_exception:

                class BoundLoggerWithoutException(wrapper_class):  # type: ignore
                    """用于不记录异常的 wrapper_class。"""

                    exception = wrapper_class.error
                    aexception = wrapper_class.aerror

                wrapper_class = BoundLoggerWithoutException

            structlog.configure(wrapper_class=wrapper_class)

    def _reload_config_dict(self) -> None:
        """重新加载配置文件。"""
        self._raw_config_dict = {}

        if self._config_dict is not None:
            self._raw_config_dict = self._config_dict
        elif self._config_file is not None:
            try:
                with Path(self._config_file).open("rb") as f:
                    if self._config_file.endswith(".json"):
                        self._raw_config_dict = json.load(f)
                    elif self._config_file.endswith(".toml"):
                        self._raw_config_dict = tomllib.load(f)
                    else:
                        logger.error(
                            "Read config file failed: "
                            "Unable to determine config file type"
                        )
            except OSError:
                logger.exception("Can not open config file:")
            except (ValueError, json.JSONDecodeError, tomllib.TOMLDecodeError):
                logger.exception("Read config file failed:")

        try:
            self.config = MainConfig(**self._raw_config_dict)
        except ValidationError:
            self.config = MainConfig()
            logger.exception("Config dict parse error")
        self._update_config()

    def reload_plugins(self) -> None:
        """手动重新加载所有插件。"""
        self.plugins_priority_dict.clear()
        self._load_plugins(*self.config.bot.plugins)
        self._load_plugins_from_dirs(*self.config.bot.plugin_dirs)
        self._load_plugins(*self._extend_plugins)
        self._load_plugins_from_dirs(*self._extend_plugin_dirs)
        self._update_config()

    async def _handle_exit_signal(self) -> None:  # pragma: no cover
        """根据平台不同注册信号处理程序。"""
        if threading.current_thread() is not threading.main_thread():
            # Signal 仅能在主线程中被处理
            return
        try:
            with anyio.open_signal_receiver(*HANDLED_SIGNALS) as signals:
                async for _signal in signals:
                    self._handle_exit()
        except NotImplementedError:
            # add_signal_handler 仅在 Unix 下可用，以下对于 Windows
            for sig in HANDLED_SIGNALS:
                signal.signal(sig, self._handle_exit)

    def _handle_exit(self, *_args: Any) -> None:  # pragma: no cover
        """当机器人收到退出信号时，根据情况进行处理。"""
        logger.info("Stopping AliceBot...")
        if self._should_exit.is_set():
            logger.warning("Force Exit AliceBot...")
            sys.exit()
        else:
            self._should_exit.set()

    async def _handle_should_exit(self, cancel_scope: anyio.CancelScope) -> None:
        """当 should_exit 被设置时取消当前的 task group。"""
        await self._should_exit.wait()
        cancel_scope.cancel()

    async def handle_event(
        self,
        current_event: Event[Any],
        *,
        handle_get: bool = True,
        show_log: bool = True,
    ) -> None:
        """被适配器对象调用，根据优先级分发事件给所有插件，并处理插件的 `stop` 、 `skip` 等信号。

        此方法不应该被用户手动调用。

        Args:
            current_event: 当前待处理的 `Event`。
            handle_get: 当前事件是否可以被 get 方法捕获，默认为 `True`。
            show_log: 是否在日志中显示，默认为 `True`。
        """
        if show_log:
            logger.info(
                "Event received from adapter",
                adapter_name=current_event.adapter.name,
                current_event=current_event,
            )

        await self._event_send_stream.send(
            EventHandleOption(
                event=current_event,
                handle_get=handle_get,
            )
        )

    async def _handle_event_receive(self) -> None:
        async with anyio.create_task_group() as tg, self._event_receive_stream:
            async for current_event, handle_get in self._event_receive_stream:
                if handle_get:
                    await tg.start(self._handle_event_wait_condition)
                    async with self._condition:
                        self._current_event = current_event
                        self._condition.notify_all()
                else:
                    tg.start_soon(self._handle_event, current_event)

    async def _handle_event_wait_condition(
        self, *, task_status: TaskStatus[None] = anyio.TASK_STATUS_IGNORED
    ) -> None:
        async with self._condition:
            task_status.started()
            await self._condition.wait()
            assert self._current_event is not None
            current_event = self._current_event
        await self._handle_event(current_event)

    async def _handle_event(self, current_event: Event[Any]) -> None:
        if current_event.__handled__:
            return

        for _hook_func in self._event_preprocessor_hooks:
            await _hook_func(current_event)

        for plugin_priority in sorted(self.plugins_priority_dict.keys()):
            logger.debug("Checking for matching plugins", priority=plugin_priority)
            stop = False
            for plugin in self.plugins_priority_dict[plugin_priority]:
                try:
                    async with AsyncExitStack() as stack:
                        _plugin = await solve_dependencies(
                            plugin,
                            use_cache=True,
                            stack=stack,
                            dependency_cache={
                                Bot: self,
                                Event: current_event,
                            },
                        )
                        if _plugin.name not in self.plugin_state:
                            plugin_state = _plugin.__init_state__()
                            if plugin_state is not None:
                                self.plugin_state[_plugin.name] = plugin_state
                        if await _plugin.rule():
                            logger.info(
                                "Event will be handled by plugin", plugin=_plugin
                            )
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
                except Exception:
                    logger.exception("Exception in plugin", plugin=plugin)
            if stop:
                break

        for _hook_func in self._event_postprocessor_hooks:
            await _hook_func(current_event)

        logger.info("Event Finished")

    @overload
    async def get(
        self,
        func: Optional[Callable[[Event[Any]], Union[bool, Awaitable[bool]]]] = None,
        *,
        event_type: None = None,
        adapter_type: None = None,
        max_try_times: Optional[int] = None,
        timeout: Optional[Union[int, float]] = None,
    ) -> Event[Any]: ...

    @overload
    async def get(
        self,
        func: Optional[Callable[[EventT], Union[bool, Awaitable[bool]]]] = None,
        *,
        event_type: None = None,
        adapter_type: type[Adapter[EventT, Any]],
        max_try_times: Optional[int] = None,
        timeout: Optional[Union[int, float]] = None,
    ) -> EventT: ...

    @overload
    async def get(
        self,
        func: Optional[Callable[[EventT], Union[bool, Awaitable[bool]]]] = None,
        *,
        event_type: type[EventT],
        adapter_type: Optional[type[AdapterT]] = None,
        max_try_times: Optional[int] = None,
        timeout: Optional[Union[int, float]] = None,
    ) -> EventT: ...

    async def get(
        self,
        func: Optional[Callable[[Any], Union[bool, Awaitable[bool]]]] = None,
        *,
        event_type: Optional[type[Event[Any]]] = None,
        adapter_type: Optional[type[Adapter[Any, Any]]] = None,
        max_try_times: Optional[int] = None,
        timeout: Optional[Union[int, float]] = None,
    ) -> Event[Any]:
        """获取满足指定条件的的事件，协程会等待直到适配器接收到满足条件的事件、超过最大事件数或超时。

        Args:
            func: 协程或者函数，函数会被自动包装为协程执行。
                要求接受一个事件作为参数，返回布尔值。当协程返回 `True` 时返回当前事件。
                当为 `None` 时相当于输入对于任何事件均返回真的协程，即返回适配器接收到的下一个事件。
            event_type: 当指定时，只接受指定类型的事件，先于 func 条件生效。默认为 `None`。
            adapter_type: 当指定时，只接受指定适配器产生的事件，先于 func 条件生效。默认为 `None`。
            max_try_times: 最大事件数。
            timeout: 超时时间。

        Returns:
            返回满足 `func` 条件的事件。

        Raises:
            GetEventTimeout: 超过最大事件数或超时。
        """
        _func = wrap_get_func(func, event_type=event_type, adapter_type=adapter_type)

        try_times = 0
        start_time = time.time()
        while not self._should_exit.is_set():
            if max_try_times is not None and try_times > max_try_times:
                break
            if timeout is not None and time.time() - start_time > timeout:
                break

            async with self._condition:
                if timeout is None:
                    await self._condition.wait()
                else:
                    try:
                        with anyio.fail_after(start_time + timeout - time.time()):
                            await self._condition.wait()
                    except TimeoutError:
                        break

                if (
                    self._current_event is not None
                    and not self._current_event.__handled__
                    and await _func(self._current_event)
                ):
                    self._current_event.__handled__ = True
                    return self._current_event

                try_times += 1

        raise GetEventTimeout

    def _load_plugin_class(
        self,
        plugin_class: type[Plugin[Any, Any, Any]],
        plugin_load_type: PluginLoadType,
        plugin_file_path: Optional[str],
    ) -> None:
        """加载插件类。"""
        priority = getattr(plugin_class, "priority", None)
        if isinstance(priority, int) and priority >= 0:
            for _plugin in self.plugins:
                if _plugin.__name__ == plugin_class.__name__:
                    logger.warning(
                        "Already have a same name plugin", name=_plugin.__name__
                    )
            plugin_class.__plugin_load_type__ = plugin_load_type
            plugin_class.__plugin_file_path__ = plugin_file_path
            self.plugins_priority_dict[priority].append(plugin_class)
            logger.info(
                "Succeeded to load plugin from class",
                name=plugin_class.__name__,
                plugin_class=plugin_class,
            )
        else:
            logger.error(
                "Load plugin from class failed: Plugin priority incorrect in the class",
                plugin_class=plugin_class,
            )

    def _load_plugins_from_module_name(
        self,
        module_name: str,
        *,
        plugin_load_type: PluginLoadType,
        reload: bool = False,
    ) -> None:
        """从模块名称中插件模块。"""
        try:
            plugin_classes = get_classes_from_module_name(
                module_name, Plugin, reload=reload
            )
        except ImportError:
            logger.exception("Import module failed", module_name=module_name)
        else:
            for plugin_class, module in plugin_classes:
                self._load_plugin_class(
                    plugin_class,  # type: ignore
                    plugin_load_type,
                    module.__file__,
                )

    def _load_plugins(
        self,
        *plugins: Union[type[Plugin[Any, Any, Any]], str, Path],
        plugin_load_type: Optional[PluginLoadType] = None,
        reload: bool = False,
    ) -> None:
        """加载插件。

        Args:
            *plugins: 插件类、插件模块名称或者插件模块文件路径。类型可以是 `Type[Plugin]`, `str` 或 `pathlib.Path`。
                如果为 `Type[Plugin]` 类型时，将作为插件类进行加载。
                如果为 `str` 类型时，将作为插件模块名称进行加载，格式和 Python `import` 语句相同。
                    例如：`path.of.plugin`。
                如果为 `pathlib.Path` 类型时，将作为插件模块文件路径进行加载。
                    例如：`pathlib.Path("path/of/plugin")`。
            plugin_load_type: 插件加载类型，如果为 `None` 则自动判断，否则使用指定的类型。
            reload: 是否重新加载模块。
        """
        for plugin_ in plugins:
            try:
                if isinstance(plugin_, type) and issubclass(plugin_, Plugin):
                    self._load_plugin_class(
                        plugin_, plugin_load_type or PluginLoadType.CLASS, None
                    )
                elif isinstance(plugin_, str):
                    logger.info("Loading plugins from module", module_name=plugin_)
                    self._load_plugins_from_module_name(
                        plugin_,
                        plugin_load_type=plugin_load_type or PluginLoadType.NAME,
                        reload=reload,
                    )
                elif isinstance(plugin_, Path):
                    logger.info("Loading plugins from path", path=plugin_)
                    if not plugin_.is_file():
                        raise LoadModuleError(  # noqa: TRY301
                            f'The plugin path "{plugin_}" must be a file'
                        )

                    if plugin_.suffix != ".py":
                        raise LoadModuleError(  # noqa: TRY301
                            f'The path "{plugin_}" must endswith ".py"'
                        )

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
                        rel_path = plugin_.resolve().relative_to(Path().cwd())
                        if rel_path.stem == "__init__":
                            plugin_module_name = ".".join(rel_path.parts[:-1])
                        else:
                            plugin_module_name = ".".join(
                                rel_path.parts[:-1] + (rel_path.stem,)
                            )

                    self._load_plugins_from_module_name(
                        plugin_module_name,
                        plugin_load_type=plugin_load_type or PluginLoadType.FILE,
                        reload=reload,
                    )
                else:
                    raise TypeError(  # noqa: TRY301
                        f"{plugin_} can not be loaded as plugin"
                    )
            except Exception:
                logger.exception("Load plugin failed:", plugin=plugin_)

    def load_plugins(
        self, *plugins: Union[type[Plugin[Any, Any, Any]], str, Path]
    ) -> None:
        """加载插件。

        Args:
            *plugins: 插件类、插件模块名称或者插件模块文件路径。
                类型可以是 `Type[Plugin]`, `str` 或 `pathlib.Path`。
                如果为 `Type[Plugin]` 类型时，将作为插件类进行加载。
                如果为 `str` 类型时，将作为插件模块名称进行加载，格式和 Python `import` 语句相同。
                    例如：`path.of.plugin`。
                如果为 `pathlib.Path` 类型时，将作为插件模块文件路径进行加载。
                    例如：`pathlib.Path("path/of/plugin")`。
        """
        self._extend_plugins.extend(plugins)
        return self._load_plugins(*plugins)

    def _load_plugins_from_dirs(self, *dirs: Path) -> None:
        """从目录中加载插件，以 `_` 开头的模块中的插件不会被导入。路径可以是相对路径或绝对路径。

        Args:
            *dirs: 储存包含插件的模块的模块路径。
                例如：`pathlib.Path("path/of/plugins/")` 。
        """
        dir_list = [str(x.resolve()) for x in dirs]
        logger.info("Loading plugins from dirs", dirs=", ".join(map(str, dir_list)))
        self._module_path_finder.path.extend(dir_list)
        for module_info in pkgutil.iter_modules(dir_list):
            if not module_info.name.startswith("_"):
                self._load_plugins_from_module_name(
                    module_info.name, plugin_load_type=PluginLoadType.DIR
                )

    def load_plugins_from_dirs(self, *dirs: Path) -> None:
        """从目录中加载插件，以 `_` 开头的模块中的插件不会被导入。路径可以是相对路径或绝对路径。

        Args:
            *dirs: 储存包含插件的模块的模块路径。
                例如：`pathlib.Path("path/of/plugins/")` 。
        """
        self._extend_plugin_dirs.extend(dirs)
        self._load_plugins_from_dirs(*dirs)

    def _load_adapters(self, *adapters: Union[type[Adapter[Any, Any]], str]) -> None:
        """加载适配器。

        Args:
            *adapters: 适配器类或适配器名称，类型可以是 `Type[Adapter]` 或 `str`。
                如果为 `Type[Adapter]` 类型时，将作为适配器类进行加载。
                如果为 `str` 类型时，将作为适配器模块名称进行加载，格式和 Python `import` 语句相同。
                    例如：`path.of.adapter`。
        """
        for adapter_ in adapters:
            adapter_object: Adapter[Any, Any]
            try:
                if isinstance(adapter_, type) and issubclass(adapter_, Adapter):
                    adapter_object = adapter_(self)
                    logger.info(
                        "Succeeded to load adapter from class",
                        name=adapter_object.__class__.__name__,
                        adapter_class=adapter_,
                    )
                elif isinstance(adapter_, str):
                    adapter_classes = get_classes_from_module_name(adapter_, Adapter)
                    if not adapter_classes:
                        raise LoadModuleError(  # noqa: TRY301
                            f"Can not find Adapter class in the {adapter_} module"
                        )
                    if len(adapter_classes) > 1:
                        raise LoadModuleError(  # noqa: TRY301
                            f"More then one Adapter class in the {adapter_} module"
                        )
                    adapter_object = adapter_classes[0][0](self)  # type: ignore
                    logger.info(
                        "Succeeded to load adapter from module",
                        name=adapter_object.__class__.__name__,
                        module_name=adapter_,
                    )
                else:
                    raise TypeError(  # noqa: TRY301
                        f"{adapter_} can not be loaded as adapter"
                    )
            except Exception:
                logger.exception("Load adapter failed", adapter=adapter_)
            else:
                self.adapters.append(adapter_object)

    def load_adapters(self, *adapters: Union[type[Adapter[Any, Any]], str]) -> None:
        """加载适配器。

        Args:
            *adapters: 适配器类或适配器名称，类型可以是 `Type[Adapter]` 或 `str`。
                如果为 `Type[Adapter]` 类型时，将作为适配器类进行加载。
                如果为 `str` 类型时，将作为适配器模块名称进行加载，格式和 Python `import` 语句相同。
                    例如：`path.of.adapter`。
        """
        self._extend_adapters.extend(adapters)
        self._load_adapters(*adapters)

    @overload
    def get_adapter(self, adapter: str) -> Adapter[Any, Any]: ...

    @overload
    def get_adapter(self, adapter: type[AdapterT]) -> AdapterT: ...

    def get_adapter(
        self, adapter: Union[str, type[AdapterT]]
    ) -> Union[Adapter[Any, Any], AdapterT]:
        """按照名称或适配器类获取已经加载的适配器。

        Args:
            adapter: 适配器名称或适配器类。

        Returns:
            获取到的适配器对象。

        Raises:
            LookupError: 找不到此名称的适配器对象。
        """
        for _adapter in self.adapters:
            if isinstance(adapter, str):
                if _adapter.name == adapter:
                    return _adapter
            elif isinstance(_adapter, adapter):
                return _adapter  # pyright: ignore[reportUnknownVariableType]
        raise LookupError(f'Can not find adapter named "{adapter}"')

    def get_plugin(self, name: str) -> type[Plugin[Any, Any, Any]]:
        """按照名称获取已经加载的插件类。

        Args:
            name: 插件名称

        Returns:
            获取到的插件类。

        Raises:
            LookupError: 找不到此名称的插件类。
        """
        for _plugin in self.plugins:
            if _plugin.__name__ == name:
                return _plugin
        raise LookupError(f'Can not find plugin named "{name}"')

    def bot_run_hook(self, func: BotHook) -> BotHook:
        """注册一个 Bot 启动时的函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._bot_run_hooks.append(func)
        return func

    def bot_exit_hook(self, func: BotHook) -> BotHook:
        """注册一个 Bot 退出时的函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._bot_exit_hooks.append(func)
        return func

    def adapter_startup_hook(self, func: AdapterHook) -> AdapterHook:
        """注册一个适配器初始化时的函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._adapter_startup_hooks.append(func)
        return func

    def adapter_run_hook(self, func: AdapterHook) -> AdapterHook:
        """注册一个适配器运行时的函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._adapter_run_hooks.append(func)
        return func

    def adapter_shutdown_hook(self, func: AdapterHook) -> AdapterHook:
        """注册一个适配器关闭时的函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._adapter_shutdown_hooks.append(func)
        return func

    def event_preprocessor_hook(self, func: EventHook) -> EventHook:
        """注册一个事件预处理函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._event_preprocessor_hooks.append(func)
        return func

    def event_postprocessor_hook(self, func: EventHook) -> EventHook:
        """注册一个事件后处理函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._event_postprocessor_hooks.append(func)
        return func
