from typing import Any
from typing_extensions import override

from alicebot import Adapter


class Adapter1(Adapter[Any, None]):
    name = "adapter1"

    @override
    async def run(self) -> None:
        self.bot.should_exit.set()


class Adapter2(Adapter[Any, None]):
    name = "adapter2"

    @override
    async def run(self) -> None:
        self.bot.should_exit.set()
