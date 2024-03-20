"""Console 适配器。

用于接收命令行输入的适配器示例。
"""

import asyncio
import sys

from alicebot import MessageEvent
from alicebot.adapter import Adapter


class ConsoleAdapterEvent(MessageEvent["ConsoleAdapter"]):
    """Console 适配器。

    Attributes:
        message: 消息内容。
    """

    message: str

    def get_sender_id(self) -> None:
        """获取消息的发送者的唯一标识符。

        Returns:
            消息的发送者的唯一标识符。
        """

    def get_plain_text(self) -> str:
        """获取消息的纯文本内容。

        Returns:
            消息的纯文本内容。
        """
        return self.message

    async def reply(self, message: str) -> None:
        """回复消息。

        Args:
            message: 回复消息的内容。
        """
        return await self.adapter.send(message)


class ConsoleAdapter(Adapter[ConsoleAdapterEvent, None]):
    """Console 适配器。"""

    name: str = "console"

    async def run(self) -> None:
        """运行适配器。"""
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
