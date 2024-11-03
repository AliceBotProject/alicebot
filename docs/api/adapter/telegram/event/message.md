# alicebot.adapter.telegram.event.message

Telegram 适配器事件。

## _class_ `MessageEvent` {#MessageEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`, `alicebot.event.MessageEvent[TelegramAdapter]`

New incoming message of any kind - text, photo, sticker, etc.

### _method_ `get_message(self)` {#MessageEvent-get-message}

获取 TelegramMessage 对象。

- **Returns**

  Type: _alicebot.adapter.telegram.message.TelegramMessage_

  TelegramMessage 对象。

### _method_ `get_plain_text(self)` {#MessageEvent-get-plain-text}

获取消息的纯文本内容。

- **Returns**

  Type: _str_

  消息的纯文本内容。

### _method_ `get_sender_id(self)` {#MessageEvent-get-sender-id}

获取消息的发送者的唯一标识符。

- **Returns**

  Type: _Union\[NoneType, int, str\]_

  消息的发送者的唯一标识符。

### _readonly property_ `message` {#MessageEvent-message}

Type: _alicebot.adapter.telegram.model.Message_

The message object.

### _async method_ `reply(self, message, disable_notification = None, protect_content = None, message_effect_id = None, reply_parameters = None, reply_markup = None, **kwargs)` {#MessageEvent-reply}

回复消息。

- **Arguments**

  - **message** (_Union\[str, alicebot.adapter.telegram.message.TelegramMessage, alicebot.adapter.telegram.media.TelegramMedia\]_) - 回复消息的内容。

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **message\_effect\_id** (_Optional\[str\]_)

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_)

  - **reply\_markup** (_Union\[alicebot.adapter.telegram.model.InlineKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardRemove, alicebot.adapter.telegram.model.ForceReply, NoneType\]_)

  - **kwargs** (_Any_)

- **Returns**

  Type: _Any_

  回复消息动作的响应。
