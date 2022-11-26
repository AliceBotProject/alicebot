# 内置消息

AliceBot 内置了一个消息类，并且建议所有适配器开发者尽可能使用，它提供了许多实用的功能，可以方便地构造富文本消息。

AliceBot 内置了 `Message` 和 `MessageSegment` 类，即消息和消息字段。

大多数适配器的消息类均是内置消息类的子类，但又有一些特殊的用法，可以参考适配器的文档。

内置的消息类和消息字段类基本上是对 OneBot 协议消息类的一个实现。

## 消息类

消息类（`Message`）是 `list` 的子类，可以视作是消息字段的列表，但额外提供了以下功能：

重写了 `__init__()` 方法可以在初始化时传入 str， Mapping， Iterable[Mapping]， MessageSegment， Message 类型的对象，其中 str 原生并不支持，需要适配器开发者实现。当传入与自身类型相同的 `Message` 对象时，会产生一个新的内容相同的 `Message` 对象。当传入 `MessageSegment` 对象时，会将此消息字段添加到列表中。而 Mapping 和 Iterable[Mapping] 主要是为了在适配器产生事件时方便使用 pydantic 进行处理，普通用户无需关心。

```python
msg_seg = MessageSegment()
mas_seg.type = "text"
msg_seg["text"] = "Hello"
msg = Message(msg_seg)

msg = Message("Hello")  # 内置的 Message 原生并不支持这种用法

msg = Message(msg)
```

实现了 `+` 和 `+=` 运算符可以直接与 `Message`，`MessageSegment`， `str` 类型的对象相加。

```python
msg = Message()

msg_seg = MessageSegment()
mas_seg.type = "text"
msg_seg["text"] = "Hello"

msg += msg_seg
msg = msg + "Hello"  # 内置的 Message 原生并不支持这种用法
```

实现了 `startswith()` ， `endswith()` 和 `replace()` 方法，类似字符串的对应方法，但可以传入 `MessageSegment` 或 `str` 类型的对象，具体请参考 [API文档](/api/message.md) 。

```python
msg.startswith("a")
```

## 消息字段

消息字段类（`MessageSegment`）是一个数据类，同时继承自 `Mapping`，之所以没有使用 pydantic 的模型类是为了方便在适配器中转化为 json。

它拥有两个字段 `type` 和 `data` ，分别表示消息字段的类型和内容。`type` 类型是 str， `data` 是 dict，你可以直接对  `MessageSegment` 对象使用对字典的相关操作，这和对  `data` 字段进行操作是相同的。如：

```python
msg_seg = MessageSegment()
mas_seg.type = "text"

msg_seg["text"] = "Hello"  # 等同与 mag_seg.data['text'] = 'Hello'
print(msg_seg.get("text"))  # 等同与 print(msg_seg.data.get('text'))
```

消息字段对象也可以直接与其他对象相加，会返回一个消息类。

```python
msg_seg_1 = MessageSegment()
msg_seg_2 = MessageSegment()
msg = msg_seg_1 + msg_seg_2
type(msg)  # Message
```

## 示例

下面让我们来实践一下，尝试使用 CQHTTP 协议适配器的消息类构建一个富文本消息。

```python
from alicebot import Plugin
from alicebot.adapter.cqhttp.message import CQHTTPMessage, CQHTTPMessageSegment


class Hello(Plugin):
    async def handle(self) -> None:
        msg = CQHTTPMessage()
        msg += CQHTTPMessageSegment.text("Hello")
        msg += CQHTTPMessageSegment.image("file:///path/hello.png")
        await self.event.reply(msg)

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return str(self.event.message) == "hello"

```

