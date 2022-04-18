# alicebot.adapter.apscheduler.event

APScheduler 适配器事件。

## *class* `APSchedulerEvent`(__pydantic_self__, **data) {#APSchedulerEvent}

Bases: `alicebot.event.Event`

APSchedulerEvent 事件基类。

- **Attributes**

  - **plugin_class** (*Type*)

### *readonly property* `job` {#APSchedulerEvent.job}

Type: *Job*

产生当前事件的 APScheduler Job 对象。

### *readonly property* `trigger` {#APSchedulerEvent.trigger}

Type: *str*

当前事件对应的 Plugin 的 trigger。

### *readonly property* `trigger_args` {#APSchedulerEvent.trigger_args}

Type: *Dict[str, Any]*

当前事件对应的 Plugin 的 trigger_args。