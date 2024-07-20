"""Console 适配器。

用于接收命令行输入的适配器示例。
"""

import asyncio
import sys
from typing_extensions import override

from alicebot import MessageEvent
from alicebot.adapter import Adapter


class ConsoleAdapterEvent(MessageEvent["ConsoleAdapter"]):
    """Console 适配器。

    Attributes:
        message: 消息内容。
    """

    message: str

    @override
    def get_sender_id(self) -> None:
        return None

    @override
    def get_plain_text(self) -> str:
        return self.message

    @override
    async def reply(self, message: str) -> None:
        return await self.adapter.send(message)


class ConsoleAdapter(Adapter[ConsoleAdapterEvent, None]):
    """Console 适配器。"""

    name: str = "console"

    @override
    async def run(self) -> None:
        while not self.bot.should_exit.is_set():
            print("Please input message: ")  # noqa: T201
            message = await asyncio.get_event_loop().run_in_executor(
                None, sys.stdin.readline
            )
            await self.handle_event(
                ConsoleAdapterEvent(adapter=self, type="message", message=message)
            )

    async def send(self, message: str) -> None:
        """发送消息。

        Args:
            message: 消息内容。
        """
        print(f"Send a message: {message}")  # noqa: T201
