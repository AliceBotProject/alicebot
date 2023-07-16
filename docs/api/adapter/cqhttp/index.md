# alicebot.adapter.cqhttp

CQHTTP 协议适配器。

本适配器适配了 OneBot v11 协议。
协议详情请参考: [OneBot](https://github.com/howmanybots/onebot/blob/master/README.md) 。

## *class* `CQHTTPAdapter`(self, bot) {#CQHTTPAdapter}

Bases: `alicebot.adapter.utils.WebSocketAdapter`

CQHTTP 协议适配器。

- **Arguments**

  - **bot** (*Bot*) - 当前机器人对象。

- **Attributes**

  - **event_models** (*ClassVar[Dict[Tuple[Optional[str], Optional[str], Optional[str]], Type[alicebot.adapter.cqhttp.event.CQHTTPEvent]]]*)

### *class* `Config`(__pydantic_self__, **data) {#Config}

Bases: `alicebot.config.ConfigModel`

CQHTTP 配置类，将在适配器被加载时被混入到机器人主配置中。

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **adapter_type** (*Literal['ws', 'reverse-ws', 'ws-reverse']*) - 适配器类型，需要和协议端配置相同。

  - **host** (*str*) - 本机域名。

  - **port** (*int*) - 监听的端口。

  - **url** (*str*) - WebSocket 路径，需和协议端配置相同。

  - **reconnect_interval** (*int*) - 重连等待时间。

  - **api_timeout** (*int*) - 进行 API 调用时等待返回响应的超时时间。

  - **access_token** (*str*) - 鉴权。

### *class method* `add_event_model(cls, event_model)` {#CQHTTPAdapter.add_event_model}

添加自定义事件模型，事件模型类必须继承于 `CQHTTPEvent`。

- **Arguments**

  - **event_model** (*Type[alicebot.adapter.cqhttp.event.CQHTTPEvent]*) - 事件模型类。

- **Returns**

  Type: *None*

### *async method* `call_api(self, api, **params)` {#CQHTTPAdapter.call_api}

调用 CQHTTP API ，协程会等待直到获得 API 响应。

- **Arguments**

  - **api** (*str*) - API 名称。

  - ****params** (*Any*) - API 参数。

- **Returns**

  Type: *Any*

  API 响应中的 data 字段。

- **Raises**

  - **NetworkError** - 网络错误。

  - **ApiNotAvailable** - API 请求响应 404 ， API 不可用。

  - **ActionFailed** - API 请求响应 failed ， API 操作失败。

  - **ApiTimeout** - API 请求响应超时。

### *class method* `get_event_model(cls, post_type, detail_type, sub_type)` {#CQHTTPAdapter.get_event_model}

根据接收到的消息类型返回对应的事件类。

- **Arguments**

  - **post_type** (*Optional[str]*) - 请求类型。

  - **detail_type** (*Optional[str]*) - 事件类型。

  - **sub_type** (*Optional[str]*) - 子类型。

- **Returns**

  Type: *Type[alicebot.adapter.cqhttp.event.CQHTTPEvent]*

  对应的事件类。

### *async method* `handle_cqhttp_event(self, msg)` {#CQHTTPAdapter.handle_cqhttp_event}

处理 CQHTTP 事件。

- **Arguments**

  - **msg** (*Dict[str, Any]*) - 接收到的信息。

### *async method* `handle_websocket_msg(self, msg)` {#CQHTTPAdapter.handle_websocket_msg}

处理 WebSocket 消息。

- **Arguments**

  - **msg** (*aiohttp.http_websocket.WSMessage*)

### *async method* `reverse_ws_connection_hook(self)` {#CQHTTPAdapter.reverse_ws_connection_hook}

反向 WebSocket 连接建立时的钩子函数。

### *async method* `send(self, message_, message_type, id_)` {#CQHTTPAdapter.send}

发送消息，调用 `send_private_msg` 或 `send_group_msg` API 发送消息。

- **Arguments**

  - **message_** (*T_CQMSG*) - 消息内容，可以是 `str`, `Mapping`, `Iterable[Mapping]`,
  `CQHTTPMessageSegment`, `CQHTTPMessage。`
  将使用 `CQHTTPMessage` 进行封装。

  - **message_type** (*Literal['private', 'group']*) - 消息类型。应该是 "private" 或者 "group"。

  - **id_** (*int*) - 发送对象的 ID ， QQ 号码或者群号码。

- **Returns**

  Type: *Any*

  API 响应。

- **Raises**

  - **TypeError** - `message_type` 不是 "private" 或 "group"。

  - **...** - 同 `call_api()` 方法。

### *async method* `startup(self)` {#CQHTTPAdapter.startup}

初始化适配器。

### *async method* `websocket_connect(self)` {#CQHTTPAdapter.websocket_connect}

创建正向 WebSocket 连接。