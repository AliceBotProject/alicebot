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

  - **plugin\_class\_to\_job** (_dict\[type\[alicebot.plugin.Plugin\[typing.Any, typing.Any, typing.Any\]\], apscheduler.job.Job\]_)

### _class_ `Config` {#Config}

Bases: `alicebot.config.ConfigModel`

APScheduler 配置类，将在适配器被加载时被混入到机器人主配置中。

- **Attributes**

  - **scheduler\_config** (_dict\[str, typing.Any\]_) - 调度器配置。

### _async method_ `create_event(self, plugin_class)` {#APSchedulerAdapter-create-event}

创建 `APSchedulerEvent` 事件。

- **Arguments**

  - **plugin\_class** (_type\[alicebot.plugin.Plugin\[typing.Any, typing.Any, typing.Any\]\]_) - `Plugin` 类。

- **Returns**

  Type: _None_

### _async method_ `run(self)` {#APSchedulerAdapter-run}

适配器运行方法，适配器开发者必须实现该方法。

适配器运行过程中保持保持运行，当此方法结束后，AliceBot 不会自动重新启动适配器。

- **Returns**

  Type: _None_

### _async method_ `send(self, *args, **kwargs)` {#APSchedulerAdapter-send}

APScheduler 适配器不适用发送消息。

- **Arguments**

  - **args** (_Any_)

  - **kwargs** (_Any_)

- **Returns**

  Type: _Any_

### _async method_ `shutdown(self)` {#APSchedulerAdapter-shutdown}

在适配器结束运行时运行的方法，用于安全地关闭适配器。

AliceBot 在接收到系统的结束信号后先发送 cancel 请求给 run 任务。
在所有适配器都停止运行后，会依次运行并等待所有适配器的 `shutdown()` 方法。
当强制退出时此方法可能未被执行。

- **Returns**

  Type: _None_

### _async method_ `startup(self)` {#APSchedulerAdapter-startup}

在适配器开始运行前运行的方法，用于初始化适配器。

AliceBot 依次运行并等待所有适配器的 `startup()` 方法，待运行完毕后再创建 `run()` 任务。

- **Returns**

  Type: _None_

## _function_ `scheduler_decorator(trigger, trigger_args, override_rule = False)` {#scheduler-decorator}

用于为插件类添加计划任务功能的装饰器。

- **Arguments**

  - **trigger** (_str_) - APScheduler 触发器。

  - **trigger\_args** (_dict\[str, typing.Any\]_) - APScheduler 触发器参数。

  - **override\_rule** (_bool_) - 是否重写 `rule()` 方法。
  若为 `True`，则会在 `rule()` 方法中添加处理本插件定义的计划任务事件的逻辑。

- **Returns**

  Type: _Callable\[\[type\[~PluginT\]\], type\[~PluginT\]\]_
