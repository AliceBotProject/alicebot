# 泛型和类型注解

如果你看到这里，相信你已经读完前面的指南了，如果还没有的话，希望你至少读完前面的[状态存储](/guide/advanced/state-storage.md)和[插件配置](/guide/advanced/plugin-config.md)，这会为你理解本章的内容提供帮助。

## 为什需要泛型插件？

如果你已经按照教程上手编写了几个自己的插件的话，你可能会发现，在编写插件时编辑器或 IDE 并没有给出正确的自动提示，也无法完成类型检查。这是因为我们还没有发挥出 AliceBot 的全部威力。记得[简介](/guide/index.md)中提到吗？AliceBot 是具有完整的类型注解的。而之前我们编写的插件中却完全没能利用这一特性，现在是时候开始让类型提示起作用了！

虽然 Python 是一门“动态强类型”语言，但是实践证明，有时候过于动态的类型不利于编程时的体验和提前发现错误。如果编辑器不知道你的变量是什么类型的，当然也就无法给出这个类型的相关自动提示了。所以 Python 在 3.5 版本之后引入了类型注解功能，使得 Python 可以像静态类型语言一样编写函数、变量和类的类型注解。

为了更好的利用 Python 的类型注解，AliceBot 的插件类是一个泛型类。

## 泛型插件

让我们想一下我们在编写插件时主要用到了什么需要让编辑器知道的类型呢？没错，事件的类型、状态的类型和配置的类型。因此插件类有三个泛型参数。

让我们扩展一下之前编写的计数插件并将它改造为一个泛型插件。

```python {10}
from alicebot import Plugin, ConfigModel
from alicebot.adapter.cqhttp.event import MessageEvent


class Config(ConfigModel):
    prefix: str = "count: "
    suffix: str = ""


class Count(Plugin[MessageEvent, int, Config], init_state=0, config=Config):
    async def handle(self) -> None:
        self.state += 1
        await self.event.reply(
            self.config.prefix + str(self.state) + self.config.suffix
        )

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return self.event.message.get_plain_text() == "count"

```

这里相当于指明了此插件所处理的事件的类型为 `MessageEvent`，储存的状态类型为 `int`，配置类为 `Config`。

当然，`rule()` 方法也可以简写成：

```python {17-21}
from alicebot import Plugin, ConfigModel
from alicebot.adapter.cqhttp.event import MessageEvent


class Config(ConfigModel):
    prefix: str = "count: "
    suffix: str = ""


class Count(Plugin[MessageEvent, int, Config], init_state=0, config=Config):
    async def handle(self) -> None:
        self.state += 1
        await self.event.reply(
            self.config.prefix + str(self.state) + self.config.suffix
        )

    async def rule(self) -> bool:
        return (
            isinstance(self.event, MessageEvent)
            and self.event.message.get_plain_text() == "count"
        )

```

强烈推荐在编写插件时使用泛型，这可以让你最大化地利用 AliceBot 的类型注解和编辑器的类型检查功能，将大多数的错误杜绝在开发阶段。

在 AliceBot 0.9 以上版本中，当你使用泛型类时，可以不必额外指定创建子类时的 `init_state` 和 `config` 参数，AliceBot 将自动从泛型参数中读取：

```python {12}
from typing_extensions import Annotated

from alicebot import ConfigModel, Plugin
from alicebot.adapter.cqhttp.event import MessageEvent


class Config(ConfigModel):
    prefix: str = "count: "
    suffix: str = ""


class Count(Plugin[MessageEvent, Annotated[int, 0], Config]):
    async def handle(self) -> None:
        self.state += 1
        await self.event.reply(
            self.config.prefix + str(self.state) + self.config.suffix
        )

    async def rule(self) -> bool:
        return (
            isinstance(self.event, MessageEvent)
            and self.event.message.get_plain_text() == "count"
        )

```

但是在运行时读取泛型参数中的事件类型并自动判断以省略 `rule()` 方法中的类型判断尚不支持。
