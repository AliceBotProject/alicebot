# alicebot.adapter

## 协议适配器

所有协议适配器都必须继承自 `AbstractAdapter` 基类。


## _class_ `AbstractAdapter`

基类：`abc.ABC`

协议适配器基类。


### `name`

适配器的名称。


### `event_queue`

事件队列，用于 `get()` 方法。


### `max_event_queue_len`

最大事件队列长度。


### `wait_for_get`

当此属性为 `Ture` 时，`handle_event()` 将不对当前事件进行传播和处理，用于 `get()` 方法。


### `bot`

当前的机器人对象。


### _async_ `safe_run()`

附带有异常处理地安全运行适配器。


### _abstract async_ `run()`

适配器运行方法，适配器开发者必须实现该方法。
适配器运行过程中保持保持运行，当此方法结束后，AliceBot 不会自动重新启动适配器。


### _async_ `startup()`

在适配器开始运行前运行的方法。
AliceBot 依次运行并等待所有适配器的 `startup()` 方法，待运行完毕后再创建 `run()` 任务。


### _async_ `shutdown()`

在适配器结束后运行后运行的方法。
AliceBot 在接收到系统的结束信号后依次运行并等待所有适配器的 `shutdown()` 方法。当强制退出时此方法可能未被执行。


### `handle_event(event)`

调用 `Bot` 对象进行事件处理，并维护一个事件队列用于 `get()` 方法，所有适配器在接收到事件后必须使用此方法进行事件处理。
:param event: 待处理的事件。


### _async_ `get(current_event, func=None, max_try_times=None, timeout=None)`

获取满足指定条件的的事件，协程会等待直到适配器接收到满足条件的事件、超过最大事件数或超时。


* **参数**

    
    * **current_event** – 当前事件，方法将仅检索此事件后接收到的事件。


    * **func** – (optional) 协程或者函数，函数会被自动包装为协程执行。要求接受一个事件作为参数，返回布尔值。当协程返回 `True` 时返回当前事件。
    当为 `None` 时相当于输入对于任何事件均返回真的协程，即返回适配器接收到的下一个事件。


    * **max_try_times** – 最大事件数。


    * **timeout** – 超时。



* **返回**

    返回满足 func 条件的事件。



* **返回类型**

    ‘T_Event’



* **引发**

    [**AdapterTimeout**](../exception.md#alicebot.exception.AdapterTimeout) – 超过最大事件数或超时。
