# alicebot.adapter.http_server_test_adapter

HTTP 服务端适配器示例。

这里是一个最简单可以直接使用的 HTTP 服务端适配器示例。

## *class* `HttpServerTestEvent`(__pydantic_self__, **data) {#HttpServerTestEvent}

Bases: `alicebot.event.Event`

HTTP 服务端示例适配器事件类。

- **Attributes**

  - **message** (*alicebot.message.Message*)

## *class* `HttpServerTestAdapter`(self, bot) {#HttpServerTestAdapter}

Bases: `alicebot.adapter.utils.HttpServerAdapter`

HTTP 服务端示例适配器类。

- **Arguments**

  - **bot** (*Bot*)

- **Attributes**

  - **get_url** (*str*)

  - **post_url** (*str*)

  - **host** (*str*)

  - **port** (*int*)

### *async method* `handle_response(self, request)` {#HttpServerTestAdapter.handle_response}

- **Arguments**

  - **request** (*aiohttp.web_request.Request*)

### *async static method* `send(msg)` {#HttpServerTestAdapter.send}

发送消息，需要适配器开发者实现。

- **Arguments**

  - **msg** (*Union[str, T_Message, T_MessageSegment]*)