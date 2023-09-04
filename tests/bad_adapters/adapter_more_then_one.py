from typing import Any

from alicebot import Adapter


class Adapter1(Adapter[Any, None]):
    name = "adapter1"

    async def run(self) -> None:
        self.bot.should_exit.set()


class Adapter2(Adapter[Any, None]):
    name = "adapter2"

    async def run(self) -> None:
        self.bot.should_exit.set()
