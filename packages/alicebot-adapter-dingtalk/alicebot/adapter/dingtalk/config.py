"""
============
DingTalk 配置
============
"""
from pydantic import BaseModel


class Config(BaseModel):
    """
    DingTalk 配置类，将在适配器被加载时被混入到机器人主配置中。
    """
    __config_name__ = 'dingtalk'
    """
    配置名称。
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
    url: str = '/dingtalk'
    """
    路径。
    
    :type: str
    """
    api_timeout: int = 1000
    """
    进行 API 调用时等待返回响应的超时时间。
    
    :type: int
    """
    app_secret: str = ''
    """
    机器人的 appSecret。
    
    :type: str
    """
