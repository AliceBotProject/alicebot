"""适配器实用工具。

这里定义了一些在编写适配器时常用的基类，适配器开发者可以直接继承自这里的类或者用作参考。
"""
import asyncio
from typing import Union, Literal
from abc import ABCMeta, abstractmethod

import aiohttp
from aiohttp import web

from alicebot.adapter import Adapter
from alicebot.typing import T_Event, T_Config
from alicebot.log import logger, error_or_exception


class PollingAdapter(Adapter[T_Event, T_Config], metaclass=ABCMeta):
    """轮询式适配器示例。"""

    delay: Union[int, float] = 0.1
    create_task: bool = False

    async def run(self):
        while not self.bot.should_exit.is_set():
            await asyncio.sleep(self.delay)
            if self.create_task:
                asyncio.create_task(self.on_tick())
            else:
                await self.on_tick()

    @abstractmethod
    async def on_tick(self):
        pass


class HttpClientAdapter(PollingAdapter[T_Event, T_Config], metaclass=ABCMeta):
    """HTTP 客户端适配器示例。"""

    session: aiohttp.ClientSession

    async def startup(self):
        self.session = aiohttp.ClientSession()

    @abstractmethod
    async def on_tick(self):
        pass

    async def shutdown(self):
        await self.session.close()


class WebSocketClientAdapter(Adapter[T_Event, T_Config], metaclass=ABCMeta):
    """WebSocket 客户端适配器示例。"""

    url: str

    async def run(self):
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect(self.url) as ws:
                msg: aiohttp.WSMessage
                async for msg in ws:
                    if self.bot.should_exit.is_set():
                        break
                    if msg.type == aiohttp.WSMsgType.ERROR:
                        break
                    await self.handle_response(msg)

    @abstractmethod
    def handle_response(self, msg: aiohttp.WSMessage):
        pass


class HttpServerAdapter(Adapter[T_Event, T_Config], metaclass=ABCMeta):
    """HTTP 服务端适配器示例。"""

    app: web.Application
    runner: web.AppRunner
    site: web.TCPSite
    host: str
    port: int
    get_url: str
    post_url: str

    async def startup(self):
        self.app = web.Application()
        self.app.add_routes(
            [
                web.get(self.get_url, self.handle_response),
                web.post(self.post_url, self.handle_response),
            ]
        )

    async def run(self):
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, self.host, self.port)
        await self.site.start()

    async def shutdown(self):
        await self.runner.cleanup()

    @abstractmethod
    async def handle_response(self, request: web.Request):
        pass


class WebSocketServerAdapter(Adapter[T_Event, T_Config], metaclass=ABCMeta):
    """WebSocket 服务端适配器示例。"""

    app: web.Application = None
    runner: web.AppRunner = None
    site: web.TCPSite = None
    websocket: web.WebSocketResponse = None
    host: str
    port: int
    url: str

    async def startup(self):
        self.app = web.Application()
        self.app.add_routes([web.get(self.url, self.handle_response)])

    async def run(self):
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, self.host, self.port)
        await self.site.start()

    async def shutdown(self):
        if self.websocket is not None:
            await self.websocket.close()
        if self.site is not None:
            await self.site.stop()
        if self.runner is not None:
            await self.runner.cleanup()

    async def handle_response(self, request: web.Request):
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
    async def handle_ws_response(self, msg: aiohttp.WSMessage):
        pass


class WebSocketAdapter(Adapter[T_Event, T_Config], metaclass=ABCMeta):
    """WebSocket 适配器示例。

    同时支持 WebSocket 客户端和服务端。
    """

    websocket: Union[web.WebSocketResponse, aiohttp.ClientWebSocketResponse] = None

    # ws
    session: aiohttp.ClientSession = None

    # reverse-ws
    app: web.Application = None
    runner: web.AppRunner = None
    site: web.TCPSite = None

    # config
    adapter_type: Literal["ws", "reverse-ws"]
    host: str
    port: int
    url: str
    reconnect_interval: int = 3

    async def startup(self):
        """初始化适配器。"""
        if self.adapter_type == "ws":
            self.session = aiohttp.ClientSession()
        elif self.adapter_type == "reverse-ws":
            self.app = web.Application()
            self.app.add_routes([web.get(self.url, self.handle_reverse_ws_response)])
        else:
            logger.error(
                'Config "adapter_type" must be "ws" or "reverse-ws", not '
                + self.adapter_type
            )

    async def run(self):
        """运行适配器。"""
        if self.adapter_type == "ws":
            while True:
                try:
                    await self.websocket_connect()
                except aiohttp.ClientError as e:
                    error_or_exception(
                        "WebSocket connection error:",
                        e,
                        self.bot.config.bot.log.verbose_exception,
                    )
                if self.bot.should_exit.is_set():
                    break
                await asyncio.sleep(self.reconnect_interval)
        elif self.adapter_type == "reverse-ws":
            self.runner = web.AppRunner(self.app)
            await self.runner.setup()
            self.site = web.TCPSite(self.runner, self.host, self.port)
            await self.site.start()

    async def shutdown(self):
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

    async def handle_reverse_ws_response(self, request: web.Request):
        """处理 aiohttp WebSocket 服务器的接收。"""
        self.websocket = web.WebSocketResponse()
        await self.websocket.prepare(request)
        await self.reverse_ws_connection_hook()
        await self.handle_websocket()
        return self.websocket

    async def reverse_ws_connection_hook(self):
        """反向 WebSocket 连接建立时的钩子函数。"""
        logger.info(f"WebSocket connected!")

    async def websocket_connect(self):
        """创建正向 WebSocket 连接。"""
        logger.info("Tying to connect to WebSocket server...")
        async with self.session.ws_connect(
            f"ws://{self.host}:{self.port}{self.url}"
        ) as self.websocket:
            await self.handle_websocket()

    async def handle_websocket(self):
        """处理 WebSocket。"""
        if self.websocket.closed:
            return
        async for msg in self.websocket:
            msg: aiohttp.WSMessage
            await self.handle_websocket_msg(msg)
        if not self.bot.should_exit.is_set():
            logger.warning("WebSocket connection closed!")

    @abstractmethod
    async def handle_websocket_msg(self, msg: aiohttp.WSMessage):
        """处理 WebSocket 消息。"""
        raise NotImplementedError
