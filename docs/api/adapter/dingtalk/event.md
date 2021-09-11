# alicebot.adapter.dingtalk.event

## DingTalk 事件


## _class_ `DingTalkEvent`

基类：[`alicebot.event.Event`](../../event.md#alicebot.event.Event)

DingTalk 事件基类


### _async_ `reply(msg, at=None)`

回复消息。


* **参数**

    
    * **msg** – 回复消息的内容，可以是 str, Dict 或 DingTalkMessage。


    * **at** – 回复消息时 At 的对象，必须时 at 类型的 DingTalkMessage，或者符合标准的 Dict。



* **返回**

    调用 Webhook 地址后钉钉服务器的响应。



* **返回类型**

    Dict



* **引发**

    
    * [**WebhookExpiredError**](exception.md#alicebot.adapter.dingtalk.exception.WebhookExpiredError) – 当前事件的 Webhook 地址已经过期。


    * **...** – 同 `DingTalkAdapter.send()` 方法。
