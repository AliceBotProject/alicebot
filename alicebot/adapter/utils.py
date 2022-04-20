"""适配器实用工具。

这里定义了一些在编写适配器时常用的基类，适配器开发者可以直接继承自这里的类或者用作参考。
"""
import asyncio
from typing import Union
from abc import ABCMeta, abstractmethod

import aiohttp
from aiohttp import web

from alicebot.adapter import Adapter


class PollingAdapter(Adapter, metaclass=ABCMeta):
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


class HttpClientAdapter(PollingAdapter, metaclass=ABCMeta):
    """HTTP 客户端适配器示例。"""
    session: aiohttp.ClientSession

    async def startup(self):
        self.session = aiohttp.ClientSession()

    @abstractmethod
    async def on_tick(self):
        pass

    async def shutdown(self):
        await self.session.close()


class WebSocketClientAdapter(Adapter, metaclass=ABCMeta):
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


class HttpServerAdapter(Adapter, metaclass=ABCMeta):
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
        self.app.add_routes([web.get(self.get_url, self.handle_response),
                             web.post(self.post_url, self.handle_response)])

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


class WebSocketServerAdapter(Adapter, metaclass=ABCMeta):
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
