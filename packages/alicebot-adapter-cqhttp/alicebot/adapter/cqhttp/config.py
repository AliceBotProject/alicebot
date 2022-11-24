"""CQHTTP 适配器配置。"""
from typing import Literal

from alicebot.config import ConfigModel


class Config(ConfigModel):
    """CQHTTP 配置类，将在适配器被加载时被混入到机器人主配置中。

    Attributes:
        adapter_type: 适配器类型，需要和协议端配置相同。
        host: 本机域名。
        port: 监听的端口。
        url: WebSocket 路径，需和协议端配置相同。
        reconnect_interval: 重连等待时间。
        api_timeout: 进行 API 调用时等待返回响应的超时时间。
        access_token: 鉴权。
    """

    __config_name__ = "cqhttp"
    adapter_type: Literal["ws", "reverse-ws", "ws-reverse"] = "reverse-ws"
    host: str = "127.0.0.1"
    port: int = 8080
    url: str = "/cqhttp/ws"
    reconnect_interval: int = 3
    api_timeout: int = 1000
    access_token: str = ""
