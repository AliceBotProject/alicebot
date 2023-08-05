# 快速上手

## 安装

::: warning 注意
AliceBot 仅支持 Python 3.8+ 版本。
:::

使用 Python 软件包安装程序 (pip) 进行安装：

```sh
pip install alicebot
```

从 GitHub 中安装最新的开发版：

```sh
git clone https://github.com/AliceBotProject/alicebot.git
cd alicebot
pdm install
```

## 安装适配器

AliceBot 本身只是一个聊天机器人框架，需要额外安装对应协议的适配器来支持特定的协议，你可以使用 pip 安装协议适配器：

```sh
pip install alicebot-adapter-cqhttp
pip install alicebot-adapter-onebot
pip install alicebot-adapter-mirai
pip install alicebot-adapter-dingtalk
```

或者你也可以在安装 AliceBot 的同时搭配对应的适配器，如：

```sh
pip install alicebot[all]
pip install alicebot[cqhttp]
pip install alicebot[onebot]
pip install alicebot[mirai]
pip install alicebot[dingtalk]
```

## 第一个项目

本文会帮助你从零开始搭建一个简单的 AliceBot 机器人项目。

1. 创建并进入一个新目录

   ```sh
   mkdir alicebot-starter && cd alicebot-starter
   ```

2. 创建一个 `main.py` 文件并写入以下内容

   ```python
   from alicebot import Bot

   bot = Bot()

   if __name__ == "__main__":
       bot.run()
   ```

3. 创建一个 `config.toml` 文件并写入以下内容

   ```toml
   [bot]
   plugin_dirs = ["plugins"]
   adapters = ["alicebot.adapter.cqhttp"]
   ```

4. 创建一个 `plugins` 目录

   ```sh
   mkdir plugins
   ```

5. 试试运行 `main.py` 吧！

   ```sh
   python main.py
   ```

你应该会看到以下输出的日志

```txt
2021-07-24 00:00:00.000 | INFO     | alicebot.bot:_load_plugins_from_dirs:689 - Loading plugins from dirs "/xxx/plugins"
2021-07-24 00:00:00.000 | INFO     | alicebot.bot:_load_adapters:746 - Succeeded to load adapter "CQHTTPAdapter" from "alicebot.adapter.cqhttp"
2021-07-24 00:00:00.000 | INFO     | alicebot:run:90 - Running AliceBot...
```

## 目录结构

AliceBot 推荐的目录结构如下：

```txt
.
├── plugins (插件目录)
│   └── xxx.py
├── config.toml (配置文件)
└── main.py
```

其中 `main.py` 和 `config.toml` 文件如上文所示。

## 配置协议端

上面的例子中使用了 `alicebot.adapter.cqhttp` 协议适配器，它是 OneBot v11 协议 (原 CKYU 平台的 CQHTTP 协议) 的适配器，需要一个兼容 OneBot 协议的协议端进行通讯，以下是一些常用的支持 OneBot 协议的 QQ 协议端：

- [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)
- [mirai](https://github.com/mamoe/mirai) + [onebot-kotlin](https://github.com/yyuueexxiinngg/onebot-kotlin)
- [oicq](https://github.com/takayama-lily/oicq)

更多信息详见 [CQHTTP 协议使用指南](/guide/adapters/cqhttp-adapter.md)。

你也可以安装其他协议适配器或者尝试自己写一个协议适配器。

## 开发建议

在使用 AliceBot 进行开发时，建议使用具有类型检查的 IDE，如 PyCharm、VSCode 等，这可以帮助你充分利用 AliceBot 的类型提示。
