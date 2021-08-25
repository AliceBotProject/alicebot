"""
============
DingTalk 异常
============
"""
from alicebot.exception import AdapterException, AdapterTimeout


class DingTalkException(AdapterException):
    """
    DingTalk 异常基类。
    """
    pass


class NetworkError(DingTalkException):
    """
    网络异常。
    """
    pass


class WebhookExpiredError(DingTalkException):
    """
    Webhook 地址已到期。
    """
    pass


class ApiTimeout(DingTalkException, AdapterTimeout):
    """
    API 请求响应超时。
    """
    pass
