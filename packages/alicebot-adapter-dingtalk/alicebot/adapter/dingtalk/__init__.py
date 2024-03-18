"""DingTalk 协议适配器。

本适配器适配了钉钉企业自建机器人协议。
协议详情请参考：[钉钉开放平台](https://open.dingtalk.com/document/robots/robot-overview)。
"""

import base64
import hashlib
import hmac
import time
from typing import Any, Dict, Literal, Union

import aiohttp
import structlog
from aiohttp import web

from alicebot.adapter import Adapter

from .config import Config
from .event import DingTalkEvent
from .exceptions import NetworkError
from .message import DingTalkMessage

__all__ = ["DingTalkAdapter"]

logger = structlog.stdlib.get_logger()


class DingTalkAdapter(Adapter[DingTalkEvent, Config]):
    """钉钉协议适配器。"""

    name: str = "dingtalk"
    Config = Config

    app: web.Application
    runner: web.AppRunner
    site: web.TCPSite

    session: aiohttp.ClientSession

    async def startup(self) -> None:
        """创建 aiohttp Application。"""
        self.app = web.Application()
        self.app.add_routes([web.post(self.config.url, self.handler)])

        self.session = aiohttp.ClientSession()

    async def run(self) -> None:
        """运行 aiohttp 服务器。"""
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, self.config.host, self.config.port)
        await self.site.start()

    async def shutdown(self) -> None:
        """清理 aiohttp AppRunner。"""
        await self.session.close()
        await self.site.stop()
        await self.runner.cleanup()

    async def handler(self, request: web.Request) -> web.Response:
        """处理 aiohttp 服务器的接收。

        Args:
            request: aiohttp 服务器的 `Request` 对象。
        """
        if "timestamp" not in request.headers or "sign" not in request.headers:
            logger.error("Illegal http header, incomplete http header")
        elif (
            abs(int(request.headers["timestamp"]) - time.time() * 1000) > 60 * 60 * 1000
        ):
            logger.error("Illegal http header", timestamp=request.headers["timestamp"])
        elif request.headers["sign"] != self.get_sign(request.headers["timestamp"]):
            logger.error("Illegal http header", sign=request.headers["sign"])
        else:
            try:
                dingtalk_event = DingTalkEvent(adapter=self, **(await request.json()))
            except Exception:
                logger.exception("Request parsing error")
                return web.Response()
            await self.handle_event(dingtalk_event)
        return web.Response()

    def get_sign(self, timestamp: str) -> str:
        """计算签名。

        Args:
            timestamp: 时间戳。

        Returns:
            签名。
        """
        hmac_code = hmac.new(
            self.config.app_secret.encode("utf-8"),
            f"{timestamp}\n{self.config.app_secret}".encode(),
            digestmod=hashlib.sha256,
        ).digest()
        return base64.b64encode(hmac_code).decode("utf-8")

    async def send(
        self,
        webhook: str,
        conversation_type: Literal["1", "2"],
        msg: Union[str, Dict[str, Any], DingTalkMessage],
        at: Union[None, Dict[str, Any], DingTalkMessage] = None,
    ) -> Dict[str, Any]:
        """发送消息。

        Args:
            webhook: Webhook 网址。
            conversation_type: 聊天类型，"1" 表示单聊，"2" 表示群聊。
            msg: 消息。
            at: At 对象，仅在群聊时生效，默认为空。

        Returns:
            钉钉服务器的响应。

        Raises:
            TypeError: 传入参数类型错误。
            ValueError: 传入参数值错误。
            NetworkError: 调用 Webhook 地址时网络错误。
        """
        if isinstance(msg, DingTalkMessage):
            pass
        elif isinstance(msg, dict):
            msg = DingTalkMessage.raw(msg)
        elif isinstance(msg, str):
            msg = DingTalkMessage.text(msg)
        else:
            raise TypeError(
                f"msg must be str, Dict or DingTalkMessage, not {type(msg)!r}"
            )

        if at is not None:
            if isinstance(at, DingTalkMessage):
                if at.type == "at":
                    pass
                else:
                    raise ValueError(f'at.type must be "at", not {at.type}')
            elif isinstance(at, dict):
                at = DingTalkMessage.raw(at)
            else:
                raise TypeError(f"at must be Dict or DingTalkMessage, not {type(at)!r}")

        data: Union[Dict[str, Any], DingTalkMessage]
        if conversation_type == "1":
            data = msg
        elif conversation_type == "2":
            if at is None:
                data = {"msgtype": msg.type, **msg.model_dump()}
            else:
                data = {"msgtype": msg.type, **msg.model_dump(), **at.model_dump()}
        else:
            raise ValueError(
                f'conversation_type must be "1" or "2" not {conversation_type}'
            )

        try:
            async with self.session.post(webhook, json=data) as resp:
                return await resp.json()
        except aiohttp.ClientError as e:
            raise NetworkError from e
