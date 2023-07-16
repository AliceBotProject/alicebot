# alicebot.adapter.onebot.message

OneBot 适配器消息。

## *class* `OneBotMessage`(self, message = None) {#OneBotMessage}

Bases: `alicebot.message.Message`

OneBot 消息。

- **Arguments**

  - **message** (*Union[Self, ~T_MessageSegment, str, Mapping[str, Any], Iterable[Union[~T_MessageSegment, str, Mapping[str, Any]]], NoneType]*) - 可以被转化为消息的数据。

  - ***args** - 其他参数。

## *class* `OneBotMessageSegment`(self, type, data = \<factory\>) {#OneBotMessageSegment}

Bases: `alicebot.message.MessageSegment`

OneBot 消息字段。

- **Arguments**

  - **type** (*str*)

  - **data** (*Dict[str, Any]*)

### *class method* `audio(cls, file_id)` {#OneBotMessageSegment.audio}

音频

- **Arguments**

  - **file_id** (*str*)

- **Returns**

  Type: *OneBotMessageSegment*

### *class method* `file(cls, file_id)` {#OneBotMessageSegment.file}

文件

- **Arguments**

  - **file_id** (*str*)

- **Returns**

  Type: *OneBotMessageSegment*

### *class method* `image(cls, file_id)` {#OneBotMessageSegment.image}

图片

- **Arguments**

  - **file_id** (*str*)

- **Returns**

  Type: *OneBotMessageSegment*

### *class method* `location(cls, latitude, longitude, title, content)` {#OneBotMessageSegment.location}

位置

- **Arguments**

  - **latitude** (*float*)

  - **longitude** (*float*)

  - **title** (*str*)

  - **content** (*str*)

- **Returns**

  Type: *OneBotMessageSegment*

### *class method* `mention(cls, user_id)` {#OneBotMessageSegment.mention}

提及

- **Arguments**

  - **user_id** (*str*)

- **Returns**

  Type: *OneBotMessageSegment*

### *class method* `mention_all(cls)` {#OneBotMessageSegment.mention_all}

提及所有人

- **Returns**

  Type: *OneBotMessageSegment*

### *class method* `reply(cls, message_id, user_id)` {#OneBotMessageSegment.reply}

回复

- **Arguments**

  - **message_id** (*str*)

  - **user_id** (*str*)

- **Returns**

  Type: *OneBotMessageSegment*

### *class method* `text(cls, text)` {#OneBotMessageSegment.text}

纯文本

- **Arguments**

  - **text** (*str*)

- **Returns**

  Type: *OneBotMessageSegment*

### *class method* `video(cls, file_id)` {#OneBotMessageSegment.video}

视频

- **Arguments**

  - **file_id** (*str*)

- **Returns**

  Type: *OneBotMessageSegment*

### *class method* `voice(cls, file_id)` {#OneBotMessageSegment.voice}

语音

- **Arguments**

  - **file_id** (*str*)

- **Returns**

  Type: *OneBotMessageSegment*