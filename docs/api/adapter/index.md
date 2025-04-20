# alicebot.adapter

AliceBot 协议适配器。

所有协议适配器都必须继承自 `Adapter` 基类。

## _abstract class_ `Adapter` {#Adapter}

Bases: `typing.Generic`, `abc.ABC`

协议适配器基类。

- **Attributes**

  - **name** (_str_) - 适配器的名称。

  - **bot** (_Bot_) - 当前的机器人对象。

  - **Config** (_type\[~ConfigT\]_)

### _method_ `__init__(self, bot)` {#Adapter---init--}

初始化。

- **Arguments**

  - **bot** (_Bot_) - 当前机器人对象。

- **Returns**

  Type: _None_

### _readonly property_ `config` {#Adapter-config}

Type: _~ConfigT_

适配器配置。

### _async method_ `get(self, func = None, *, event_type = None, max_try_times = None, timeout = None)` {#Adapter-get}

获取满足指定条件的的事件，协程会等待直到适配器接收到满足条件的事件、超过最大事件数或超时。

类似 `Bot` 类的 `get()` 方法，但是隐含了判断产生事件的适配器是本适配器。
等效于 `Bot` 类的 `get()` 方法传入 adapter_type 为本适配器类型。

- **Arguments**

  - **func** (_Optional\[Callable\[\[Any\], Union\[bool, collections.abc.Awaitable\[bool\]\]\]\]_) - 协程或者函数，函数会被自动包装为协程执行。
  要求接受一个事件作为参数，返回布尔值。
  当协程返回 `True` 时返回当前事件。
  当为 `None` 时相当于输入对于任何事件均返回真的协程，即返回适配器接收到的下一个事件。

  - **event\_type** (_Any_) - 当指定时，只接受指定类型的事件，先于 func 条件生效。默认为 `None`。

  - **max\_try\_times** (_Optional\[int\]_) - 最大事件数。

  - **timeout** (_Union\[int, float, NoneType\]_) - 超时时间。

- **Returns**

  Type: _alicebot.event.Event\[Any\]_

  返回满足 func 条件的事件。

- **Raises**

  - **GetEventTimeout** - 超过最大事件数或超时。

### _async method_ `run(self)` {#Adapter-run}

适配器运行方法，适配器开发者必须实现该方法。

适配器运行过程中保持保持运行，当此方法结束后，AliceBot 不会自动重新启动适配器。

- **Returns**

  Type: _None_

### _async method_ `safe_run(self)` {#Adapter-safe-run}

附带有异常处理地安全运行适配器。

- **Returns**

  Type: _None_

### _async method_ `shutdown(self)` {#Adapter-shutdown}

在适配器结束运行时运行的方法，用于安全地关闭适配器。

AliceBot 在接收到系统的结束信号后先发送 cancel 请求给 run 任务。
在所有适配器都停止运行后，会依次运行并等待所有适配器的 `shutdown()` 方法。
当强制退出时此方法可能未被执行。

- **Returns**

  Type: _None_

### _async method_ `startup(self)` {#Adapter-startup}

在适配器开始运行前运行的方法，用于初始化适配器。

AliceBot 依次运行并等待所有适配器的 `startup()` 方法，待运行完毕后再创建 `run()` 任务。

- **Returns**

  Type: _None_
