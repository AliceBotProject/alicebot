"""适配器实用工具。

这里定义了一些在编写适配器时常用的基类，适配器开发者可以直接继承自这里的类或者用作参考。
"""

import asyncio
from abc import ABCMeta, abstractmethod
from typing import Literal, Optional, Union

import aiohttp
import structlog
from aiohttp import web

from alicebot.adapter import Adapter
from alicebot.typing import ConfigT, EventT

__all__ = [
    "PollingAdapter",
    "HttpClientAdapter",
    "WebSocketClientAdapter",
    "HttpServerAdapter",
    "WebSocketServerAdapter",
    "WebSocketAdapter",
]

logger = structlog.stdlib.get_logger()


class PollingAdapter(Adapter[EventT, ConfigT], metaclass=ABCMeta):
    """轮询式适配器示例。"""

    delay: float = 0.1
    create_task: bool = False
    _on_tick_task: Optional["asyncio.Task[None]"] = None

    async def run(self) -> None:
        """运行适配器。"""
        while not self.bot.should_exit.is_set():
            await asyncio.sleep(self.delay)
            if self.create_task:
                self._on_tick_task = asyncio.create_task(self.on_tick())
            else:
                await self.on_tick()

    @abstractmethod
    async def on_tick(self) -> None:
        """当轮询发生。"""


class HttpClientAdapter(PollingAdapter[EventT, ConfigT], metaclass=ABCMeta):
    """HTTP 客户端适配器示例。"""

    session: aiohttp.ClientSession

    async def startup(self) -> None:
        """初始化适配器。"""
        self.session = aiohttp.ClientSession()

    @abstractmethod
    async def on_tick(self) -> None:
        """当轮询发生。"""

    async def shutdown(self) -> None:
        """关闭并清理连接。"""
        await self.session.close()


class WebSocketClientAdapter(Adapter[EventT, ConfigT], metaclass=ABCMeta):
    """WebSocket 客户端适配器示例。"""

    url: str

    async def run(self) -> None:
        """运行适配器。"""
        async with aiohttp.ClientSession() as session, session.ws_connect(
            self.url
        ) as ws:
            msg: aiohttp.WSMessage
            async for msg in ws:
                if self.bot.should_exit.is_set():
                    break
                if msg.type == aiohttp.WSMsgType.ERROR:
                    break
                await self.handle_response(msg)

    @abstractmethod
    async def handle_response(self, msg: aiohttp.WSMessage) -> None:
        """处理响应。"""


class HttpServerAdapter(Adapter[EventT, ConfigT], metaclass=ABCMeta):
    """HTTP 服务端适配器示例。"""

    app: web.Application
    runner: web.AppRunner
    site: web.TCPSite
    host: str
    port: int
    get_url: str
    post_url: str

    async def startup(self) -> None:
        """初始化适配器。"""
        self.app = web.Application()
        self.app.add_routes(
            [
                web.get(self.get_url, self.handle_response),
                web.post(self.post_url, self.handle_response),
            ]
        )

    async def run(self) -> None:
        """运行适配器。"""
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, self.host, self.port)
        await self.site.start()

    async def shutdown(self) -> None:
        """关闭并清理连接。"""
        await self.runner.cleanup()

    @abstractmethod
    async def handle_response(self, request: web.Request) -> web.StreamResponse:
        """处理响应。"""


class WebSocketServerAdapter(Adapter[EventT, ConfigT], metaclass=ABCMeta):
    """WebSocket 服务端适配器示例。"""

    app: web.Application
    runner: web.AppRunner
    site: web.TCPSite
    websocket: web.WebSocketResponse
    host: str
    port: int
    url: str

    async def startup(self) -> None:
        """初始化适配器。"""
        self.app = web.Application()
        self.app.add_routes([web.get(self.url, self.handle_response)])

    async def run(self) -> None:
        """运行适配器。"""
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, self.host, self.port)
        await self.site.start()

    async def shutdown(self) -> None:
        """关闭并清理连接。"""
        await self.websocket.close()
        await self.site.stop()
        await self.runner.cleanup()

    async def handle_response(self, request: web.Request) -> web.WebSocketResponse:
        """处理 WebSocket。"""
        ws = web.WebSocketResponse()
        await ws.prepare(request)
        self.websocket = ws

        msg: aiohttp.WSMessage
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                await self.handle_ws_response(msg)
            elif msg.type == aiohttp.WSMsgType.ERROR:
                break

        return ws

    @abstractmethod
    async def handle_ws_response(self, msg: aiohttp.WSMessage) -> None:
        """处理 WebSocket 响应。"""


class WebSocketAdapter(Adapter[EventT, ConfigT], metaclass=ABCMeta):
    """WebSocket 适配器示例。

    同时支持 WebSocket 客户端和服务端。
    """

    websocket: Union[web.WebSocketResponse, aiohttp.ClientWebSocketResponse, None] = (
        None
    )

    # ws
    session: Optional[aiohttp.ClientSession]

    # reverse-ws
    app: Optional[web.Application]
    runner: Optional[web.AppRunner]
    site: Optional[web.TCPSite]

    # config
    adapter_type: Literal["ws", "reverse-ws"]
    host: str
    port: int
    url: str
    reconnect_interval: int = 3

    async def startup(self) -> None:
        """初始化适配器。"""
        if self.adapter_type == "ws":
            self.session = aiohttp.ClientSession()
        elif self.adapter_type == "reverse-ws":
            self.app = web.Application()
            self.app.add_routes([web.get(self.url, self.handle_reverse_ws_response)])
        else:
            logger.error(
                'Config "adapter_type" must be "ws" or "reverse-ws"',
                adapter_type=self.adapter_type,
            )

    async def run(self) -> None:
        """运行适配器。"""
        if self.adapter_type == "ws":
            while True:
                try:
                    await self.websocket_connect()
                except aiohttp.ClientError:
                    logger.exception("WebSocket connection error")
                if self.bot.should_exit.is_set():
                    break
                await asyncio.sleep(self.reconnect_interval)
        elif self.adapter_type == "reverse-ws":
            assert self.app is not None
            self.runner = web.AppRunner(self.app)
            await self.runner.setup()
            self.site = web.TCPSite(self.runner, self.host, self.port)
            await self.site.start()

    async def shutdown(self) -> None:
        """关闭并清理连接。"""
        if self.websocket is not None:
            await self.websocket.close()
        if self.adapter_type == "ws":
            if self.session is not None:
                await self.session.close()
        elif self.adapter_type == "reverse-ws":
            if self.site is not None:
                await self.site.stop()
            if self.runner is not None:
                await self.runner.cleanup()

    async def handle_reverse_ws_response(
        self, request: web.Request
    ) -> web.WebSocketResponse:
        """处理 aiohttp WebSocket 服务器的接收。"""
        self.websocket = web.WebSocketResponse()
        await self.websocket.prepare(request)
        await self.reverse_ws_connection_hook()
        await self.handle_websocket()
        return self.websocket

    async def reverse_ws_connection_hook(self) -> None:
        """反向 WebSocket 连接建立时的钩子函数。"""
        logger.info("WebSocket connected!")

    async def websocket_connect(self) -> None:
        """创建正向 WebSocket 连接。"""
        assert self.session is not None
        logger.info("Tying to connect to WebSocket server...")
        async with self.session.ws_connect(
            f"ws://{self.host}:{self.port}{self.url}"
        ) as self.websocket:
            await self.handle_websocket()

    async def handle_websocket(self) -> None:
        """处理 WebSocket。"""
        if self.websocket is None or self.websocket.closed:
            return
        async for msg in self.websocket:
            await self.handle_websocket_msg(msg)
        if not self.bot.should_exit.is_set():
            logger.warning("WebSocket connection closed!")

    @abstractmethod
    async def handle_websocket_msg(self, msg: aiohttp.WSMessage) -> None:
        """处理 WebSocket 消息。"""
        raise NotImplementedError
