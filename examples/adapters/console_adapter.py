"""Console 适配器。

用于接收命令行输入的适配器示例。
"""

import sys
from typing_extensions import override

import anyio.to_thread

from alicebot import MessageEvent
from alicebot.adapter.utils import PollingAdapter


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


class ConsoleAdapter(PollingAdapter[ConsoleAdapterEvent, None]):
    """Console 适配器。"""

    name: str = "console"

    @override
    async def on_tick(self) -> None:
        print("Please input message: ")  # noqa: T201
        message = await anyio.to_thread.run_sync(sys.stdin.readline)
        await self.handle_event(
            ConsoleAdapterEvent(adapter=self, type="message", message=message)
        )

    async def send(self, message: str) -> None:
        """发送消息。

        Args:
            message: 消息内容。
        """
        print(f"Send a message: {message}")  # noqa: T201
