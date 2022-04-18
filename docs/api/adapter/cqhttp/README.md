# alicebot.adapter.cqhttp

CQHTTP 协议适配器。

本适配器适配了 OneBot v11 协议。
协议详情请参考: [OneBot](https://github.com/howmanybots/onebot/blob/master/README.md) 。

## *class* `CQHTTPAdapter`(self, bot) {#CQHTTPAdapter}

Bases: `alicebot.adapter.Adapter`

CQHTTP 协议适配器。

在插件中可以直接使用 `self.adapter.xxx_api(**params)` 调用名称为 `xxx_api` 的 API，和调用 `call_api()` 方法相同。

- **Arguments**

  - **bot** (*Bot*)

- **Attributes**

  - **name** (*str*)

  - **app** (*aiohttp.web_app.Application*)

  - **runner** (*aiohttp.web_runner.AppRunner*)

  - **site** (*aiohttp.web_runner.TCPSite*)

  - **websocket** (*aiohttp.web_ws.WebSocketResponse*)

  - **api_response_cond** (*alicebot.utils.Condition*)

### *async method* `call_api(self, api, **params)` {#CQHTTPAdapter.call_api}

调用 CQHTTP API，协程会等待直到获得 API 响应。

- **Arguments**

  - **api** (*str*) - API 名称。

  - ****params** - API 参数。

- **Returns**

  Type: *Dict[str, Any]*

  API 响应中的 data 字段。

- **Raises**

  - **NetworkError** - 网络错误。

  - **ApiNotAvailable** - API 请求响应 404， API 不可用。

  - **ActionFailed** - API 请求响应 failed， API 操作失败。

  - **ApiTimeout** - API 请求响应超时。

### *readonly property* `config` {#CQHTTPAdapter.config}

本适配器的配置。

### *async method* `handle_cqhttp_event(self, msg)` {#CQHTTPAdapter.handle_cqhttp_event}

处理 CQHTTP 事件。

- **Arguments**

  - **msg** (*Dict[str, Any]*) - 接收到的信息。

### *async method* `handle_response(self, request)` {#CQHTTPAdapter.handle_response}

处理 aiohttp WebSocket 服务器的接收。

- **Arguments**

  - **request** (*aiohttp.web_request.Request*) - aiohttp WebSocket 服务器的 Request 对象。

### *async method* `run(self)` {#CQHTTPAdapter.run}

运行 aiohttp WebSocket 服务器。

### *async method* `send(self, message_, message_type, id_)` {#CQHTTPAdapter.send}

发送消息，调用 send_private_msg 或 send_group_msg API 发送消息。

- **Arguments**

  - **message_** (*Union[str, Mapping, Iterable[Mapping], CQHTTPMessageSegment, CQHTTPMessage]*) - 消息内容，可以是 str, Mapping, Iterable[Mapping], 'CQHTTPMessageSegment', 'CQHTTPMessage'。
  将使用 `CQHTTPMessage` 进行封装。

  - **message_type** (*Literal['private', 'group']*) - 消息类型。应该是 private 或者 group。

  - **id_** (*int*) - 发送对象的 ID ，QQ 号码或者群号码。

- **Returns**

  Type: *Dict[str, Any]*

  API 响应。

- **Raises**

  - **TypeError** - message_type 不是 'private' 或 'group'。

  - **...** - 同 `call_api()` 方法。

### *async method* `shutdown(self)` {#CQHTTPAdapter.shutdown}

清理 aiohttp AppRunner。

### *async method* `startup(self)` {#CQHTTPAdapter.startup}

创建 aiohttp Application。