# 插件进阶

## 事件传播控制

有时候，我们可能需要对事件的传播进行一些控制，除了基础的定义 `bolck` 属性来决定此插件执行结束后是否继续进行事件传播外，AilceBot 还提供了一些方法以供高级的逻辑控制。

### `skip()` 方法

`skip()` 方法用于跳过当前插件继续事件传播。通常来说，你也可以在 `handle()` 方法使用 `return` 语句实现类似的效果，但这个方法在某些情况下可以简化一些操作。如：

```python
from alicebot.plugin import Plugin


class TestPlugin(Plugin):
    async def handle(self) -> None:
        await self.foo()

    async def rule(self) -> bool:
        return True

    async def foo(self):
        self.skip()

```

也就是 `skip()` 方法可以在插件类的任何方法内被调用并立刻生效。

### `stop()` 方法

`stop()` 方法用于结束当前事件传播。但请注意，当此方法被调用后当前事件传播并不会被立即结束，与本插件同优先级的插件仍会被执行完毕。也就是说，本方法的作用是使比当前插件优先级低的插件不被执行。

### `stop()` 方法和 `block` 属性

你可能会发现，设置 `block` 属性为 `True` 和在 `handle()` 方法最后加一句 `self.stop()` 没什么区别。实际上，它们在大多数情况下确实没有区别，除了一种情况，即当 `handle()` 方法中出现异常时，最后的 `self.stop()` 语句不会被执行，但 `block` 属性仍会起效。也就是， `block` 属性为 `True` 和下面的示例效果大致上等同：

```python
from alicebot.plugin import Plugin


class TestPlugin(Plugin):
    async def handle(self) -> None:
        try:
            # do something
            pass
        finally:
            self.stop()

    async def rule(self) -> bool:
        return True

```

### 原理

实际上，这两个方法是使用 Python 的异常处理实现的，所以，在编写插件时请注意不要捕获所有异常，如：

```python
# 错误代码：skip() 方法不会生效
from alicebot.plugin import Plugin


class TestPlugin(Plugin):
    async def handle(self) -> None:
        try:
            self.skip()
        except:
            pass

    async def rule(self) -> bool:
        return True

```

而应该至少使用：

```python
from alicebot.plugin import Plugin


class TestPlugin(Plugin):
    async def handle(self) -> None:
        try:
            self.skip()
        except Exception:
            pass

    async def rule(self) -> bool:
        return True

```

## 状态存储

插件类在每次运行时都会被实例化，也就是说，对于每个事件，都是不同的 `Plugin` 实例，但有时候，我们可能会希望插件可以存储一些数据，每次调用时都可以使用，这时候就要用到状态存储了。

插件类有一个 `state` 属性，你可以将其视为一个普通的属性，初始值是 `None` ，但是，它会被永久存储下来，即使在同一个插件的不同的实例中访问它也会得到相同的值。

下面我们使用一个计数插件为例：

```python
from alicebot.plugin import Plugin


class Count(Plugin):
    async def handle(self) -> None:
        if self.state is None:
            self.state = 0
        self.state += 1
        await self.event.reply(f'count: {self.state}')

    async def rule(self) -> bool:
        if self.event.adapter.name != 'cqhttp':
            return False
        if self.event.type != 'message':
            return False
        return self.event.message.get_plain_text() == 'count'

```

每次收到 count 消息，插件都会回复一个数字，并且是递增的。

你可以根据需要对 `state` 赋值为任何数据。

但是 `state` 是被存储在内存中的，则意味着，当你关闭 AliceBot 再次打开，并不会得到存储的状态，你可以通过 Python 自带的 [pickle](https://docs.python.org/zh-cn/3/library/pickle.html) 或 [json](https://docs.python.org/zh-cn/3/library/json.html) 库进行序列化，将状态保存到文件中。

此外， `state` 每个插件是独立的，它可以在同一个插件的不同实例中共享，但不能在不同插件中共享，如果你需要在不同插件中共享状态，可以使用全局状态，即 `self.bot.global_state` 属性，全局状态是一个 Python 字典。

下面的示例是两个不同的插件，实现分别对一个数字全局状态进行增减。

```python
from alicebot.plugin import Plugin


class GlobalStateTest1(Plugin):
    async def handle(self) -> None:
        if self.bot.global_state.get('count', None) is None:
            self.bot.global_state['count'] = 0
        self.bot.global_state['count'] += 1
        await self.event.reply(f'add: {self.bot.global_state["count"]}')

    async def rule(self) -> bool:
        if self.event.adapter.name != 'cqhttp':
            return False
        if self.event.type != 'message':
            return False
        return self.event.message.get_plain_text() == 'add'

```

```python
from alicebot.plugin import Plugin


class GlobalStateTest2(Plugin):
    async def handle(self) -> None:
        if self.bot.global_state.get('count', None) is None:
            self.bot.global_state['count'] = 0
        self.bot.global_state['count'] -= 1
        await self.event.reply(f'sub: {self.bot.global_state["count"]}')

    async def rule(self) -> bool:
        if self.event.adapter.name != 'cqhttp':
            return False
        if self.event.type != 'message':
            return False
        return self.event.message.get_plain_text() == 'sub'

```

## 插件配置

在 [基础配置](./basic-config.md) 一节中提到，你可以直接通过 `self.config` 访问当前机器人的配置。但有时我们可能会希望插件配置像适配器配置一样放在一个独立的键中，以提高这个插件的可移植性，那么我们可以这样处理：

```python
from pydantic import BaseModel
from alicebot.plugin import Plugin


class TestPlugin(Plugin):
    async def handle(self) -> None:
        print(self.config.test_plugin.a)
        print(self.config.test_plugin.b)

    async def rule(self) -> bool:
        return True


class Config(BaseModel):
    __config_name__ = 'test_plugin'
    a: str = 'test'
    b: int = 1

```

`config.json` 文件对应如下：

```json
{
    "plugin_dir": ["plugins"],
    "adapters": ["alicebot.adapter.cqhttp"],
    "test_plugin": {
        "a": "abc",
        "b": 123
    }
}
```

需要在插件内写一个名称为 `Config` 的继承于 `pydantic.BaseModel` 的类，这是一个 `pydantic` 的模型类，具体可以参考 [pydantic 的文档](https://pydantic-docs.helpmanual.io/) ，简而言之，格式为：

`变量名称: 类型[ = 默认值] `

如果不指定默认值，且类型不是 `Optional[...]`， `Union[None, ...]` 或 `Any`，则这个字段是必填的，在非必需的情况下，建议不要在插件中使用必填字段，这会导致不指定这个字段时，不只是这个插件，整个 AliceBot 都不能运行。

特别的是，`Config` 类中**必须**要有一个 `__config_name__` 属性，表示这个插件在配置文件中对应的键名。

如果你使用了包的格式编写插件的话，建议把 `Config` 类放在单独的 `config.py` 文件中。

然后在 `__init__.py` 中导入：

```python
from .config import Config
...
```

::: tip 注意
这个类的类名必须为 `Config` 且必须包含 `__config_name__` 属性。
:::

## `get()` 方法

在 [插件基础](/guide/plugin-basics) 中相信你已经使用过了 `get()` 方法。

实际上，`Bot` 和 `Adapter` 类都有一个 `get()` 方法。

```python
self.bot.get()
self.event.adapter.get()
```

它们的区别在于，`Bot` 的 `get()` 方法会捕获所有适配器产生的事件，而 `Adapter` 的 `get()` 方法仅会捕获此适配器产生的时间，即相当于在条件中隐含了判断适配器是自身的条件。

## 初始化后处理

插件类会在事件传播时被实例化，对于每个事件都会实例化一个新的插件类，如果你需要在被实例化时就进行一些操作，为了避免一些不必要的麻烦，建议不要直接重写 `__init__()` 方法。为此，AliceBot 提供了一个 `__post_init__()` 方法。`__post_init__()` 方法将被 `__init__()` 方法在最后调用，默认没有定义任何内容，你可以通过重写该方法进行初始化后处理。

```python
from alicebot.plugin import Plugin


class TestPlugin(Plugin):
    def __post_init__(self):
        pass

    async def handle(self) -> None:
        pass

    async def rule(self) -> bool:
        return True

```

## 输出日志

如果你想要在插件中输出到控制台什么东西的话，建议不要直接使用 `print()`，可以这样输出日志：

```python
from alicebot.plugin import Plugin
from alicebot.log import logger


class TestPlugin(Plugin):

    async def handle(self) -> None:
        logger.info('TestPlugin Processing!')

    async def rule(self) -> bool:
        return True

```

## 为多个插件的共用部分创建基类

如果你编写了许多个有着不少相同的部分的插件，编写多次相同代码显然不是一个优雅的解决方案，我们可以利用类的继承创建一个所有插件的共用基类。

```python
from abc import ABC

class BasePlugin(Plugin, ABC):
    ...
```

注意：这个插件基类必须像上面那样显式继承自 `abc.ABC` 类。
