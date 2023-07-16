# alicebot.log

AliceBot 日志。

AliceBot 使用 [loguru](https://github.com/Delgan/loguru) 来记录日志信息。
自定义 logger 请参考 [loguru](https://github.com/Delgan/loguru) 文档。

## *function* `error_or_exception(message, exception, verbose)` {#error_or_exception}

输出 error 或者 exception 日志。

- **Arguments**

  - **message** (*str*) - 消息。

  - **exception** (*Exception*) - 异常。

  - **verbose** (*bool*) - 是否使用 exception。