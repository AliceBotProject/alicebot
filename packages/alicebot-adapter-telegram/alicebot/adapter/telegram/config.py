"""Telegram 适配器配置"""

from typing import Literal, Optional

from alicebot.config import ConfigModel

__all__ = ["Config"]


class Config(ConfigModel):
    """Telegram 适配器配置

    Attributes:
        adapter_type: 适配器运行模式
        bot_token: 从 `BotFather` 获取的 token 值。
            参考：https://core.telegram.org/bots#how-do-i-create-a-bot
        api_server: 自定义 API 服务器
        webhook_host: 自定义 Webhook 服务器地址
        webhook_port: 自定义 Webhook 服务器端口
        webhook_url: 自定义 Webhook 服务器路径
        proxy: 代理服务器地址，为空时表示不使用代理
        api_timeout: 进行 API 调用时等待返回响应的超时时间。
    """

    __config_name__ = "telegram"
    adapter_type: Literal["polling", "webhook"] = "polling"
    bot_token: str = ""
    api_server: str = "https://api.telegram.org/"
    webhook_host: Optional[str] = "127.0.0.1"
    webhook_port: Optional[int] = 443
    webhook_url: Optional[str] = "/telegram"
    proxy: Optional[str] = None
    api_timeout: int = 2000
