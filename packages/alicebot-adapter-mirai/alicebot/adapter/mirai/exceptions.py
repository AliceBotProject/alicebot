"""Mirai 适配器异常。"""

from typing import Any, Dict

from alicebot.exceptions import AdapterException

__all__ = ["MiraiException", "NetworkError", "ActionFailed", "ApiTimeout"]


class MiraiException(AdapterException):
    """Mirai 异常基类。"""


class NetworkError(MiraiException):
    """网络异常。"""


class ActionFailed(MiraiException):
    """API 请求成功响应，但响应表示 API 操作失败。"""

    def __init__(self, code: int, resp: Dict[str, Any]) -> None:
        """初始化。

        Args:
            code: 错误代码。
            resp: 返回的响应。
        """
        self.code = code
        self.resp = resp


class ApiTimeout(MiraiException):
    """API 请求响应超时。"""
