# alicebot

## *class* `Bot`(self, config_file = 'config.json', config_dict = None) {#Bot}

Bases: `object`

AliceBot 机器人对象，定义了机器人的基本方法，读取并储存配置 `Config`，加载适配器 `Adapter` 和插件 `Plugin`，并进行事件分发。

- **Arguments**

  - **config_file** (*Optional[str]*) - 配置文件，如不指定则使用默认的 `config.json`， 若指定为 None，则不加载配置文件。

  - **config_dict** (*Optional[Dict]*) - 配置字典，默认为 None，若指定字典，则会忽略 config_file 配置，不再读取配置文件。

- **Attributes**

  - **config** (*alicebot.config.MainConfig*) - 机器人配置。

  - **config_dict** (*Dict[str, Any]*) - 机器人配置字典。

  - **loop** (*asyncio.events.AbstractEventLoop*) - 事件循环。

  - **should_exit** (*bool*) - 机器人是否应该进入准备退出状态。

  - **adapters** (*List[T_Adapter]*) - 适配器列表。

  - **plugins_priority_dict** (*Dict[int, List[Type[T_Plugin]]]*) - 插件优先级字典。

### *method* `adapter_run_hook(self, func)` {#Bot.adapter_run_hook}

注册一个适配器运行时的函数。

- **Arguments**

  - **func** (*Callable[[T_Adapter], Awaitable[NoReturn]]*) - 被注册的函数。

- **Returns**

  Type: *Callable[[T_Adapter], Awaitable[NoReturn]]*

  被注册的函数。

### *method* `adapter_shutdown_hook(self, func)` {#Bot.adapter_shutdown_hook}

注册一个适配器关闭时的函数。

- **Arguments**

  - **func** (*Callable[[T_Adapter], Awaitable[NoReturn]]*) - 被注册的函数。

- **Returns**

  Type: *Callable[[T_Adapter], Awaitable[NoReturn]]*

  被注册的函数。

### *method* `adapter_startup_hook(self, func)` {#Bot.adapter_startup_hook}

注册一个适配器初始化时的函数。

- **Arguments**

  - **func** (*Callable[[T_Adapter], Awaitable[NoReturn]]*) - 被注册的函数。

- **Returns**

  Type: *Callable[[T_Adapter], Awaitable[NoReturn]]*

  被注册的函数。

### *method* `bot_exit_hook(self, func)` {#Bot.bot_exit_hook}

注册一个 Bot 退出时的函数。

- **Arguments**

  - **func** (*Callable[[Bot], NoReturn]*) - 被注册的函数。

- **Returns**

  Type: *Callable[[Bot], NoReturn]*

  被注册的函数。

### *method* `bot_run_hook(self, func)` {#Bot.bot_run_hook}

注册一个 Bot 启动时的函数。

- **Arguments**

  - **func** (*Callable[[Bot], Awaitable[NoReturn]]*) - 被注册的函数。

- **Returns**

  Type: *Callable[[Bot], Awaitable[NoReturn]]*

  被注册的函数。

### *method* `event_postprocessor_hook(self, func)` {#Bot.event_postprocessor_hook}

注册一个事件后处理函数。

- **Arguments**

  - **func** (*Callable[[T_Event], Awaitable[NoReturn]]*) - 被注册的函数。

- **Returns**

  Type: *Callable[[T_Event], Awaitable[NoReturn]]*

  被注册的函数。

### *method* `event_preprocessor_hook(self, func)` {#Bot.event_preprocessor_hook}

注册一个事件预处理函数。

- **Arguments**

  - **func** (*Callable[[T_Event], Awaitable[NoReturn]]*) - 被注册的函数。

- **Returns**

  Type: *Callable[[T_Event], Awaitable[NoReturn]]*

  被注册的函数。

### *method* `get_loaded_adapter_by_name(self, name)` {#Bot.get_loaded_adapter_by_name}

按照名称获取已经加载的适配器。

- **Arguments**

  - **name** (*str*) - 适配器名称。

- **Returns**

  Type: *T_Adapter*

  获取到的适配器对象。

- **Raises**

  - **LookupError** - 找不到此名称的适配器对象。

### *async method* `handle_event(self, current_event)` {#Bot.handle_event}

被适配器对象调用，根据优先级分发事件给所有插件，并处理插件的 `stop` 、 `skip` 等信号。

此方法不应该被用户手动调用。

- **Arguments**

  - **current_event** (*T_Event*) - 当前待处理的 `Event`。

### *method* `handle_exit(self)` {#Bot.handle_exit}

当机器人收到退出信号时，根据情况进行处理。

### *method* `load_adapter(self, name)` {#Bot.load_adapter}

加载单个适配器。

- **Arguments**

  - **name** (*str*) - 适配器名称，格式和 Python `import` 语句相同。

- **Returns**

  Type: *Optional[T_Adapter]*

  被加载的适配器对象。

### *method* `load_plugin(self, name)` {#Bot.load_plugin}

加载单个插件。

- **Arguments**

  - **name** (*str*) - 插件名称，格式和 Python `import` 语句相同。

- **Returns**

  Type: *Optional[Type[T_Plugin]]*

  被加载的插件类。

### *method* `load_plugins_from_dir(self, path)` {#Bot.load_plugins_from_dir}

从指定路径列表中加载插件，以 `_` 开头的插件不会被导入。路径可以是相对路径或绝对路径。

- **Arguments**

  - **path** (*Iterable[str]*) - 由储存插件的路径文本组成的列表。 例如： `['path/of/plugins/', '/home/xxx/alicebot/plugins']` 。

### *async method* `main_loop(self)` {#Bot.main_loop}

### *readonly property* `plugins` {#Bot.plugins}

Type: *List[Type[T_Plugin]]*

当前已经加载的插件的列表。

### *method* `run(self)` {#Bot.run}

运行 AliceBot ，监听并拦截系统退出信号，更新机器人配置。