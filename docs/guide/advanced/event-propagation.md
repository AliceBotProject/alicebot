# 事件传播

之前我们已经了解事件在产生后会按照优先级地分发给各个插件，这个过程被称为事件的传播。

有时候，我们可能需要对事件的传播进行一些控制，除了基础的定义插件的 `block` 属性来决定此插件执行结束后是否继续进行事件传播外，AliceBot 还提供了一些方法以供高级的逻辑控制。

## `skip()` 方法

`skip()` 方法用于跳过当前插件继续事件传播。通常来说，你也可以在 `handle()` 方法使用 `return` 语句实现类似的效果，但这个方法在某些情况下可以简化一些操作。如：

```python
from alicebot import Plugin


class TestPlugin(Plugin):
    async def handle(self) -> None:
        await self.foo()

    async def rule(self) -> bool:
        return True

    async def foo(self):
        self.skip()

```

也就是 `skip()` 方法可以在插件类的任何方法内被调用并立刻生效。

## `stop()` 方法

`stop()` 方法用于结束当前事件传播。但请注意，当此方法被调用后当前事件传播并不会被立即结束，与本插件同优先级的插件仍会被执行完毕。也就是说，本方法的作用是使比当前插件优先级低的插件不被执行。

## `stop()` 方法和 `block` 属性

你可能会发现，设置 `block` 属性为 `True` 和在 `handle()` 方法最后加一句 `self.stop()` 没什么区别。实际上，它们在大多数情况下确实没有区别，除了一种情况，即当 `handle()` 方法中出现异常时，最后的 `self.stop()` 语句不会被执行，但 `block` 属性仍会起效。也就是说，设置 `block` 属性为 `True` 和下面的示例效果大致上等同：

```python
from alicebot import Plugin


class TestPlugin(Plugin):
    async def handle(self) -> None:
        try:
            # do something
        finally:
            self.stop()

    async def rule(self) -> bool:
        return True

```

## 原理

实际上，这两个方法是使用 Python 的异常处理实现的，所以，在编写插件时请注意不要捕获所有异常，如：

```python
# 错误：skip() 方法不会生效
from alicebot import Plugin


class TestPlugin(Plugin):
    async def handle(self) -> None:
        try:
            self.skip()
        except BaseException:
            pass

    async def rule(self) -> bool:
        return True

```

而应该至少使用：

```python
from alicebot import Plugin


class TestPlugin(Plugin):
    async def handle(self) -> None:
        try:
            self.skip()
        except Exception:
            pass

    async def rule(self) -> bool:
        return True

```
