"""HTTP 服务端适配器示例。

这里是一个最简单可以直接使用的 HTTP 服务端适配器示例。
"""

from typing import override

from aiohttp import web

from alicebot.adapter.utils import HttpServerAdapter
from alicebot.event import Event


class HttpServerTestEvent(Event["HttpServerTestAdapter"]):
    """HTTP 服务端示例适配器事件类。"""

    _adapter: "HttpServerTestAdapter"
    message: str

    def __init__(self, adapter: "HttpServerTestAdapter", message: str) -> None:
        """初始化 HttpServerTestEvent。"""
        self._adapter = adapter
        self.message = message

    @property
    @override
    def adapter(self) -> "HttpServerTestAdapter":
        return self._adapter


class HttpServerTestAdapter(HttpServerAdapter[HttpServerTestEvent, None]):
    """HTTP 服务端示例适配器类。"""

    name: str = "http_server_adapter"
    get_url: str = "/"
    post_url: str = "/"
    host: str = "127.0.0.1"
    port: int = 8080

    @override
    async def handle_response(self, request: web.Request) -> web.StreamResponse:
        message = await request.text()
        event = HttpServerTestEvent(adapter=self, message=message)
        await self.handle_event(event)
        return web.Response()
