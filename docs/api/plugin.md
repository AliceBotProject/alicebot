# alicebot.plugin

## 插件

所有 AliceBot 插件的基类。所有用户编写的插件必须继承自 `Plugin` 类。


## _class_ `Plugin`

基类：`abc.ABC`

所有 AliceBot 插件的基类。


### `priority`

插件的优先级，数字越小表示优先级越高，默认为 0。


### `block`

插件执行结束后是否阻止事件的传播。`True` 表示阻止。
相当于在 `handle()` 方法最后调用 `self.stop()` 。


### `event`

当前正在被此插件处理的事件。


### property `name: str`


* **返回**

    插件类名称。



* **返回类型**

    str



### property `adapter: T_Adapter`


* **返回**

    产生当前事件的适配器对象。



* **返回类型**

    T_Adapter



### property `bot: Bot`


* **返回**

    机器人对象。



### property `config`


* **返回**

    机器人配置。



### `stop()`

停止当前事件传播。


### `skip()`

跳过自身继续当前事件传播。


### _abstract async_ `handle()`

处理事件的方法。当 `rule()` 方法返回 `True` 时 AliceBot 会调用此方法。每个插件必须实现此方法。


### _abstract async_ `rule()`

匹配事件的方法。事件处理时，会按照插件的优先级依次调用此方法，当此方法返回 `True` 时将事件交由此插件处理。每个插件必须实现此方法。
注意：不建议直接在此方法内实现对事件的处理，事件的具体处理请交由 `handle()` 方法。


* **返回类型**

    bool
