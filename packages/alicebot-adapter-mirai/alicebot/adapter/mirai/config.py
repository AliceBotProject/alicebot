"""
============
Mirai 配置
============
"""
from pydantic import BaseModel


class Config(BaseModel):
    """
    Mirai 配置类，将在适配器被加载时被混入到机器人主配置中。
    """
    __config_name__ = 'mirai'
    """
    配置名称。
    """
    adapter_type: str = 'ws'
    """
    适配器类型，需要和 mirai-api-http 配置相同。
    
    :type: str
    """
    host: str = '127.0.0.1'
    """
    本机域名。
    
    :type: str
    """
    port: int = 8080
    """
    监听的端口。
    
    :type: int
    """
    url: str = '/mirai/ws'
    """
    WebSocket 路径，需要和 mirai-api-http 配置相同。
    
    :type: str
    """
    api_timeout: int = 1000
    """
    进行 API 调用时等待返回响应的超时时间。
    
    :type: int
    """
    verify_key: str = ''
    """
    建立连接时的认证密钥，需要和 mirai-api-http 配置中的 verifyKey 相同，如果关闭验证则留空。
    
    :type: str
    """
    qq: int = 10001
    """
    机器人的 QQ 号码，必须指定。
    
    :type: int
    """
