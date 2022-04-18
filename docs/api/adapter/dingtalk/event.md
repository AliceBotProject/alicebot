# alicebot.adapter.dingtalk.event

DingTalk 适配器事件。

## *class* `UserInfo`(__pydantic_self__, **data) {#UserInfo}

Bases: `pydantic.main.BaseModel`

- **Attributes**

  - **dingtalkId** (*str*)

  - **staffId** (*Optional[str]*)

## *class* `Text`(__pydantic_self__, **data) {#Text}

Bases: `pydantic.main.BaseModel`

- **Attributes**

  - **content** (*str*)

## *class* `DingTalkEvent`(__pydantic_self__, **data) {#DingTalkEvent}

Bases: `alicebot.event.Event`

DingTalk 事件基类

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

  - **message** (*Optional[alicebot.adapter.dingtalk.message.DingTalkMessage]*)

  - **response_msg** (*Union[NoneType, str, Dict, alicebot.adapter.dingtalk.message.DingTalkMessage]*)

  - **response_at** (*Union[NoneType, Dict, alicebot.adapter.dingtalk.message.DingTalkMessage]*)

### *async method* `reply(self, msg, at = None)` {#DingTalkEvent.reply}

回复消息。

- **Arguments**

  - **msg** (*Union[str, Dict, alicebot.adapter.dingtalk.message.DingTalkMessage]*) - 回复消息的内容，可以是 str, Dict 或 DingTalkMessage。

  - **at** (*Union[NoneType, Dict, alicebot.adapter.dingtalk.message.DingTalkMessage]*) - 回复消息时 At 的对象，必须时 at 类型的 DingTalkMessage，或者符合标准的 Dict。

- **Returns**

  Type: *Dict[str, Any]*

  调用 Webhook 地址后钉钉服务器的响应。

- **Raises**

  - **WebhookExpiredError** - 当前事件的 Webhook 地址已经过期。

  - **...** - 同 `DingTalkAdapter.send()` 方法。

### *class method* `set_ts_now(cls, v, values, **kwargs)` {#DingTalkEvent.set_ts_now}

- **Arguments**

  - **v**

  - **values**