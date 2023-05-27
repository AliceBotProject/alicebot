# 加载插件

在 [快速上手](/guide/quick-start.md) 一章中我们创建了一个 `plugins` 目录，并在配置文件中设置其为插件目录。所以，放入 `plugins` 目录的任何不以 `_` 开头的 Python 模块都会被自动加载并测试是否是插件。

不过你也可以不配置 `plugin_dirs` 并通过以下方式“程序式”地加载插件。

**但通常情况下，不需要使用下面的方法，推荐通过配置文件中的 `plugin_dirs` 或 `plugins` 配置项来加载插件。**

如果你只是想要编写一个插件，你可以跳过本节直接进入下一节。

## 加载插件目录

在 `main.py` 文件中添加以下行：

```python {4}
from alicebot import Bot

bot = Bot()
bot.load_plugins_from_dirs("plugins", "/home/xxx/alicebot/plugins")

if __name__ == "__main__":
    bot.run()

```

这实际上和配置 `plugin_dirs` 为 `["plugins", "/home/xxx/alicebot/plugins"]` 是相同的，目录可以是相对路径或者绝对路径。以 `_` 开头的插件不会被加载。

## 加载单个插件

在 `main.py` 文件中添加以下行：

```python {7}
from alicebot import Bot

class TestPlugin(Plugin):
    pass

bot = Bot()
bot.load_plugins("plugins.hello", TestPlugin)

if __name__ == "__main__":
    bot.run()

```

`load_plugins` 方法可以传入插件类、字符串或者 `pathlib.Path` 对象，如果为后两者会分别视为插件模块的名称（格式和 Python `import` 语句相同）和插件模块文件的路径进行加载。
