# alicebot.adapter.apscheduler

APScheduler 适配器。

本适配器用于实现定时任务，适配器将使用 APScheduler 实现定时任务，在设定的时间产生一个事件供插件处理。
APScheduler 使用方法请参考：[APScheduler](https://apscheduler.readthedocs.io/)。

## _class_ `APSchedulerAdapter` {#APSchedulerAdapter}

Bases: `alicebot.adapter.Adapter`

APScheduler 适配器。

- **Attributes**

  - **name** (_str_)

  - **scheduler** (_apscheduler.schedulers.asyncio.AsyncIOScheduler_)

  - **plugin\_class\_to\_job** (_Dict\[Type\[alicebot.plugin.Plugin\[Any, Any, Any\]\], apscheduler.job.Job\]_)

### _class_ `Config` {#Config}

Bases: `alicebot.config.ConfigModel`

APScheduler 配置类，将在适配器被加载时被混入到机器人主配置中。

- **Attributes**

  - **scheduler\_config** (_Dict\[str, Any\]_) - 调度器配置。

#### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

### _method_ `__init__(self, bot)` {#Adapter.\_\_init\_\_}

初始化。

- **Arguments**

  - **bot** (_Bot_) - 当前机器人对象。

- **Returns**

  Type: _None_

### _async method_ `create_event(self, plugin_class)` {#APSchedulerAdapter.create\_event}

创建 `APSchedulerEvent` 事件。

- **Arguments**

  - **plugin\_class** (_Type\[alicebot.plugin.Plugin\[Any, Any, Any\]\]_) - `Plugin` 类。

- **Returns**

  Type: _None_

### _async method_ `run(self)` {#APSchedulerAdapter.run}

启动调度器。

- **Returns**

  Type: _None_

### _async method_ `send(self, *args, **kwargs)` {#APSchedulerAdapter.send}

APScheduler 适配器不适用发送消息。

- **Arguments**

  - **args** (_Any_)

  - **kwargs** (_Any_)

- **Returns**

  Type: _Any_

### _async method_ `shutdown(self)` {#APSchedulerAdapter.shutdown}

关闭调度器。

- **Returns**

  Type: _None_

### _async method_ `startup(self)` {#APSchedulerAdapter.startup}

创建 `AsyncIOScheduler` 对象。

- **Returns**

  Type: _None_

## _function_ `scheduler_decorator(trigger, trigger_args, override_rule = False)` {#scheduler\_decorator}

用于为插件类添加计划任务功能的装饰器。

- **Arguments**

  - **trigger** (_str_) - APScheduler 触发器。

  - **trigger\_args** (_Dict\[str, Any\]_) - APScheduler 触发器参数。

  - **override\_rule** (_bool_) - 是否重写 `rule()` 方法。
  若为 `True`，则会在 `rule()` 方法中添加处理本插件定义的计划任务事件的逻辑。

- **Returns**

  Type: _Callable\[\[Type\[~PluginT\]\], Type\[~PluginT\]\]_
