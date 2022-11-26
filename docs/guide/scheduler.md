# 定时任务

AliceBot 的定时任务底层是使用 [APScheduler](https://apscheduler.readthedocs.io/) 库实现的，AliceBot 将其封装为一个适配器，提供与普通适配器相同的接口。

## 下载与加载适配器

定时任务适配器像其他适配器一样需要独立下载：

```sh
pip install alicebot-adapter-apscheduler
```

或者在安装 AliceBot 的同时搭配对应的适配器：

```sh
pip install aliebot[apscheduler]
```

下载后，你可以像加载一个普通的适配器一样在 `config.toml` 配置文件中配置：

```toml
[bot]
adapters = ["alicebot.adapter.xxxx", "alicebot.adapter.apscheduler"]
```

或者也可以手动加载：

```python
from alicebot import Bot

bot = Bot()
bot.load_adapters("alicebot.adapter.apscheduler")

if __name__ == "__main__":
    bot.run()

```

但是，需要注意的是，在手动加载时需要在加载所有插件后再加载适配器。

## 配置 APScheduler

`alicebot-adapter-apscheduler` 适配器只有一个配置项 `scheduler_config` ：

```toml
[bot]
adapters = ["alicebot.adapter.xxxx", "alicebot.adapter.apscheduler"]

[adapter.apscheduler]
scheduler_config = { "apscheduler.timezone" = "Asia/Shanghai" }
```

具体配置项请参考 APScheduler 文档： [scheduler-config](https://apscheduler.readthedocs.io/en/latest/userguide.html#scheduler-config) 。

## 使用

### 直接添加属性

加载适配器后，对于需要定时被执行的插件需要具有类似下面的格式：

```python
from alicebot import Plugin


class TestPlugin(Plugin):
    __schedule__ = True
    trigger = "interval"
    trigger_args = {"seconds": 10}

    async def handle(self) -> None:
        pass

    async def rule(self) -> bool:
        return (
            self.event.adapter.name == "apscheduler"
            and type(self) == self.event.plugin_class
        )

```

定时执行的插件必须要设置 `__schedule__` 、 `trigger` 和 `trigger_args` 属性。

其中 `__schedule__` 必须为 True，`trigger` 表示 APScheduler 的触发器， `trigger_args` 表示适配器配置，他们将会按照下面的形式传递给调度器（schedulers）的 `add_job()` 方法：

```python
scheduler.add_job(func, trigger, **trigger_args)
```

APScheduler 适配器在启动时会遍历所有插件，寻找符合上述条件的插件，并按照插件中的描述添加定时任务。

当定时任务被触发时，APScheduler 适配器将会产生一个事件，并进行正常的事件传播。

这个事件的 `type` 属性总是 `apscheduler` ，并且具有一个 `plugin_class` 属性，表示定义了这个定时任务的插件类。你可以通过在 `rule()` 方法中添加 `type(self) == self.event.plugin_class` 保证这个插件仅处理它自己定义的定时事件。

### 使用类装饰器（推荐）

除了上面的方法外，你还可以使用类装饰器将一个已有的插件装饰为定时任务插件。

```python
from alicebot import Plugin
from alicebot.adapter.apscheduler import scheduler_decorator


@scheduler_decorator(
    trigger="interval", trigger_args={"seconds": 10}, override_rule=True
)
class TestPlugin(Plugin):
    async def handle(self) -> None:
        pass

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return str(self.event.message).lower() == "hello"

```

上面的写法等效于：

```python
from alicebot import Plugin


class TestPlugin(Plugin):
    __schedule__ = True
    trigger = "interval"
    trigger_args = {"seconds": 10}

    async def handle(self) -> None:
        pass

    async def rule(self) -> bool:
        if self.event.name == "apscheduler" and type(self) == self.event.plugin_class:
            return True
        else:
            if self.event.adapter.name != "cqhttp":
                return False
            if self.event.type != "message":
                return False
            return str(self.event.message).lower() == "hello"

```

如上面的例子所示，设置 `override_rule` 参数为 True 可以自动重写 `rule()` 方法，添加处理定时任务事件的相关逻辑。

## 使用技巧

当需要同一个定时任务同时唤醒多个插件，同时又设置了多个定时任务，不希望它们相互干扰时，可以像下面这样做。

第一个插件：

```python
from alicebot import Plugin
from alicebot.adapter.apscheduler import scheduler_decorator


@scheduler_decorator(
    trigger="interval", trigger_args={"seconds": 10}, override_rule=False
)
class PluginA(Plugin):
    scheduler_flag = "abc"

    async def handle(self) -> None:
        pass

    async def rule(self) -> bool:
        if (
            self.event.type == "apscheduler"
            and getattr(self.event.plugin_class, "scheduler_flag", "") == "abc"
        ):
            return True
        else:
            pass

```

第二个插件：

```python
from alicebot import Plugin


class PluginB(Plugin):
    async def handle(self) -> None:
        pass

    async def rule(self) -> bool:
        if (
            self.event.type == "apscheduler"
            and getattr(self.event.plugin_class, "scheduler_flag", "") == "abc"
        ):
            return True
        else:
            pass

```

你需要为定义了定时任务的插件设置一个独一无二的 `scheduler_flag` 属性，当然这个属性也可以叫做任何其他的名称，然后第二个插件判断 `scheduler_flag` 的值，即可判断当前事件是否是第一个插件定义的定时事件。
