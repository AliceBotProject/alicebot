# 通用插件

之前我们编写的插件都是针对于某一个协议的，而 AliceBot 提供了一种方法用于编写简单的通用插件。

AliceBot 提供了一个通用的 `MessageEvent` ，所有适配器的消息事件都是它的子类，并尽可能实现了它的特性，你可以编写一个适用于通用的 `MessageEvent` 的插件用于处理所有适配器的消息事件。

```python
from alicebot import Plugin
from alicebot.event import MessageEvent
from alicebot.exceptions import GetEventTimeout


class HalloAlice(Plugin[MessageEvent, None, None]):
    async def handle(self) -> None:
        try:
            name_event = await self.event.ask("What is you name?", timeout=10)

            # await self.event.reply("What is you name?")
            # name_event = await self.event.get(timeout=10)
        except GetEventTimeout:
            return
        else:
            await self.event.reply(f"Hello, {name_event.get_plain_text()}!")

    async def rule(self) -> bool:
        return (
            isinstance(self.event, MessageEvent)
            and self.event.get_plain_text() == "hello"
        )

```

通用的 `MessageEvent` 提供了 `get_plain_text()`、`reply()`、`get()` 和 `ask()` 方法，对于简单的消息处理插件，这些已经足够了。
