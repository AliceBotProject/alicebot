from typing import Any, override

from alicebot import Adapter


class Adapter2(Adapter[Any, None]):
    name = "adapter2"

    @override
    async def run(self) -> None:
        self.bot.exit()
