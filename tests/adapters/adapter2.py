from typing import Any
from typing_extensions import override

from alicebot import Adapter


class Adapter2(Adapter[Any, None]):
    name = "adapter2"

    @override
    async def run(self) -> None:
        self.bot.should_exit.set()
