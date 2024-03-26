# alicebot.adapter.mirai

Mirai 协议适配器。

本适配器适配了 mirai-api-http 协议，仅支持 mirai-api-http 2.3.0 及以上版本。
本适配器支持 mirai-api-http 的 Websocket Adapter 模式和 Reverse Websocket Adapter 模式。
协议详情请参考：[mirai-api-http](https://github.com/project-mirai/mirai-api-http)。

## _class_ `MiraiAdapter` {#MiraiAdapter}

Bases: `alicebot.adapter.utils.WebSocketAdapter`

Mirai 协议适配器。

在插件中可以直接使用 `self.adapter.xxx_api(**params)` 调用名称为 `xxx_api` 的 API，
和调用 `call_api()` 方法相同。

- **Attributes**

  - **name** (_str_)

  - **event\_models** (_ClassVar\[Dict\[str, Type\[alicebot.adapter.mirai.event.base.MiraiEvent\]\]\]_)

### _class_ `Config` {#Config}

Bases: `alicebot.config.ConfigModel`

Mirai 配置类，将在适配器被加载时被混入到机器人主配置中。

- **Attributes**

  - **adapter\_type** (_Literal\['ws', 'reverse-ws'\]_) - 适配器类型，需要和协议端配置相同。

  - **host** (_str_) - 本机域名。

  - **port** (_int_) - 监听的端口。

  - **url** (_str_) - WebSocket 路径，需要和协议端配置相同。

  - **reconnect\_interval** (_int_) - 重连等待时间。

  - **api\_timeout** (_int_) - 进行 API 调用时等待返回响应的超时时间。

  - **verify\_key** (_str_) - 建立连接时的认证密钥，需要和 mirai-api-http 配置中的 `verifyKey` 相同，如果关闭验证则留空。

  - **qq** (_int_) - 机器人的 QQ 号码，必须指定。

#### _method_ `__init__(self, /, **data)` {#BaseModel---init--}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

### _method_ `__init__(self, bot)` {#Adapter---init--}

初始化。

- **Arguments**

  - **bot** (_Bot_) - 当前机器人对象。

- **Returns**

  Type: _None_

### _async method_ `call_api(self, command, sub_command = None, **content)` {#MiraiAdapter-call-api}

调用 Mirai API，协程会等待直到获得 API 响应。

- **Arguments**

  - **command** (_str_) - 命令字。

  - **sub\_command** (_Optional\[str\]_) - 子命令字。

  - **\*\*content** (_Any_) - 请求内容。

- **Returns**

  Type: _Any_

  API 响应中的 data 字段，即 Mirai-api-http API 通用接口中的内容。

- **Raises**

  - **NetworkError** - 网络错误。

  - **ActionFailed** - API 操作失败。

  - **ApiTimeout** - API 请求响应超时。

### _method_ `get_event_model(event_type)` {#MiraiAdapter-get-event-model}

根据接收到的消息类型返回对应的事件类。

- **Returns**

  Type: _Type\[alicebot.adapter.mirai.event.base.MiraiEvent\]_

  对应的事件类。

### _async method_ `handle_mirai_event(self, msg)` {#MiraiAdapter-handle-mirai-event}

处理 Mirai 事件。

- **Arguments**

  - **msg** (_Dict\[str, Any\]_) - 接收到的信息。

- **Returns**

  Type: _None_

### _async method_ `handle_websocket_msg(self, msg)` {#MiraiAdapter-handle-websocket-msg}

处理 WebSocket 消息。

- **Arguments**

  - **msg** (_aiohttp.http\_websocket.WSMessage_)

- **Returns**

  Type: _None_

### _async method_ `reverse_ws_connection_hook(self)` {#MiraiAdapter-reverse-ws-connection-hook}

反向 WebSocket 连接建立时的钩子函数。

- **Returns**

  Type: _None_

### _async method_ `send(self, message_, message_type, target, quote = None)` {#MiraiAdapter-send}

调用 Mirai API 发送消息。

- **Arguments**

  - **message\_** (_Union\[List\[alicebot.adapter.mirai.message.MiraiMessageSegment\], alicebot.adapter.mirai.message.MiraiMessageSegment, str, Mapping\[str, Any\]\]_) - 消息内容，可以是 `str`, `Mapping`, `Iterable[Mapping]`,
  `MiraiMessageSegment`, `MiraiMessage`。
  将使用 `MiraiMessage` 进行封装。

  - **message\_type** (_Literal\['private', 'friend', 'group'\]_) - 消息类型。应该是 "private", "friend" 或者 "group"。其中 "private" 和 "friend" 相同。

  - **target** (_int_) - 发送对象的 ID， QQ 号码或者群号码。

  - **quote** (_Optional\[int\]_) - 引用的消息的 `messageId`。默认为 `None`，不引用任何消息。

- **Returns**

  Type: _Any_

  API 响应。

- **Raises**

  - **TypeError** - message_type 非法。

  - **...** - 同 `call_api()` 方法。

### _async method_ `startup(self)` {#MiraiAdapter-startup}

初始化适配器。

- **Returns**

  Type: _None_

### _async method_ `verify_identity(self)` {#MiraiAdapter-verify-identity}

验证身份，创建与 Mirai-api-http 的连接。

- **Returns**

  Type: _None_

### _async method_ `websocket_connect(self)` {#MiraiAdapter-websocket-connect}

创建正向 WebSocket 连接。

- **Returns**

  Type: _None_
