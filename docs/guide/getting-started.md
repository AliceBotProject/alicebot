# 快速上手

## 安装

::: warning 注意
AliceBot 仅支持 Python 3.7+ 版本。
:::

使用 Python 软件包安装程序（pip）进行安装：

```sh
pip install alicebot
```

从 GitHub 中安装最新的测试版：

```sh
git clone https://github.com/st1020/alicebot.git
cd alicebot
poetry install --no-dev  # 推荐
pip install .  # 不推荐
```

## 第一个项目

本文会帮助你从零开始搭建一个简单的 AliceBot 机器人项目。

::: tip 提示
下列命令默认适用于 *nix 系统，如 Linux、BSD、Mac OS 等，对于 Windows 系统，你可以以图形化或对应的 Windows 命令的方式完成下列操作。
:::

1. 创建并进入一个新目录

   ```sh
   mkdir alicebot-starter && cd alicebot-starter
   ```

2. 创建一个 `main.py` 文件

   ```sh
   touch main.py
   ```

   并写入以下内容

   ```python
   from alicebot import Bot
   
   bot = Bot()
   
   if __name__ == '__main__':
       bot.run()
   ```

3. 创建一个 `config.json` 文件

   ```sh
   touch config.json
   ```

   并写入以下内容

   ```json
   {
       "plugins": null,
       "plugin_dir": ["plugins"],
       "adapters": ["alicebot.adapter.cqhttp"]
   }
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

```
2021-07-24 00:00:00.000 | INFO     | alicebot:load_adapter:235 - Succeeded to load adapter "alicebot.adapter.cqhttp"
2021-07-24 00:00:00.000 | INFO     | alicebot:run:90 - Running AliceBot...
```

## 目录结构

AliceBot 推荐的目录结构如下：

::: vue
.
├── `plugins` _(**插件目录**)_
│   └── xxx.py
├── `config.json` _(**配置文件**)_
└── main.py
:::

其中 `main.py` 和 `config.json` 文件如上文所示。

## 配置协议端

上面的例子中使用了 `alicebot.adapter.cqhttp` 协议适配器，它是 OneBot 协议（原 CKYU 平台的 CQHTTP 协议）的适配器，需要一个兼容 OneBot 协议的协议端进行通讯，以下是一些常用的支持 OneBot 协议的 QQ 协议端：

- [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)
- [mirai](https://github.com/mamoe/mirai) + [onebot-kotlin](https://github.com/yyuueexxiinngg/onebot-kotlin)
- [node-onebot](https://github.com/takayama-lily/node-onebot) （基于 [oicq](https://github.com/takayama-lily/oicq)）

更多信息详见 [CQHTTP 协议使用指南](./cqhttp.md) 。
