"""CQHTTP 适配器配置。"""
from pydantic import BaseModel


class Config(BaseModel):
    """CQHTTP 配置类，将在适配器被加载时被混入到机器人主配置中。

    Attributes:
        __config_name__: 配置名称。
        host: 本机域名。
        port: 监听的端口。
        url: WebSocket 路径，需和客户端配置相同。
        api_timeout: 进行 API 调用时等待返回响应的超时时间。
    """
    __config_name__ = 'cqhttp'
    adapter_type: str = 'reverse-ws'
    host: str = '127.0.0.1'
    port: int = 8080
    url: str = '/cqhttp/ws'
    reconnect_interval: int = 3
    api_timeout: int = 1000
    access_token: str = ''
