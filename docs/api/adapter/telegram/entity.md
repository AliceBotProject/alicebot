# alicebot.adapter.telegram.entity

Telegram Entity 模型。

## _abstract class_ `Entity` {#Entity}

Bases: `alicebot.message.MessageSegment`

消息字段。

本类实现了所有 `Mapping` 类型的方法，这些方法全部是对 `data` 属性的操作。
本类重写了 `+` 和 `+=` 运算符，可以直接和 `Message`, `MessageSegment` 等类型的对象执行取和运算，返回 `Message` 对象。
适配器开发者需要继承本类并重写 `get_message_class()` 方法。

- **Attributes**

  - **type** - 消息字段类型。

  - **data** - 消息字段内容。

### _method_ `blockquote(text)` {#Entity-blockquote}

- **Returns**

  Type: _Self_

### _method_ `bold(text)` {#Entity-bold}

- **Returns**

  Type: _Self_

### _method_ `bot_command(text)` {#Entity-bot-command}

- **Returns**

  Type: _Self_

### _method_ `cashtag(text)` {#Entity-cashtag}

- **Returns**

  Type: _Self_

### _method_ `code(text)` {#Entity-code}

- **Returns**

  Type: _Self_

### _method_ `custom_emoji(text, custom_emoji_id = None)` {#Entity-custom-emoji}

- **Arguments**

  - **custom\_emoji\_id** (_Optional\[str\]_)

- **Returns**

  Type: _Self_

### _method_ `email(text)` {#Entity-email}

- **Returns**

  Type: _Self_

### _method_ `expandable_blockquote(text)` {#Entity-expandable-blockquote}

- **Returns**

  Type: _Self_

### _method_ `hashtag(text)` {#Entity-hashtag}

- **Returns**

  Type: _Self_

### _method_ `italic(text)` {#Entity-italic}

- **Returns**

  Type: _Self_

### _method_ `mention(text)` {#Entity-mention}

- **Returns**

  Type: _Self_

### _method_ `phone_number(text)` {#Entity-phone-number}

- **Returns**

  Type: _Self_

### _method_ `pre(text, language = None)` {#Entity-pre}

- **Arguments**

  - **language** (_Optional\[str\]_)

- **Returns**

  Type: _Self_

### _method_ `spoiler(text)` {#Entity-spoiler}

- **Returns**

  Type: _Self_

### _method_ `strikethrough(text)` {#Entity-strikethrough}

- **Returns**

  Type: _Self_

### _method_ `text_link(text, url = None)` {#Entity-text-link}

- **Arguments**

  - **url** (_Optional\[str\]_)

- **Returns**

  Type: _Self_

### _method_ `text_mention(text, user = None)` {#Entity-text-mention}

- **Arguments**

  - **user** (_Optional\[alicebot.adapter.telegram.model.User\]_)

- **Returns**

  Type: _Self_

### _method_ `underline(text)` {#Entity-underline}

- **Returns**

  Type: _Self_

### _method_ `url(text)` {#Entity-url}

- **Returns**

  Type: _Self_

## _abstract class_ `Entity[TelegramMessage]` {#Entity-TelegramMessage-}

Bases: `alicebot.adapter.telegram.entity.Entity`

消息字段。

本类实现了所有 `Mapping` 类型的方法，这些方法全部是对 `data` 属性的操作。
本类重写了 `+` 和 `+=` 运算符，可以直接和 `Message`, `MessageSegment` 等类型的对象执行取和运算，返回 `Message` 对象。
适配器开发者需要继承本类并重写 `get_message_class()` 方法。

- **Attributes**

  - **type** - 消息字段类型。

  - **data** - 消息字段内容。
