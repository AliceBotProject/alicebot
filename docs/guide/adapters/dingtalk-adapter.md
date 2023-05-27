# DingTalk 协议适配器

## 安装

```sh
pip install alicebot-adapter-dingtalk
```

## 配置协议端

DingTalk 协议适配器是钉钉企业机器人协议的适配器，钉钉的企业机器人使用 outgoing（回调）机制，在用户@机器人后，钉钉会将消息内容 POST 到开发者的消息接收地址。

具体配置参考钉钉开放平台的相关文档：

- [机器人概述](https://open.dingtalk.com/document/group/robot-overview)
- [企业内部开发机器人](https://open.dingtalk.com/document/group/enterprise-created-chatbot)

在测试时你可能没有自己的公网域名或 IP，钉钉官方提供了一个内网穿透工具：[内网穿透工具](https://open.dingtalk.com/document/resourcedownload/http-intranet-penetration)。

## 配置 AliceBot

你需要编辑 `config.toml` 来配置钉钉适配器，参考 [基本配置](./basic-config.md) 和 [DingTalk 配置](/api/adapter/dingtalk/config.md) 。

## 发送富文本消息

在编写插件时，除了发送普通的文本消息外，也可以轻松地构造并发送富文本消息，请确保查看本节时你已经阅读了 [内置消息](./builtin-message.md) 。

比较特殊的是，由于钉钉富文本消息的特殊性，钉钉适配器的消息类 `DingTalkMessage` 并非 `Message` 的子类，而是 `MessageSegment` 的子类。你无法通过常用的消息字段相加的方式构建消息。而需要手动写 Markdown 文本。

```python
from alicebot import Plugin
from alicebot.adapter.digntalk.message import DingTalkMessage


class HalloAlice(Plugin):
    async def handle(self) -> None:
        await self.event.reply(DingTalkMessage.markdown("# hello\n\nHello, Alice!"))

    async def rule(self) -> bool:
        if self.event.adapter.name != "dingtalk":
            return False
        return str(self.event.message).strip().lower() == "hello"

```

更多使用方法请参考 [消息类型和数据格式](https://open.dingtalk.com/document/group/message-types-and-data-format) 和 [CQHTTP 消息](/api/adapter/dingtalk/message.md) 。
