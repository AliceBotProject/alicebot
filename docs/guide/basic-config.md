# 基本配置

## 配置文件

AliceBot 的所有配置均储存在配置文件 `config.toml` 文件中。

`config.toml` 文件为标准的 [TOML](https://toml.io/) v1.0.0 文件。TOML 是一种“语义明显且易于阅读的最小化配置文件格式”。建议在开始之前先简单了解一下 TOML 语言的基础格式。

AliceBot 的配置项将存储在不同的表（table）中，AliceBot 自身的配置位于 `bot` 表中，而所有适配器和插件的配置则分别位于 `adapter` 和 `plugin` 表中。

AliceBot 自身拥有如下配置项：

- **plugins**

  将被加载的插件列表，将被 `Bot` 类的 `load_plugins()` 方法加载。

- **plugin_dirs**

  将被加载的插件目录列表，将被 `Bot` 类的 `load_plugins_from_dirs()` 方法加载。

- **adapters**

  将被加载的适配器列表，将依次被 `Bot` 类的 `load_adapters()` 方法加载。

与日志记录相关的配置位于 `bot.log` 表中，如下：

- **level**

  日志级别。

- **verbose_exception**

  详细的异常记录，设置为 True 时会在日志中添加异常的 Traceback。

不同的适配器或插件的配置将位于 `adapter` 和 `plugin` 的子表中。

例如一个包含 `cqhttp` 适配器配置的配置文件如下：

```toml
[bot]
# 这里是 AliceBot 自身的配置
plugins = []
plugin_dirs = ["plugins"]
adapters = ["alicebot.adapter.cqhttp"]

[bot.log]
# 这里是 AliceBot 自身日志相关的配置
level = "INFO"
verbose_exception = true

[adapter.cqhttp]
# 这里是 CQHTTP 适配器的配置
adapter_type = "reverse-ws"
host = "127.0.0.1"
port = 8080
url = "/cqhttp/ws"

```

你可以写入任意未被定义的配置项，它们同样会被 AliceBot 加载，这些自定义配置可以用于插件中，如你可以通过定义 `superuser` 来表示控制当前当前机器的特殊用户，或者用 `nickname` 表示当前机器人的昵称。

```toml
# 这里是任意未被使用的键名
superuser = 10001
nickname = "小爱"

[bot]
# 这里是 AliceBot 自身的配置
plugins = []
plugin_dirs = ["plugins"]
adapters = ["alicebot.adapter.cqhttp"]

```

在插件中，整个配置可以通过 `self.bot.config` 来访问。例如：

```python
from alicebot import Plugin


class HalloAlice(Plugin):
    async def handle(self) -> None:
        await self.event.reply(f"Hello, I am {self.config.nickname}!")

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return (
            self.event.user_id == self.bot.config.superuser
            and str(self.event.message).lower() == "hello"
        )

```

## 自定义配置文件或不使用配置文件

你可以在实例化 `Bot` 对象时传入 `config_file` 或 `config_dict` 属性来实现自定义配置文件或者不使用配置文件或者直接在 Python 文件中配置。

AliceBot 会判断 `config_file` 的拓展名，允许 `.toml` 或 `.json` 文件。如果配置文件是 JSON 文件，则要求文件是使用 UTF-8 编码的标准 [JSON](https://www.json.org/) 文件，内容等同于上述 TOML 格式配置文件对应的 JSON 格式内容。

当指定 `config_dict` 属性时，AliceBot 将不再读取配置文件，并直接从给定的配置字典读取配置。

```python
# 自定义配置文件名
bot = Bot(config_file="my_config.json")

# 不使用配置文件
bot = Bot(
    config_dict={
        "bot": {
            "plugin_dirs": ["plugins"],
            "adapters": ["alicebot.adapter.cqhttp"],
        }
    }
)

```
