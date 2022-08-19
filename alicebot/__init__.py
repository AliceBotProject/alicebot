import os
import sys
import json
import time
import signal
import asyncio
import threading
from functools import wraps
from itertools import chain
from collections import defaultdict
from typing import (
    Any,
    Dict,
    List,
    Type,
    Tuple,
    Union,
    Callable,
    Iterable,
    Optional,
    Awaitable,
)

from pydantic import BaseModel, ValidationError, create_model

from alicebot.plugin import Plugin
from alicebot.adapter import Adapter
from alicebot.config import MainConfig
from alicebot.log import logger, error_or_exception
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
    Condition,
    ModuleInfo,
    ModulePathFinder,
    samefile,
    load_module_form_file,
    load_module_from_name,
    load_modules_from_dir,
)

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
        adapters: 适配器列表。
        plugins_priority_dict: 插件优先级字典。
        plugin_state: 插件状态。
        global_state: 全局状态。
    """

    config: MainConfig = None

    should_exit: asyncio.Event
    adapters: List[Adapter]
    plugins_priority_dict: Dict[int, List[ModuleInfo]]
    plugin_state: Dict[str, Any]
    global_state: Dict[Any, Any]

    _condition: Condition[T_Event]

    _restart_flag: bool
    _module_path_finder: ModulePathFinder
    _config_update_dict: Dict[str, Tuple[Type[BaseModel], Any]]

    _config_file: Optional[str]
    _config_dict: Dict[str, Any]
    _hot_reload: bool

    _bot_run_hook: List[T_BotHook]
    _bot_exit_hook: List[T_BotExitHook]
    _adapter_startup_hook: List[T_AdapterHook]
    _adapter_run_hook: List[T_AdapterHook]
    _adapter_shutdown_hook: List[T_AdapterHook]
    _event_preprocessor_hook: List[T_EventHook]
    _event_postprocessor_hook: List[T_EventHook]

    def __init__(
        self,
        *,
        config_file: Optional[str] = "config.json",
        config_dict: Optional[Dict] = None,
        hot_reload: bool = False,
    ):
        """初始化 AliceBot ，读取配置文件，创建配置，加载适配器和插件。

        Args:
            config_file: 配置文件，如不指定则使用默认的 `config.json`。
                若指定为 None，则不加载配置文件。
            config_dict: 配置字典，默认为 None。
                若指定字典，则会忽略 config_file 配置，不再读取配置文件。
            hot_reload: 热重载。
                启用后将自动检查 `plugin_dir` 中的插件文件更新，并在更新时自动重新加载。
        """
        self.config = MainConfig()

        self.adapters = []
        self.plugins_priority_dict = {}
        self.plugin_state = defaultdict(type(None))
        self.global_state = {}

        self._restart_flag = False
        self._module_path_finder = ModulePathFinder()
        self._config_update_dict = {}

        self._config_file = config_file
        self._config_dict = config_dict
        self._hot_reload = hot_reload

        self._bot_run_hook = []
        self._bot_exit_hook = []
        self._adapter_startup_hook = []
        self._adapter_run_hook = []
        self._adapter_shutdown_hook = []
        self._event_preprocessor_hook = []
        self._event_postprocessor_hook = []

        sys.meta_path.insert(0, self._module_path_finder)

    @property
    def plugins(self) -> List[Type[Plugin]]:
        """当前已经加载的插件的列表。"""
        return list(
            map(
                lambda x: x.module_class,
                chain(*self.plugins_priority_dict.values()),
            )
        )

    def run(self):
        """运行 AliceBot，监听并拦截系统退出信号，更新机器人配置。"""
        self._restart_flag = True
        while self._restart_flag:
            self._restart_flag = False
            asyncio.run(self._run())

    def restart(self):
        """退出并重新运行 AliceBot。"""
        logger.info("Restarting AliceBot...")
        self._restart_flag = True
        self.should_exit.set()

    async def _run(self):
        """运行 AliceBot。"""
        self.should_exit = asyncio.Event()
        self._condition = Condition()

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
        config_dict = {}
        if self._config_dict is not None:
            config_dict = self._config_dict
        elif self._config_file is not None:
            try:
                with open(self._config_file, "r", encoding="utf8") as f:
                    config_dict = json.load(f)
            except OSError as e:
                logger.warning(f"Can not open config file: {e!r}")
            except json.JSONDecodeError as e:
                logger.warning(f"Read config file failed: {e!r}")
            except ValueError as e:
                error_or_exception(
                    "Read config file failed:", e, self.config.verbose_exception_log
                )

        try:
            self.config = MainConfig(**config_dict)
        except ValidationError as e:
            self.config = MainConfig()
            error_or_exception(
                "Config dict parse error:", e, self.config.verbose_exception_log
            )

        self.load_plugins_from_dir(self.config.plugin_dir)
        for _plugin in self.config.plugins:
            self.load_plugin(_plugin)
        for _adapter in self.config.adapters:
            self.load_adapter(_adapter)
        self._reload_config()

        # 启动 AliceBot
        logger.info("Running AliceBot...")

        hot_reload_task = None
        if self._hot_reload:
            hot_reload_task = asyncio.create_task(self._run_hot_reload())

        for _hook_func in self._bot_run_hook:
            await _hook_func(self)

        try:
            for _adapter in self.adapters:
                for _hook_func in self._adapter_startup_hook:
                    await _hook_func(_adapter)
                try:
                    await _adapter.startup()
                except Exception as e:
                    error_or_exception(
                        f"Startup adapter {_adapter!r} failed:",
                        e,
                        self.config.verbose_exception_log,
                    )

            for _adapter in self.adapters:
                for _hook_func in self._adapter_run_hook:
                    await _hook_func(_adapter)
                asyncio.create_task(_adapter.safe_run())

            await self.should_exit.wait()

            if hot_reload_task is not None:
                await hot_reload_task
        finally:
            for _adapter in self.adapters:
                for _hook_func in self._adapter_shutdown_hook:
                    await _hook_func(_adapter)
                await _adapter.shutdown()
            for _hook_func in self._bot_exit_hook:
                _hook_func(self)

            self.adapters.clear()
            self.plugins_priority_dict.clear()
            self._config_update_dict.clear()

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
                os.path.abspath,
                self.config.plugin_dir.union(
                    {self._config_file}
                    if self._config_dict is None and self._config_file is not None
                    else set()
                ),
            ),
            stop_event=self.should_exit,
        ):
            for change_type, file in changes:
                if (
                    samefile(self._config_file, file)
                    and change_type == change_type.modified
                ):
                    logger.info(f'Reload config file "{self._config_file}"')
                    self.restart()
                    continue
                if not file.endswith(".py"):
                    continue
                if change_type == Change.added:
                    try:
                        plugin_info = load_module_form_file(
                            self._module_path_finder, file, Plugin
                        )
                        self._load_plugin(plugin_info)
                        self._reload_config()
                    except Exception as e:
                        error_or_exception(
                            f'Add new plugin from file "{file}" failed:',
                            e,
                            self.config.verbose_exception_log,
                        )
                    else:
                        logger.info(
                            f"Added new plugin "
                            f'"{plugin_info.module_class.__name__}" '
                            f'from file "{file}"'
                        )
                    continue
                for plugins in self.plugins_priority_dict.values():
                    for i, _plugin in enumerate(plugins):
                        if samefile(getattr(_plugin.module, "__file__", None), file):
                            if change_type == Change.modified:
                                try:
                                    self._remove_config_module(_plugin.config_class)
                                    plugins.pop(i)
                                    plugin_info = load_module_form_file(
                                        self._module_path_finder, file, Plugin
                                    )
                                    self._load_plugin(plugin_info)
                                    self._reload_config()
                                except Exception as e:
                                    error_or_exception(
                                        f'Reload plugin from file "{file}" failed:',
                                        e,
                                        self.config.verbose_exception_log,
                                    )
                                else:
                                    logger.info(
                                        f"Succeeded to reload plugin "
                                        f'"{_plugin.module_class.__name__}" '
                                        f'from file "{file}"'
                                    )
                            elif change_type == Change.deleted:
                                try:
                                    plugins.pop(i)
                                    self._remove_config_module(_plugin.config_class)
                                    self._reload_config()
                                except Exception as e:
                                    error_or_exception(
                                        f'Removed plugin from file "{file}" failed:',
                                        e,
                                        self.config.verbose_exception_log,
                                    )
                                else:
                                    logger.info(
                                        f"Succeeded to remove plugin "
                                        f'"{_plugin.module_class.__name__}" '
                                        f'from file "{file}"'
                                    )
                            break

    def reload_plugins(self):
        """手动重新加载所有插件。"""
        self.plugins_priority_dict.clear()
        self._config_update_dict.clear()
        self.load_plugins_from_dir(self.config.plugin_dir)
        for _plugin in self.config.plugins:
            self.load_plugin(_plugin)
        self._reload_config()

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
                self._condition.notify_all(current_event)
        else:
            asyncio.create_task(self._handle_event(current_event))

    async def _handle_event(self, current_event: Optional[T_Event] = None):
        if current_event is None:
            async with self._condition:
                current_event = await self._condition.wait()
            if current_event.__handled__:
                return

        for _hook_func in self._event_preprocessor_hook:
            await _hook_func(current_event)

        for plugin_priority in sorted(self.plugins_priority_dict.keys()):
            try:
                logger.debug(
                    f"Checking for matching plugins with priority {plugin_priority!r}"
                )
                stop = False
                for _plugin in self.plugins_priority_dict[plugin_priority]:
                    try:
                        _plugin = _plugin.module_class(current_event)
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
                            self.config.verbose_exception_log,
                        )
                if stop:
                    break
            except Exception as e:
                error_or_exception(
                    f"Exception in handling event {current_event!r}:",
                    e,
                    self.config.verbose_exception_log,
                )

        for _hook_func in self._event_postprocessor_hook:
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

        async def always_true(_):
            return True

        def async_wrapper(_func):
            @wraps(_func)
            async def _wrapper(_event):
                return _func(_event)

            return _wrapper

        if func is None:
            func = always_true
        elif not asyncio.iscoroutinefunction(func):
            func = async_wrapper(func)

        try_times = 0
        start_time = time.time()
        while not self.should_exit.is_set():
            if max_try_times is not None and try_times > max_try_times:
                break
            if timeout is not None and time.time() - start_time > timeout:
                break

            async with self._condition:
                if timeout is None:
                    event = await self._condition.wait()
                else:
                    try:
                        event = await asyncio.wait_for(
                            self._condition.wait(),
                            timeout=start_time + timeout - time.time(),
                        )
                    except asyncio.TimeoutError:
                        break

                if not event.__handled__:
                    if await func(event):
                        event.__handled__ = True
                        return event

                try_times += 1

        if not self.should_exit.is_set():
            raise GetEventTimeout

    def _load_plugin(self, plugin_info: ModuleInfo):
        """加载插件。"""
        priority = getattr(plugin_info.module_class, "priority", None)
        if type(priority) is int and priority >= 0:
            if priority not in self.plugins_priority_dict:
                self.plugins_priority_dict[priority] = []
            self.plugins_priority_dict[priority].append(plugin_info)
            self._update_config_module(plugin_info.config_class)
        else:
            raise LoadModuleError(
                "Plugin class priority incorrect in the module "
                + plugin_info.module.__name__
            )

    def load_plugin(self, name: str) -> Optional[Type[Plugin]]:
        """加载单个插件。

        Args:
            name: 插件名称，格式和 Python `import` 语句相同。

        Returns:
            被加载的插件类。
        """
        self.config.plugins.add(name)
        try:
            plugin_info = load_module_from_name(name, Plugin)
            self._load_plugin(plugin_info)
        except Exception as e:
            error_or_exception(
                f'Load plugin from module "{name}" failed:',
                e,
                self.config.verbose_exception_log,
            )
        else:
            logger.info(
                f'Succeeded to load plugin "{plugin_info.module_class.__name__}" '
                f'from module "{name}"'
            )
            return plugin_info.module_class

    def load_plugins_from_dir(self, path: Iterable[str]):
        """从指定路径列表中加载插件，以 `_` 开头的插件不会被导入。路径可以是相对路径或绝对路径。

        Args:
            path: 由储存插件的路径文本组成的列表。
                例如： `['path/of/plugins/', '/home/xxx/alicebot/plugins']` 。
        """
        self.config.plugin_dir.update(path)
        for plugin_info in load_modules_from_dir(
            self._module_path_finder, path, Plugin
        ):
            try:
                self._load_plugin(plugin_info)
            except Exception as e:
                error_or_exception(
                    f'Load plugin "{plugin_info.module_class.__name__}" '
                    f'from file "{plugin_info.module.__file__}" failed:',
                    e,
                    self.config.verbose_exception_log,
                )
            else:
                logger.info(
                    f'Succeeded to load plugin "{plugin_info.module_class.__name__}" '
                    f'from file "{plugin_info.module.__file__}"'
                )

    def load_adapter(self, name: str) -> Optional[Adapter]:
        """加载单个适配器。

        Args:
            name: 适配器名称，格式和 Python `import` 语句相同。

        Returns:
            被加载的适配器对象。
        """
        self.config.adapters.add(name)
        try:
            adapter_info = load_module_from_name(name, Adapter)
            adapter_object = adapter_info.module_class(self)
        except Exception as e:
            error_or_exception(
                f'Load adapter "{name}" failed:', e, self.config.verbose_exception_log
            )
        else:
            self.adapters.append(adapter_object)
            self._update_config_module(adapter_info.config_class)
            logger.info(
                f'Succeeded to load adapter "{adapter_info.module_class.__name__}" '
                f'from module "{name}"'
            )
            return adapter_object

    def _update_config_module(self, config_class: Optional[Type[BaseModel]]):
        """更新配置模型。"""
        if config_class is None:
            return
        try:
            default_value = config_class()
        except ValidationError:
            default_value = ...
        self._config_update_dict[getattr(config_class, "__config_name__")] = (
            config_class,
            default_value,
        )

    def _remove_config_module(self, config_class: Optional[Type[BaseModel]]):
        """删除配置模型。"""
        if config_class is None:
            return
        try:
            self._config_update_dict.pop(getattr(config_class, "__config_name__"))
        except KeyError:
            pass

    def _reload_config(self):
        """更新 config，合并入来自 Plugin 和 Adapter 的 Config"""
        self.config = create_model(
            "Config", **self._config_update_dict, __base__=MainConfig
        )(**self.config.dict())

    def get_loaded_adapter_by_name(self, name: str) -> Adapter:
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
        raise LookupError

    def bot_run_hook(self, func: T_BotHook) -> T_BotHook:
        """注册一个 Bot 启动时的函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._bot_run_hook.append(func)
        return func

    def bot_exit_hook(self, func: T_BotExitHook) -> T_BotExitHook:
        """注册一个 Bot 退出时的函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._bot_exit_hook.append(func)
        return func

    def adapter_startup_hook(self, func: T_AdapterHook) -> T_AdapterHook:
        """注册一个适配器初始化时的函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._adapter_startup_hook.append(func)
        return func

    def adapter_run_hook(self, func: T_AdapterHook) -> T_AdapterHook:
        """注册一个适配器运行时的函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._adapter_run_hook.append(func)
        return func

    def adapter_shutdown_hook(self, func: T_AdapterHook) -> T_AdapterHook:
        """注册一个适配器关闭时的函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._adapter_shutdown_hook.append(func)
        return func

    def event_preprocessor_hook(self, func: T_EventHook) -> T_EventHook:
        """注册一个事件预处理函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._event_preprocessor_hook.append(func)
        return func

    def event_postprocessor_hook(self, func: T_EventHook) -> T_EventHook:
        """注册一个事件后处理函数。

        Args:
            func: 被注册的函数。

        Returns:
            被注册的函数。
        """
        self._event_postprocessor_hook.append(func)
        return func
