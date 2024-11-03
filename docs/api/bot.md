# alicebot.bot

AliceBot 机器人对象。

AliceBot 的基础模块，每一个 AliceBot 机器人即是一个 `Bot` 实例。

## _class_ `Bot` {#Bot}

Bases: `object`

AliceBot 机器人对象，定义了机器人的基本方法。

读取并储存配置 `Config`，加载适配器 `Adapter` 和插件 `Plugin`，并进行事件分发。

- **Attributes**

  - **config** (_alicebot.config.MainConfig_) - 机器人配置。

  - **adapters** (_list\[alicebot.adapter.Adapter\[typing.Any, typing.Any\]\]_) - 当前已经加载的适配器的列表。

  - **plugins\_priority\_dict** (_dict\[int, list\[type\[alicebot.plugin.Plugin\[typing.Any, typing.Any, typing.Any\]\]\]\]_) - 插件优先级字典。

  - **plugin\_state** (_dict\[str, typing.Any\]_) - 插件状态。

  - **global\_state** (_dict\[typing.Any, typing.Any\]_) - 全局状态。

### _method_ `__init__(self, *, config_file = 'config.toml', config_dict = None, hot_reload = False, handle_signals = True)` {#Bot---init--}

初始化 AliceBot，读取配置文件，创建配置，加载适配器和插件。

- **Arguments**

  - **config\_file** (_Optional\[str\]_) - 配置文件，如不指定则使用默认的 `config.toml`。
  若指定为 `None`，则不加载配置文件。

  - **config\_dict** (_Optional\[dict\[str, Any\]\]_) - 配置字典，默认为 `None。`
  若指定字典，则会忽略 `config_file` 配置，不再读取配置文件。

  - **hot\_reload** (_bool_) - 热重载。
  启用后将自动检查 `plugin_dir` 中的插件文件更新，并在更新时自动重新加载。

  - **handle\_signals** (_bool_) - 是否处理系统信号，默认为 `True`。

- **Returns**

  Type: _None_

### _method_ `adapter_run_hook(self, func)` {#Bot-adapter-run-hook}

注册一个适配器运行时的函数。

- **Arguments**

  - **func** (_Callable\[\[Adapter\[Any, Any\]\], collections.abc.Awaitable\[None\]\]_) - 被注册的函数。

- **Returns**

  Type: _Callable\[\[Adapter\[Any, Any\]\], collections.abc.Awaitable\[None\]\]_

  被注册的函数。

### _method_ `adapter_shutdown_hook(self, func)` {#Bot-adapter-shutdown-hook}

注册一个适配器关闭时的函数。

- **Arguments**

  - **func** (_Callable\[\[Adapter\[Any, Any\]\], collections.abc.Awaitable\[None\]\]_) - 被注册的函数。

- **Returns**

  Type: _Callable\[\[Adapter\[Any, Any\]\], collections.abc.Awaitable\[None\]\]_

  被注册的函数。

### _method_ `adapter_startup_hook(self, func)` {#Bot-adapter-startup-hook}

注册一个适配器初始化时的函数。

- **Arguments**

  - **func** (_Callable\[\[Adapter\[Any, Any\]\], collections.abc.Awaitable\[None\]\]_) - 被注册的函数。

- **Returns**

  Type: _Callable\[\[Adapter\[Any, Any\]\], collections.abc.Awaitable\[None\]\]_

  被注册的函数。

### _method_ `bot_exit_hook(self, func)` {#Bot-bot-exit-hook}

注册一个 Bot 退出时的函数。

- **Arguments**

  - **func** (_Callable\[\[Bot\], collections.abc.Awaitable\[None\]\]_) - 被注册的函数。

- **Returns**

  Type: _Callable\[\[Bot\], collections.abc.Awaitable\[None\]\]_

  被注册的函数。

### _method_ `bot_run_hook(self, func)` {#Bot-bot-run-hook}

注册一个 Bot 启动时的函数。

- **Arguments**

  - **func** (_Callable\[\[Bot\], collections.abc.Awaitable\[None\]\]_) - 被注册的函数。

- **Returns**

  Type: _Callable\[\[Bot\], collections.abc.Awaitable\[None\]\]_

  被注册的函数。

### _method_ `event_postprocessor_hook(self, func)` {#Bot-event-postprocessor-hook}

注册一个事件后处理函数。

- **Arguments**

  - **func** (_Callable\[\[Event\[Any\]\], collections.abc.Awaitable\[None\]\]_) - 被注册的函数。

- **Returns**

  Type: _Callable\[\[Event\[Any\]\], collections.abc.Awaitable\[None\]\]_

  被注册的函数。

### _method_ `event_preprocessor_hook(self, func)` {#Bot-event-preprocessor-hook}

注册一个事件预处理函数。

- **Arguments**

  - **func** (_Callable\[\[Event\[Any\]\], collections.abc.Awaitable\[None\]\]_) - 被注册的函数。

- **Returns**

  Type: _Callable\[\[Event\[Any\]\], collections.abc.Awaitable\[None\]\]_

  被注册的函数。

### _method_ `exit(self)` {#Bot-exit}

退出 AliceBot。

- **Returns**

  Type: _None_

### _async method_ `get(self, func = None, *, event_type = None, adapter_type = None, max_try_times = None, timeout = None)` {#Bot-get}

获取满足指定条件的的事件，协程会等待直到适配器接收到满足条件的事件、超过最大事件数或超时。

- **Arguments**

  - **func** (_Optional\[Callable\[\[Any\], Union\[bool, collections.abc.Awaitable\[bool\]\]\]\]_) - 协程或者函数，函数会被自动包装为协程执行。
  要求接受一个事件作为参数，返回布尔值。当协程返回 `True` 时返回当前事件。
  当为 `None` 时相当于输入对于任何事件均返回真的协程，即返回适配器接收到的下一个事件。

  - **event\_type** (_Optional\[type\[alicebot.event.Event\[Any\]\]\]_) - 当指定时，只接受指定类型的事件，先于 func 条件生效。默认为 `None`。

  - **adapter\_type** (_Optional\[type\[alicebot.adapter.Adapter\[Any, Any\]\]\]_) - 当指定时，只接受指定适配器产生的事件，先于 func 条件生效。默认为 `None`。

  - **max\_try\_times** (_Optional\[int\]_) - 最大事件数。

  - **timeout** (_Union\[int, float, NoneType\]_) - 超时时间。

- **Returns**

  Type: _alicebot.event.Event\[Any\]_

  返回满足 `func` 条件的事件。

- **Raises**

  - **GetEventTimeout** - 超过最大事件数或超时。

### _method_ `get_adapter(self, adapter)` {#Bot-get-adapter}

按照名称或适配器类获取已经加载的适配器。

- **Arguments**

  - **adapter** (_Union\[str, type\[~AdapterT\]\]_) - 适配器名称或适配器类。

- **Returns**

  Type: _Union\[alicebot.adapter.Adapter\[Any, Any\], ~AdapterT\]_

  获取到的适配器对象。

- **Raises**

  - **LookupError** - 找不到此名称的适配器对象。

### _method_ `get_plugin(self, name)` {#Bot-get-plugin}

按照名称获取已经加载的插件类。

- **Arguments**

  - **name** (_str_) - 插件名称

- **Returns**

  Type: _type\[alicebot.plugin.Plugin\[typing.Any, typing.Any, typing.Any\]\]_

  获取到的插件类。

- **Raises**

  - **LookupError** - 找不到此名称的插件类。

### _async method_ `handle_event(self, current_event, *, handle_get = True, show_log = True)` {#Bot-handle-event}

被适配器对象调用，根据优先级分发事件给所有插件，并处理插件的 `stop` 、 `skip` 等信号。

此方法不应该被用户手动调用。

- **Arguments**

  - **current\_event** (_alicebot.event.Event\[Any\]_) - 当前待处理的 `Event`。

  - **handle\_get** (_bool_) - 当前事件是否可以被 get 方法捕获，默认为 `True`。

  - **show\_log** (_bool_) - 是否在日志中显示，默认为 `True`。

- **Returns**

  Type: _None_

### _method_ `load_adapters(self, *adapters)` {#Bot-load-adapters}

加载适配器。

- **Arguments**

  - **\*adapters** (_Union\[type\[alicebot.adapter.Adapter\[Any, Any\]\], str\]_) - 适配器类或适配器名称，类型可以是 `Type[Adapter]` 或 `str`。
  如果为 `Type[Adapter]` 类型时，将作为适配器类进行加载。
  如果为 `str` 类型时，将作为适配器模块名称进行加载，格式和 Python `import` 语句相同。
      例如：`path.of.adapter`。

- **Returns**

  Type: _None_

### _method_ `load_plugins(self, *plugins)` {#Bot-load-plugins}

加载插件。

- **Arguments**

  - **\*plugins** (_Union\[type\[alicebot.plugin.Plugin\[Any, Any, Any\]\], str, pathlib.Path\]_) - 插件类、插件模块名称或者插件模块文件路径。
  类型可以是 `Type[Plugin]`, `str` 或 `pathlib.Path`。
  如果为 `Type[Plugin]` 类型时，将作为插件类进行加载。
  如果为 `str` 类型时，将作为插件模块名称进行加载，格式和 Python `import` 语句相同。
      例如：`path.of.plugin`。
  如果为 `pathlib.Path` 类型时，将作为插件模块文件路径进行加载。
      例如：`pathlib.Path("path/of/plugin")`。

- **Returns**

  Type: _None_

### _method_ `load_plugins_from_dirs(self, *dirs)` {#Bot-load-plugins-from-dirs}

从目录中加载插件，以 `_` 开头的模块中的插件不会被导入。路径可以是相对路径或绝对路径。

- **Arguments**

  - **\*dirs** (_pathlib.Path_) - 储存包含插件的模块的模块路径。
  例如：`pathlib.Path("path/of/plugins/")` 。

- **Returns**

  Type: _None_

### _readonly property_ `plugins` {#Bot-plugins}

Type: _list\[type\[alicebot.plugin.Plugin\[typing.Any, typing.Any, typing.Any\]\]\]_

当前已经加载的插件的列表。

### _method_ `reload_plugins(self)` {#Bot-reload-plugins}

手动重新加载所有插件。

- **Returns**

  Type: _None_

### _method_ `restart(self)` {#Bot-restart}

退出并重新运行 AliceBot。

- **Returns**

  Type: _None_

### _method_ `run(self)` {#Bot-run}

运行 AliceBot，监听并拦截系统退出信号，更新机器人配置。

- **Returns**

  Type: _None_

### _async method_ `run_async(self)` {#Bot-run-async}

异步运行 AliceBot。

- **Returns**

  Type: _None_
