# alicebot.adapter.mirai.message

Mirai 适配器消息。

## _class_ `MiraiMessage` {#MiraiMessage}

Bases: `alicebot.message.Message`

Mirai 消息

### _method_ `__init__(self, *messages)` {#Message---init--}

初始化。

- **Arguments**

  - **\*messages** (_Union\[List\[~MessageSegmentT\], ~MessageSegmentT, str, Mapping\[str, Any\]\]_) - 可以被转化为消息的数据。

- **Returns**

  Type: _None_

### _method_ `as_message_chain(self)` {#MiraiMessage-as-message-chain}

返回符合 Mirai-api-http 标准的 messageChain 数组。

- **Returns**

  Type: _List\[Dict\[str, Any\]\]_

  messageChain 数组。

### _method_ `get_segment_class()` {#MiraiMessage-get-segment-class}

获取消息字段类。

- **Returns**

  Type: _Type\[MiraiMessageSegment\]_

  消息字段类。

## _class_ `MiraiMessageSegment` {#MiraiMessageSegment}

Bases: `alicebot.message.MessageSegment[MiraiMessage]`

Mirai 消息段

### _method_ `__init__(self, type, **data)` {#MiraiMessageSegment---init--}

初始化。

- **Arguments**

  - **type** (_str_) - 消息类型。

  - **\*\*data** (_Any_) - 消息内容。

- **Returns**

  Type: _None_

### _method_ `app(content)` {#MiraiMessageSegment-app}

App 消息

- **Returns**

  Type: _Self_

### _method_ `at(target)` {#MiraiMessageSegment-at}

At 消息

- **Returns**

  Type: _Self_

### _method_ `at_all()` {#MiraiMessageSegment-at-all}

AtAll 消息

- **Returns**

  Type: _Self_

### _method_ `dice(value)` {#MiraiMessageSegment-dice}

Dice 消息

- **Returns**

  Type: _Self_

### _method_ `face(face_id = None, name = None)` {#MiraiMessageSegment-face}

Face 消息

- **Arguments**

  - **name** (_Optional\[str\]_)

- **Returns**

  Type: _Self_

### _method_ `flash_image(image_id = None, url = None, path = None)` {#MiraiMessageSegment-flash-image}

FlashImage 消息

- **Arguments**

  - **url** (_Optional\[str\]_)

  - **path** (_Optional\[str\]_)

- **Returns**

  Type: _Self_

### _method_ `from_str(msg)` {#MiraiMessageSegment-from-str}

用于将 `str` 转换为消息字段。

- **Returns**

  Type: _Self_

  由 `str` 转换的消息字段。

### _method_ `get_message_class()` {#MiraiMessageSegment-get-message-class}

获取消息类。

- **Returns**

  Type: _Type\[MiraiMessage\]_

  消息类。

### _method_ `image(image_id = None, url = None, path = None)` {#MiraiMessageSegment-image}

Image 消息

- **Arguments**

  - **url** (_Optional\[str\]_)

  - **path** (_Optional\[str\]_)

- **Returns**

  Type: _Self_

### _method_ `is_text(self)` {#MiraiMessageSegment-is-text}

是否是纯文本消息字段。

- **Returns**

  Type: _bool_

  是否是纯文本消息字段。

### _method_ `json(json_)` {#MiraiMessageSegment-json}

Json 消息

- **Returns**

  Type: _Self_

### _method_ `music_share(kind, title, summary, jump_url, picture_url, music_url, brief)` {#MiraiMessageSegment-music-share}

MusicShare 消息

- **Arguments**

  - **title** (_str_)

  - **summary** (_str_)

  - **jump\_url** (_str_)

  - **picture\_url** (_str_)

  - **music\_url** (_str_)

  - **brief** (_str_)

- **Returns**

  Type: _Self_

### _method_ `plain(text)` {#MiraiMessageSegment-plain}

Plain 消息

- **Returns**

  Type: _Self_

### _method_ `poke(name)` {#MiraiMessageSegment-poke}

Poke 消息

- **Returns**

  Type: _Self_

### _method_ `quote(id_, group_id, sender_id, target_id, origin)` {#MiraiMessageSegment-quote}

Quote 消息

- **Arguments**

  - **group\_id** (_int_)

  - **sender\_id** (_int_)

  - **target\_id** (_int_)

  - **origin** (_MiraiMessage_)

- **Returns**

  Type: _Self_

### _method_ `ser_model(self)` {#MiraiMessageSegment-ser-model}

返回符合 Mirai-api-http 标准的消息字段字典。

- **Returns**

  Type: _Dict\[str, Any\]_

  符合 Mirai-api-http 标准的消息字段字典。

### _method_ `source(id_, time)` {#MiraiMessageSegment-source}

Source 消息

- **Arguments**

  - **time** (_int_)

- **Returns**

  Type: _Self_

### _method_ `voice(voice_id = None, url = None, path = None)` {#MiraiMessageSegment-voice}

Voice 消息

- **Arguments**

  - **url** (_Optional\[str\]_)

  - **path** (_Optional\[str\]_)

- **Returns**

  Type: _Self_

### _method_ `xml(xml)` {#MiraiMessageSegment-xml}

Xml 消息

- **Returns**

  Type: _Self_
