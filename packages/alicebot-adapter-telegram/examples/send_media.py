"""发送 Media 消息。"""

from typing_extensions import override

import anyio

from alicebot import Plugin
from alicebot.adapter.telegram.event import MessageEvent
from alicebot.adapter.telegram.media import (
    Animation,
    Audio,
    Dice,
    Document,
    Location,
    Photo,
    Poll,
    Video,
)
from alicebot.adapter.telegram.model import InputPollOption


class SendMedia(Plugin[MessageEvent, None, None]):
    """发送 Media 消息。"""

    @override
    async def handle(self) -> None:
        command = self.event.get_plain_text().removeprefix("/media@")
        if command == "photo":
            async with await anyio.Path("../docs/public/logo.png").open("rb") as f:
                await self.event.reply(
                    Photo(
                        photo=await f.read(),
                        caption="Hello, I am Alice.",
                    )
                )
        elif command == "audio":
            await self.event.reply(
                Audio(
                    audio="https://sample-videos.com/audio/mp3/crowd-cheering.mp3",
                    caption="Hello, I am Alice.",
                )
            )
        elif command == "document":
            filename = "logo.png"
            async with await anyio.Path("../docs/public/logo.png").open("rb") as f:
                await self.event.reply(
                    Document(
                        document=(filename, await f.read()),
                        caption="Hello, I am Alice.",
                    )
                )
        elif command == "video":
            await self.event.reply(
                Video(
                    video="https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4",
                    caption="Hello, I am Alice.",
                )
            )
        elif command == "animation":
            await self.event.reply(
                Animation(
                    animation="https://sample-videos.com/gif/3.gif",
                    caption="Hello, I am Alice.",
                )
            )
        elif command == "media_group":
            pass
        elif command == "location":
            await self.event.reply(
                Location(
                    latitude=51,
                    longitude=0,
                )
            )
        elif command == "poll":
            await self.event.reply(
                Poll(
                    question="What is your favorite programming language?",
                    options=[
                        InputPollOption(text="Python", text_entities=[]),
                        InputPollOption(text="TypeScript", text_entities=[]),
                        InputPollOption(text="Rust", text_entities=[]),
                    ],
                )
            )
        elif command == "dice":
            await self.event.reply(Dice())
        else:
            await self.event.reply("Unknown command.")

    @override
    async def rule(self) -> bool:
        return isinstance(
            self.event, MessageEvent
        ) and self.event.get_plain_text().startswith("/media")
