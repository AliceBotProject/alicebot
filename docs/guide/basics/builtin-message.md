# 内置消息

AliceBot 内置了一个消息类，并且建议所有适配器开发者尽可能使用，它提供了许多实用的功能，可以方便地构造富文本消息。

AliceBot 内置了 `Message` 和 `MessageSegment` 类，即消息和消息字段。

大多数适配器的消息类均是内置消息类的子类，但又有一些特殊的用法，可以参考适配器的文档。

内置的消息类和消息字段类基本上是对 OneBot 协议消息类的一个实现。

下面我们以一个 `FakeMessage` 为例：

```python
from typing import Type
from typing_extensions import Self

from alicebot.message import Message, MessageSegment


class FakeMessage(Message["FakeMessageSegment"]):
    """用于测试的消息。"""

    @classmethod
    def get_segment_class(cls) -> Type["FakeMessageSegment"]:
        """获取消息字段类。

        Returns:
            消息字段类。
        """
        return FakeMessageSegment


class FakeMessageSegment(MessageSegment["FakeMessage"]):
    """用于测试的消息字段。"""

    @classmethod
    def get_message_class(cls) -> Type["FakeMessage"]:
        """获取消息类。

        Returns:
            消息类。
        """
        return FakeMessage

    @classmethod
    def from_str(cls, msg: str) -> Self:
        """用于将 `str` 转换为消息字段。

        Args:
            msg: 要解析为消息字段的数据。

        Returns:
            由 `str` 转换的消息字段。
        """
        return cls.text(msg)

    def __str__(self) -> str:
        """返回消息的文本表示。

        Returns:
            消息的文本表示。
        """
        if self.type == "text":
            return self.data.get("text", "")
        return f"[{self.type}: {self.data!r}]"

    @classmethod
    def text(cls, text: str) -> Self:
        """纯文本"""
        return cls(type="text", data={"text": text})

```

实际使用时你应该使用对应适配器提供的消息类。

## 消息类

消息类 (`Message`) 是 `list` 的子类，可以视作是消息字段的列表，但额外提供了以下功能：

重写了 `__init__()` 方法，可以在初始化时传入 `str`、`Mapping`、`MessageSegment`、`List[MessageSegment]` 类型的对象。当传入与自身类型相同的 `Message` 对象时，会产生一个新的内容相同的 `Message` 对象。当传入 `MessageSegment` 对象时，会将此消息字段添加到列表中。而 `Mapping` 主要是为了在适配器产生事件时方便使用 Pydantic 进行处理，普通用户无需关心。

```python
msg_seg = FakeMessageSegment(type="text")
msg_seg["text"] = "Hello"

msg = FakeMessage(msg_seg)
msg = FakeMessage("Hello")
msg = FakeMessage(msg)
```

实现了 `+` 和 `+=` 运算符，可以直接与 `Message`，`MessageSegment`，`str` 类型的对象相加。

```python
msg = FakeMessage()

msg_seg = FakeMessageSegment(type="text")
msg_seg["text"] = "Hello"

msg += msg_seg
msg = msg + "Hello"
```

实现了 `startswith()`，`endswith()` 和 `replace()` 方法，类似字符串的对应方法，但可以传入 `MessageSegment` 或 `str` 类型的对象，具体请参考 [API 文档](/api/message.md)。

```python
msg = FakeMessage("abc")
msg.startswith("a")
```

## 消息字段

消息字段类 (`MessageSegment`) 是一个数据类，同时继承自 `Mapping`，之所以没有使用 pydantic 的模型类是为了方便在适配器中转化为 json。

它拥有两个字段 `type` 和 `data`，分别表示消息字段的类型和内容。`type` 类型是 `str`，`data` 是 `dict`，你可以直接对 `MessageSegment` 对象使用对字典的相关操作，这和对 `data` 字段进行操作是相同的。如：

```python
msg_seg = FakeMessageSegment(type="text")

msg_seg["text"] = "Hello"  # 等同与 mag_seg.data['text'] = 'Hello'
print(msg_seg.get("text"))  # 等同与 print(msg_seg.data.get('text'))
```

消息字段对象也可以直接与其他对象相加，会返回一个消息类。

```python
msg_seg = FakeMessageSegment(type="text")
msg_seg = FakeMessageSegment(type="text")
msg = msg_seg_1 + msg_seg_2
type(msg)  # Message
```

## 实践

上面介绍的都是 AliceBot 内置的消息类，大多数适配器都基于此实现了自己的消息类。

下面让我们来实践一下，尝试使用 CQHTTP 协议适配器的消息类构建一个富文本消息。

```python
from alicebot import Plugin
from alicebot.adapter.cqhttp.message import CQHTTPMessage, CQHTTPMessageSegment


class HalloAlice(Plugin):
    async def handle(self) -> None:
        msg = CQHTTPMessage()
        msg += CQHTTPMessageSegment.text("Hello, Alice!")
        msg += CQHTTPMessageSegment.image("file:///path/hello.png")
        await self.event.reply(msg)

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return str(self.event.message).lower() == "hello"

```
