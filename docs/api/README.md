# alicebot


## _class_ `Bot`

基类：`object`

AliceBot 机器人对象，定义了机器人的基本方法，读取并储存配置 `Config` ，加载适配器 `Adapter` 和插件 `Plugin`，并进行事件分发。


### _property_ `plugins`


* **返回**

    当前已经加载的插件的列表。



* **返回类型**

    List[‘T_Plugin’]



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

    被加载的适配器类。



* **返回类型**

    Optional[Type[‘T_Adapter’]]



### `load_plugins_from_dir(path)`

从指定路径列表中加载插件，以 `_` 开头的插件不会被导入。
路径可以是相对路径或绝对路径。


* **参数**

    **path** – 由储存插件的路径文本组成的列表。 `['path/of/plugins/', '/home/xxx/alicebot/plugins']`
