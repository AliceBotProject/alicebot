from typing import Any
from typing_extensions import override

from alicebot import Plugin


class Plugin2(Plugin[Any, None, None]):
    @override
    async def handle(self) -> None:
        pass

    @override
    async def rule(self) -> bool:
        return True
