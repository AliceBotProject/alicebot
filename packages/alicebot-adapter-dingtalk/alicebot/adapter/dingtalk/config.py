"""DingTalk 适配器配置。"""

from alicebot.config import ConfigModel

__all__ = ["Config"]


class Config(ConfigModel):
    """DingTalk 配置类，将在适配器被加载时被混入到机器人主配置中。

    Attributes:
        host: 本机域名。
        port: 监听的端口。
        url: 路径。
        api_timeout: 进行 API 调用时等待返回响应的超时时间。
        app_secret: 机器人的 `appSecret`。
    """

    __config_name__ = "dingtalk"
    host: str = "127.0.0.1"
    port: int = 8080
    url: str = "/dingtalk"
    api_timeout: int = 1000
    app_secret: str = ""
