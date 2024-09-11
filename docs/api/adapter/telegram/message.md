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

Bases: `alicebot.message.MessageSegment[TelegramMessage]`

Telegram 消息字段，对应 Telegram 的 MessageEntity。

### _method_ `blockquote(text)` {#TelegramMessageSegment-blockquote}

- **Returns**

  Type: _Self_

### _method_ `bold(text)` {#TelegramMessageSegment-bold}

- **Returns**

  Type: _Self_

### _method_ `bot_command(text)` {#TelegramMessageSegment-bot-command}

- **Returns**

  Type: _Self_

### _method_ `cashtag(text)` {#TelegramMessageSegment-cashtag}

- **Returns**

  Type: _Self_

### _method_ `code(text)` {#TelegramMessageSegment-code}

- **Returns**

  Type: _Self_

### _method_ `custom_emoji(text, custom_emoji_id)` {#TelegramMessageSegment-custom-emoji}

- **Arguments**

  - **custom\_emoji\_id** (_str_)

- **Returns**

  Type: _Self_

### _method_ `email(text)` {#TelegramMessageSegment-email}

- **Returns**

  Type: _Self_

### _method_ `expandable_blockquote(text)` {#TelegramMessageSegment-expandable-blockquote}

- **Returns**

  Type: _Self_

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

### _method_ `hashtag(text)` {#TelegramMessageSegment-hashtag}

- **Returns**

  Type: _Self_

### _method_ `is_text(self)` {#TelegramMessageSegment-is-text}

是否是纯文本消息字段。

- **Returns**

  Type: _bool_

  是否是纯文本消息字段。

### _method_ `italic(text)` {#TelegramMessageSegment-italic}

- **Returns**

  Type: _Self_

### _readonly property_ `length` {#TelegramMessageSegment-length}

Type: _int_

### _method_ `mention(text)` {#TelegramMessageSegment-mention}

- **Returns**

  Type: _Self_

### _method_ `phone_number(text)` {#TelegramMessageSegment-phone-number}

- **Returns**

  Type: _Self_

### _method_ `pre(text, language)` {#TelegramMessageSegment-pre}

- **Arguments**

  - **language** (_str_)

- **Returns**

  Type: _Self_

### _method_ `spoiler(text)` {#TelegramMessageSegment-spoiler}

- **Returns**

  Type: _Self_

### _method_ `strikethrough(text)` {#TelegramMessageSegment-strikethrough}

- **Returns**

  Type: _Self_

### _method_ `text(text)` {#TelegramMessageSegment-text}

- **Returns**

  Type: _Self_

### _method_ `text_link(text, url)` {#TelegramMessageSegment-text-link}

- **Arguments**

  - **url** (_str_)

- **Returns**

  Type: _Self_

### _method_ `text_mention(text, user)` {#TelegramMessageSegment-text-mention}

- **Arguments**

  - **user** (_alicebot.adapter.telegram.model.User_)

- **Returns**

  Type: _Self_

### _method_ `underline(text)` {#TelegramMessageSegment-underline}

- **Returns**

  Type: _Self_

### _method_ `url(text)` {#TelegramMessageSegment-url}

- **Returns**

  Type: _Self_
