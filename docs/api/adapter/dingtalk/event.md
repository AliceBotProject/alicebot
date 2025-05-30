# alicebot.adapter.dingtalk.event

DingTalk 适配器事件。

## _class_ `UserInfo` {#UserInfo}

Bases: `pydantic.main.BaseModel`

用户信息

- **Attributes**

  - **dingtalkId** (_str_)

  - **staffId** (_Optional\[str\]_)

## _class_ `Text` {#Text}

Bases: `pydantic.main.BaseModel`

文本消息

- **Attributes**

  - **content** (_str_)

## _class_ `DingTalkEvent` {#DingTalkEvent}

Bases: `alicebot.event.MessageEvent[DingTalkAdapter]`

DingTalk 事件基类

- **Attributes**

  - **type** (_Optional\[str\]_)

  - **msgtype** (_str_)

  - **msgId** (_str_)

  - **createAt** (_str_)

  - **conversationType** (_Literal\['1', '2'\]_)

  - **conversationId** (_str_)

  - **conversationTitle** (_Optional\[str\]_)

  - **senderId** (_str_)

  - **senderNick** (_str_)

  - **senderCorpId** (_Optional\[str\]_)

  - **sessionWebhook** (_str_)

  - **sessionWebhookExpiredTime** (_int_)

  - **isAdmin** (_Optional\[bool\]_)

  - **chatbotCorpId** (_Optional\[str\]_)

  - **isInAtList** (_Optional\[bool\]_)

  - **senderStaffId** (_Optional\[str\]_)

  - **chatbotUserId** (_str_)

  - **atUsers** (_list\[alicebot.adapter.dingtalk.event.UserInfo\]_)

  - **text** (_Text_)

  - **response\_msg** (_Union\[NoneType, str, dict\[str, Any\], alicebot.adapter.dingtalk.message.DingTalkMessage\]_)

  - **response\_at** (_Union\[NoneType, dict\[str, Any\], alicebot.adapter.dingtalk.message.DingTalkMessage\]_)

### _method_ `get_plain_text(self)` {#DingTalkEvent-get-plain-text}

获取消息的纯文本内容。

- **Returns**

  Type: _str_

  消息的纯文本内容。

### _method_ `get_sender_id(self)` {#DingTalkEvent-get-sender-id}

获取消息的发送者的唯一标识符。

- **Returns**

  Type: _str_

  消息的发送者的唯一标识符。

### _readonly property_ `message` {#DingTalkEvent-message}

Type: _alicebot.adapter.dingtalk.message.DingTalkMessage_

返回 message 字段。

### _async method_ `reply(self, message, at = None)` {#DingTalkEvent-reply}

回复消息。

- **Arguments**

  - **message** (_Union\[str, dict\[str, Any\], alicebot.adapter.dingtalk.message.DingTalkMessage\]_) - 回复消息的内容，可以是 `str`, `Dict` 或 `DingTalkMessage`。

  - **at** (_Union\[NoneType, dict\[str, Any\], alicebot.adapter.dingtalk.message.DingTalkMessage\]_) - 回复消息时 At 的对象，必须时 at 类型的 `DingTalkMessage`，或者符合标准的 `Dict`。

- **Returns**

  Type: _dict\[str, typing.Any\]_

  调用 Webhook 地址后钉钉服务器的响应。

- **Raises**

  - **WebhookExpiredError** - 当前事件的 Webhook 地址已经过期。

  - **...** - 同 `DingTalkAdapter.send()` 方法。
