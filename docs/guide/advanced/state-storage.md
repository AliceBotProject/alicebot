# 状态存储

插件类在每次处理事件时都会被实例化，也就是说，对于每个事件，都是不同的 `Plugin` 实例，但有时候，我们可能会希望插件可以存储一些数据，每次实例化后都可以使用，这时候就要用到状态存储了。

## 插件状态

插件类有一个 `state` 属性，你可以将其视为一个普通的属性，初始值是 `None`，但是，它会被永久存储下来，即使在同一个插件的不同的实例中访问它也会得到相同的值。

下面我们使用一个计数插件为例：

```python
from alicebot import Plugin


class Count(Plugin):
    async def handle(self) -> None:
        if self.state is None:
            self.state = 0
        self.state += 1
        await self.event.reply(f"count: {self.state}")

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return self.event.message.get_plain_text() == "count"

```

每次收到 count 消息，插件都会回复一个数字，并且是递增的。

你可以根据需要对 `state` 赋值为任何数据。

但是 `state` 是被存储在内存中的，这意味着，当你关闭 AliceBot 再次打开，并不会得到存储的状态，你可以通过 Python 自带的 [pickle](https://docs.python.org/zh-cn/3/library/pickle.html) 或 [json](https://docs.python.org/zh-cn/3/library/json.html) 库进行序列化，将状态保存到文件中。

## 初始化插件状态

注意到上面的计数插件中，我们在使用状态之前先判断了 `self.state` 是否为 `None`，这是因为当插件第一次被执行时，插件状态还未被设置，默认为 `None`，我们需要对插件状态进行初始化。

那么我们是否可以换一种方式进行插件状态的初始化呢？

AliceBot 提供了 `__init_state__()` 方法用于初始化插件状态。

```python {5-6}
from alicebot import Plugin


class Count(Plugin):
    def __init_state__(self):
        return 0

    async def handle(self) -> None:
        self.state += 1
        await self.event.reply(f"count: {self.state}")

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return self.event.message.get_plain_text() == "count"

```

AliceBot 将在检测到插件状态没有被设置时，自动将插件状态设置为 `__init_state__()` 方法的返回值。

除此之外，AliceBot 还提供了另一种初始化插件状态的方法。

```python {4}
from alicebot import Plugin


class Count(Plugin, init_state=0):
    async def handle(self) -> None:
        self.state += 1
        await self.event.reply(f"count: {self.state}")

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return self.event.message.get_plain_text() == "count"

```

这种方法将会自动设置 `__init_state__()` 方法，主要用于静态数值的初始化。

## 全局状态

`state` 对于每个插件是独立的，它可以在**同一个插件**的**不同实例**中共享，但不能在**不同插件**中共享。如果你需要在不同插件中共享状态，可以使用全局状态，即 `self.bot.global_state` 属性，全局状态是一个 Python 字典。

下面的示例是两个不同的插件，实现分别对一个数字全局状态进行增减。

```python
from alicebot import Plugin


class GlobalStateTest1(Plugin):
    async def handle(self) -> None:
        if self.bot.global_state.get("count", None) is None:
            self.bot.global_state["count"] = 0
        self.bot.global_state["count"] += 1
        await self.event.reply(f'add: {self.bot.global_state["count"]}')

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return self.event.message.get_plain_text() == "add"

```

```python
from alicebot import Plugin


class GlobalStateTest2(Plugin):
    async def handle(self) -> None:
        if self.bot.global_state.get("count", None) is None:
            self.bot.global_state["count"] = 0
        self.bot.global_state["count"] -= 1
        await self.event.reply(f"sub: {self.bot.global_state['count']}")

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return self.event.message.get_plain_text() == "sub"

```
