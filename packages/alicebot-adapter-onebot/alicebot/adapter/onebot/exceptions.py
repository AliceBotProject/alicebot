"""OneBot 适配器异常。"""

from typing import Any

from alicebot.exceptions import AdapterException

__all__ = ["OneBotException", "NetworkError", "ActionFailed", "ApiTimeout"]


class OneBotException(AdapterException):
    """OneBot 异常基类。"""


class NetworkError(OneBotException):
    """网络异常。"""


class ActionFailed(OneBotException):
    """API 请求成功响应，但响应表示 API 操作失败。"""

    def __init__(self, resp: Any) -> None:
        """初始化。

        Args:
            resp: 返回的响应。
        """
        self.resp = resp


class ApiTimeout(OneBotException):
    """API 请求响应超时。"""
