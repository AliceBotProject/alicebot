"""HTTP 服务端适配器示例。

这里是一个最简单可以直接使用的 HTTP 服务端适配器示例。
"""

from typing_extensions import override

from aiohttp import web

from alicebot.adapter.utils import HttpServerAdapter
from alicebot.event import Event


class HttpServerTestEvent(Event["HttpServerTestAdapter"]):
    """HTTP 服务端示例适配器事件类。"""

    message: str


class HttpServerTestAdapter(HttpServerAdapter[HttpServerTestEvent, None]):
    """HTTP 服务端示例适配器类。"""

    name: str = "http_server_adapter"
    get_url: str = "/"
    post_url: str = "/"
    host: str = "127.0.0.1"
    port: int = 8080

    @override
    async def handle_response(self, request: web.Request) -> web.StreamResponse:
        event = HttpServerTestEvent(
            adapter=self,
            type="message",
            message=await request.text(),
        )
        await self.handle_event(event)
        return web.Response()
