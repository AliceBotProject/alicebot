"""AliceBot 日志。

AliceBot 使用 [loguru](https://github.com/Delgan/loguru) 来记录日志信息。
自定义 logger 请参考 [loguru](https://github.com/Delgan/loguru) 文档。
"""
from loguru import logger as _logger

logger = _logger


def error_or_exception(message: str, exception: Exception, verbose: bool):
    if verbose:
        logger.exception(message)
    else:
        logger.error(f"{message} {exception!r}")
