"""
============
CQHTTP 配置
============
"""
from pydantic import BaseModel


class Config(BaseModel):
    """
    CQHTTP 配置类，将在适配器被加载时被混入到机器人主配置中。
    """
    __config_name__ = 'cqhttp'
    """
    配置名称。
    """
    host: str = '127.0.0.1'
    """
    本机域名。
    """
    port: int = 8080
    """
    监听的端口。
    """
    url: str = '/cqhttp/ws'
    """
    WebSocket 路径，需和客户端配置相同。
    """
    api_timeout: int = 1000
    """
    进行 API 调用时等待返回响应的超时时间。
    """
