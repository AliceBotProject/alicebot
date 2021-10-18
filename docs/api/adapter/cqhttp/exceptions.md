# alicebot.adapter.cqhttp.exceptions

## CQHTTP 异常


## _exception_ `CQHTTPException`

基类：[`alicebot.exceptions.AdapterException`](../../exceptions.md#alicebot.exceptions.AdapterException)

CQHTTP 异常基类。


## _exception_ `NetworkError`

基类：`alicebot.adapter.cqhttp.exceptions.CQHTTPException`

网络异常。


## _exception_ `ActionFailed`

基类：`alicebot.adapter.cqhttp.exceptions.CQHTTPException`

API 请求成功响应，但响应表示 API 操作失败。
:param resp: 返回的响应。


## _exception_ `ApiNotAvailable`

基类：`alicebot.adapter.cqhttp.exceptions.ActionFailed`

API 请求返回 404，表示当前请求的 API 不可用或不存在。


## _exception_ `ApiTimeout`

基类：`alicebot.adapter.cqhttp.exceptions.CQHTTPException`, [`alicebot.exceptions.AdapterTimeout`](../../exceptions.md#alicebot.exceptions.AdapterTimeout)

API 请求响应超时。
