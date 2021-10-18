# alicebot.adapter.mirai

## Mirai 协议适配器

本适配器适配了 mirai-api-http 协议，仅支持 mirai-api-http 2.0 及以上版本。
本适配器支持 mirai-api-http 的 Websocket Adapter 模式和 Reverse Websocket Adapter 模式。
协议详情请参考: [mirai-api-http](https://github.com/project-mirai/mirai-api-http) 。


## _class_ `MiraiAdapter`

基类：[`alicebot.adapter.Adapter`](../README.md#alicebot.adapter.Adapter)

Mirai 协议适配器。
在插件中可以直接使用 `self.adapter.xxx_api(**params)` 调用名称为 `xxx_api` 的 API，和调用 `call_api()` 方法相同。


### property `config`


* **返回**

    本适配器的配置。



### _async_ `startup()`

初始化适配器。


### _async_ `run()`

运行适配器。


### _async_ `shutdown()`

关闭并清理连接。


### _async_ `handle_response(request)`

处理 aiohttp WebSocket 服务器的接收。


* **参数**

    **request** – aiohttp WebSocket 服务器的 Request 对象。



### _async_ `websocket_connect()`

创建正向 WebSocket 连接。


### _async_ `handle_websocket_msg()`

处理 WebSocket 消息。


### _async_ `handle_mirai_event(msg)`

处理 Mirai 事件。


* **参数**

    **msg** – 接收到的信息。



### _async_ `handle_non_standard_response(data)`

处理 Mirai 返回的非标准响应。


* **参数**

    **data** – 接收到的信息。



### _async_ `verify_identity()`

验证身份，创建与 Mirai-api-http 的连接。


### _async_ `call_api(command, sub_command=None, **content)`

调用 Mirai API，协程会等待直到获得 API 响应。


* **参数**

    
    * **command** – 命令字。


    * **sub_command** – 子命令字。


    * **content** – 请求内容。



* **返回**

    API 响应中的 data 字段，即 Mirai-api-http API 通用接口中的内容。



* **返回类型**

    Dict[str, Any]



* **引发**

    
    * [**NetworkError**](../cqhttp/exceptions.md#alicebot.adapter.cqhttp.exceptions.NetworkError) – 网络错误。


    * [**ActionFailed**](../cqhttp/exceptions.md#alicebot.adapter.cqhttp.exceptions.ActionFailed) – API 操作失败。


    * [**ApiTimeout**](../cqhttp/exceptions.md#alicebot.adapter.cqhttp.exceptions.ApiTimeout) – API 请求响应超时。



### _async_ `send(message_, message_type, target, quote=None)`

调用 Mirai API 发送消息。


* **参数**

    
    * **message** – 消息内容，可以是 str, Mapping, Iterable[Mapping], ‘MiraiMessageSegment’, ‘MiraiMessage’。
    将使用 `MiraiMessage` 进行封装。


    * **message_type** – 消息类型。应该是 private, friend 或者 group。其中 private 和 friend 相同。


    * **target** – 发送对象的 ID ，QQ 号码或者群号码。


    * **quote** – 引用的消息的 messageId。默认为 `None` ，不引用任何消息。



* **返回**

    API 响应。



* **返回类型**

    Dict[str, Any]



* **引发**

    
    * **TypeError** – message_type 非法。


    * **...** – 同 `call_api()` 方法。
