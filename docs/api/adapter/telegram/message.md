# alicebot.adapter.telegram.message

Telegram 适配器消息。

## _class_ `TelegramMessage` {#TelegramMessage}

Bases: `alicebot.message.Message`

Telegram 消息。

### _method_ `from_entities(text, entities)` {#TelegramMessage-from-entities}

- **Arguments**

  - **entities** (_list\[alicebot.adapter.telegram.model.MessageEntity\]_)

- **Returns**

  Type: _Self_

### _method_ `get_segment_class()` {#TelegramMessage-get-segment-class}

获取消息字段类。

- **Returns**

  Type: _type\['TelegramMessageSegment'\]_

  消息字段类。

### _method_ `to_entities(self)` {#TelegramMessage-to-entities}

- **Returns**

  Type: _list\[alicebot.adapter.telegram.model.MessageEntity\]_

### _method_ `to_text(self)` {#TelegramMessage-to-text}

- **Returns**

  Type: _str_

## _class_ `TelegramMessageSegment` {#TelegramMessageSegment}

Bases: `alicebot.adapter.telegram.entity.Entity[TelegramMessage]`

Telegram 消息字段，对应 Telegram 的 MessageEntity。

### _method_ `from_str(msg)` {#TelegramMessageSegment-from-str}

用于将 `str` 转换为消息字段，子类应重写此方法。

- **Returns**

  Type: _Self_

  由 `str` 转换的消息字段。

### _method_ `get_message_class()` {#TelegramMessageSegment-get-message-class}

获取消息类。

- **Returns**

  Type: _type\['TelegramMessage'\]_

  消息类。

### _method_ `is_text(self)` {#TelegramMessageSegment-is-text}

是否是纯文本消息字段。

- **Returns**

  Type: _bool_

  是否是纯文本消息字段。

### _readonly property_ `length` {#TelegramMessageSegment-length}

Type: _int_

### _method_ `text(text)` {#TelegramMessageSegment-text}

- **Returns**

  Type: _Self_
