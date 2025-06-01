# Telegram 协议适配器

## 安装

```sh
pip install alicebot-adapter-telegram
```

## 配置协议端

Telegram 协议适配器是 Telegram Bot 协议的适配器，你需要根据 [Telegram Bots 文档](https://core.telegram.org/bots)创建机器人并且获得一个类似 `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11` 这样的的 token。

## 配置 AliceBot

你需要编辑 `config.toml` 来配置 Telegram 适配器：

```toml
[adapter.telegram]
bot_token = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
```

如果你在访问 Telegram API 时需要通过代理，可以像这样配置代理：

```toml
[adapter.telegram]
bot_token = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
proxy = "http://127.0.0.1:1234"
```

如果你部署 AliceBot 的服务器具有公网 IP 或者域名，则可以使用 Webhook 获取事件 (不推荐)。

```toml
[adapter.telegram]
adapter_type = "webhook"
bot_token = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
webhook_host = "example.com" # 你部署 AliceBot 的服务器具有公网 IP 或者域名
webhook_port = 443
webhook_url = "/telegram"
```

其他配置可以参考[基本配置](/guide/basic-config.md)和 [Telegram 配置](/api/adapter/telegram/config.md)。

## 插件示例

```python
from typing_extensions import override

from alicebot import Plugin
from alicebot.adapter.telegram.event import MessageEvent


class HelloWorld(Plugin[MessageEvent, None, None]):
    @override
    async def handle(self) -> None:
        await self.event.reply("Hello, I am Alice.")

    @override
    async def rule(self) -> bool:
        return (
            isinstance(self.event, MessageEvent)
            and self.event.get_plain_text() == "/hello"
        )
```

向机器人发送 `/hello`，你将收到 `Hello, I am Alice.` 的回复。

更多示例可以参考 <https://github.com/AliceBotProject/alicebot/tree/main/packages/alicebot-adapter-telegram/examples>。

## 调用 Telegram API

你可以使用下面的方法调用 Telegram API：

```python
from typing_extensions import override

from alicebot import Plugin
from alicebot.adapter.telegram.event import MessageEvent

class DownloadFile(Plugin[MessageEvent, None, None]):
    @override
    async def handle(self) -> None:
        if self.event.message.document is None:
            await self.event.reply("Please send me a file.")
            return

        file = await self.event.adapter.get_file(
            file_id=self.event.message.document.file_id
        )

        ...

    @override
    async def rule(self) -> bool:
        return isinstance(self.event, MessageEvent) and (
            self.event.get_plain_text() == "/download"
            or self.event.message.caption == "/download"
        )

```

全部 Telegram API 请参考 [Telegram Bot API](https://core.telegram.org/bots/api)。
