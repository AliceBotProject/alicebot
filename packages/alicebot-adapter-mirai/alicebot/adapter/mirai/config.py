"""Mirai 适配器配置。"""
from typing import Literal

from alicebot.config import ConfigModel


class Config(ConfigModel):
    """Mirai 配置类，将在适配器被加载时被混入到机器人主配置中。

    Attributes:
        adapter_type: 适配器类型，需要和协议端配置相同。
        host: 本机域名。
        port: 监听的端口。
        url: WebSocket 路径，需要和协议端配置相同。
        reconnect_interval: 重连等待时间。
        api_timeout: 进行 API 调用时等待返回响应的超时时间。
        verify_key: 建立连接时的认证密钥，需要和 mirai-api-http 配置中的 verifyKey 相同，如果关闭验证则留空。
        qq: 机器人的 QQ 号码，必须指定。
    """

    __config_name__ = "mirai"
    adapter_type: Literal["ws", "reverse-ws"] = "ws"
    host: str = "127.0.0.1"
    port: int = 8080
    url: str = "/mirai/ws"
    reconnect_interval: int = 3
    api_timeout: int = 1000
    verify_key: str = ""
    qq: int = 10001
