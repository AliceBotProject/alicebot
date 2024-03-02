"""AliceBot

简单的 Python 异步多后端机器人框架

本模块从子模块导入了以下内容：
- `Bot` => [`alicebot.bot.Bot`](./bot#Bot)
- `Event` => [`alicebot.event.Event`](./event#Event)
- `MessageEvent` => [`alicebot.event.MessageEvent`](./event#MessageEvent)
- `Plugin` => [`alicebot.plugin.Plugin`](./plugin#Plugin)
- `Adapter` => [`alicebot.adapter.Adapter`](./adapter/#Adapter)
- `ConfigModel` => [`alicebot.config.ConfigModel`](./config#ConfigModel)
- `Depends` => [`alicebot.dependencies.Depends`](./dependencies#Depends)
"""

from alicebot.adapter import Adapter
from alicebot.bot import Bot
from alicebot.config import ConfigModel
from alicebot.dependencies import Depends
from alicebot.event import Event, MessageEvent
from alicebot.plugin import Plugin

__all__ = [
    "Adapter",
    "Bot",
    "ConfigModel",
    "Depends",
    "Event",
    "MessageEvent",
    "Plugin",
]
