# alicebot.adapter.mirai.message

Mirai 适配器消息。

## *class* `MiraiMessage`(self, message = None) {#MiraiMessage}

Bases: `alicebot.message.Message`

Mirai 消息

- **Arguments**

  - **message** (*Union[Self, ~T_MessageSegment, str, Mapping[str, Any], Iterable[Union[~T_MessageSegment, str, Mapping[str, Any]]], NoneType]*) - 可以被转化为消息的数据。

  - ***args** - 其他参数。

### *method* `as_message_chain(self)` {#MiraiMessage.as_message_chain}

返回符合 Mirai-api-http 标准的 messageChain 数组。

- **Returns**

  Type: *List[Dict[str, Any]]*

  messageChain 数组。

## *class* `MiraiMessageSegment`(self, type, **data) {#MiraiMessageSegment}

Bases: `alicebot.message.MessageSegment`

Mirai 消息段

- **Arguments**

  - **type** (*str*) - 消息类型。

  - ****data** (*Any*) - 消息内容。

### *class method* `app(cls, content)` {#MiraiMessageSegment.app}

App 消息

- **Arguments**

  - **content** (*str*)

### *method* `as_dict(self)` {#MiraiMessageSegment.as_dict}

返回符合 Mirai-api-http 标准的消息字段字典。

- **Returns**

  Type: *Dict[str, Any]*

  符合 Mirai-api-http 标准的消息字段字典。

### *class method* `at(cls, target)` {#MiraiMessageSegment.at}

At 消息

- **Arguments**

  - **target** (*int*)

### *class method* `at_all(cls)` {#MiraiMessageSegment.at_all}

AtAll 消息

### *class method* `dice(cls, value)` {#MiraiMessageSegment.dice}

Dice 消息

- **Arguments**

  - **value** (*int*)

### *class method* `face(cls, face_id = None, name = None)` {#MiraiMessageSegment.face}

Face 消息

- **Arguments**

  - **face_id** (*Optional[int]*)

  - **name** (*Optional[str]*)

### *class method* `flash_image(cls, image_id = None, url = None, path = None)` {#MiraiMessageSegment.flash_image}

FlashImage 消息

- **Arguments**

  - **image_id** (*Optional[str]*)

  - **url** (*Optional[str]*)

  - **path** (*Optional[str]*)

### *class method* `image(cls, image_id = None, url = None, path = None)` {#MiraiMessageSegment.image}

Image 消息

- **Arguments**

  - **image_id** (*Optional[str]*)

  - **url** (*Optional[str]*)

  - **path** (*Optional[str]*)

### *method* `is_text(self)` {#MiraiMessageSegment.is_text}

是否是纯文本消息字段。

- **Returns**

  Type: *bool*

  是否是纯文本消息字段。

### *class method* `json(cls, json_)` {#MiraiMessageSegment.json}

Json 消息

- **Arguments**

  - **json_** (*str*)

### *class method* `music_share(cls, kind, title, summary, jump_url, picture_url, music_url, brief)` {#MiraiMessageSegment.music_share}

MusicShare 消息

- **Arguments**

  - **kind** (*str*)

  - **title** (*str*)

  - **summary** (*str*)

  - **jump_url** (*str*)

  - **picture_url** (*str*)

  - **music_url** (*str*)

  - **brief** (*str*)

### *class method* `plain(cls, text)` {#MiraiMessageSegment.plain}

Plain 消息

- **Arguments**

  - **text** (*str*)

### *class method* `poke(cls, name)` {#MiraiMessageSegment.poke}

Poke 消息

- **Arguments**

  - **name** (*str*)

### *class method* `quote(cls, id_, group_id, sender_id, target_id, origin)` {#MiraiMessageSegment.quote}

Quote 消息

- **Arguments**

  - **id_** (*int*)

  - **group_id** (*int*)

  - **sender_id** (*int*)

  - **target_id** (*int*)

  - **origin** (*alicebot.adapter.mirai.message.MiraiMessage*)

### *class method* `source(cls, id_, time)` {#MiraiMessageSegment.source}

Source 消息

- **Arguments**

  - **id_** (*int*)

  - **time** (*int*)

### *class method* `voice(cls, voice_id = None, url = None, path = None)` {#MiraiMessageSegment.voice}

Voice 消息

- **Arguments**

  - **voice_id** (*Optional[str]*)

  - **url** (*Optional[str]*)

  - **path** (*Optional[str]*)

### *class method* `xml(cls, xml)` {#MiraiMessageSegment.xml}

Xml 消息

- **Arguments**

  - **xml** (*str*)