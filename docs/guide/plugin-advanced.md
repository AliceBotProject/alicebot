# 插件进阶

## 事件传播控制

有时候，我们可能需要对事件的传播进行一些控制，除了基础的定义 `bolck` 属性是否为真来决定此插件执行结束后还是否继续进行事件传播外，AilceBot 还提供了一些方法以供高级的逻辑控制。

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

::: tip 提示
实际上，上面的写法并不完全等同，它会导致即使 `# do something` 部分出现异常，AliceBot 的日志也不会捕获到异常，所以并不推荐这种写法，除非做好了异常的捕获。
:::

## 插件配置

在 [基础配置](./basic-config.md) 一节中提到，你可以直接通过 `self.config` 访问当前机器人的配置。但有时我们可能会希望插件会像适配器配置一样放在一个独立的键中，以提高这个插件的可移植性，那么我们可以这样处理：

```python
from pydantic import BaseModel
from alicebot.plugin import Plugin


class TestPlugin(Plugin):
    async def handle(self) -> None:
      	print(self.config.test_plugin.a)
        print(self.config.test_plugin.b)
        pass

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
    "plugins": null,
    "plugin_dir": ["plugins"],
    "adapters": ["alicebot.adapter.cqhttp"],
    "test_plugin": {
        "a": "abc",
        "b": 123
    }
}
```

需要在插件内写一个名称为 `Config` 继承于 `pydantic.BaseModel` 的类，这是一个 `pydantic` 的模型类，具体可以参考 [pydantic 的文档](https://pydantic-docs.helpmanual.io/) ，简而言之，格式为：

`变量名称: 类型[ = 默认值] `

如果不指定默认值，且类型不是 `Optional[...]`， `Union[None, ...]` 或 `Any`，则这个字段是必填的，在非必需的情况下，建议不要在插件中使用必填字段，这会导致不指定这个字段时 AliceBot 不能运行，而不止仅仅是这个插件。

特别的是，`Config` 类中**必须**要有一个 `__config_name__` 属性，表示这个插件在配置文件中对应的键名。

如果你使用了包的格式编写插件的话，建议把 `Config` 类放在单独的 `config.py` 文件中。

然后在 `__init__.py` 中导入：

```python
from .config import Config
...
```

## `send()` 和 `get()` 方法

实际上，`send()` 和 `get()` 方法都是适配器的方法，插件中的只是引用了适配器中的方法。

```python
async def send(self, *args, **kwargs):
    return await self.adapter.send(*args, **kwargs)

async def get(self,
              func: Optional[Callable[['T_Event'], Union[bool, Awaitable[bool]]]] = None,
              max_try_times: int = None,
              timeout: Optional[Union[int, float]] = None) -> Optional['T_Event']:
    return await self.adapter.get(self.event, func, max_try_times, timeout)

```

其中 `send()` 方法和适配器中的完全相同，但 `get()` 方法中的无需传如当前正在被处理的事件，

## 初始化后处理

插件类会在事件传播时被实例化，如果你需要在被实例化时就进行一些操作，为了避免一些不必要的麻烦，建议不要直接重写 `__init__()` 方法。为此，AliceBot 提供了一个 `__post_init__()` 方法。`__post_init__()` 方法将被 `__init__()` 方法在最后调用，默认没有定义任何内容，你可以通过重写该方法进行初始化后处理。

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

如果你想要在插件中输出到控制台什么东西的话，建议不要直接使用 `print()`，可以这样做：

```python
from alicebot.plugin import Plugin
from alicebot.log import logger


class TestPlugin(Plugin):

    async def handle(self) -> None:
        logger.info('TestPlugin Processing!')

    async def rule(self) -> bool:
        return True

```
