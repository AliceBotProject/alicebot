import sys
import json
import signal
import asyncio
import threading
from itertools import chain
from typing import Any, Awaitable, Callable, Dict, List, Iterable, Tuple, Type, NoReturn, Optional, TYPE_CHECKING

from pydantic import BaseModel, ValidationError, create_model

from alicebot.log import logger
from alicebot.config import MainConfig, config_file, config
from alicebot.exception import StopException, SkipException, LoadModuleError
from alicebot.load_module import ModulePathFinder, load_module, load_modules_from_dir

if TYPE_CHECKING:
    from alicebot.event import T_Event
    from alicebot.plugin import T_Plugin
    from alicebot.adapter import T_Adapter

__all__ = ['Bot']

HANDLED_SIGNALS = (
    signal.SIGINT,  # Unix signal 2. Sent by Ctrl+C.
    signal.SIGTERM,  # Unix signal 15. Sent by `kill <pid>`.
)


class Bot:
    """
    AliceBot 机器人对象，定义了机器人的基本方法，读取并储存配置 ``Config`` ，加载适配器 ``Adapter`` 和插件 ``Plugin``，并进行事件分发。
    """
    config_json: Dict[str, Any] = {}
    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
    should_exit: bool = False
    adapters: List['T_Adapter'] = []
    plugins_priority_dict: Dict[int, List[Type['T_Plugin']]] = {}
    _module_path_finder: ModulePathFinder = ModulePathFinder()
    _config_update_dict: Dict[str, Tuple[Type[BaseModel], Any]] = {}

    _bot_run_hook: List[Callable[['Bot'], Awaitable[NoReturn]]] = []
    _bot_exit_hook: List[Callable[['Bot'], NoReturn]] = []
    _adapter_startup_hook: List[Callable[['T_Adapter'], Awaitable[NoReturn]]] = []
    _adapter_run_hook: List[Callable[['T_Adapter'], Awaitable[NoReturn]]] = []
    _adapter_shutdown_hook: List[Callable[['T_Adapter'], Awaitable[NoReturn]]] = []
    _event_preprocessor_hook: List[Callable[['T_Event'], Awaitable[NoReturn]]] = []
    _event_postprocessor_hook: List[Callable[['T_Event'], Awaitable[NoReturn]]] = []

    def __init__(self, config_file_: Optional[str] = None):
        """
        初始化 AliceBot ，读取配置文件，创建配置，加载适配器和插件。

        :param config_file_: (optional) 指定配置文件，如不指定使用默认的 ``config.json`` 。
        """
        if config_file_ is None:
            config_file_ = config_file
        sys.meta_path.insert(0, self._module_path_finder)
        try:
            with open(config_file_, 'r', encoding='utf8') as f:
                self.config_json = json.load(f)
                self.config = MainConfig(**self.config_json)
        except OSError as e:
            logger.warning(f'Can not open config file: {e!r}')
        except json.JSONDecodeError as e:
            logger.warning(f'Read config file failed: {e!r}')
        except ValidationError as e:
            logger.error(f'Config file error: {e!r}')
        except ValueError as e:
            logger.error(f'Read config file failed: {e!r}')

        if self.config is None:
            return

        if self.config.plugin_dir:
            self.load_plugins_from_dir(self.config.plugin_dir)
        if self.config.plugins:
            for _plugin in self.config.plugins:
                self.load_plugin(_plugin)
        if self.config.adapters:
            for _adapter in self.config.adapters:
                self.load_adapter(_adapter)

    @property
    def config(self):
        return config.get()

    @config.setter
    def config(self, value):
        config.set(value)

    @property
    def plugins(self) -> List[Type['T_Plugin']]:
        """
        :return: 当前已经加载的插件的列表。
        :rtype: List[Type['T_Plugin']]
        """
        return list(chain(*self.plugins_priority_dict.values()))

    def run(self):
        """
        运行 AliceBot ，监听并拦截系统退出信号，更新机器人配置。
        """
        logger.info('Running AliceBot...')
        # 监听并拦截系统退出信号，从而完成一些善后工作后再关闭程序
        if threading.current_thread() is threading.main_thread():
            # Signal 仅能在主线程中被处理。
            try:
                for sig in HANDLED_SIGNALS:
                    self.loop.add_signal_handler(sig, self.handle_exit)
            except NotImplementedError:
                # add_signal_handler 仅在 Unix 下可用，以下对于 Windows。
                for sig in HANDLED_SIGNALS:
                    signal.signal(sig, self.handle_exit)

        # 更新 config，合并入来自 Plugin 和 Adapter 的 Config
        if self._config_update_dict and self.config_json:
            self.config = create_model('Config', **self._config_update_dict, __base__=MainConfig)(**self.config_json)

        try:
            self.loop.run_until_complete(self._run())
        finally:
            try:
                self._cancel_all_tasks()
                self.loop.run_until_complete(self.loop.shutdown_asyncgens())
            finally:
                asyncio.set_event_loop(None)
                self.loop.close()

    async def _run(self):
        for _hook_func in self._bot_run_hook:
            await _hook_func(self)

        try:
            for _adapter in self.adapters:
                for _hook_func in self._adapter_startup_hook:
                    await _hook_func(_adapter)
                try:
                    await _adapter.startup()
                except Exception as e:
                    logger.error(f'Startup adapter {_adapter!r} failed: {e!r}')

            for _adapter in self.adapters:
                for _hook_func in self._adapter_run_hook:
                    await _hook_func(_adapter)
                self.loop.create_task(_adapter.safe_run())

            await self.main_loop()
        finally:
            for _adapter in self.adapters:
                for _hook_func in self._adapter_shutdown_hook:
                    await _hook_func(_adapter)
                await _adapter.shutdown()

    async def main_loop(self):
        while not self.should_exit:
            await asyncio.sleep(0.1)

    def handle_exit(self):
        """
        当机器人收到退出信号时，根据情况进行处理。
        """
        logger.info(f'Stopping AliceBot...')
        for _hook_func in self._bot_exit_hook:
            _hook_func(self)
        if self.should_exit:
            logger.warning(f'Force Exit AliceBot...')
            sys.exit()
        else:
            self.should_exit = True

    def _cancel_all_tasks(self):
        to_cancel = asyncio.all_tasks(self.loop)
        if not to_cancel:
            return
        for task in to_cancel:
            task.cancel()
        self.loop.run_until_complete(asyncio.gather(*to_cancel, loop=self.loop, return_exceptions=True))
        for task in to_cancel:
            if task.cancelled():
                continue
            if task.exception() is not None:
                logger.error('Unhandled exception during event loop shutdown')

    async def handle_event(self, current_event: 'T_Event'):
        """
        被适配器对象调用，根据优先级分发事件给所有插件，并处理插件的 ``stop`` 、 ``skip`` 等信号。
        此方法不应该被用户手动调用。

        :param current_event: 当前待处理的 ``Event``。
        """
        if current_event is None:
            return

        for _hook_func in self._event_preprocessor_hook:
            await _hook_func(current_event)

        for plugin_priority in sorted(self.plugins_priority_dict.keys()):
            try:
                logger.debug(f'Checking for matching plugins with priority {plugin_priority!r}')
                stop = False
                for _plugin in self.plugins_priority_dict[plugin_priority]:
                    try:
                        _plugin = _plugin(current_event)
                        if await _plugin.rule():
                            logger.info(f'Event will be handled by {_plugin!r}')
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
                        logger.error(f'Exception in plugin "{_plugin}": {e!r}')
                if stop:
                    break
            except Exception as e:
                logger.error(f'Exception in handling event {current_event!r}: {e!r}')

        for _hook_func in self._event_postprocessor_hook:
            await _hook_func(current_event)

        logger.info(f'Event Finished')

    def _load_plugin(self, plugin_class: Type['T_Plugin']):
        if type(plugin_class.priority) is int and plugin_class.priority >= 0:
            if plugin_class.priority in self.plugins_priority_dict:
                self.plugins_priority_dict[plugin_class.priority].append(plugin_class)
            else:
                self.plugins_priority_dict[plugin_class.priority] = [plugin_class]
        else:
            raise LoadModuleError(f'Plugin class priority incorrect in the module "{plugin_class!r}"')

    def load_plugin(self, name: str) -> Optional[Type['T_Plugin']]:
        """
        加载单个插件。

        :param name: 插件名称，格式和 Python ``import`` 语句相同，
        :return: 被加载的插件类。
        :rtype: Optional[Type['T_Plugin']]
        """
        from alicebot.plugin import Plugin
        try:
            plugin_class, config_class = load_module(name, Plugin)
            self._load_plugin(plugin_class)
        except Exception as e:
            logger.error(f'Import plugin "{name}" failed: {e!r}')
        else:
            self._update_config(config_class)
            logger.info(f'Succeeded to import plugin "{name}"')
            return plugin_class

    def load_adapter(self, name: str) -> Optional['T_Adapter']:
        """
        加载单个适配器。

        :param name: 适配器名称，格式和 Python ``import`` 语句相同，
        :return: 被加载的适配器对象。
        :rtype: Optional['T_Adapter']
        """
        from alicebot.adapter import BaseAdapter
        try:
            adapter_object, config_class = load_module(name, BaseAdapter, True, self)
        except Exception as e:
            logger.error(f'Load adapter "{name}" failed: {e!r}')
        else:
            self.adapters.append(adapter_object)
            self._update_config(config_class)
            logger.info(f'Succeeded to load adapter "{name}"')
            return adapter_object

    def load_plugins_from_dir(self, path: Iterable[str]):
        """
        从指定路径列表中加载插件，以 ``_`` 开头的插件不会被导入。
        路径可以是相对路径或绝对路径。

        :param path: 由储存插件的路径文本组成的列表。 ``['path/of/plugins/', '/home/xxx/alicebot/plugins']``
        """
        from alicebot.plugin import Plugin
        for module, config_class, module_info in load_modules_from_dir(self._module_path_finder, path, Plugin):
            try:
                self._load_plugin(module)
            except Exception as e:
                # noinspection PyUnresolvedReferences
                logger.error(
                    f'Import plugin "{module_info.name}" from path "{module_info.module_finder.path}" failed: {e!r}')
            else:
                self._update_config(config_class)
                # noinspection PyUnresolvedReferences
                logger.info(
                    f'Succeeded to import plugin "{module_info.name}" from path "{module_info.module_finder.path}"')

    def _update_config(self, config_class: Optional[Type['BaseModel']]):
        def _get_default_value():
            try:
                _config = config_class()
            except ValidationError:
                return ...
            else:
                return _config

        if config_class is not None:
            self._config_update_dict[getattr(config_class, '__config_name__')] = (config_class, _get_default_value())

    def get_loaded_adapter_by_name(self, name: str) -> 'T_Adapter':
        """
        按照名称获取已经加载的适配器。

        :param name: 适配器名称。
        :return: 获取到的适配器对象。
        :exception LookupError: 找不到此名称的适配器对象。
        """
        for _adapter in self.adapters:
            if _adapter.name == name:
                return _adapter
        raise LookupError

    def bot_run_hook(self, func: Callable[['Bot'], Awaitable[NoReturn]]) -> \
            Callable[['Bot'], Awaitable[NoReturn]]:
        """
        注册一个 Bot 启动时的函数。

        :param func: 被注册的函数。
        :return: 被注册的函数。
        :rtype: Callable[['Bot'], Awaitable[NoReturn]]
        """
        self._bot_run_hook.append(func)
        return func

    def bot_exit_hook(self, func: Callable[['Bot'], NoReturn]) -> Callable[['Bot'], NoReturn]:
        """
        注册一个 Bot 退出时的函数。

        :param func: 被注册的函数。
        :return: 被注册的函数。
        :rtype: Callable[['Bot'], Awaitable[NoReturn]]
        """
        self._bot_exit_hook.append(func)
        return func

    def adapter_startup_hook(self, func: Callable[['T_Adapter'], Awaitable[NoReturn]]) -> \
            Callable[['T_Adapter'], Awaitable[NoReturn]]:
        """
        注册一个适配器初始化时的函数。

        :param func: 被注册的函数。
        :return: 被注册的函数。
        :rtype: Callable[['T_Adapter'], Awaitable[NoReturn]]
        """
        self._adapter_startup_hook.append(func)
        return func

    def adapter_run_hook(self, func: Callable[['T_Adapter'], Awaitable[NoReturn]]) -> \
            Callable[['T_Adapter'], Awaitable[NoReturn]]:
        """
        注册一个适配器运行时的函数。

        :param func: 被注册的函数。
        :return: 被注册的函数。
        :rtype: Callable[['T_Adapter'], Awaitable[NoReturn]]
        """
        self._adapter_run_hook.append(func)
        return func

    def adapter_shutdown_hook(self, func: Callable[['T_Adapter'], Awaitable[NoReturn]]) -> \
            Callable[['T_Adapter'], Awaitable[NoReturn]]:
        """
        注册一个适配器关闭时的函数。

        :param func: 被注册的函数。
        :return: 被注册的函数。
        :rtype: Callable[['T_Adapter'], Awaitable[NoReturn]]
        """
        self._adapter_shutdown_hook.append(func)
        return func

    def event_preprocessor_hook(self, func: Callable[['T_Event'], Awaitable[NoReturn]]) -> \
            Callable[['T_Event'], Awaitable[NoReturn]]:
        """
        注册一个事件预处理函数。

        :param func: 被注册的函数。
        :return: 被注册的函数。
        :rtype: Callable[['T_Event'], Awaitable[NoReturn]]
        """
        self._event_preprocessor_hook.append(func)
        return func

    def event_postprocessor_hook(self, func: Callable[['T_Event'], Awaitable[NoReturn]]) -> \
            Callable[['T_Event'], Awaitable[NoReturn]]:
        """
        注册一个事件后处理函数。

        :param func: 被注册的函数。
        :return: 被注册的函数。
        :rtype: Callable[['T_Event'], Awaitable[NoReturn]]
        """
        self._event_postprocessor_hook.append(func)
        return func
