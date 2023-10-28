<div align="center">
  <a href="https://docs.alicebot.dev/"><img src="https://raw.githubusercontent.com/AliceBotProject/alicebot/master/docs/public/logo.png" width="200" height="200" alt="logo"></a>

# AliceBot

**简单的 Python 异步多后端机器人框架**

</div>

<div align="center">
  <a href="https://raw.githubusercontent.com/AliceBotProject/alicebot/master/LICENSE">
    <img src="https://img.shields.io/github/license/AliceBotProject/alicebot" alt="license">
  </a>
  <a href="https://pypi.python.org/pypi/alicebot">
    <img src="https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fgithub.com%2FAliceBotProject%2Falicebot%2Fraw%2Fmaster%2Fpyproject.toml" alt="pypi">
  </a>
  <a href="https://pypi.python.org/pypi/alicebot">
    <img src="https://img.shields.io/pypi/v/alicebot" alt="pypi">
  </a>
  <a href="https://github.com/AliceBotProject/alicebot/">
    <img src="https://img.shields.io/github/stars/AliceBotProject/alicebot?style=social" alt="github">
  </a>
  <br />
  <a href="https://github.com/psf/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="black">
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="ruff">
  </a>
  <a href="https://github.com/pylint-dev/pylint">
    <img src="https://img.shields.io/badge/linting-pylint-blue" alt="pylint">
  </a>
  <a href="https://github.com/Microsoft/pyright">
    <img src="https://img.shields.io/badge/type%20checker-pyright-yellowgreen" alt="pyright">
  </a>
  <a href="https://github.com/python/mypy">
    <img src="https://img.shields.io/badge/type%20checker-mypy-blue" alt="mypy">
  </a>
  <br />
  <a href="https://codecov.io/gh/AliceBotProject/alicebot">
    <img src="https://codecov.io/gh/AliceBotProject/alicebot/graph/badge.svg?token=3H6ZU6NN0J" alt="codecov">
  </a>
  <a href="https://github.com/AliceBotProject/alicebot/actions/workflows/test.yml">
    <img src="https://github.com/AliceBotProject/alicebot/actions/workflows/test.yml/badge.svg?branch=master&event=push" alt="github">
  </a>
  <a href="https://github.com/AliceBotProject/alicebot/actions/workflows/lint.yml">
    <img src="https://github.com/AliceBotProject/alicebot/actions/workflows/lint.yml/badge.svg?branch=master&event=push" alt="github">
  </a>
  <a href="https://github.com/AliceBotProject/alicebot/actions/workflows/docs.yml">
    <img src="https://github.com/AliceBotProject/alicebot/actions/workflows/docs.yml/badge.svg?branch=master&event=push" alt="github">
  </a>
  <br />
  <a href="https://jq.qq.com/?_wv=1027&k=ZbE3p6tq">
    <img src="https://img.shields.io/badge/QQ%E7%BE%A4-674802046-orange" alt="qq-group">
  </a>
</div>

<p align="center">
  <a href="https://docs.alicebot.dev/">文档</a>
  ·
  <a href="https://docs.alicebot.dev/guide/">指南</a>
  ·
  <a href="https://docs.alicebot.dev/guide/">API 参考</a>
  ·
  <a href="https://github.com/AliceBotProject/alicebot-example">示例</a>
</p>

## 简介

AliceBot 是一个简单的 Python 异步多后端机器人框架，支持多种协议适配，可以轻松地编写易于学习和使用的插件来拓展其功能。

本项目受到了 [NoneBot](https://github.com/nonebot/nonebot2/) 项目的启发，您可以在[对比](#对比)小节中查看这两个项目的异同，以便您选择更适合自己的机器人框架。

## 特点

- **简单**：AliceBot 使用了非常灵活且易于使用的插件编写方式，您只需要编写两个方法即可实现一个功能强大的插件。
- **灵活**：AliceBot 的适配协议并不与任何一种库或网络协议绑定，您可以自由选择或编写适合您的适配器。
- **高效**：AliceBot 基于 Python 的异步 I/O，轻松处理大量请求。较少的封装，在保持易用的同时追求最好的性能。

目前 AliceBot 官方维护了以下协议适配：

- [OneBot (CQHTTP) 协议](https://github.com/botuniverse/onebot-11) (支持 QQ 等) [ws](https://github.com/botuniverse/onebot-11/blob/master/communication/ws.md) 和 [ws-reverse](https://github.com/botuniverse/onebot-11/blob/master/communication/ws-reverse.md) 连接方式
- [OneBot v12 协议](https://12.onebot.dev/) 的 [ws](https://12.onebot.dev/connect/communication/websocket/) 和 [ws-reverse](https://12.onebot.dev/connect/communication/websocket-reverse/) 连接方式
- [mirai-api-http 协议](https://github.com/project-mirai/mirai-api-http) 2.0+ [ws](https://github.com/project-mirai/mirai-api-http/blob/master/docs/adapter/WebsocketAdapter.md) 和 [reverse-ws](https://github.com/project-mirai/mirai-api-http/blob/master/docs/adapter/ReverseWebsocketAdapter.md) 连接方式
- [钉钉](https://developers.dingtalk.com/document/robots/robot-overview)企业机器人的 outgoing (回调) 连接方式

更多协议正在适配中 ...

更多信息：[简介 - AliceBot 文档](https://docs.alicebot.dev/guide/)

## 即刻开始

1. 安装：

   ```bash
   pip install alicebot[all]
   ```

2. 第一个 AliceBot 项目：

   ```python
   from alicebot import Bot

   bot = Bot()
   bot.load_adapters("alicebot.adapter.cqhttp")

   bot.run()
   ```

3. 第一个 AliceBot 插件：

   ```python
   from alicebot import Plugin


   class Echo(Plugin):
       async def handle(self) -> None:
           await self.event.reply(self.event.message.replace("echo ", ""))

       async def rule(self) -> bool:
           if self.event.adapter.name != "cqhttp":
               return False
           if self.event.type != "message":
               return False
           return self.event.message.startswith("echo ")
   ```

更多信息请参阅 AliceBot [文档](https://docs.alicebot.dev/)。

## 对比

本项目受到了 [NoneBot](https://github.com/nonebot/nonebot2) 项目的启发，以下简单介绍两者的异同。

相同点：

- 两者都是使用 Python 编写的，使用了协程异步的高性能机器人框架。
- 两者都支持多种协议。
- 两者都会对机器人收到的事件进行解析和处理，并按优先级分发给插件 (事件响应器) 来完成具体的功能。
- 两者都基于 MIT 协议开源，这意味着您可以在遵循协议的前提下任意使用本项目。

不同点：

- 总的来说，NoneBot 是一个较为全面的机器人框架，而 AliceBot 是一个小巧简洁的机器人框架，它不包含一些复杂的高级特性，但更加灵活且易于学习。
- AliceBot 的插件编写风格和 NoneBot 不同，相对而言，AliceBot 更加注重于易于入门和“渐进式框架”，这意味着 AliceBot 大部分的功能都是可选的，您只需要了解很少的知识即可开始使用，随着项目规模的扩大和复杂性的增加，您可以继续深入需要的特性，而不需要一开始就掌握全部的特性。“它是一个可以与你共同成长、适应你不同需求的框架。”
- NoneBot 在实现上与 HTTP / WebSocket 通讯协议深度绑定，它需要一个支持 ASGI 服务器协议的“驱动器”，而 AliceBot 并不与任何协议绑定，它甚至可以用来驱动您的树莓派智能音箱。当然，如果您只需要一个支持常见网络聊天工具的机器人框架的话，它们并没有什么区别。
- NoneBot 拥有相对庞大的用户基数和社区规模，也拥有数量众多的插件，而 AliceBot 则是一个新生项目，这意味着如果您使用 NoneBot 您可能会更加容易找到已经编写完毕的您感兴趣的插件，并且您当您遇到问题时也能够更快地查找到相关资料或者获得解答。

总而言之，两者有着各自的特点，您可以根据需要选用。

## 许可证

AliceBot 采用 MIT 许可证开放源代码。

本项目的图标由**迷糊小梦神**绘制，作为本项目的一部分，使用与本项目相同的许可证开放使用。
