from typing import Any

from alicebot import Adapter


class Adapter2(Adapter[Any, None]):
    name = "adapter2"

    async def run(self) -> None:
        self.bot.should_exit.set()
