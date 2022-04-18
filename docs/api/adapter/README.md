# alicebot.adapter

AliceBot 协议适配器。

所有协议适配器都必须继承自 `Adapter` 基类。

## *abstract class* `BaseAdapter`(self, bot) {#BaseAdapter}

Bases: `abc.ABC`

协议适配器基类，仅实现最基础的适配器功能，通常情况下，适配器开发者开发的适配器应继承自 `Adapter` 而非本类。

- **Arguments**

  - **bot** (*Bot*)

- **Attributes**

  - **name** (*str*) - 适配器的名称。

  - **bot** (*Bot*) - 当前的机器人对象。

### *async method* `run(self)` {#BaseAdapter.run}

适配器运行方法，适配器开发者必须实现该方法。

适配器运行过程中保持保持运行，当此方法结束后，AliceBot 不会自动重新启动适配器。

### *async method* `safe_run(self)` {#BaseAdapter.safe_run}

附带有异常处理地安全运行适配器。

### *async method* `shutdown(self)` {#BaseAdapter.shutdown}

在适配器结束运行时运行的方法，用于安全地关闭适配器。

AliceBot 在接收到系统的结束信号后依次运行并等待所有适配器的 `shutdown()` 方法。当强制退出时此方法可能未被执行。

### *async method* `startup(self)` {#BaseAdapter.startup}

在适配器开始运行前运行的方法，用于初始化适配器。

AliceBot 依次运行并等待所有适配器的 `startup()` 方法，待运行完毕后再创建 `run()` 任务。

## *abstract class* `Adapter`(self, bot) {#Adapter}

Bases: `alicebot.adapter.BaseAdapter`, `abc.ABC`

协议适配器基类，在 `BaseAdapter` 的基础上提供了 `handle_event()` 和 `get()` 等方法，通常情况下推荐使用。

- **Arguments**

  - **bot** (*Bot*)

- **Attributes**

  - **cond** (*alicebot.utils.Condition*) - Condition 对象，用于事件处理。

### *async method* `get(self, func = None, max_try_times = None, timeout = None)` {#Adapter.get}

获取满足指定条件的的事件，协程会等待直到适配器接收到满足条件的事件、超过最大事件数或超时。

- **Arguments**

  - **func** (*Optional[Callable[[T_Event], Union[bool, Awaitable[bool]]]]*) - 协程或者函数，函数会被自动包装为协程执行。要求接受一个事件作为参数，返回布尔值。当协程返回 `True` 时返回当前事件。
  当为 `None` 时相当于输入对于任何事件均返回真的协程，即返回适配器接收到的下一个事件。

  - **max_try_times** (*Optional[int]*) - 最大事件数。

  - **timeout** (*Union[int, float, NoneType]*) - 超时时间。

- **Returns**

  Type: *T_Event*

  返回满足 func 条件的事件。

- **Raises**

  - **AdapterTimeout** - 超过最大事件数或超时。

### *async method* `handle_event(self, event)` {#Adapter.handle_event}

进行事件处理。

- **Arguments**

  - **event** (*T_Event*) - 待处理的事件。

### *async method* `send(self, *args, **kwargs)` {#Adapter.send}

发送消息，需要适配器开发者实现。