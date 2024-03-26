# alicebot.adapter.onebot

OneBot 协议适配器。

本适配器适配了 OneBot v12 协议。
协议详情请参考：[OneBot](https://12.onebot.dev/)。

## _class_ `OneBotAdapter` {#OneBotAdapter}

Bases: `alicebot.adapter.utils.WebSocketAdapter`

OneBot 协议适配器。

- **Attributes**

  - **event\_models** (_ClassVar\[Dict\[Tuple\[Optional\[str\], Optional\[str\], Optional\[str\]\], Type\[alicebot.adapter.onebot.event.OntBotEvent\]\]\]_)

### _class_ `Config` {#Config}

Bases: `alicebot.config.ConfigModel`

OneBot 配置类，将在适配器被加载时被混入到机器人主配置中。

- **Attributes**

  - **adapter\_type** (_Literal\['ws', 'reverse-ws', 'ws-reverse'\]_) - 适配器类型，需要和协议端配置相同。

  - **host** (_str_) - 本机域名。

  - **port** (_int_) - 监听的端口。

  - **url** (_str_) - WebSocket 路径，需和协议端配置相同。

  - **reconnect\_interval** (_int_) - 重连等待时间。

  - **api\_timeout** (_int_) - 进行 API 调用时等待返回响应的超时时间。

  - **access\_token** (_str_) - 鉴权。

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

### _method_ `add_event_model(event_model)` {#OneBotAdapter-add-event-model}

添加自定义事件模型，事件模型类必须继承于 `OntBotEvent`。

- **Returns**

  Type: _None_

### _async method_ `call_api(self, api, bot_self, **params)` {#OneBotAdapter-call-api}

调用 OneBot API，协程会等待直到获得 API 响应。

- **Arguments**

  - **api** (_str_) - API 名称。

  - **bot\_self** (_alicebot.adapter.onebot.event.BotSelf_) - `Self` 字段。

  - **\*\*params** (_Any_) - API 参数。

- **Returns**

  Type: _Any_

  API 响应中的 data 字段。

- **Raises**

  - **NetworkError** - 网络错误。

  - **ApiNotAvailable** - API 请求响应 404， API 不可用。

  - **ActionFailed** - API 请求响应 failed， API 操作失败。

  - **ApiTimeout** - API 请求响应超时。

### _method_ `get_event_model(post_type, detail_type, sub_type)` {#OneBotAdapter-get-event-model}

根据接收到的消息类型返回对应的事件类。

- **Arguments**

  - **detail\_type** (_Optional\[str\]_) - 事件类型。

  - **sub\_type** (_Optional\[str\]_) - 子类型。

- **Returns**

  Type: _Type\[alicebot.adapter.onebot.event.OntBotEvent\]_

  对应的事件类。

### _async method_ `handle_onebot_event(self, msg)` {#OneBotAdapter-handle-onebot-event}

处理 OneBot 事件。

- **Arguments**

  - **msg** (_Dict\[str, Any\]_) - 接收到的信息。

- **Returns**

  Type: _None_

### _async method_ `handle_websocket_msg(self, msg)` {#OneBotAdapter-handle-websocket-msg}

处理 WebSocket 消息。

- **Arguments**

  - **msg** (_aiohttp.http\_websocket.WSMessage_)

- **Returns**

  Type: _None_

### _async method_ `reverse_ws_connection_hook(self)` {#OneBotAdapter-reverse-ws-connection-hook}

反向 WebSocket 连接建立时的钩子函数。

- **Returns**

  Type: _None_

### _async method_ `send(self, message_, message_type, id_)` {#OneBotAdapter-send}

发送消息，调用 `send_message` API 发送消息。

- **Arguments**

  - **message\_** (_Union\[List\[alicebot.adapter.onebot.message.OneBotMessageSegment\], alicebot.adapter.onebot.message.OneBotMessageSegment, str, Mapping\[str, Any\]\]_) - 消息内容，可以是 `str`, `Mapping`, `Iterable[Mapping]`,
  `OneBotMessageSegment`, `OneBotMessage`。
  将使用 `OneBotMessage` 进行封装。

  - **message\_type** (_Union\[Literal\['private', 'group'\], str\]_) - 消息类型。
  可以为 "private", "group" 或扩展的类型，和消息事件的 `detail_type` 字段对应。

  - **id\_** (_str_) - 发送对象的 ID， QQ 号码或者群号码。

- **Returns**

  Type: _Any_

  API 响应。

- **Raises**

  - **TypeError** - message_type 不是 "private" 或 "group"。

  - **...** - 同 `call_api()` 方法。

### _async method_ `startup(self)` {#OneBotAdapter-startup}

初始化适配器。

- **Returns**

  Type: _None_

### _async method_ `websocket_connect(self)` {#OneBotAdapter-websocket-connect}

创建正向 WebSocket 连接。

- **Returns**

  Type: _None_
