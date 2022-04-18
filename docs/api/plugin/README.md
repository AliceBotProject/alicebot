# alicebot.plugin

AliceBot 插件。

所有 AliceBot 插件的基类。所有用户编写的插件必须继承自 `Plugin` 类。

## *abstract class* `Plugin`(self, event) {#Plugin}

Bases: `abc.ABC`

所有 AliceBot 插件的基类。

- **Arguments**

  - **event**

- **Attributes**

  - **event** (*T_Event*) - 当前正在被此插件处理的事件。

  - **priority** (*int*) - 插件的优先级，数字越小表示优先级越高，默认为 0。

  - **block** (*bool*) - 插件执行结束后是否阻止事件的传播。True 表示阻止。

### *readonly property* `adapter` {#Plugin.adapter}

Type: *T_Adapter*

产生当前事件的适配器对象。

### *readonly property* `bot` {#Plugin.bot}

Type: *Bot*

机器人对象。

### *readonly property* `config` {#Plugin.config}

Type: *MainConfig*

机器人配置。

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

### *method* `stop(self)` {#Plugin.stop}

停止当前事件传播。

- **Returns**

  Type: *NoReturn*