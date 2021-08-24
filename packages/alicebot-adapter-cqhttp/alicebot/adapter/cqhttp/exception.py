"""
============
CQHTTP 异常
============
"""
from alicebot.exception import AdapterException, AdapterTimeout


class CQHTTPException(AdapterException):
    """
    CQHTTP 异常基类。
    """
    pass


class NetworkError(CQHTTPException):
    """
    网络异常。
    """
    pass


class ActionFailed(CQHTTPException):
    """
    API 请求成功响应，但响应表示 API 操作失败。
    :param resp: 返回的响应。
    """

    def __init__(self, resp):
        self.resp = resp


class ApiNotAvailable(ActionFailed):
    """
    API 请求返回 404，表示当前请求的 API 不可用或不存在。
    """


class ApiTimeout(CQHTTPException, AdapterTimeout):
    """
    API 请求响应超时。
    """
    pass
