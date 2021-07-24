import sys
import json
import signal
import asyncio
import threading
from itertools import chain
from typing import Any, List, Dict, Iterable, Tuple, Type, TypeVar, Optional, TYPE_CHECKING

from pydantic import create_model, ValidationError

from alicebot.log import logger
from alicebot.plugin import Plugin
from alicebot.adapter import AbstractAdapter
from alicebot.config import MainConfig, BaseModel, config_file
from alicebot.exception import StopException, SkipException, LoadModuleError
from alicebot.load_module import load_module, ModulePathFinder, load_modules_from_dir

if TYPE_CHECKING:
    from alicebot.event import T_Event
    from alicebot.plugin import T_Plugin
    from alicebot.adapter import T_Adapter

HANDLED_SIGNALS = (
    signal.SIGINT,  # Unix signal 2. Sent by Ctrl+C.
    signal.SIGTERM,  # Unix signal 15. Sent by `kill <pid>`.
)

_T = TypeVar('_T')


class Bot:
    """
    AliceBot 机器人对象，定义了机器人的基本方法，读取并储存配置 ``Config`` ，加载适配器 ``Adapter`` 和插件 ``Plugin``，并进行事件分发。
    """
    config = None
    config_json: Dict[str, Any] = {}
    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
    should_exit: bool = False
    adapters: List['T_Adapter'] = []
    plugins_priority_dict: Dict[int, List[Type['T_Plugin']]] = {}
    _module_path_finder: ModulePathFinder = ModulePathFinder()
    _config_update_dict: Dict[str, Tuple[Type[BaseModel], Any]] = {}

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
    def plugins(self) -> List['T_Plugin']:
        """
        :return: 当前已经加载的插件的列表。
        :rtype: List['T_Plugin']
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

        # 更新config，合并入来自Plugin和Adapter的Config
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
        try:
            for _adapter in self.adapters:
                try:
                    await _adapter.startup()
                except Exception as e:
                    logger.error(f'Startup _adapter {_adapter!r} failed: {e!r}')
            for _adapter in self.adapters:
                self.loop.create_task(_adapter.safe_run())
            await self.main_loop()
        finally:
            for _adapter in self.adapters:
                await _adapter.shutdown()

    async def main_loop(self):
        while not self.should_exit:
            await asyncio.sleep(0.1)

    def handle_exit(self):
        """
        当机器人收到退出信号时，根据情况进行处理。
        """
        logger.info(f'Stopping AliceBot...')
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
        for plugin_priority in sorted(self.plugins_priority_dict.keys()):
            try:
                logger.debug(f'Checking for matching plugins with priority {plugin_priority!r}')
                for _plugin in self.plugins_priority_dict[plugin_priority]:
                    try:
                        _plugin = _plugin(current_event)
                        if await _plugin.rule():
                            logger.info(f'Event will be handled by {_plugin!r}')
                            await _plugin.handle()
                            if _plugin.block:
                                raise StopException()
                    except SkipException or StopException as e:
                        raise e
                    except Exception as e:
                        logger.error(f'Exception in plugin "{_plugin}": {e!r}')
            except StopException:
                # 插件要求停止当前事件传播
                break
            except SkipException:
                # 插件要求跳过自身继续当前事件传播
                continue
            except Exception as e:
                logger.error(f'Exception in handling event {current_event!r}: {e!r}')
            logger.info(f'Event Finished')

    def _load_plugin(self, plugin_class: Type['T_Plugin']):
        if type(plugin_class.priority) is int and plugin_class.priority >= 0:
            if plugin_class.priority in self.plugins_priority_dict:
                self.plugins_priority_dict[plugin_class.priority].append(plugin_class)
            else:
                self.plugins_priority_dict[plugin_class.priority] = [plugin_class]
        else:
            logger.error(f'Plugin class priority incorrect in the module "{plugin_class!r}"')
            raise LoadModuleError()

    def load_plugin(self, name: str) -> Optional[Type['T_Plugin']]:
        """
        加载单个插件。

        :param name: 插件名称，格式和 Python ``import`` 语句相同，
        :return: 被加载的插件类。
        :rtype: Optional[Type['T_Plugin']]
        """
        try:
            plugin_class, config_class = load_module(name, Plugin, None)
            self._load_plugin(plugin_class)
        except Exception as e:
            logger.error(f'Import plugin "{name}" failed: {e!r}')
        else:
            self._update_config(config_class)
            logger.info(f'Succeeded to import plugin "{name}"')
            return plugin_class

    def load_adapter(self, name: str) -> Optional[Type['T_Adapter']]:
        """
        加载单个适配器。

        :param name: 适配器名称，格式和 Python ``import`` 语句相同，
        :return: 被加载的适配器类。
        :rtype: Optional[Type['T_Adapter']]
        """
        try:
            adapter_class, config_class = load_module(name, AbstractAdapter, self)
            self.adapters.append(adapter_class(self))
        except Exception as e:
            logger.error(f'Load adapter "{name}" failed: {e!r}')
        else:
            self._update_config(config_class)
            logger.info(f'Succeeded to load adapter "{name}"')
            return adapter_class

    def load_plugins_from_dir(self, path: Iterable[str]):
        """
        从指定路径列表中加载插件，以 ``_`` 开头的插件不会被导入。
        路径可以是相对路径或绝对路径。

        :param path: 由储存插件的路径文本组成的列表。 ``['path/of/plugins/', '/home/xxx/alicebot/plugins']``
        """
        for module, config_class, module_info in load_modules_from_dir(self._module_path_finder, path, Plugin, None):
            try:
                self._load_plugin(module)
            except Exception as e:
                logger.error(
                    f'Import plugin "{module_info.name}" from path "{module_info.module_finder.path}" failed: {e!r}')
            else:
                self._update_config(config_class)
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
