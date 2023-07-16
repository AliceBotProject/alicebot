# alicebot.plugin

AliceBot 插件。

所有 AliceBot 插件的基类。所有用户编写的插件必须继承自 `Plugin` 类。

## *class* `PluginLoadType` {#PluginLoadType}

Bases: `enum.Enum`

插件加载类型。

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