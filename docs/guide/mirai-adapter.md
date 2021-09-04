# Mirai 协议适配器

Mirai 协议适配器是 [mirai-api-http](https://github.com/project-mirai/mirai-api-http) 协议的适配器，你需要先按照 mirai-api-http 文档的说明安装 mirai-api-http 。

值得注意的是，本适配器仅支持 mirai-api-http 2.0 以上版本。

本适配器支持 mirai-api-http 的 Websocket Adapter 模式和 Reverse Websocket Adapter 模式。

目前更加推荐使用 Websocket Adapter 模式。

## 安装

```sh
pip install alicebot-adapter-mirai
```

## 配置协议端

编辑 mirai-api-http 的配置文件 `setting.yml` 。

### Websocket Adapter 模式

```yaml
adapters:
  - ws
enableVerify: true
verifyKey: 1234567890
adapterSettings:
  ws:
    host: localhost
    port: 8080
    reservedSyncId: -1
```

### Reverse Websocket Adapter 模式

```yaml
adapters:
  - reverse-ws
enableVerify: true
verifyKey: 1234567890
singleMode: true
adapterSettings:
  reverse-ws:
    destinations:
    - host: localhost
      port: 8080
      path: /mirai/ws
      protocol: ws
      method: GET
    reservedSyncId: -1
```

## 配置 AliceBot

编辑 AliceBot 的配置文件 `config.json` 。

更多项目请参考 [Mirai 配置](/api/adapter/mirai/config.md) 。

### Websocket Adapter 模式

```json
{
    "adapters": ["alicebot.adapter.mirai"],
    "mirai": {
        "adapter_type": "ws",
        "verify_key": "1234567890",
        "qq": 机器人QQ号
    }
}
```

### Reverse Websocket Adapter 模式

```json
{
    "adapters": ["alicebot.adapter.mirai"],
    "mirai": {
        "adapter_type": "reverse-ws",
        "verify_key": "1234567890",
        "qq": 机器人QQ号
    }
}
```

## 发送富文本消息

与 CQHTTP 协议适配器类似，Mirai 适配器也可以轻松地构建富文本消息。

```python
from alicebot.plugin import Plugin
from alicebot.adapter.mirai.message import CQHTTPMessageSegment


class HalloAlice(Plugin):
    async def handle(self) -> None:
        msg = CQHTTPMessageSegment.plain('Hello, Alice!') + CQHTTPMessageSegment.image(url='https://www.example.org/1.jpg')
        await self.event.replay(msg)

    async def rule(self) -> bool:
        if self.adapter.name != 'mirai':
            return False
        if self.event.type != 'FriendMessage':
            return False
        return self.event.message.get_plain_text().lower() == 'hello'

```

更多使用方法请参考 [mirai-api-http 消息段类型](https://docs.mirai.mamoe.net/mirai-api-http/api/MessageType.html) 和 [Mirai 消息](/api/adapter/mirai/message.md) 。

## 调用 mirai-api-http API

你可以使用下面的方法调用 mirai-api-http API：

```python
from alicebot.plugin import Plugin


class TestPlugin(Plugin):
    async def handle(self) -> None:
        resp = await self.adapter.call_api('friendProfile', target=10001)
        # 等效于 resp = await self.adapter.friendProfile(target=10001)

    async def rule(self) -> bool:
        return self.adapter.name == 'mirai'

```

更多使用方法请参考 [mirai-api-http 文档](https://docs.mirai.mamoe.net/mirai-api-http/adapter/WebsocketAdapter.html)。