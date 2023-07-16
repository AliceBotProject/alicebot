# alicebot.adapter

AliceBot 协议适配器。

所有协议适配器都必须继承自 `Adapter` 基类。

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