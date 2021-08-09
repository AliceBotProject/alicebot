# alicebot.adapter.cqhttp.exception

## CQHTTP 异常


## _exception_ `CQHTTPException`

基类：[`alicebot.exception.AdapterException`](../../exception.md#alicebot.exception.AdapterException)

CQHTTP 异常基类。


## _exception_ `NetworkError`

基类：`alicebot.adapter.cqhttp.exception.CQHTTPException`

网络异常。


## _exception_ `ActionFailed`

基类：`alicebot.adapter.cqhttp.exception.CQHTTPException`

API 请求成功响应，当响应表示 API 操作失败。
:param resp: 返回的响应。


## _exception_ `ApiNotAvailable`

基类：`alicebot.adapter.cqhttp.exception.ActionFailed`

API 请求返回 404，表示当前请求的 API 不可用或不存在。


## _exception_ `ApiTimeout`

基类：[`alicebot.exception.AdapterTimeout`](../../exception.md#alicebot.exception.AdapterTimeout)

API 请求响应超时。
