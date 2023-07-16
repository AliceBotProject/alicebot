# alicebot.adapter.onebot

OneBot 协议适配器。

本适配器适配了 OneBot v12 协议。
协议详情请参考: [OneBot](https://12.onebot.dev/) 。

## *class* `OneBotAdapter`(self, bot) {#OneBotAdapter}

Bases: `alicebot.adapter.utils.WebSocketAdapter`

OneBot 协议适配器。

- **Arguments**

  - **bot** (*Bot*) - 当前机器人对象。

- **Attributes**

  - **event_models** (*ClassVar[Dict[Tuple[Optional[str], Optional[str], Optional[str]], Type[alicebot.adapter.onebot.event.OntBotEvent]]]*)

### *class* `Config`(__pydantic_self__, **data) {#Config}

Bases: `alicebot.config.ConfigModel`

OneBot 配置类，将在适配器被加载时被混入到机器人主配置中。

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

### *class method* `add_event_model(cls, event_model)` {#OneBotAdapter.add_event_model}

添加自定义事件模型，事件模型类必须继承于 `OntBotEvent`。

- **Arguments**

  - **event_model** (*Type[alicebot.adapter.onebot.event.OntBotEvent]*) - 事件模型类。

- **Returns**

  Type: *None*

### *async method* `call_api(self, api, bot_self, **params)` {#OneBotAdapter.call_api}

调用 OneBot API ，协程会等待直到获得 API 响应。

- **Arguments**

  - **api** (*str*) - API 名称。

  - **bot_self** (*alicebot.adapter.onebot.event.BotSelf*) - `Self` 字段。

  - ****params** (*Any*) - API 参数。

- **Returns**

  Type: *Any*

  API 响应中的 data 字段。

- **Raises**

  - **NetworkError** - 网络错误。

  - **ApiNotAvailable** - API 请求响应 404 ， API 不可用。

  - **ActionFailed** - API 请求响应 failed ， API 操作失败。

  - **ApiTimeout** - API 请求响应超时。

### *class method* `get_event_model(cls, post_type, detail_type, sub_type)` {#OneBotAdapter.get_event_model}

根据接收到的消息类型返回对应的事件类。

- **Arguments**

  - **post_type** (*Optional[str]*) - 请求类型。

  - **detail_type** (*Optional[str]*) - 事件类型。

  - **sub_type** (*Optional[str]*) - 子类型。

- **Returns**

  Type: *Type[alicebot.adapter.onebot.event.OntBotEvent]*

  对应的事件类。

### *async method* `handle_onebot_event(self, msg)` {#OneBotAdapter.handle_onebot_event}

处理 OneBot 事件。

- **Arguments**

  - **msg** (*Dict[str, Any]*) - 接收到的信息。

### *async method* `handle_websocket_msg(self, msg)` {#OneBotAdapter.handle_websocket_msg}

处理 WebSocket 消息。

- **Arguments**

  - **msg** (*aiohttp.http_websocket.WSMessage*)

### *async method* `reverse_ws_connection_hook(self)` {#OneBotAdapter.reverse_ws_connection_hook}

反向 WebSocket 连接建立时的钩子函数。

### *async method* `send(self, message_, message_type, id_)` {#OneBotAdapter.send}

发送消息，调用 `send_message` API 发送消息。

- **Arguments**

  - **message_** (*T_OBMSG*) - 消息内容，可以是 `str`, `Mapping`, `Iterable[Mapping]`,
  `OneBotMessageSegment`, `OneBotMessage`。
  将使用 `OneBotMessage` 进行封装。

  - **message_type** (*Union[Literal['private', 'group'], str]*) - 消息类型。
  可以为 "private", "group" 或扩展的类型，和消息事件的 `detail_type` 字段对应。

  - **id_** (*str*) - 发送对象的 ID ， QQ 号码或者群号码。

- **Returns**

  Type: *Any*

  API 响应。

- **Raises**

  - **TypeError** - message_type 不是 "private" 或 "group"。

  - **...** - 同 `call_api()` 方法。

### *async method* `startup(self)` {#OneBotAdapter.startup}

初始化适配器。

### *async method* `websocket_connect(self)` {#OneBotAdapter.websocket_connect}

创建正向 WebSocket 连接。