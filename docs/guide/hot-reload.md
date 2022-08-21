# 热重载

## 手动冷重载

AliceBot 提供了一个 `restart()` 方法用于退出并重新启动 AliceBot，你可以编写这样一个插件用于重新启动 AliceBot：

```python
from alicebot.plugin import Plugin


class Restart(Plugin):
    async def handle(self) -> None:
        self.bot.restart()

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return self.event.message.get_plain_text() == "restart"

```

有一个细节是，使用此函数和手动退出 AliceBot 再重新运行有一些细微的差异，主要体现在使用此函数不会清空插件状态和全局状态。

## 重新加载插件

除此之外 AliceBot 还提供了一个 `reload_plugins()` 方法用于重新加载所有插件，此方法不会重新加载配置文件、适配器等。

## 自动热重载

自 0.4.0 版本开始，AliceBot 开始支持自动热重载，即当插件文件或配置文件更新时 AliceBot 不需要重新启动，就会自动加载变化。

此功能需要 `watchfiles` 库的支持，请手动安装此 Python 库。

当配置文件发生更新时，会调用 `restart()` 方法重新启动 AliceBot。

而当 `plugin_dir` 设置的的目录中的插件文件发生新增、修改、删除时，则会自动尝试导入、重新加载、删除对应的插件。

开启方式非常简单，只需要在实例化 `Bot` 类时传入 `hot_reload` 参数即可。

```python
from alicebot import Bot

bot = Bot(hot_reload=True)

if __name__ == "__main__":
    bot.run()

```

但请注意，此功能目前仍处于早期实验阶段，如果在使用过程中出现任何问题，请提交反馈，并且此功能可能会略微影响性能，如果你的应用场景对性能十分敏感，请不要在生产环境启用此功能。

