"""CQHTTP 适配器异常。"""
from alicebot.exceptions import AdapterException


class CQHTTPException(AdapterException):
    """CQHTTP 异常基类。"""


class NetworkError(CQHTTPException):
    """网络异常。"""


class ActionFailed(CQHTTPException):
    """API 请求成功响应，但响应表示 API 操作失败。"""

    def __init__(self, resp):
        """
        Args:
            resp: 返回的响应。
        """
        self.resp = resp


class ApiNotAvailable(ActionFailed):
    """API 请求返回 404，表示当前请求的 API 不可用或不存在。"""


class ApiTimeout(CQHTTPException):
    """API 请求响应超时。"""
