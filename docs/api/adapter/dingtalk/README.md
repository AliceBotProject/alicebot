# alicebot.adapter.dingtalk

## DingTalk 协议适配器

本适配器适配了钉钉企业自建机器人协议。
协议详情请参考: [钉钉开放平台](https://developers.dingtalk.com/document/robots/robot-overview) 。


## _class_ `DingTalkAdapter`

基类：[`alicebot.adapter.Adapter`](../README.md#alicebot.adapter.Adapter)

钉钉协议适配器。


### property `config`


* **返回**

    本适配器的配置。



### _async_ `startup()`

创建 aiohttp Application。


### _async_ `run()`

运行 aiohttp 服务器。


### _async_ `shutdown()`

清理 aiohttp AppRunner。


### _async_ `handler(request)`

处理 aiohttp 服务器的接收。


* **参数**

    **request** – aiohttp 服务器的 Request 对象。



### `get_sign(timestamp)`

计算签名。


* **参数**

    **timestamp** – 时间戳。



* **返回**

    签名。



* **返回类型**

    str



### _async_ `send(webhook, conversation_type, msg, at=None)`

发送消息。


* **参数**

    
    * **webhook** – Webhook 网址。


    * **conversation_type** – 聊天类型，’1’ 表示单聊，’2’ 表示群聊。


    * **msg** – 消息。


    * **at** – At 对象，仅在群聊时生效，默认为空。



* **返回**

    钉钉服务器的响应。



* **返回类型**

    Dict[str, Any]



* **引发**

    
    * **TypeError** – 传入参数类型错误。


    * **ValueError** – 传入参数值错误。


    * [**NetworkError**](../cqhttp/exception.md#alicebot.adapter.cqhttp.exception.NetworkError) – 调用 Webhook 地址时网络错误。
