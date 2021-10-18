"""
============
Mirai 异常
============
"""
from alicebot.exceptions import AdapterException, AdapterTimeout


class MiraiException(AdapterException):
    """
    Mirai 异常基类。
    """
    pass


class NetworkError(MiraiException):
    """
    网络异常。
    """
    pass


class ActionFailed(MiraiException):
    """
    API 请求成功响应，但响应表示 API 操作失败。
    :param resp: 返回的响应。
    """

    def __init__(self, code, resp):
        self.code = code
        self.resp = resp


class ApiTimeout(MiraiException, AdapterTimeout):
    """
    API 请求响应超时。
    """
    pass
