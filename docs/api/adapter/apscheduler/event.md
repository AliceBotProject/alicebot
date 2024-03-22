# alicebot.adapter.apscheduler.event

APScheduler 适配器事件。

## _class_ `APSchedulerEvent` {#APSchedulerEvent}

Bases: `alicebot.event.Event[APSchedulerAdapter]`

APSchedulerEvent 事件基类。

- **Attributes**

  - **type** (_Optional\[str\]_)

  - **plugin\_class** (_Type\[alicebot.plugin.Plugin\]_)

### _method_ `__init__(self, /, **data)` {#BaseModel.\_\_init\_\_}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

### _readonly property_ `job` {#APSchedulerEvent.job}

Type: _apscheduler.job.Job_

产生当前事件的 APScheduler `Job` 对象。

### _readonly property_ `trigger` {#APSchedulerEvent.trigger}

Type: _Union\[str, apscheduler.triggers.base.BaseTrigger, NoneType\]_

当前事件对应的 Plugin 的 `trigger`。

### _readonly property_ `trigger_args` {#APSchedulerEvent.trigger\_args}

Type: _Optional\[Dict\[str, Any\]\]_

当前事件对应的 Plugin 的 `trigger_args`。
