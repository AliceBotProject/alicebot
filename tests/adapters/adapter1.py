from typing import Any, override

from alicebot import Adapter


class Adapter1(Adapter[Any, None]):
    name = "adapter1"

    @override
    async def run(self) -> None:
        self.bot.exit()
