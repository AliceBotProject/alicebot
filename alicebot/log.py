"""AliceBot 日志。

AliceBot 使用 [structlog](https://www.structlog.org/) 来记录日志信息。
自定义 logger 请参考 [structlog](https://www.structlog.org/) 文档。

请注意，此模块已经被弃用，并将在 v0.10.0 版本中被移除。
请迁移到使用 `logger = structlog.stdlib.get_logger()`。
"""

import warnings

import structlog

__all__ = ["logger"]

logger = structlog.stdlib.get_logger()

warnings.warn(
    '"from alicebot.log import logger" is deprecated',
    DeprecationWarning,
    stacklevel=1,
)
