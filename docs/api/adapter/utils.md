# alicebot.adapter.utils

适配器实用工具。

这里定义了一些在编写适配器时常用的基类，适配器开发者可以直接继承自这里的类或者用作参考。

## _abstract class_ `PollingAdapter` {#PollingAdapter}

Bases: `alicebot.adapter.Adapter`

轮询式适配器示例。

### _async method_ `on_tick(self)` {#PollingAdapter-on-tick}

当轮询发生。

- **Returns**

  Type: _None_

### _async method_ `run(self)` {#PollingAdapter-run}

适配器运行方法，适配器开发者必须实现该方法。

适配器运行过程中保持保持运行，当此方法结束后，AliceBot 不会自动重新启动适配器。

- **Returns**

  Type: _None_

## _abstract class_ `HttpClientAdapter` {#HttpClientAdapter}

Bases: `alicebot.adapter.utils.PollingAdapter`

HTTP 客户端适配器示例。

- **Attributes**

  - **session** (_aiohttp.client.ClientSession_)

### _async method_ `shutdown(self)` {#HttpClientAdapter-shutdown}

在适配器结束运行时运行的方法，用于安全地关闭适配器。

AliceBot 在接收到系统的结束信号后先发送 cancel 请求给 run 任务。
在所有适配器都停止运行后，会依次运行并等待所有适配器的 `shutdown()` 方法。
当强制退出时此方法可能未被执行。

- **Returns**

  Type: _None_

### _async method_ `startup(self)` {#HttpClientAdapter-startup}

在适配器开始运行前运行的方法，用于初始化适配器。

AliceBot 依次运行并等待所有适配器的 `startup()` 方法，待运行完毕后再创建 `run()` 任务。

- **Returns**

  Type: _None_

## _abstract class_ `WebSocketClientAdapter` {#WebSocketClientAdapter}

Bases: `alicebot.adapter.Adapter`

WebSocket 客户端适配器示例。

- **Attributes**

  - **url** (_str_)

### _async method_ `handle_response(self, msg)` {#WebSocketClientAdapter-handle-response}

处理响应。

- **Arguments**

  - **msg** (_aiohttp.http\_websocket.WSMessage_)

- **Returns**

  Type: _None_

### _async method_ `run(self)` {#WebSocketClientAdapter-run}

适配器运行方法，适配器开发者必须实现该方法。

适配器运行过程中保持保持运行，当此方法结束后，AliceBot 不会自动重新启动适配器。

- **Returns**

  Type: _None_

## _abstract class_ `HttpServerAdapter` {#HttpServerAdapter}

Bases: `alicebot.adapter.Adapter`

HTTP 服务端适配器示例。

- **Attributes**

  - **app** (_aiohttp.web\_app.Application_)

  - **runner** (_aiohttp.web\_runner.AppRunner_)

  - **site** (_aiohttp.web\_runner.TCPSite_)

  - **host** (_str_)

  - **port** (_int_)

  - **get\_url** (_str_)

  - **post\_url** (_str_)

### _async method_ `handle_response(self, request)` {#HttpServerAdapter-handle-response}

处理响应。

- **Arguments**

  - **request** (_aiohttp.web\_request.Request_)

- **Returns**

  Type: _aiohttp.web\_response.StreamResponse_

### _async method_ `run(self)` {#HttpServerAdapter-run}

适配器运行方法，适配器开发者必须实现该方法。

适配器运行过程中保持保持运行，当此方法结束后，AliceBot 不会自动重新启动适配器。

- **Returns**

  Type: _None_

### _async method_ `shutdown(self)` {#HttpServerAdapter-shutdown}

在适配器结束运行时运行的方法，用于安全地关闭适配器。

AliceBot 在接收到系统的结束信号后先发送 cancel 请求给 run 任务。
在所有适配器都停止运行后，会依次运行并等待所有适配器的 `shutdown()` 方法。
当强制退出时此方法可能未被执行。

- **Returns**

  Type: _None_

### _async method_ `startup(self)` {#HttpServerAdapter-startup}

在适配器开始运行前运行的方法，用于初始化适配器。

AliceBot 依次运行并等待所有适配器的 `startup()` 方法，待运行完毕后再创建 `run()` 任务。

- **Returns**

  Type: _None_

## _abstract class_ `WebSocketServerAdapter` {#WebSocketServerAdapter}

Bases: `alicebot.adapter.Adapter`

WebSocket 服务端适配器示例。

- **Attributes**

  - **app** (_aiohttp.web\_app.Application_)

  - **runner** (_aiohttp.web\_runner.AppRunner_)

  - **site** (_aiohttp.web\_runner.TCPSite_)

  - **websocket** (_aiohttp.web\_ws.WebSocketResponse_)

  - **host** (_str_)

  - **port** (_int_)

  - **url** (_str_)

### _async method_ `handle_response(self, request)` {#WebSocketServerAdapter-handle-response}

处理 WebSocket。

- **Arguments**

  - **request** (_aiohttp.web\_request.Request_)

- **Returns**

  Type: _aiohttp.web\_ws.WebSocketResponse_

### _async method_ `handle_ws_response(self, msg)` {#WebSocketServerAdapter-handle-ws-response}

处理 WebSocket 响应。

- **Arguments**

  - **msg** (_aiohttp.http\_websocket.WSMessage_)

- **Returns**

  Type: _None_

### _async method_ `run(self)` {#WebSocketServerAdapter-run}

适配器运行方法，适配器开发者必须实现该方法。

适配器运行过程中保持保持运行，当此方法结束后，AliceBot 不会自动重新启动适配器。

- **Returns**

  Type: _None_

### _async method_ `shutdown(self)` {#WebSocketServerAdapter-shutdown}

在适配器结束运行时运行的方法，用于安全地关闭适配器。

AliceBot 在接收到系统的结束信号后先发送 cancel 请求给 run 任务。
在所有适配器都停止运行后，会依次运行并等待所有适配器的 `shutdown()` 方法。
当强制退出时此方法可能未被执行。

- **Returns**

  Type: _None_

### _async method_ `startup(self)` {#WebSocketServerAdapter-startup}

在适配器开始运行前运行的方法，用于初始化适配器。

AliceBot 依次运行并等待所有适配器的 `startup()` 方法，待运行完毕后再创建 `run()` 任务。

- **Returns**

  Type: _None_

## _abstract class_ `WebSocketAdapter` {#WebSocketAdapter}

Bases: `alicebot.adapter.Adapter`

WebSocket 适配器示例。

同时支持 WebSocket 客户端和服务端。

- **Attributes**

  - **websocket** (_Union\[aiohttp.web\_ws.WebSocketResponse, aiohttp.client\_ws.ClientWebSocketResponse, NoneType\]_)

  - **session** (_Optional\[aiohttp.client.ClientSession\]_)

  - **app** (_Optional\[aiohttp.web\_app.Application\]_)

  - **runner** (_Optional\[aiohttp.web\_runner.AppRunner\]_)

  - **site** (_Optional\[aiohttp.web\_runner.TCPSite\]_)

  - **adapter\_type** (_Literal\['ws', 'reverse-ws'\]_)

  - **host** (_str_)

  - **port** (_int_)

  - **url** (_str_)

  - **reconnect\_interval** (_int_)

### _async method_ `handle_reverse_ws_response(self, request)` {#WebSocketAdapter-handle-reverse-ws-response}

处理 aiohttp WebSocket 服务器的接收。

- **Arguments**

  - **request** (_aiohttp.web\_request.Request_)

- **Returns**

  Type: _aiohttp.web\_ws.WebSocketResponse_

### _async method_ `handle_websocket(self)` {#WebSocketAdapter-handle-websocket}

处理 WebSocket。

- **Returns**

  Type: _None_

### _async method_ `handle_websocket_msg(self, msg)` {#WebSocketAdapter-handle-websocket-msg}

处理 WebSocket 消息。

- **Arguments**

  - **msg** (_aiohttp.http\_websocket.WSMessage_)

- **Returns**

  Type: _None_

### _async method_ `reverse_ws_connection_hook(self)` {#WebSocketAdapter-reverse-ws-connection-hook}

反向 WebSocket 连接建立时的钩子函数。

- **Returns**

  Type: _None_

### _async method_ `run(self)` {#WebSocketAdapter-run}

适配器运行方法，适配器开发者必须实现该方法。

适配器运行过程中保持保持运行，当此方法结束后，AliceBot 不会自动重新启动适配器。

- **Returns**

  Type: _None_

### _async method_ `shutdown(self)` {#WebSocketAdapter-shutdown}

在适配器结束运行时运行的方法，用于安全地关闭适配器。

AliceBot 在接收到系统的结束信号后先发送 cancel 请求给 run 任务。
在所有适配器都停止运行后，会依次运行并等待所有适配器的 `shutdown()` 方法。
当强制退出时此方法可能未被执行。

- **Returns**

  Type: _None_

### _async method_ `startup(self)` {#WebSocketAdapter-startup}

初始化适配器。

- **Returns**

  Type: _None_

### _async method_ `websocket_connect(self)` {#WebSocketAdapter-websocket-connect}

创建正向 WebSocket 连接。

- **Returns**

  Type: _None_
