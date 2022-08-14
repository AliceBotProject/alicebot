"""DingTalk 协议适配器。

本适配器适配了钉钉企业自建机器人协议。
协议详情请参考: [钉钉开放平台](https://developers.dingtalk.com/document/robots/robot-overview) 。
"""
import hmac
import time
import base64
import hashlib
from typing import Any, Dict, Union, Literal

import aiohttp
from aiohttp import web

from alicebot.adapter import Adapter
from alicebot.log import logger, error_or_exception

from .config import Config
from .event import DingTalkEvent
from .message import DingTalkMessage
from .exceptions import ApiTimeout, NetworkError

__all__ = ["DingTalkAdapter"]


class DingTalkAdapter(Adapter):
    """钉钉协议适配器。"""

    name: str = "dingtalk"
    app: web.Application = None
    runner: web.AppRunner = None
    site: web.TCPSite = None

    session: aiohttp.ClientSession = None

    @property
    def config(self):
        """本适配器的配置。"""
        return getattr(self.bot.config, Config.__config_name__)

    async def startup(self):
        """创建 aiohttp Application。"""
        self.app = web.Application()
        self.app.add_routes([web.post(self.config.url, self.handler)])

        self.session = aiohttp.ClientSession()

    async def run(self):
        """运行 aiohttp 服务器。"""
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, self.config.host, self.config.port)
        await self.site.start()

    async def shutdown(self):
        """清理 aiohttp AppRunner。"""
        if self.session is not None:
            await self.session.close()
        if self.site is not None:
            await self.site.stop()
        if self.runner is not None:
            await self.runner.cleanup()

    async def handler(self, request: web.Request):
        """处理 aiohttp 服务器的接收。

        Args:
            request: aiohttp 服务器的 Request 对象。
        """
        if "timestamp" not in request.headers or "sign" not in request.headers:
            logger.error(f"Illegal http header, incomplete http header")
        elif abs(int(request.headers["timestamp"]) - time.time() * 1000) > 3600000:
            logger.error(
                f'Illegal http header, timestamp: {request.headers["timestamp"]}'
            )
        elif request.headers["sign"] != self.get_sign(request.headers["timestamp"]):
            logger.error(f'Illegal http header, sign: {request.headers["sign"]}')
        else:
            try:
                dingtalk_event = DingTalkEvent(adapter=self, **(await request.json()))
            except Exception as e:
                error_or_exception(
                    "Request parsing error:", e, self.bot.config.verbose_exception_log
                )
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
            "{}\n{}".format(timestamp, self.config.app_secret).encode("utf-8"),
            digestmod=hashlib.sha256,
        ).digest()
        return base64.b64encode(hmac_code).decode("utf-8")

    async def send(
        self,
        webhook: str,
        conversation_type: Literal["1", "2"],
        msg: Union[str, Dict, DingTalkMessage],
        at: Union[None, Dict, DingTalkMessage] = None,
    ) -> Dict[str, Any]:
        """发送消息。

        Args:
            webhook: Webhook 网址。
            conversation_type: 聊天类型，'1' 表示单聊，'2' 表示群聊。
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

        if conversation_type == "1":
            data = msg
        elif conversation_type == "2":
            if at is None:
                data = {"msgtype": msg.type, **msg.as_dict()}
            else:
                data = {"msgtype": msg.type, **msg.as_dict(), **at.as_dict()}
        else:
            raise ValueError(
                f'conversation_type must be "1" or "2" not {conversation_type}'
            )

        try:
            async with self.session.post(webhook, json=data) as resp:
                return await resp.json()
        except aiohttp.ClientError:
            raise NetworkError
