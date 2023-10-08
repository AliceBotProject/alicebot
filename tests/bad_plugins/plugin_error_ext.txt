from typing import Any

from alicebot import Plugin


class Plugin1(Plugin[Any, None, None]):
    async def handle(self) -> None:
        pass

    async def rule(self) -> bool:
        return True
