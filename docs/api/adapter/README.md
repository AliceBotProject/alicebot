# alicebot.adapter

## 协议适配器

所有协议适配器都必须继承自 `Adapter` 基类。


## _class_ `BaseAdapter`

基类：`abc.ABC`

协议适配器基类，仅实现最基础的适配器功能，通常情况下，适配器开发者开发的适配器应继承自 `Adapter` 而非本类。


### `name`

适配器的名称。


### `bot`

当前的机器人对象。


### _async_ `safe_run()`

附带有异常处理地安全运行适配器。


### _abstract async_ `run()`

适配器运行方法，适配器开发者必须实现该方法。
适配器运行过程中保持保持运行，当此方法结束后，AliceBot 不会自动重新启动适配器。


### _async_ `startup()`

在适配器开始运行前运行的方法，用于初始化适配器。
AliceBot 依次运行并等待所有适配器的 `startup()` 方法，待运行完毕后再创建 `run()` 任务。


### _async_ `shutdown()`

在适配器结束运行时运行的方法，用于安全地关闭适配器。
AliceBot 在接收到系统的结束信号后依次运行并等待所有适配器的 `shutdown()` 方法。当强制退出时此方法可能未被执行。


## _class_ `Adapter`

基类：`alicebot.adapter.BaseAdapter`, `abc.ABC`

协议适配器基类，在 `BaseAdapter` 的基础上提供了 `handle_event()` 和 `get()` 等方法，通常情况下推荐使用。


### `cond`

Condition 对象，用于事件处理。


### _async_ `handle_event(event)`

进行事件处理。


* **参数**

    **event** – 待处理的事件。



### _async_ `get(func=None, max_try_times=None, timeout=None)`

获取满足指定条件的的事件，协程会等待直到适配器接收到满足条件的事件、超过最大事件数或超时。


* **参数**

    
    * **func** – (optional) 协程或者函数，函数会被自动包装为协程执行。要求接受一个事件作为参数，返回布尔值。当协程返回 `True` 时返回当前事件。
    当为 `None` 时相当于输入对于任何事件均返回真的协程，即返回适配器接收到的下一个事件。


    * **max_try_times** – 最大事件数。


    * **timeout** – 超时。



* **返回**

    返回满足 func 条件的事件。



* **返回类型**

    ‘T_Event’



* **引发**

    [**AdapterTimeout**](../exceptions.md#alicebot.exceptions.AdapterTimeout) – 超过最大事件数或超时。



### _async_ `send(*args, **kwargs)`

发送消息，需要适配器开发者实现。
