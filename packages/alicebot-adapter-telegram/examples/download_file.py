"""下载文件。"""

from typing_extensions import override

import aiohttp
import anyio
import structlog

from alicebot import Plugin
from alicebot.adapter.telegram.event import MessageEvent

logger = structlog.stdlib.get_logger()


class DownloadFile(Plugin[MessageEvent, None, None]):
    """下载文件。"""

    @override
    async def handle(self) -> None:
        if self.event.message.document is None:
            await self.event.reply("Please send me a file.")
            return

        file = await self.event.adapter.get_file(
            file_id=self.event.message.document.file_id
        )
        if not file.file_path:
            await self.event.reply("Can not get file path.")
            return

        path = anyio.Path(file.file_path)
        if await path.exists():
            # 本地搭建的 Telegram Bot API 服务器会返回本地路径
            data = await path.read_bytes()
        else:
            url = f"{self.event.adapter.config.api_server}file/bot{self.event.adapter.config.bot_token}/{file.file_path}"
            async with (
                aiohttp.ClientSession() as session,
                session.get(url) as resp,
            ):
                data = await resp.read()

        download_path = anyio.Path(await anyio.Path.cwd() / "download" / path)
        logger.info("Download file", path=download_path)
        await download_path.write_bytes(data)

    @override
    async def rule(self) -> bool:
        return isinstance(self.event, MessageEvent) and (
            self.event.get_plain_text() == "/download"
            or self.event.message.caption == "/download"
        )
