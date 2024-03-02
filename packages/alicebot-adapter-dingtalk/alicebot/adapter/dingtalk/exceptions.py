"""DingTalk 适配器异常。"""

from alicebot.exceptions import AdapterException

__all__ = ["DingTalkException", "NetworkError", "WebhookExpiredError"]


class DingTalkException(AdapterException):
    """DingTalk 异常基类。"""


class NetworkError(DingTalkException):
    """网络异常。"""


class WebhookExpiredError(DingTalkException):
    """Webhook 地址已到期。"""
