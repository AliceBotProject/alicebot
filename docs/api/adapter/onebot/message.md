# alicebot.adapter.onebot.message

OneBot 适配器消息。

## _class_ `OneBotMessage` {#OneBotMessage}

Bases: `alicebot.message.Message`

OneBot 消息。

### _method_ `get_segment_class()` {#OneBotMessage-get-segment-class}

获取消息字段类。

- **Returns**

  Type: _type\['OneBotMessageSegment'\]_

  消息字段类。

## _class_ `OneBotMessageSegment` {#OneBotMessageSegment}

Bases: `alicebot.message.MessageSegment[OneBotMessage]`

OneBot 消息字段。

### _method_ `audio(file_id)` {#OneBotMessageSegment-audio}

音频

- **Returns**

  Type: _Self_

### _method_ `file(file_id)` {#OneBotMessageSegment-file}

文件

- **Returns**

  Type: _Self_

### _method_ `from_str(msg)` {#OneBotMessageSegment-from-str}

用于将 `str` 转换为消息字段，子类应重写此方法。

- **Returns**

  Type: _Self_

  由 `str` 转换的消息字段。

### _method_ `get_message_class()` {#OneBotMessageSegment-get-message-class}

获取消息类。

- **Returns**

  Type: _type\['OneBotMessage'\]_

  消息类。

### _method_ `image(file_id)` {#OneBotMessageSegment-image}

图片

- **Returns**

  Type: _Self_

### _method_ `location(latitude, longitude, title, content)` {#OneBotMessageSegment-location}

位置

- **Arguments**

  - **longitude** (_float_)

  - **title** (_str_)

  - **content** (_str_)

- **Returns**

  Type: _Self_

### _method_ `mention(user_id)` {#OneBotMessageSegment-mention}

提及

- **Returns**

  Type: _Self_

### _method_ `mention_all()` {#OneBotMessageSegment-mention-all}

提及所有人

- **Returns**

  Type: _Self_

### _method_ `reply(message_id, user_id)` {#OneBotMessageSegment-reply}

回复

- **Arguments**

  - **user\_id** (_str_)

- **Returns**

  Type: _Self_

### _method_ `text(text)` {#OneBotMessageSegment-text}

纯文本

- **Returns**

  Type: _Self_

### _method_ `video(file_id)` {#OneBotMessageSegment-video}

视频

- **Returns**

  Type: _Self_

### _method_ `voice(file_id)` {#OneBotMessageSegment-voice}

语音

- **Returns**

  Type: _Self_
