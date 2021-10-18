# alicebot.adapter.dingtalk.exceptions

## DingTalk 异常


## _exception_ `DingTalkException`

基类：[`alicebot.exceptions.AdapterException`](../../exceptions.md#alicebot.exceptions.AdapterException)

DingTalk 异常基类。


## _exception_ `NetworkError`

基类：`alicebot.adapter.dingtalk.exceptions.DingTalkException`

网络异常。


## _exception_ `WebhookExpiredError`

基类：`alicebot.adapter.dingtalk.exceptions.DingTalkException`

Webhook 地址已到期。


## _exception_ `ApiTimeout`

基类：`alicebot.adapter.dingtalk.exceptions.DingTalkException`, [`alicebot.exceptions.AdapterTimeout`](../../exceptions.md#alicebot.exceptions.AdapterTimeout)

API 请求响应超时。
