<div align="center">
  <a href="https://docs.alicebot.dev/"><img src="https://raw.githubusercontent.com/st1020/alicebot/master/docs/public/logo.png" width="200" height="200" alt="logo"></a>

# AliceBot

**简单的 Python 异步多后端机器人框架**

</div>

<div align="center">
  <a href="https://raw.githubusercontent.com/st1020/alicebot/master/LICENSE">
    <img src="https://img.shields.io/github/license/st1020/alicebot" alt="license">
  </a>
  <a href="https://pypi.python.org/pypi/alicebot">
    <img src="https://img.shields.io/pypi/v/alicebot" alt="pypi">
  </a>
  <a href="https://pypi.python.org/pypi/alicebot">
    <img src="https://img.shields.io/pypi/pyversions/alicebot" alt="pypi">
  </a>
  <a href="https://github.com/st1020/alicebot/">
    <img src="https://img.shields.io/github/stars/st1020/alicebot?style=social" alt="github">
  </a>
</div>

<p align="center">
  <a href="https://docs.alicebot.dev/">文档</a>
  ·
  <a href="https://docs.alicebot.dev/guide/">指南</a>
  ·
  <a href="https://docs.alicebot.dev/guide/">API 参考</a>
  ·
  <a href="https://github.com/st1020/alicebot-example">示例</a>
</p>

## 简介

AliceBot 是一个简单的 Python 异步多后端机器人框架，支持多种协议适配，可以轻松地编写易于学习和使用的插件来拓展其功能。

本项目受到了 [NoneBot](https://github.com/nonebot/nonebot2/) 项目的启发，您可以在 [对比](#对比) 小节中查看这两个项目的异同，以便您选择更适合自己的机器人框架。

## 特点

AliceBot 使用了非常灵活且易于使用的插件编写方式，您只需要编写两个方法即可实现一个功能强大的插件。

AliceBot 的适配协议并不与任何一种库或网络协议绑定，您可以自由选择或编写适合您的适配器。

目前 AliceBot 官方维护了以下协议适配：

- [OneBot (CQHTTP) 协议](https://github.com/botuniverse/onebot) （支持QQ等）[ws](https://github.com/botuniverse/onebot-11/blob/master/communication/ws.md) 和 [ws-reverse](https://github.com/botuniverse/onebot-11/blob/master/communication/ws-reverse.md) 连接方式
- [mirai-api-http 协议](https://github.com/project-mirai/mirai-api-http) 2.0+ [ws](https://github.com/project-mirai/mirai-api-http/blob/master/docs/adapter/WebsocketAdapter.md) 和 [reverse-ws](https://github.com/project-mirai/mirai-api-http/blob/master/docs/adapter/ReverseWebsocketAdapter.md) 连接方式
- [钉钉](https://developers.dingtalk.com/document/robots/robot-overview) 企业机器人的 outgoing （回调）连接方式

更多协议正在适配中 ...

## 即刻开始

1. 安装：

   ```bash
   pip install alicebot[all]
   ```

2. 第一个 AliceBot 项目：

   ```python
   from alicebot import Bot
   
   bot = Bot()
   bot.load_adapter("alicebot.adapter.cqhttp")
   
   bot.run()
   ```

3. 第一个 AliceBot 插件：

   ```python
   from alicebot.plugin import Plugin
   
   
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

本项目受到了 [NoneBot](https://github.com/nonebot/nonebot2/) 项目的启发，以下简单介绍两者的异同。

相同点：

- 两者都是使用 Python 编写的，使用了协程异步的高性能机器人框架。
- 两者都支持多种协议。
- 两者都会对机器人收到的事件进行解析和处理，并按优先级分发给插件（事件响应器）来完成具体的功能。
- 两者都基于 MIT 协议开源，这意味着您可以在遵循协议的前提下任意使用本项目。

不同点：

- 总的来说，NoneBot 是一个较为全面的机器人框架，而 AliceBot 是一个小巧简洁的机器人框架，它不包含一些复杂的高级特性，但更加灵活且易于学习。
- NoneBot 在实现上与 WebSocket 通讯协议深度绑定，它需要一个支持 ASGI 服务器协议的驱动框架，而 AliceBot 并不与任何协议绑定，它甚至可以用来驱动您的树莓派智能音箱。当然，如果您只需要一个支持常见网络聊天工具的机器人框架的话，它们并没有什么区别。
- NoneBot 提供了很多预设规则和权限控制机制，而 AliceBot 则没有提供，由于插件编写方式的不同，AliceBot 选择给您最大的自由，您需要自行编写插件在何时运行的方法（`rule()` 方法），这在绝大部份情况下并不会造成您编写更多的代码或是影响插件的可读性，自行实现也不会非常困难，但如果您真的需要这些高级功能又不想自己实现的话，NoneBot 提供了更好的选择。
- NoneBot 拥有相对庞大的用户基数和社区规模，也拥有数量众多的插件，而 AliceBot 则是一个新生项目，这意味着如果您使用 NoneBot 您可能会更加容易找到已经编写完毕的您感兴趣的插件，并且您当您遇到问题时也能够更快地查找到相关资料或者获得解答。
- NoneBot 相对较为庞大，封装相对较多，完全学习理解需要一定时间，而 AliceBot 小巧简洁，封装较少，很容易掌握。

总而言之，两者有着各自的特点，您可以根据需要选用。

作者就是在使用 NoneBot 时觉得插件编写不是很易用，于是萌发了编写一个新的机器人框架的想法，AliceBot 就这样诞生了。

## 许可证

AliceBot 采用 MIT 许可证开放源代码。

本项目的图标由 迷糊小梦神 绘制，作为本项目的一部分，使用与本项目相同的许可证开放使用。
