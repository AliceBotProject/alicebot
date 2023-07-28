# alicebot

AliceBot

简单的 Python 异步多后端机器人框架

本模块从子模块导入了以下内容：
- `Bot` =\> [`alicebot.bot.Bot`](./bot#Bot)
- `Event` =\> [`alicebot.event.Event`](./event#Event)
- `Plugin` =\> [`alicebot.plugin.Plugin`](./plugin#Plugin)
- `Adapter` =\> [`alicebot.adapter.Adapter`](./adapter/#Adapter)
- `ConfigModel` =\> [`alicebot.config.ConfigModel`](./config#ConfigModel)
- `Depends` =\> [`alicebot.dependencies.Depends`](./dependencies#Depends)

## *abstract class* `Adapter`(self, bot) {#Adapter}

Bases: `typing.Generic`, `abc.ABC`

协议适配器基类。

- **Arguments**

  - **bot** (*Bot*) - 当前机器人对象。

- **Attributes**

  - **name** (*str*) - 适配器的名称。

  - **bot** (*Bot*) - 当前的机器人对象。

  - **Config** (*Type[~T_Config]*)

### *readonly property* `config` {#Adapter.config}

Type: *~T_Config*

适配器配置。

### *async method* `get(self, func = None, *, event_type = None, max_try_times = None, timeout = None)` {#Adapter.get}

获取满足指定条件的的事件，协程会等待直到适配器接收到满足条件的事件、超过最大事件数或超时。

类似 `Bot` 类的 `get()` 方法，但是隐含了判断产生事件的适配器是本适配器。
等效于 `Bot` 类的 `get()` 方法传入 adapter_type 为本适配器类型。

- **Arguments**

  - **func** (*Optional[Callable[[~T_Event], Union[bool, Awaitable[bool]]]]*) - 协程或者函数，函数会被自动包装为协程执行。
  要求接受一个事件作为参数，返回布尔值。
  当协程返回 `True` 时返回当前事件。
  当为 `None` 时相当于输入对于任何事件均返回真的协程，即返回适配器接收到的下一个事件。

  - **event_type** (*Union[Type[~T_Event], Type[~_T_Event], NoneType]*) - 当指定时，只接受指定类型的事件，先于 func 条件生效。默认为 `None`。

  - **max_try_times** (*Optional[int]*) - 最大事件数。

  - **timeout** (*Union[int, float, NoneType]*) - 超时时间。

- **Returns**

  Type: *Union[~T_Event, ~_T_Event]*

  返回满足 func 条件的事件。

- **Raises**

  - **GetEventTimeout** - 超过最大事件数或超时。

### *async method* `run(self)` {#Adapter.run}

适配器运行方法，适配器开发者必须实现该方法。

适配器运行过程中保持保持运行，当此方法结束后， AliceBot 不会自动重新启动适配器。

- **Returns**

  Type: *None*

### *async method* `safe_run(self)` {#Adapter.safe_run}

附带有异常处理地安全运行适配器。

### *async method* `send(self, *args, **kwargs)` {#Adapter.send}

发送消息，需要适配器开发者实现。

- **Arguments**

  - **args** (*Any*)

  - **kwargs** (*Any*)

- **Returns**

  Type: *Any*

### *async method* `shutdown(self)` {#Adapter.shutdown}

在适配器结束运行时运行的方法，用于安全地关闭适配器。

AliceBot 在接收到系统的结束信号后依次运行并等待所有适配器的 `shutdown()` 方法。
当强制退出时此方法可能未被执行。

### *async method* `startup(self)` {#Adapter.startup}

在适配器开始运行前运行的方法，用于初始化适配器。

AliceBot 依次运行并等待所有适配器的 `startup()` 方法，待运行完毕后再创建 `run()` 任务。

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

## *class* `ConfigModel`(__pydantic_self__, **data) {#ConfigModel}

Bases: `pydantic.main.BaseModel`

AliceBot 配置模型。

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **__config_name__** - 配置名称。

### *class* `Config`(self, /, *args, **kwargs) {#ConfigModel.Config}

Bases: `object`

- **Arguments**

  - **args**

  - **kwargs**

## *function* `Depends(dependency = None, *, use_cache = True)` {#Depends}

子依赖装饰器。

- **Arguments**

  - **dependency** (*Union[Type[Union[~T, AsyncContextManager[~T], ContextManager[~T]]], Callable[[], AsyncGenerator[~T, NoneType]], Callable[[], Generator[~T, NoneType, NoneType]], NoneType]*) - 依赖类。如果不指定则根据字段的类型注释自动判断。

  - **use_cache** (*bool*) - 是否使用缓存。默认为 `True`。

- **Returns**

  Type: *~T*

  返回内部子依赖对象。

## *class* `Event`(self, adapter, **data) {#Event}

Bases: `abc.ABC`, `pydantic.main.BaseModel`, `typing.Generic`

事件类的基类。

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **adapter** (*~T_Adapter*) - 产生当前事件的适配器对象。

  - **type** (*Optional[str]*) - 事件类型。

  - **__handled__** - 表示事件是否被处理过了，用于适配器处理。警告：请勿手动更改此属性的值。

### *class* `Config`(self, /, *args, **kwargs) {#Event.Config}

Bases: `object`

- **Arguments**

  - **args**

  - **kwargs**

### *readonly property* `adapter` {#Event.adapter}

Type: *~T_Adapter*

产生当前事件的适配器对象。

## *abstract class* `Plugin`(self, /, *args, **kwargs) {#Plugin}

Bases: `abc.ABC`, `typing.Generic`

所有 AliceBot 插件的基类。

- **Arguments**

  - **args**

  - **kwargs**

- **Attributes**

  - **event** (*~T_Event*) - 当前正在被此插件处理的事件。

  - **priority** (*ClassVar[int]*) - 插件的优先级，数字越小表示优先级越高，默认为 0。

  - **block** (*ClassVar[bool]*) - 插件执行结束后是否阻止事件的传播。`True` 表示阻止。

  - **Config** (*Type[~T_Config]*)

  - **__plugin_load_type__** - 插件加载类型，由 AliceBot 自动设置，反映了此插件是如何被加载的。

  - **__plugin_file_path__** - 当插件加载类型为 `PluginLoadType.CLASS` 时为 `None`，
  否则为定义插件在的 Python 模块的位置。

### *readonly property* `bot` {#Plugin.bot}

Type: *Bot*

机器人对象。

### *readonly property* `config` {#Plugin.config}

Type: *~T_Config*

插件配置。

### *async method* `handle(self)` {#Plugin.handle}

处理事件的方法。当 `rule()` 方法返回 `True` 时 AliceBot 会调用此方法。每个插件必须实现此方法。

- **Returns**

  Type: *None*

### *readonly property* `name` {#Plugin.name}

Type: *str*

插件类名称。

### *async method* `rule(self)` {#Plugin.rule}

匹配事件的方法。事件处理时，会按照插件的优先级依次调用此方法，当此方法返回 `True` 时将事件交由此插件处理。每个插件必须实现此方法。

注意：不建议直接在此方法内实现对事件的处理，事件的具体处理请交由 `handle()` 方法。

- **Returns**

  Type: *bool*

### *method* `skip(self)` {#Plugin.skip}

跳过自身继续当前事件传播。

- **Returns**

  Type: *NoReturn*

### *data descriptor* `state` {#Plugin.state}

插件状态。

### *method* `stop(self)` {#Plugin.stop}

停止当前事件传播。

- **Returns**

  Type: *NoReturn*