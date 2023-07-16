# alicebot.bot

AliceBot 机器人对象。

AliceBot 的基础模块，每一个 AliceBot 机器人即是一个 `Bot` 实例。

## *class* `Bot`(self, *, config_file = 'config.toml', config_dict = None, hot_reload = False) {#Bot}

Bases: `object`

AliceBot 机器人对象，定义了机器人的基本方法。

读取并储存配置 `Config`，加载适配器 `Adapter` 和插件 `Plugin`，并进行事件分发。

- **Arguments**

  - **config_file** (*Optional[str]*) - 配置文件，如不指定则使用默认的 `config.toml`。
  若指定为 `None`，则不加载配置文件。

  - **config_dict** (*Optional[Dict[str, Any]]*) - 配置字典，默认为 `None。`
  若指定字典，则会忽略 `config_file` 配置，不再读取配置文件。

  - **hot_reload** (*bool*) - 热重载。
  启用后将自动检查 `plugin_dir` 中的插件文件更新，并在更新时自动重新加载。

- **Attributes**

  - **config** (*alicebot.config.MainConfig*) - 机器人配置。

  - **should_exit** (*asyncio.locks.Event*) - 机器人是否应该进入准备退出状态。

  - **adapters** (*List[alicebot.adapter.Adapter[Any, Any]]*) - 当前已经加载的适配器的列表。

  - **plugins_priority_dict** (*Dict[int, List[Type[alicebot.plugin.Plugin[Any, Any, Any]]]]*) - 插件优先级字典。

  - **plugin_state** (*Dict[str, Any]*) - 插件状态。

  - **global_state** (*Dict[Any, Any]*) - 全局状态。

### *method* `adapter_run_hook(self, func)` {#Bot.adapter_run_hook}

注册一个适配器运行时的函数。

- **Arguments**

  - **func** (*Callable[[Adapter[Any, Any]], Awaitable[NoneType]]*) - 被注册的函数。

- **Returns**

  Type: *Callable[[Adapter[Any, Any]], Awaitable[NoneType]]*

  被注册的函数。

### *method* `adapter_shutdown_hook(self, func)` {#Bot.adapter_shutdown_hook}

注册一个适配器关闭时的函数。

- **Arguments**

  - **func** (*Callable[[Adapter[Any, Any]], Awaitable[NoneType]]*) - 被注册的函数。

- **Returns**

  Type: *Callable[[Adapter[Any, Any]], Awaitable[NoneType]]*

  被注册的函数。

### *method* `adapter_startup_hook(self, func)` {#Bot.adapter_startup_hook}

注册一个适配器初始化时的函数。

- **Arguments**

  - **func** (*Callable[[Adapter[Any, Any]], Awaitable[NoneType]]*) - 被注册的函数。

- **Returns**

  Type: *Callable[[Adapter[Any, Any]], Awaitable[NoneType]]*

  被注册的函数。

### *method* `bot_exit_hook(self, func)` {#Bot.bot_exit_hook}

注册一个 Bot 退出时的函数。

- **Arguments**

  - **func** (*Callable[[Bot], Awaitable[NoneType]]*) - 被注册的函数。

- **Returns**

  Type: *Callable[[Bot], Awaitable[NoneType]]*

  被注册的函数。

### *method* `bot_run_hook(self, func)` {#Bot.bot_run_hook}

注册一个 Bot 启动时的函数。

- **Arguments**

  - **func** (*Callable[[Bot], Awaitable[NoneType]]*) - 被注册的函数。

- **Returns**

  Type: *Callable[[Bot], Awaitable[NoneType]]*

  被注册的函数。

### *method* `event_postprocessor_hook(self, func)` {#Bot.event_postprocessor_hook}

注册一个事件后处理函数。

- **Arguments**

  - **func** (*Callable[[Event[Any]], Awaitable[NoneType]]*) - 被注册的函数。

- **Returns**

  Type: *Callable[[Event[Any]], Awaitable[NoneType]]*

  被注册的函数。

### *method* `event_preprocessor_hook(self, func)` {#Bot.event_preprocessor_hook}

注册一个事件预处理函数。

- **Arguments**

  - **func** (*Callable[[Event[Any]], Awaitable[NoneType]]*) - 被注册的函数。

- **Returns**

  Type: *Callable[[Event[Any]], Awaitable[NoneType]]*

  被注册的函数。

### *async method* `get(self, func = None, *, event_type = None, adapter_type = None, max_try_times = None, timeout = None)` {#Bot.get}

获取满足指定条件的的事件，协程会等待直到适配器接收到满足条件的事件、超过最大事件数或超时。

- **Arguments**

  - **func** (*Optional[Callable[[alicebot.event.Event[Any]], Union[bool, Awaitable[bool]]]]*) - 协程或者函数，函数会被自动包装为协程执行。
  要求接受一个事件作为参数，返回布尔值。当协程返回 `True` 时返回当前事件。
  当为 `None` 时相当于输入对于任何事件均返回真的协程，即返回适配器接收到的下一个事件。

  - **event_type** (*Optional[Type[alicebot.event.Event[Any]]]*) - 当指定时，只接受指定类型的事件，先于 func 条件生效。默认为 `None`。

  - **adapter_type** (*Optional[Type[alicebot.adapter.Adapter[Any, Any]]]*) - 当指定时，只接受指定适配器产生的事件，先于 func 条件生效。默认为 `None`。

  - **max_try_times** (*Optional[int]*) - 最大事件数。

  - **timeout** (*Union[int, float, NoneType]*) - 超时时间。

- **Returns**

  Type: *alicebot.event.Event[typing.Any]*

  返回满足 `func` 条件的事件。

- **Raises**

  - **GetEventTimeout** - 超过最大事件数或超时。

### *method* `get_adapter(self, adapter)` {#Bot.get_adapter}

按照名称或适配器类获取已经加载的适配器。

- **Arguments**

  - **adapter** (*Union[str, Type[~T_Adapter]]*) - 适配器名称或适配器类。

- **Returns**

  Type: *Union[alicebot.adapter.Adapter[Any, Any], ~T_Adapter]*

  获取到的适配器对象。

- **Raises**

  - **LookupError** - 找不到此名称的适配器对象。

### *method* `get_plugin(self, name)` {#Bot.get_plugin}

按照名称获取已经加载的插件类。

- **Arguments**

  - **name** (*str*) - 插件名称

- **Returns**

  Type: *Type[alicebot.plugin.Plugin[Any, Any, Any]]*

  获取到的插件类。

- **Raises**

  - **LookupError** - 找不到此名称的插件类。

### *async method* `handle_event(self, current_event, *, handle_get = True, show_log = True)` {#Bot.handle_event}

被适配器对象调用，根据优先级分发事件给所有插件，并处理插件的 `stop` 、 `skip` 等信号。

此方法不应该被用户手动调用。

- **Arguments**

  - **current_event** (*alicebot.event.Event[typing.Any]*) - 当前待处理的 `Event`。

  - **handle_get** (*bool*) - 当前事件是否可以被 get 方法捕获，默认为 `True`。

  - **show_log** (*bool*) - 是否在日志中显示，默认为 `True`。

### *method* `load_adapters(self, *adapters)` {#Bot.load_adapters}

加载适配器。

- **Arguments**

  - ***adapters** (*Union[Type[alicebot.adapter.Adapter[Any, Any]], str]*) - 适配器类或适配器名称，类型可以是 `Type[Adapter]` 或 `str`。
  如果为 `Type[Adapter]` 类型时，将作为适配器类进行加载。
  如果为 `str` 类型时，将作为适配器模块名称进行加载，格式和 Python `import` 语句相同。
      例如：`path.of.adapter`。

### *method* `load_plugins(self, *plugins)` {#Bot.load_plugins}

加载插件。

- **Arguments**

  - ***plugins** (*Union[Type[alicebot.plugin.Plugin[Any, Any, Any]], str, pathlib.Path]*) - 插件类、插件模块名称或者插件模块文件路径。
  类型可以是 `Type[Plugin]`, `str` 或 `pathlib.Path`。
  如果为 `Type[Plugin]` 类型时，将作为插件类进行加载。
  如果为 `str` 类型时，将作为插件模块名称进行加载，格式和 Python `import` 语句相同。
      例如：`path.of.plugin`。
  如果为 `pathlib.Path` 类型时，将作为插件模块文件路径进行加载。
      例如：`pathlib.Path("path/of/plugin")`。

### *method* `load_plugins_from_dirs(self, *dirs)` {#Bot.load_plugins_from_dirs}

从目录中加载插件，以 `_` 开头的模块中的插件不会被导入。路径可以是相对路径或绝对路径。

- **Arguments**

  - ***dirs** (*pathlib.Path*) - 储存包含插件的模块的模块路径。
  例如：`pathlib.Path("path/of/plugins/")` 。

### *readonly property* `plugins` {#Bot.plugins}

Type: *List[Type[alicebot.plugin.Plugin[Any, Any, Any]]]*

当前已经加载的插件的列表。

### *method* `reload_plugins(self)` {#Bot.reload_plugins}

手动重新加载所有插件。

### *method* `restart(self)` {#Bot.restart}

退出并重新运行 AliceBot。

### *method* `run(self)` {#Bot.run}

运行 AliceBot ，监听并拦截系统退出信号，更新机器人配置。