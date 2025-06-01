"""Telegram 适配器异常。"""

from typing import Any

from alicebot.exceptions import AdapterException

__all__ = ["ActionFailed", "NetworkError", "TelegramException"]


class TelegramException(AdapterException):
    """Telegram 异常基类。"""


class NetworkError(TelegramException):
    """网络异常。"""


class ActionFailed(TelegramException):
    """API 请求成功响应，但响应表示 API 操作失败。"""

    def __init__(self, resp: Any) -> None:
        """初始化。

        Args:
            resp: 返回的响应。
        """
        super().__init__()
        self.resp = resp
