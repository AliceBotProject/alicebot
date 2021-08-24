"""
==================
DingTalk 协议适配器
==================
本适配器适配了钉钉企业自建机器人协议。
协议详情请参考: `钉钉开放平台`_ 。

.. _钉钉开放平台: https://developers.dingtalk.com/document/robots/robot-overview
"""
import time
import json
import hmac
import base64
import hashlib

from aiohttp import web

from alicebot.log import logger
from alicebot.adapter import AbstractAdapter
from alicebot.message import DataclassEncoder

from .config import Config
from .event import DingTalkEvent
from .exception import ApiTimeout
from .message import DingTalkMessage


class DingTalkAdapter(AbstractAdapter):
    """
    钉钉协议适配器。
    """
    name: str = 'dingtalk'
    app: web.Application = None
    runner: web.AppRunner = None
    site: web.TCPSite = None

    @property
    def config(self):
        """
        :return: 本适配器的配置。
        """
        return getattr(self.bot.config, Config.__config_name__)

    async def startup(self):
        """
        创建 aiohttp Application。
        """
        self.app = web.Application()
        self.app.add_routes([web.post(self.config.url, self.handler)])

    async def run(self):
        """
        运行 aiohttp 服务器。
        """
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, self.config.host, self.config.port)
        await self.site.start()

    async def shutdown(self):
        """
        清理 aiohttp AppRunner。
        """
        if self.site is not None:
            await self.site.stop()
        if self.runner is not None:
            await self.runner.cleanup()

    async def get(self, *args, **kwargs):
        """
        钉钉协议适配器暂不支持 get() 方法。
        """
        raise NotImplementedError

    async def send(self, *args, **kwargs):
        """
        钉钉协议适配器暂不支持 send() 方法。
        """
        raise NotImplementedError

    async def handler(self, request: web.Request):
        """
        处理 aiohttp 服务器的接收。

        :param request: aiohttp 服务器的 Request 对象。
        """

        if 'timestamp' not in request.headers or 'sign' not in request.headers:
            logger.error(f'Illegal http header, incomplete http header')
            return web.Response()
        elif abs(int(request.headers['timestamp']) - time.time() * 1000) > 3600000:
            logger.error(f'Illegal http header, timestamp: {request.headers["timestamp"]}')
            return web.Response()
        elif request.headers['sign'] != self.get_sign(request.headers['timestamp']):
            logger.error(f'Illegal http header, sign: {request.headers["sign"]}')
            return web.Response()

        try:
            dingtalk_event = DingTalkEvent(**(await request.json()))
            dingtalk_event.adapter = self
        except Exception as e:
            logger.error(f'Request parsing error: {e!r}')
            return web.Response()

        logger.info(f'Adapter {self.__class__.__name__} received: {dingtalk_event!r}')
        await self.bot.handle_event(dingtalk_event)

        if dingtalk_event.response_msg is None:
            return web.Response()
        if dingtalk_event.conversationType == '1':
            response = web.Response(text=json.dumps(dingtalk_event.response_msg, cls=DataclassEncoder),
                                    content_type='application/json')
        elif dingtalk_event.conversationType == '2':
            if dingtalk_event.response_at is None:
                response = web.Response(text=json.dumps({'msgtype': dingtalk_event.response_msg.type,
                                                         **dingtalk_event.response_msg.as_dict()}),
                                        content_type='application/json')
            else:
                response = web.Response(text=json.dumps({'msgtype': dingtalk_event.response_msg.type,
                                                         **dingtalk_event.response_msg.as_dict(),
                                                         **dingtalk_event.response_at.as_dict()}),
                                        content_type='application/json')
        else:
            logger.error(f'conversationType error: {dingtalk_event.conversationType}')
            return web.Response()
        return response

    def get_sign(self, timestamp: str) -> str:
        """
        计算签名。

        :param timestamp: 时间戳。
        :return: 签名。
        :rtype: str
        """
        hmac_code = hmac.new(self.config.app_secret.encode('utf-8'),
                             '{}\n{}'.format(timestamp, self.config.app_secret).encode('utf-8'),
                             digestmod=hashlib.sha256).digest()
        return base64.b64encode(hmac_code).decode('utf-8')
