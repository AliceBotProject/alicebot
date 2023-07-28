# alicebot.adapter.mirai

Mirai 协议适配器。

本适配器适配了 mirai-api-http 协议，仅支持 mirai-api-http 2.3.0 及以上版本。
本适配器支持 mirai-api-http 的 Websocket Adapter 模式和 Reverse Websocket Adapter 模式。
协议详情请参考: [mirai-api-http](https://github.com/project-mirai/mirai-api-http) 。

## *class* `MiraiAdapter`(self, bot) {#MiraiAdapter}

Bases: `alicebot.adapter.utils.WebSocketAdapter`

Mirai 协议适配器。

在插件中可以直接使用 `self.adapter.xxx_api(**params)` 调用名称为 `xxx_api` 的 API ，
和调用 `call_api()` 方法相同。

- **Arguments**

  - **bot** (*Bot*) - 当前机器人对象。

- **Attributes**

  - **name** (*str*)

  - **event_models** (*ClassVar[Dict[str, Type[alicebot.adapter.mirai.event.base.MiraiEvent]]]*)

### *class* `Config`(__pydantic_self__, **data) {#Config}

Bases: `alicebot.config.ConfigModel`

Mirai 配置类，将在适配器被加载时被混入到机器人主配置中。

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **adapter_type** (*Literal['ws', 'reverse-ws']*) - 适配器类型，需要和协议端配置相同。

  - **host** (*str*) - 本机域名。

  - **port** (*int*) - 监听的端口。

  - **url** (*str*) - WebSocket 路径，需要和协议端配置相同。

  - **reconnect_interval** (*int*) - 重连等待时间。

  - **api_timeout** (*int*) - 进行 API 调用时等待返回响应的超时时间。

  - **verify_key** (*str*) - 建立连接时的认证密钥，需要和 mirai-api-http 配置中的 `verifyKey` 相同，如果关闭验证则留空。

  - **qq** (*int*) - 机器人的 QQ 号码，必须指定。

### *async method* `call_api(self, command, sub_command = None, **content)` {#MiraiAdapter.call_api}

调用 Mirai API ，协程会等待直到获得 API 响应。

- **Arguments**

  - **command** (*str*) - 命令字。

  - **sub_command** (*Optional[str]*) - 子命令字。

  - ****content** (*Any*) - 请求内容。

- **Returns**

  Type: *Any*

  API 响应中的 data 字段，即 Mirai-api-http API 通用接口中的内容。

- **Raises**

  - **NetworkError** - 网络错误。

  - **ActionFailed** - API 操作失败。

  - **ApiTimeout** - API 请求响应超时。

### *class method* `get_event_model(cls, event_type)` {#MiraiAdapter.get_event_model}

根据接收到的消息类型返回对应的事件类。

- **Arguments**

  - **event_type** (*str*) - 事件类型。

- **Returns**

  Type: *Type[alicebot.adapter.mirai.event.base.MiraiEvent]*

  对应的事件类。

### *async method* `handle_mirai_event(self, msg)` {#MiraiAdapter.handle_mirai_event}

处理 Mirai 事件。

- **Arguments**

  - **msg** (*Dict[str, Any]*) - 接收到的信息。

### *async method* `handle_websocket_msg(self, msg)` {#MiraiAdapter.handle_websocket_msg}

处理 WebSocket 消息。

- **Arguments**

  - **msg** (*aiohttp.http_websocket.WSMessage*)

### *async method* `reverse_ws_connection_hook(self)` {#MiraiAdapter.reverse_ws_connection_hook}

反向 WebSocket 连接建立时的钩子函数。

### *async method* `send(self, message_, message_type, target, quote = None)` {#MiraiAdapter.send}

调用 Mirai API 发送消息。

- **Arguments**

  - **message_** (*T_MiraiMSG*) - 消息内容，可以是 `str`, `Mapping`, `Iterable[Mapping]`,
  `MiraiMessageSegment`, `MiraiMessage`。
  将使用 `MiraiMessage` 进行封装。

  - **message_type** (*Literal['private', 'friend', 'group']*) - 消息类型。应该是 "private", "friend" 或者 "group"。其中 "private" 和 "friend" 相同。

  - **target** (*int*) - 发送对象的 ID ， QQ 号码或者群号码。

  - **quote** (*Optional[int]*) - 引用的消息的 `messageId`。默认为 `None`，不引用任何消息。

- **Returns**

  Type: *Any*

  API 响应。

- **Raises**

  - **TypeError** - message_type 非法。

  - **...** - 同 `call_api()` 方法。

### *async method* `startup(self)` {#MiraiAdapter.startup}

初始化适配器。

### *async method* `verify_identity(self)` {#MiraiAdapter.verify_identity}

验证身份，创建与 Mirai-api-http 的连接。

### *async method* `websocket_connect(self)` {#MiraiAdapter.websocket_connect}

创建正向 WebSocket 连接。