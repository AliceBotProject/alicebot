# alicebot.plugin

AliceBot 插件。

所有 AliceBot 插件的基类。所有用户编写的插件必须继承自 `Plugin` 类。

## _class_ `PluginLoadType` {#PluginLoadType}

Bases: `enum.Enum`

插件加载类型。

## _abstract class_ `Plugin` {#Plugin}

Bases: `abc.ABC`, `typing.Generic`

所有 AliceBot 插件的基类。

- **Attributes**

  - **priority** (_ClassVar\[int\]_) - 插件的优先级，数字越小表示优先级越高，默认为 0。

  - **block** (_ClassVar\[bool\]_) - 插件执行结束后是否阻止事件的传播。`True` 表示阻止。

  - **Config** (_Type\[~ConfigT\]_)

  - **event** - 当前正在被此插件处理的事件。

  - **\_\_plugin\_load\_type\_\_** - 插件加载类型，由 AliceBot 自动设置，反映了此插件是如何被加载的。

  - **\_\_plugin\_file\_path\_\_** - 当插件加载类型为 `PluginLoadType.CLASS` 时为 `None`，
  否则为定义插件在的 Python 模块的位置。

### _readonly property_ `bot` {#Plugin-bot}

Type: _Bot_

机器人对象。

### _readonly property_ `config` {#Plugin-config}

Type: _~ConfigT_

插件配置。

### _async method_ `handle(self)` {#Plugin-handle}

处理事件的方法。当 `rule()` 方法返回 `True` 时 AliceBot 会调用此方法。每个插件必须实现此方法。

- **Returns**

  Type: _None_

### _readonly property_ `name` {#Plugin-name}

Type: _str_

插件类名称。

### _async method_ `rule(self)` {#Plugin-rule}

匹配事件的方法。事件处理时，会按照插件的优先级依次调用此方法，当此方法返回 `True` 时将事件交由此插件处理。每个插件必须实现此方法。

注意：不建议直接在此方法内实现对事件的处理，事件的具体处理请交由 `handle()` 方法。

- **Returns**

  Type: _bool_

### _method_ `skip(self)` {#Plugin-skip}

跳过自身继续当前事件传播。

- **Returns**

  Type: _NoReturn_

### _property_ `state` {#Plugin-state}

Type: _~StateT_

插件状态。

### _method_ `stop(self)` {#Plugin-stop}

停止当前事件传播。

- **Returns**

  Type: _NoReturn_
