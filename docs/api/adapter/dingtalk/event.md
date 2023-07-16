# alicebot.adapter.dingtalk.event

DingTalk 适配器事件。

## *class* `UserInfo`(__pydantic_self__, **data) {#UserInfo}

Bases: `pydantic.main.BaseModel`

用户信息

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **dingtalkId** (*str*)

  - **staffId** (*Optional[str]*)

## *class* `Text`(__pydantic_self__, **data) {#Text}

Bases: `pydantic.main.BaseModel`

文本消息

- **Arguments**

  - **data** (*Any*)

- **Attributes**

  - **content** (*str*)

## *class* `DingTalkEvent`(self, adapter, **data) {#DingTalkEvent}

Bases: `alicebot.event.MessageEvent`

DingTalk 事件基类

- **Arguments**

  - **adapter** (*~T_Adapter*) - 产生此事件的适配器对象。

  - ****data** (*Any*) - 事件数据。

- **Attributes**

  - **type** (*Optional[str]*)

  - **msgtype** (*str*)

  - **msgId** (*str*)

  - **createAt** (*str*)

  - **conversationType** (*Literal['1', '2']*)

  - **conversationId** (*str*)

  - **conversationTitle** (*Optional[str]*)

  - **senderId** (*str*)

  - **senderNick** (*str*)

  - **senderCorpId** (*Optional[str]*)

  - **sessionWebhook** (*str*)

  - **sessionWebhookExpiredTime** (*int*)

  - **isAdmin** (*Optional[bool]*)

  - **chatbotCorpId** (*Optional[str]*)

  - **isInAtList** (*Optional[bool]*)

  - **senderStaffId** (*Optional[str]*)

  - **chatbotUserId** (*str*)

  - **atUsers** (*List[alicebot.adapter.dingtalk.event.UserInfo]*)

  - **text** (*alicebot.adapter.dingtalk.event.Text*)

  - **response_msg** (*Union[NoneType, str, Dict[str, Any], alicebot.adapter.dingtalk.message.DingTalkMessage]*)

  - **response_at** (*Union[NoneType, Dict[str, Any], alicebot.adapter.dingtalk.message.DingTalkMessage]*)

### *method* `get_plain_text(self)` {#DingTalkEvent.get_plain_text}

获取消息的纯文本内容。

- **Returns**

  Type: *str*

  消息的纯文本内容。

### *async method* `is_same_sender(self, other)` {#DingTalkEvent.is_same_sender}

判断自身和另一个事件是否是同一个发送者。

- **Arguments**

  - **other** (*Self*) - 另一个事件。

- **Returns**

  Type: *bool*

  是否是同一个发送者。

### *readonly property* `message` {#DingTalkEvent.message}

Type: *alicebot.adapter.dingtalk.message.DingTalkMessage*

返回 message 字段。

### *async method* `reply(self, message, at = None)` {#DingTalkEvent.reply}

回复消息。

- **Arguments**

  - **message** (*Union[str, Dict[str, Any], alicebot.adapter.dingtalk.message.DingTalkMessage]*) - 回复消息的内容，可以是 `str`, `Dict` 或 `DingTalkMessage`。

  - **at** (*Union[NoneType, Dict[str, Any], alicebot.adapter.dingtalk.message.DingTalkMessage]*) - 回复消息时 At 的对象，必须时 at 类型的 `DingTalkMessage`，或者符合标准的 `Dict`。

- **Returns**

  Type: *Dict[str, Any]*

  调用 Webhook 地址后钉钉服务器的响应。

- **Raises**

  - **WebhookExpiredError** - 当前事件的 Webhook 地址已经过期。

  - **...** - 同 `DingTalkAdapter.send()` 方法。