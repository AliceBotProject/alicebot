# CQHTTP 协议适配器

## 安装

```sh
pip install alicebot-adapter-cqhttp
```

## 配置协议端

CQHTTP 协议适配器是 OneBot 协议（原 CKYU 平台的 CQHTTP 协议）的适配器，需要一个兼容 OneBot 协议的协议端进行通讯，以下是一些常用的支持 OneBot 协议的 QQ 协议端：

- [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)
- [mirai](https://github.com/mamoe/mirai) + [onebot-kotlin](https://github.com/yyuueexxiinngg/onebot-kotlin)
- [node-onebot](https://github.com/takayama-lily/node-onebot) （基于 [oicq](https://github.com/takayama-lily/oicq)）

以下以 go-cqhttp 为例：

1. 下载 go-cqhttp 对应平台的发行版：[Github Releases](https://github.com/Mrs4s/go-cqhttp/releases)
2. 运行 `go-cqhttp` 或 `go-cqhttp.exe` 生成默认配置文件
3. 编辑配置文件 `config.hjson` 并重启程序

目前 CQHTTP 适配器仅支持反向 WebSocket 连接，go-cqhttp 配置文件应该像下面所示：

```json
{
    // QQ号
    uin: 机器人QQ号
    // QQ密码
    password: "机器人密码"
    // 反向WS设置
    ws_reverse_servers: [
        // 可以添加多个反向WS推送
        {
            // 是否启用该推送
            enabled: true
            // 反向WS Universal 地址
            reverse_url: ws://127.0.0.1:8080/cqhttp/ws
        }
    ]
    // 上报数据类型
    // 可选: string array
    post_message_format: array
}
```

其他条目保持默认即可。

## 配置 AliceBot

如果你安装上面配置 go-cqhttp 的话，将不需要对 AliceBot 进行配置。

如果你有其他特别的需求的话可以编辑 `config.json` 来配置，参考 [基本配置](./basic-config.md) 和 [CQHTTP 配置](/api/adapter/cqhttp/config.md) 。

## 运行测试

如果你正确配置了协议端和 AliceBot ，运行 AliceBot 后控制台将出现以下日志内容：

```
2021-09-01 18:05:29.740 | INFO     | alicebot.adapter.cqhttp:handle_cqhttp_event:138 - WebSocket connection from CQHTTP Bot 2835383466 accepted!
```

## 发送富文本消息

在编写插件时，除了发送普通的文本消息外，也可以轻松地构造并发送富文本消息，请确保查看本节时你已经阅读了 [内置消息](./builtin-message.md) 。

```python
from alicebot.plugin import Plugin
from alicebot.adapter.cqhttp.message import CQHTTPMessageSegment


class HalloAlice(Plugin):
    async def handle(self) -> None:
        msg = CQHTTPMessageSegment.text('Hello, Alice!') + CQHTTPMessageSegment.image('https://www.example.org/1.jpg')
        await self.event.replay(msg)

    async def rule(self) -> bool:
        if self.adapter.name != 'cqhttp':
            return False
        if self.event.type != 'message':
            return False
        return str(self.event.message).lower() == 'hello'

```

更多使用方法请参考 [OneBot 消息段类型](https://github.com/botuniverse/onebot/blob/master/v11/specs/message/segment.md) 和 [CQHTTP 消息](/api/adapter/cqhttp/message.md) 。

## 调用 OneBot API

你可以使用下面的方法调用 OneBot API：

```python
from alicebot.plugin import Plugin


class TestPlugin(Plugin):
    async def handle(self) -> None:
        resp = await self.adapter.call_api('send_like', user_id=10001)
        # 等效于 resp = await self.adapter.send_like(user_id=10001)

    async def rule(self) -> bool:
        return self.adapter.name == 'cqhttp'

```

更多使用方法请参考 [OneBot 公开 API](https://github.com/botuniverse/onebot/blob/master/v11/specs/api/public.md) 。