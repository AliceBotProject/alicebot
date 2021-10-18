# alicebot


## _class_ `Bot`

基类：`object`

AliceBot 机器人对象，定义了机器人的基本方法，读取并储存配置 `Config`，加载适配器 `Adapter` 和插件 `Plugin`，并进行事件分发。


### property `plugins: List[Type[T_Plugin]]`


* **返回**

    当前已经加载的插件的列表。



* **返回类型**

    List[Type[‘T_Plugin’]]



### `run()`

运行 AliceBot ，监听并拦截系统退出信号，更新机器人配置。


### `handle_exit()`

当机器人收到退出信号时，根据情况进行处理。


### _async_ `handle_event(current_event)`

被适配器对象调用，根据优先级分发事件给所有插件，并处理插件的 `stop` 、 `skip` 等信号。
此方法不应该被用户手动调用。


* **参数**

    **current_event** – 当前待处理的 `Event`。



### `load_plugin(name)`

加载单个插件。


* **参数**

    **name** – 插件名称，格式和 Python `import` 语句相同，



* **返回**

    被加载的插件类。



* **返回类型**

    Optional[Type[‘T_Plugin’]]



### `load_adapter(name)`

加载单个适配器。


* **参数**

    **name** – 适配器名称，格式和 Python `import` 语句相同，



* **返回**

    被加载的适配器对象。



* **返回类型**

    Optional[‘T_Adapter’]



### `load_plugins_from_dir(path)`

从指定路径列表中加载插件，以 `_` 开头的插件不会被导入。
路径可以是相对路径或绝对路径。


* **参数**

    **path** – 由储存插件的路径文本组成的列表。 `['path/of/plugins/', '/home/xxx/alicebot/plugins']`



### `get_loaded_adapter_by_name(name)`

按照名称获取已经加载的适配器。


* **参数**

    **name** – 适配器名称。



* **返回**

    获取到的适配器对象。



* **引发**

    **LookupError** – 找不到此名称的适配器对象。



### `bot_run_hook(func)`

注册一个 Bot 启动时的函数。


* **参数**

    **func** – 被注册的函数。



* **返回**

    被注册的函数。



* **返回类型**

    Callable[[‘Bot’], Awaitable[NoReturn]]



### `bot_exit_hook(func)`

注册一个 Bot 退出时的函数。


* **参数**

    **func** – 被注册的函数。



* **返回**

    被注册的函数。



* **返回类型**

    Callable[[‘Bot’], Awaitable[NoReturn]]



### `adapter_startup_hook(func)`

注册一个适配器初始化时的函数。


* **参数**

    **func** – 被注册的函数。



* **返回**

    被注册的函数。



* **返回类型**

    Callable[[‘T_Adapter’], Awaitable[NoReturn]]



### `adapter_run_hook(func)`

注册一个适配器运行时的函数。


* **参数**

    **func** – 被注册的函数。



* **返回**

    被注册的函数。



* **返回类型**

    Callable[[‘T_Adapter’], Awaitable[NoReturn]]



### `adapter_shutdown_hook(func)`

注册一个适配器关闭时的函数。


* **参数**

    **func** – 被注册的函数。



* **返回**

    被注册的函数。



* **返回类型**

    Callable[[‘T_Adapter’], Awaitable[NoReturn]]



### `event_preprocessor_hook(func)`

注册一个事件预处理函数。


* **参数**

    **func** – 被注册的函数。



* **返回**

    被注册的函数。



* **返回类型**

    Callable[[‘T_Event’], Awaitable[NoReturn]]



### `event_postprocessor_hook(func)`

注册一个事件后处理函数。


* **参数**

    **func** – 被注册的函数。



* **返回**

    被注册的函数。



* **返回类型**

    Callable[[‘T_Event’], Awaitable[NoReturn]]
