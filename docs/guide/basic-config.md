# 基本配置

## 配置文件

AliceBot 的所有配置均储存在 `config.json` 文件中。

`config.json` 文件的内容要求是使用 UTF-8 编码的标准 [JSON](https://www.json.org/) 文件。

如果你不打算写入任何配置，请勿留空此文件，因为空文件并不符合 JSON 语法（虽然这实际上也起到了不进行任何配置的功能，但程序会报错，尽管这并不会有什么影响，但你应该不会希望每次启动机器人都会出现一个红色的 ERROR 的），你可以写入一个 `{}` 表示留空。

AliceBot 有如下配置项：

- **plugins**

  将被加载的插件列表，将依次被 `Bot` 类的 `load_plugin()` 方法加载。

- **plugin_dir**

  将被加载的插件目录列表，将被 `Bot` 类的 `load_plugins_from_dir()` 方法加载。

- **adapters**

  将被加载的适配器列表，将依次被 `Bot` 类的 `load_adapter()` 方法加载。

适配器的配置会被放置于独立的键中，如一个包含 `cqhttp` 适配器配置的配置文件如下：

```json
{
    "plugins": null,
    "plugin_dir": ["plugins"],
    "adapters": ["alicebot.adapter.cqhttp"],
    "cqhttp": {
        "host": "127.0.0.1",
        "port": 8080,
        "url": "/cqhttp/ws",
        "api_timeout": 1000
    }
}
```

你可以写入任意未被定义的配置项，这些自定义配置可以用于插件中，如你可以通过定义 `superuser` 来表示控制当前当前机器的特殊用户，或者用 `nickname` 表示当前机器人的昵称。

```json
{
    "superuser": 10001,
    "nickname": "小爱"
}
```

在插件中，配置可以通过 `self.config` 来访问。例如：

```python
from alicebot.plugin import Plugin


class HalloAlice(Plugin):
    async def handle(self) -> None:
        await self.event.reply(f'Hello, I am {self.config.nickname}!')

    async def rule(self) -> bool:
        if self.event.adapter.name != 'cqhttp':
            return False
        if self.event.type != 'message':
            return False
        return self.event.user_id == self.config.superuser and str(self.event.message).lower() == 'hello'
```

## 自定义配置文件或不使用配置文件

你可以在实例化 `Bot` 对象时传入 `config_file` 或 `config_dict` 属性来实现自定义配置文件或者不使用配置文件或者直接在 Python 文件中配置。

当指定 `config_dict` 属性时，AliceBot 将不再读取配置文件。

```python
# 自定义配置文件名
bot = Bot(config_file='my_config.json')

# 不使用配置文件
bot = Bot(config_dict={
    'plugin_dir': ['plugins'],
    'adapters': ['alicebot.adapter.cqhttp'],
})
```

