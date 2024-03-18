# 编写插件

每个插件即是一个插件类。

虽然并非强制，但建议将一个插件类存放在一个单独的 Python 模块中。

```txt
.
├── plugins
│   ├── a.py (单个 Python 文件)
│   └── b (Python 包)
│      └── __init__.py
├── config.toml
└── main.py
```

下面让我们在 `plugins` 目录中新建一个 `hello.py` 文件。下面的所有操作都发生在这个文件中。

## `Plugin` 类

插件类必须是 `Plugin` 类的子类，并且必须实现 `rule()` 和 `handle()` 方法。

```python {5-6}
from alicebot import Plugin


class HalloAlice(Plugin):
    priority: int = 0
    block: bool = False

    async def handle(self) -> None:
        pass

    async def rule(self) -> bool:
        return True

```

其中类名 `TestPlugin` 建议不要重复。

`priority` 属性表示插件的优先级，数字越小表示优先级越高。

`block` 属性表示当前插件执行结束后是否阻止事件的传播，如果设置为 `True`，则当前插件执行完毕后会停止当前事件传播，比当前插件优先级低的插件将不会被执行。

以上两个属性都是可选的，默认为 `0` 和 `False`。

如[它是如何工作的？](/guide/#它是如何工作的)一节中所说，当协议适配器产生一个事件 (比如机器人接收到了一条消息) 后，会按照优先级分发事件给各个插件，AliceBot 会依次执行每个插件的 `rule()` 方法，根据返回值判断是否要执行 `handle()` 方法。

`Plugin` 类内置了一些属性和方法：

- `self.event`：当前正在被此插件处理的事件。
- `self.name`：插件类名称。
- `self.bot`：机器人对象。
- `self.config`：插件配置。
- `self.state`：插件状态。
- `self.stop()`：停止当前事件传播。
- `self.skip()`：跳过自身继续当前事件传播。

除了 `self.event` 之外的属性和方法将在进阶中详细介绍。

不同适配器产生的事件是不同的，下文以 CQHTTP 适配器为例编写一个 Hello 插件。

## 编写 `rule()` 方法

```python {9-13}
from alicebot import Plugin


class HalloAlice(Plugin):
    async def handle(self) -> None:
        pass

    async def rule(self) -> bool:
        return (
            self.event.adapter.name == "cqhttp"
            and self.event.type == "message"
            and str(self.event.message).lower() == "hello"
        )

```

如果你觉得把所有条件都写在一行不够好看的话也可以这样写：

```python {9-13}
from alicebot import Plugin


class HalloAlice(Plugin):
    async def handle(self) -> None:
        pass

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return str(self.event.message).lower() == "hello"

```

由于不同的适配器产生的事件是不同的，所以应该先判断产生当前事件的适配器名称。

然后应该判断当前事件的类型，CQHTTP 适配器产生的事件的类型有：`message`、`notice` 和 `request`，只有 `message` 类型的适配器才有 `message` 属性，这个插件只对消息事件进行响应。

CQHTTP 适配器消息事件的 `message` 属性表示当前接收到的消息，类型是 `CQHTTPMessage`，是 AliceBot 内置 `Message` 类的子类。

AliceBot 内置的 `Message` 类实现了许多实用的方法，建议所有适配器开发者尽可能使用，CQHTTP 适配器就使用了内置的 `Message` 类。具体使用在[插件进阶](/guide/basics/builtin-message.md)中有提到。在这里可以直接使用 `str()` 函数将 `Message` 类型的 `self.event.message` 转换为字符串。

除此之外，在 `rule()` 方法中常用的还有 `self.event.message.startswith('xxx')` 和 `self.event.message.endswith('xxx')`。相当于字符串的 `startswith()` 和 `endswith()` 方法。

## 编写 `handle()` 方法

```python {6}
from alicebot import Plugin


class HalloAlice(Plugin):
    async def handle(self) -> None:
        await self.event.reply("Hello, Alice!")

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return str(self.event.message).lower() == "hello"

```

正如之前所说的，当 `rule()` 方法返回 `True` 时，`handle()` 方法将会被调用。这里我们使用了 CQHTTP 适配器 `message` 类型事件的一个方法，`reply()` 用于快捷回复当前消息，而不需要额外指定发送消息的接收者。

`reply()` 方法是一个异步方法，所以在调用它时必须加上 `await`，表示等待它直到返回结果。

现在我们的 Hello 插件就编写完成了。现在运行 `main.py` 启动 AliceBot，向机器人发送 `hello` 试一下吧。

## 使用 `get()` 和 `ask()` 方法获取事件

但是有时候，我们的插件可能并不是简单的获取事件之后回复，而是需要进行多轮对话。

下面让我们拓展刚才的 Hello 插件，当用户向机器人问好后，机器人会先询问用户的姓名，然后再回复问好。

```python {8,10-11,13-21}
from alicebot import Plugin
from alicebot.exceptions import GetEventTimeout


class HalloAlice(Plugin):
    async def handle(self) -> None:
        try:
            name_event = await self.event.ask("What is you name?", timeout=10)

            # await self.event.reply("What is you name?")
            # name_event = await self.event.get(timeout=10)

            # await self.event.reply("What is you name?")
            # name_event = await self.bot.get(
            #     lambda event: (
            #         event.adapter.name == "cqhttp"
            #         and event.type == "message"
            #         and event.sender.user_id == self.event.sender.user_id
            #     ),
            #     timeout=10,
            # )
        except GetEventTimeout:
            return
        else:
            await self.event.reply(f"Hello, {name_event.message}!")

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return str(self.event.message).lower() == "hello"

```

这里，我们需要用到 `ask()` 方法，它表示向用户询问，即先向用户发送消息，之后等待用户的回应。

实际上，`ask()` 方法是一个简写，它是下面注释的代码的简写。而其中 `Event` 的 `get()` 方法又是下面注释的 `Bot` 的 `get()` 方法的一种简写形式。

对于 `Bot` 的 `get()` 方法，它的使用方法可以参考 [API 文档](/api/bot.html#Bot.get)。简而言之，它就是用于获取符合条件的事件的，同样的，它也是一个异步方法，请使用 `await` 等待。

需要注意的是，`get()` 和 `ask()` 方法都可以指定超时时间，以避免插件一直等待获取事件，当超时发生时，会引发 `alicebot.exception.GetEventTimeout` 异常，请留心对这种情况的处理。

`Bot`、`Adapter` 和 `Event` 类都有一个 `get()` 方法。

```python
self.bot.get()
self.event.adapter.get()
self.event.get()
```

它们的区别在于，`Bot` 的 `get()` 方法会捕获所有适配器产生的事件，而 `Adapter` 的 `get()` 方法仅会捕获此适配器产生的事件。`Event` 的 `get()` 方法则是一种简写形式，它不需要传入条件，已经隐含了适配器、事件类型和发送者相同的条件。它们的底层实现是完全一致的。

## 输出日志

如果你想要在插件中输出到控制台什么东西的话，建议不要直接使用 `print()`，可以这样输出日志：

```python
import structlog
from alicebot import Plugin

logger = structlog.stdlib.get_logger()


class TestPlugin(Plugin):
    async def handle(self) -> None:
        logger.info("TestPlugin Processing!")

    async def rule(self) -> bool:
        return True

```

## 示例：天气插件

```python
from alicebot import Plugin
from alicebot.exceptions import GetEventTimeout


class Weather(Plugin):
    async def handle(self) -> None:
        args = self.event.get_plain_text().split(" ")

        if len(args) >= 2:
            await self.event.reply(await self.get_weather(args[1]))
            return

        try:
            city_event = await self.event.ask("请输入想要查询天气的城市：", timeout=10)
        except GetEventTimeout:
            return
        else:
            await self.event.reply(await self.get_weather(city_event.get_plain_text()))

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return self.event.message.startswith("天气") or self.event.message.startswith(
            "weather"
        )

    @staticmethod
    async def get_weather(city):
        if city not in ["北京", "上海"]:
            return "你想查询的城市暂不支持！"
        return f"{city}的天气是..."

```

你可以通过向机器人发送 `天气 北京` 格式的消息来获取天气信息，同时，也可以只发送 `天气`，这时机器人会向你询问城市，再次发送要查询的城市名称即可查询天气。

此外，这里的 `get_weather()` 方法并没有接入真正的天气数据，你可以使用任意的天气 API 代替，但请注意，在进行网络请求时需要使用基于协程异步的网络库，如 aiohttp 或 httpx，而不能使用如 requests 等同步的网络请求库，这会导致程序被阻塞。

相信阅读到这里，你应该已经可以写出一个 AliceBot 插件了。接下来建议你继续按顺序阅读下面的教程和你将要使用的适配器的教程。
