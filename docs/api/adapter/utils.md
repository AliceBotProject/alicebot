# alicebot.adapter.utils

适配器实用工具。

这里定义了一些在编写适配器时常用的基类，适配器开发者可以直接继承自这里的类或者用作参考。

## *abstract class* `PollingAdapter`(self, bot) {#PollingAdapter}

Bases: `alicebot.adapter.Adapter`

轮询式适配器示例。

- **Arguments**

  - **bot** (*Bot*) - 当前机器人对象。

- **Attributes**

  - **delay** (*float*)

  - **create_task** (*bool*)

### *async method* `on_tick(self)` {#PollingAdapter.on_tick}

当轮询发生。

### *async method* `run(self)` {#PollingAdapter.run}

运行适配器。

## *abstract class* `HttpClientAdapter`(self, bot) {#HttpClientAdapter}

Bases: `alicebot.adapter.utils.PollingAdapter`

HTTP 客户端适配器示例。

- **Arguments**

  - **bot** (*Bot*) - 当前机器人对象。

- **Attributes**

  - **session** (*aiohttp.client.ClientSession*)

### *async method* `on_tick(self)` {#HttpClientAdapter.on_tick}

当轮询发生。

### *async method* `shutdown(self)` {#HttpClientAdapter.shutdown}

关闭并清理连接。

### *async method* `startup(self)` {#HttpClientAdapter.startup}

初始化适配器。

## *abstract class* `WebSocketClientAdapter`(self, bot) {#WebSocketClientAdapter}

Bases: `alicebot.adapter.Adapter`

WebSocket 客户端适配器示例。

- **Arguments**

  - **bot** (*Bot*) - 当前机器人对象。

- **Attributes**

  - **url** (*str*)

### *async method* `handle_response(self, msg)` {#WebSocketClientAdapter.handle_response}

处理响应。

- **Arguments**

  - **msg** (*aiohttp.http_websocket.WSMessage*)

### *async method* `run(self)` {#WebSocketClientAdapter.run}

运行适配器。

## *abstract class* `HttpServerAdapter`(self, bot) {#HttpServerAdapter}

Bases: `alicebot.adapter.Adapter`

HTTP 服务端适配器示例。

- **Arguments**

  - **bot** (*Bot*) - 当前机器人对象。

- **Attributes**

  - **app** (*aiohttp.web_app.Application*)

  - **runner** (*aiohttp.web_runner.AppRunner*)

  - **site** (*aiohttp.web_runner.TCPSite*)

  - **host** (*str*)

  - **port** (*int*)

  - **get_url** (*str*)

  - **post_url** (*str*)

### *async method* `handle_response(self, request)` {#HttpServerAdapter.handle_response}

处理响应。

- **Arguments**

  - **request** (*aiohttp.web_request.Request*)

- **Returns**

  Type: *aiohttp.web_response.StreamResponse*

### *async method* `run(self)` {#HttpServerAdapter.run}

运行适配器。

### *async method* `shutdown(self)` {#HttpServerAdapter.shutdown}

关闭并清理连接。

### *async method* `startup(self)` {#HttpServerAdapter.startup}

初始化适配器。

## *abstract class* `WebSocketServerAdapter`(self, bot) {#WebSocketServerAdapter}

Bases: `alicebot.adapter.Adapter`

WebSocket 服务端适配器示例。

- **Arguments**

  - **bot** (*Bot*) - 当前机器人对象。

- **Attributes**

  - **app** (*aiohttp.web_app.Application*)

  - **runner** (*aiohttp.web_runner.AppRunner*)

  - **site** (*aiohttp.web_runner.TCPSite*)

  - **websocket** (*aiohttp.web_ws.WebSocketResponse*)

  - **host** (*str*)

  - **port** (*int*)

  - **url** (*str*)

### *async method* `handle_response(self, request)` {#WebSocketServerAdapter.handle_response}

处理 WebSocket。

- **Arguments**

  - **request** (*aiohttp.web_request.Request*)

- **Returns**

  Type: *aiohttp.web_ws.WebSocketResponse*

### *async method* `handle_ws_response(self, msg)` {#WebSocketServerAdapter.handle_ws_response}

处理 WebSocket 响应。

- **Arguments**

  - **msg** (*aiohttp.http_websocket.WSMessage*)

### *async method* `run(self)` {#WebSocketServerAdapter.run}

运行适配器。

### *async method* `shutdown(self)` {#WebSocketServerAdapter.shutdown}

关闭并清理连接。

### *async method* `startup(self)` {#WebSocketServerAdapter.startup}

初始化适配器。

## *abstract class* `WebSocketAdapter`(self, bot) {#WebSocketAdapter}

Bases: `alicebot.adapter.Adapter`

WebSocket 适配器示例。

同时支持 WebSocket 客户端和服务端。

- **Arguments**

  - **bot** (*Bot*) - 当前机器人对象。

- **Attributes**

  - **websocket** (*Union[aiohttp.web_ws.WebSocketResponse, aiohttp.client_ws.ClientWebSocketResponse, NoneType]*)

  - **session** (*Optional[aiohttp.client.ClientSession]*)

  - **app** (*Optional[aiohttp.web_app.Application]*)

  - **runner** (*Optional[aiohttp.web_runner.AppRunner]*)

  - **site** (*Optional[aiohttp.web_runner.TCPSite]*)

  - **adapter_type** (*Literal['ws', 'reverse-ws']*)

  - **host** (*str*)

  - **port** (*int*)

  - **url** (*str*)

  - **reconnect_interval** (*int*)

### *async method* `handle_reverse_ws_response(self, request)` {#WebSocketAdapter.handle_reverse_ws_response}

处理 aiohttp WebSocket 服务器的接收。

- **Arguments**

  - **request** (*aiohttp.web_request.Request*)

- **Returns**

  Type: *aiohttp.web_ws.WebSocketResponse*

### *async method* `handle_websocket(self)` {#WebSocketAdapter.handle_websocket}

处理 WebSocket。

### *async method* `handle_websocket_msg(self, msg)` {#WebSocketAdapter.handle_websocket_msg}

处理 WebSocket 消息。

- **Arguments**

  - **msg** (*aiohttp.http_websocket.WSMessage*)

- **Returns**

  Type: *None*

### *async method* `reverse_ws_connection_hook(self)` {#WebSocketAdapter.reverse_ws_connection_hook}

反向 WebSocket 连接建立时的钩子函数。

### *async method* `run(self)` {#WebSocketAdapter.run}

运行适配器。

### *async method* `shutdown(self)` {#WebSocketAdapter.shutdown}

关闭并清理连接。

### *async method* `startup(self)` {#WebSocketAdapter.startup}

初始化适配器。

### *async method* `websocket_connect(self)` {#WebSocketAdapter.websocket_connect}

创建正向 WebSocket 连接。