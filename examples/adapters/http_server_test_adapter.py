"""HTTP 服务端适配器示例。

这里是一个最简单可以直接使用的 HTTP 服务端适配器示例。
"""
from aiohttp import web

from alicebot.adapter.utils import HttpServerAdapter
from alicebot.event import Event
from alicebot.message import Message, MessageSegment


class HttpServerTestEvent(Event["HttpServerTestAdapter"]):
    """HTTP 服务端示例适配器事件类。"""

    message: Message  # type: ignore


class HttpServerTestAdapter(HttpServerAdapter[HttpServerTestEvent, None]):
    """HTTP 服务端示例适配器类。"""

    get_url: str = "/"
    post_url: str = "/"
    host: str = "127.0.0.1"
    port: int = 8080

    async def handle_response(self, request: web.Request):
        """处理响应。"""
        event = HttpServerTestEvent(
            adapter=self,
            type="message",
            message=Message(
                MessageSegment(type="text", data={"text": await request.text()})
            ),
        )
        await self.handle_event(event)
        return web.Response()
