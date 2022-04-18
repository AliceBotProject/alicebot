# alicebot.adapter.mirai

Mirai 协议适配器。

本适配器适配了 mirai-api-http 协议，仅支持 mirai-api-http 2.0 及以上版本。
本适配器支持 mirai-api-http 的 Websocket Adapter 模式和 Reverse Websocket Adapter 模式。
协议详情请参考: [mirai-api-http](https://github.com/project-mirai/mirai-api-http) 。

## *class* `MiraiAdapter`(self, bot) {#MiraiAdapter}

Bases: `alicebot.adapter.Adapter`

Mirai 协议适配器。

在插件中可以直接使用 `self.adapter.xxx_api(**params)` 调用名称为 `xxx_api` 的 API，和调用 `call_api()` 方法相同。

- **Arguments**

  - **bot** (*Bot*)

- **Attributes**

  - **name** (*str*)

  - **websocket** (*Union[aiohttp.web_ws.WebSocketResponse, aiohttp.client_ws.ClientWebSocketResponse]*)

  - **session** (*aiohttp.client.ClientSession*)

  - **app** (*aiohttp.web_app.Application*)

  - **runner** (*aiohttp.web_runner.AppRunner*)

  - **site** (*aiohttp.web_runner.TCPSite*)

  - **api_response_cond** (*alicebot.utils.Condition*)

### *async method* `call_api(self, command, sub_command = None, **content)` {#MiraiAdapter.call_api}

调用 Mirai API，协程会等待直到获得 API 响应。

- **Arguments**

  - **command** (*str*) - 命令字。

  - **sub_command** (*Optional[str]*) - 子命令字。

  - ****content** - 请求内容。

- **Returns**

  Type: *Dict[str, Any]*

  API 响应中的 data 字段，即 Mirai-api-http API 通用接口中的内容。

- **Raises**

  - **NetworkError** - 网络错误。

  - **ActionFailed** - API 操作失败。

  - **ApiTimeout** - API 请求响应超时。

### *readonly property* `config` {#MiraiAdapter.config}

本适配器的配置。

### *async method* `handle_mirai_event(self, msg)` {#MiraiAdapter.handle_mirai_event}

处理 Mirai 事件。

- **Arguments**

  - **msg** (*Dict[str, Any]*) - 接收到的信息。

### *async method* `handle_non_standard_response(self, data)` {#MiraiAdapter.handle_non_standard_response}

处理 Mirai 返回的非标准响应。

- **Arguments**

  - **data** (*Union[str, Dict[str, Any]]*) - 接收到的信息。

### *async method* `handle_response(self, request)` {#MiraiAdapter.handle_response}

处理 aiohttp WebSocket 服务器的接收。

- **Arguments**

  - **request** (*aiohttp.web_request.Request*) - aiohttp WebSocket 服务器的 Request 对象。

### *async method* `handle_websocket_msg(self)` {#MiraiAdapter.handle_websocket_msg}

处理 WebSocket 消息。

### *async method* `run(self)` {#MiraiAdapter.run}

运行适配器。

### *async method* `send(self, message_, message_type, target, quote = None)` {#MiraiAdapter.send}

调用 Mirai API 发送消息。

- **Arguments**

  - **message_** (*Union[str, Mapping, Iterable[Mapping], MiraiMessageSegment, MiraiMessage]*) - 消息内容，可以是 str, Mapping, Iterable[Mapping], 'MiraiMessageSegment', 'MiraiMessage'。
  将使用 `MiraiMessage` 进行封装。

  - **message_type** (*Literal['private', 'friend', 'group']*) - 消息类型。应该是 private, friend 或者 group。其中 private 和 friend 相同。

  - **target** (*int*) - 发送对象的 ID ，QQ 号码或者群号码。

  - **quote** (*int*) - 引用的消息的 messageId。默认为 `None` ，不引用任何消息。

- **Returns**

  Type: *Dict[str, Any]*

  API 响应。

- **Raises**

  - **TypeError** - message_type 非法。

  - **...** - 同 `call_api()` 方法。

### *async method* `shutdown(self)` {#MiraiAdapter.shutdown}

关闭并清理连接。

### *async method* `startup(self)` {#MiraiAdapter.startup}

初始化适配器。

### *async method* `verify_identity(self)` {#MiraiAdapter.verify_identity}

验证身份，创建与 Mirai-api-http 的连接。

### *async method* `websocket_connect(self)` {#MiraiAdapter.websocket_connect}

创建正向 WebSocket 连接。