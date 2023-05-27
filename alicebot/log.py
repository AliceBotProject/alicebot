"""AliceBot 日志。

AliceBot 使用 [loguru](https://github.com/Delgan/loguru) 来记录日志信息。
自定义 logger 请参考 [loguru](https://github.com/Delgan/loguru) 文档。
"""
from loguru import logger as _logger

logger = _logger


def error_or_exception(message: str, exception: Exception, verbose: bool):
    """输出 error 或者 exception 日志。

    Args:
        message: 消息。
        exception: 异常。
        verbose: 是否使用 exception。
    """
    if verbose:
        logger.exception(message)
    else:
        logger.error(f"{message} {exception!r}")
