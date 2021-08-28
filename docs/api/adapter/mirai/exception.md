# alicebot.adapter.mirai.exception

## Mirai 异常


## _exception_ `MiraiException`

基类：[`alicebot.exception.AdapterException`](../../exception.md#alicebot.exception.AdapterException)

Mirai 异常基类。


## _exception_ `NetworkError`

基类：`alicebot.adapter.mirai.exception.MiraiException`

网络异常。


## _exception_ `ActionFailed`

基类：`alicebot.adapter.mirai.exception.MiraiException`

API 请求成功响应，但响应表示 API 操作失败。
:param resp: 返回的响应。


## _exception_ `ApiTimeout`

基类：`alicebot.adapter.mirai.exception.MiraiException`, [`alicebot.exception.AdapterTimeout`](../../exception.md#alicebot.exception.AdapterTimeout)

API 请求响应超时。
