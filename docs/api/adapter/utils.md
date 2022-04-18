# alicebot.adapter.utils

适配器实用工具。

这里定义了一些在编写适配器时常用的基类，适配器开发者可以直接继承自这里的类或者用作参考。

## *abstract class* `PollingAdapter`(self, bot) {#PollingAdapter}

Bases: `alicebot.adapter.Adapter`

轮询式适配器示例。

- **Arguments**

  - **bot** (*Bot*)

- **Attributes**

  - **delay** (*Union[int, float]*)

  - **create_task** (*bool*)

### *async method* `on_tick(self)` {#PollingAdapter.on_tick}

### *async method* `run(self)` {#PollingAdapter.run}

适配器运行方法，适配器开发者必须实现该方法。

适配器运行过程中保持保持运行，当此方法结束后，AliceBot 不会自动重新启动适配器。

## *abstract class* `HttpClientAdapter`(self, bot) {#HttpClientAdapter}

Bases: `alicebot.adapter.utils.PollingAdapter`

HTTP 客户端适配器示例。

- **Arguments**

  - **bot** (*Bot*)

- **Attributes**

  - **session** (*aiohttp.client.ClientSession*)

### *async method* `on_tick(self)` {#HttpClientAdapter.on_tick}

### *async method* `shutdown(self)` {#HttpClientAdapter.shutdown}

在适配器结束运行时运行的方法，用于安全地关闭适配器。

AliceBot 在接收到系统的结束信号后依次运行并等待所有适配器的 `shutdown()` 方法。当强制退出时此方法可能未被执行。

### *async method* `startup(self)` {#HttpClientAdapter.startup}

在适配器开始运行前运行的方法，用于初始化适配器。

AliceBot 依次运行并等待所有适配器的 `startup()` 方法，待运行完毕后再创建 `run()` 任务。

## *abstract class* `WebSocketClientAdapter`(self, bot) {#WebSocketClientAdapter}

Bases: `alicebot.adapter.Adapter`

WebSocket 客户端适配器示例。

- **Arguments**

  - **bot** (*Bot*)

- **Attributes**

  - **url** (*str*)

### *method* `handle_response(self, msg)` {#WebSocketClientAdapter.handle_response}

- **Arguments**

  - **msg** (*aiohttp.http_websocket.WSMessage*)

### *async method* `run(self)` {#WebSocketClientAdapter.run}

适配器运行方法，适配器开发者必须实现该方法。

适配器运行过程中保持保持运行，当此方法结束后，AliceBot 不会自动重新启动适配器。

## *abstract class* `HttpServerAdapter`(self, bot) {#HttpServerAdapter}

Bases: `alicebot.adapter.Adapter`

HTTP 服务端适配器示例。

- **Arguments**

  - **bot** (*Bot*)

- **Attributes**

  - **app** (*aiohttp.web_app.Application*)

  - **runner** (*aiohttp.web_runner.AppRunner*)

  - **site** (*aiohttp.web_runner.TCPSite*)

  - **host** (*str*)

  - **port** (*int*)

  - **get_url** (*str*)

  - **post_url** (*str*)

### *async method* `handle_response(self, request)` {#HttpServerAdapter.handle_response}

- **Arguments**

  - **request** (*aiohttp.web_request.Request*)

### *async method* `run(self)` {#HttpServerAdapter.run}

适配器运行方法，适配器开发者必须实现该方法。

适配器运行过程中保持保持运行，当此方法结束后，AliceBot 不会自动重新启动适配器。

### *async method* `shutdown(self)` {#HttpServerAdapter.shutdown}

在适配器结束运行时运行的方法，用于安全地关闭适配器。

AliceBot 在接收到系统的结束信号后依次运行并等待所有适配器的 `shutdown()` 方法。当强制退出时此方法可能未被执行。

### *async method* `startup(self)` {#HttpServerAdapter.startup}

在适配器开始运行前运行的方法，用于初始化适配器。

AliceBot 依次运行并等待所有适配器的 `startup()` 方法，待运行完毕后再创建 `run()` 任务。

## *abstract class* `WebSocketServerAdapter`(self, bot) {#WebSocketServerAdapter}

Bases: `alicebot.adapter.Adapter`

WebSocket 服务端适配器示例。

- **Arguments**

  - **bot** (*Bot*)

- **Attributes**

  - **app** (*aiohttp.web_app.Application*)

  - **runner** (*aiohttp.web_runner.AppRunner*)

  - **site** (*aiohttp.web_runner.TCPSite*)

  - **websocket** (*aiohttp.web_ws.WebSocketResponse*)

  - **host** (*str*)

  - **port** (*int*)

  - **url** (*str*)

### *async method* `handle_response(self, request)` {#WebSocketServerAdapter.handle_response}

- **Arguments**

  - **request** (*aiohttp.web_request.Request*)

### *async method* `handle_ws_response(self, msg)` {#WebSocketServerAdapter.handle_ws_response}

- **Arguments**

  - **msg** (*aiohttp.http_websocket.WSMessage*)

### *async method* `run(self)` {#WebSocketServerAdapter.run}

适配器运行方法，适配器开发者必须实现该方法。

适配器运行过程中保持保持运行，当此方法结束后，AliceBot 不会自动重新启动适配器。

### *async method* `shutdown(self)` {#WebSocketServerAdapter.shutdown}

在适配器结束运行时运行的方法，用于安全地关闭适配器。

AliceBot 在接收到系统的结束信号后依次运行并等待所有适配器的 `shutdown()` 方法。当强制退出时此方法可能未被执行。

### *async method* `startup(self)` {#WebSocketServerAdapter.startup}

在适配器开始运行前运行的方法，用于初始化适配器。

AliceBot 依次运行并等待所有适配器的 `startup()` 方法，待运行完毕后再创建 `run()` 任务。