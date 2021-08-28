# alicebot.adapter.cqhttp

## CQHTTP 协议适配器

本适配器适配了 OneBot v11 协议。
协议详情请参考: [OneBot](https://github.com/howmanybots/onebot/blob/master/README.md) 。


## _class_ `CQHTTPAdapter`

基类：[`alicebot.adapter.Adapter`](../README.md#alicebot.adapter.Adapter)

CQHTTP 协议适配器。
在插件中可以直接使用 `self.adapter.xxx_api(**params)` 调用名称为 `xxx_api` 的 API，和调用 `call_api()` 方法相同。


### property `config`


* **返回**

    本适配器的配置。



### _async_ `startup()`

创建 aiohttp Application。


### _async_ `run()`

运行 aiohttp WebSocket 服务器。


### _async_ `shutdown()`

清理 aiohttp AppRunner。


### _async_ `handle_response(request)`

处理 aiohttp WebSocket 服务器的接收。


* **参数**

    **request** – aiohttp WebSocket 服务器的 Request 对象。



### _async_ `handle_cqhttp_event(msg)`

处理 CQHTTP 事件。


* **参数**

    **msg** – 接收到的信息。



### _async_ `call_api(api, **params)`

调用 CQHTTP API，协程会等待直到获得 API 响应。


* **参数**

    
    * **api** – API 名称。


    * **params** – API 参数。



* **返回**

    API 响应中的 data 字段。



* **返回类型**

    Dict[str, Any]



* **引发**

    
    * [**NetworkError**](exception.md#alicebot.adapter.cqhttp.exception.NetworkError) – 网络错误。


    * [**ApiNotAvailable**](exception.md#alicebot.adapter.cqhttp.exception.ApiNotAvailable) – API 请求响应 404， API 不可用。


    * [**ActionFailed**](exception.md#alicebot.adapter.cqhttp.exception.ActionFailed) – API 请求响应 failed， API 操作失败。


    * [**ApiTimeout**](exception.md#alicebot.adapter.cqhttp.exception.ApiTimeout) – API 请求响应超时。



### _async_ `send(message_, message_type, id_)`

发送消息，调用 send_private_msg 或 send_group_msg API 发送消息。


* **参数**

    
    * **message** – 消息内容，可以是 str, Mapping, Iterable[Mapping], ‘CQHTTPMessageSegment’, ‘CQHTTPMessage’。
    将使用 `CQHTTPMessage` 进行封装。


    * **message_type** – 消息类型。应该是 private 或者 group。


    * **id** – 发送对象的 ID ，QQ 号码或者群号码。



* **返回**

    API 响应。



* **返回类型**

    Dict[str, Any]



* **引发**

    
    * **TypeError** – message_type 不是 ‘private’ 或 ‘group’。


    * **...** – 同 `call_api()` 方法。
