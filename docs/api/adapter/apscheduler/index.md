# alicebot.adapter.apscheduler

APScheduler 适配器。

本适配器用于实现定时任务，适配器将使用 APScheduler 实现定时任务，在设定的时间产生一个事件供插件处理。
APScheduler 使用方法请参考: [APScheduler](https://apscheduler.readthedocs.io/) 。

## *class* `APSchedulerAdapter`(self, bot) {#APSchedulerAdapter}

Bases: `alicebot.adapter.Adapter`

APScheduler 适配器。

- **Arguments**

  - **bot** (*Bot*) - 当前机器人对象。

- **Attributes**

  - **name** (*str*)

  - **scheduler** (*apscheduler.schedulers.asyncio.AsyncIOScheduler*)

  - **plugin_class_to_job** (*Dict[Type[alicebot.plugin.Plugin[Any, Any, Any]], apscheduler.job.Job]*)

### *class* `Config`(__pydantic_self__, **data) {#Config}

Bases: `alicebot.config.ConfigModel`

APScheduler 配置类，将在适配器被加载时被混入到机器人主配置中。

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **scheduler_config** (*Dict[str, Any]*) - 调度器配置。

### *async method* `create_event(self, plugin_class)` {#APSchedulerAdapter.create_event}

创建 `APSchedulerEvent` 事件。

- **Arguments**

  - **plugin_class** (*Type[alicebot.plugin.Plugin[Any, Any, Any]]*) - `Plugin` 类。

### *async method* `run(self)` {#APSchedulerAdapter.run}

启动调度器。

### *async method* `send(self, *args, **kwargs)` {#APSchedulerAdapter.send}

APScheduler 适配器不适用发送消息。

- **Arguments**

  - **args** (*Any*)

  - **kwargs** (*Any*)

- **Returns**

  Type: *Any*

### *async method* `shutdown(self)` {#APSchedulerAdapter.shutdown}

关闭调度器。

### *async method* `startup(self)` {#APSchedulerAdapter.startup}

创建 `AsyncIOScheduler` 对象。

## *function* `scheduler_decorator(trigger, trigger_args, override_rule = False)` {#scheduler_decorator}

用于为插件类添加计划任务功能的装饰器。

- **Arguments**

  - **trigger** (*str*) - APScheduler 触发器。

  - **trigger_args** (*Dict[str, Any]*) - APScheduler 触发器参数。

  - **override_rule** (*bool*) - 是否重写 `rule()` 方法。
  若为 `True`，则会在 `rule()` 方法中添加处理本插件定义的计划任务事件的逻辑。