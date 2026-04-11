"""Console 适配器。

用于接收命令行输入的适配器示例。
"""

import sys
from typing import override

import anyio.to_thread

from alicebot import MessageEvent
from alicebot.adapter.utils import PollingAdapter


class ConsoleAdapterEvent(MessageEvent["ConsoleAdapter"]):
    """Console 适配器。

    Attributes:
        message: 消息内容。
    """

    _adapter: "ConsoleAdapter"
    message: str

    def __init__(self, adapter: "ConsoleAdapter", message: str) -> None:
        """初始化 ConsoleAdapterEvent。"""
        self._adapter = adapter
        self.message = message

    @property
    @override
    def adapter(self) -> "ConsoleAdapter":
        return self._adapter

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
        event = ConsoleAdapterEvent(adapter=self, message=message.strip())
        await self.handle_event(event)

    async def send(self, message: str) -> None:
        """发送消息。

        Args:
            message: 消息内容。
        """
        print(f"Send a message: {message}")  # noqa: T201
