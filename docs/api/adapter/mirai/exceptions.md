# alicebot.adapter.mirai.exceptions

## Mirai 异常


## _exception_ `MiraiException`

基类：[`alicebot.exceptions.AdapterException`](../../exceptions.md#alicebot.exceptions.AdapterException)

Mirai 异常基类。


## _exception_ `NetworkError`

基类：`alicebot.adapter.mirai.exceptions.MiraiException`

网络异常。


## _exception_ `ActionFailed`

基类：`alicebot.adapter.mirai.exceptions.MiraiException`

API 请求成功响应，但响应表示 API 操作失败。
:param resp: 返回的响应。


## _exception_ `ApiTimeout`

基类：`alicebot.adapter.mirai.exceptions.MiraiException`, [`alicebot.exceptions.AdapterTimeout`](../../exceptions.md#alicebot.exceptions.AdapterTimeout)

API 请求响应超时。
