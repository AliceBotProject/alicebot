# 插件配置

在 [基础配置](../basic-config.md) 一节中提到，可以直接通过 `self.bot.config` 访问当前机器人的配置。但有时我们可能会希望插件配置像适配器配置一样放在一个独立的键中，以提高这个插件的可移植性，那么我们可以这样处理：

```python
from alicebot import Plugin, ConfigModel


class TestPlugin(Plugin):
    class Config(ConfigModel):
        __config_name__ = "test_plugin"
        a: str = "test"
        b: int = 1

    async def handle(self) -> None:
        print(self.config.a)
        print(self.config.b)

    async def rule(self) -> bool:
        return True

```

`config.toml` 文件对应如下：

```toml
[plugin.test_plugin]
a = "abc"
b = 123
```

需要在插件类内编写一个名称为 `Config` 的继承于 `alicebot.ConfigModel` 的类，这是一个 `pydantic` 的模型类，具体可以参考 [pydantic 的文档](https://docs.pydantic.dev/) ，简而言之，格式为：

`变量名称: 类型[ = 默认值]`

如果不指定默认值，且类型不是 `Optional[...]`， `Union[None, ...]` 或 `Any`，则这个字段是必填的，在非必需的情况下，建议不要在插件中使用必填字段，这会导致不指定这个字段时，不只是这个插件，整个 AliceBot 都不能运行。

特别的是，`Config` 类中**必须**要有一个 `__config_name__` 属性，表示这个插件在配置文件中对应的键名。

如果你将插件类放在 Python 包中的话，建议把 `Config` 类放在单独的 `config.py` 文件中。

```txt
.
├── plugins
│   └── test_plugin
│      ├── config.py
│      └── __init__.py
├── config.toml
└── main.py
```

然后在 `__init__.py` 中导入：

```python {7}
from alicebot import Plugin

from .config import Config


class TestPlugin(Plugin):
    Config = Config

    async def handle(self) -> None:
        print(self.config.a)
        print(self.config.b)

    async def rule(self) -> bool:
        return True

```

除此之外，也可以使用另一种写法：

```python {6}
from alicebot import Plugin

from .config import Config


class TestPlugin(Plugin, config=Config):
    async def handle(self) -> None:
        print(self.config.a)
        print(self.config.b)

    async def rule(self) -> bool:
        return True

```

::: tip 注意
配置类的类名必须为 `Config` 且必须包含 `__config_name__` 属性。
:::
