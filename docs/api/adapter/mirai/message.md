# alicebot.adapter.mirai.message

Mirai 适配器消息。

## *class* `MiraiMessage`(self, message = None, *args, **kwargs) {#MiraiMessage}

Bases: `alicebot.message.Message`

- **Arguments**

  - **message** (*Union[NoneType, ~T_Message, ~T_MessageSegment, str, Mapping, Iterable[Union[~T_MessageSegment, str, Mapping]]]*)

### *method* `as_message_chain(self)` {#MiraiMessage.as_message_chain}

返回符合 Mirai-api-http 标准的 messageChain 数组。

- **Returns**

  Type: *List[Dict[str, Any]]*

  messageChain 数组。

### *method* `get_plain_text(self)` {#MiraiMessage.get_plain_text}

获取消息中的纯文本部分。

- **Returns**

  Type: *str*

  消息中的纯文本部分。

### *method* `is_text(self)` {#MiraiMessage.is_text}

- **Returns**

  Type: *bool*

## *class* `MiraiMessageSegment`(self, type, **data) {#MiraiMessageSegment}

Bases: `alicebot.message.MessageSegment`

- **Arguments**

  - **type** (*str*)

### *class method* `app(cls, content)` {#MiraiMessageSegment.app}

- **Arguments**

  - **content** (*str*)

### *method* `as_dict(self)` {#MiraiMessageSegment.as_dict}

返回符合 Mirai-api-http 标准的消息字段字典。

- **Returns**

  Type: *Dict[str, Any]*

  符合 Mirai-api-http 标准的消息字段字典。

### *class method* `at(cls, target)` {#MiraiMessageSegment.at}

- **Arguments**

  - **target** (*int*)

### *class method* `at_all(cls)` {#MiraiMessageSegment.at_all}

### *class method* `dice(cls, value)` {#MiraiMessageSegment.dice}

- **Arguments**

  - **value** (*int*)

### *class method* `face(cls, face_id = None, name = None)` {#MiraiMessageSegment.face}

- **Arguments**

  - **face_id** (*Optional[int]*)

  - **name** (*Optional[str]*)

### *class method* `flash_image(cls, image_id = None, url = None, path = None)` {#MiraiMessageSegment.flash_image}

- **Arguments**

  - **image_id** (*Optional[str]*)

  - **url** (*Optional[str]*)

  - **path** (*Optional[str]*)

### *class method* `image(cls, image_id = None, url = None, path = None)` {#MiraiMessageSegment.image}

- **Arguments**

  - **image_id** (*Optional[str]*)

  - **url** (*Optional[str]*)

  - **path** (*Optional[str]*)

### *method* `is_text(self)` {#MiraiMessageSegment.is_text}

- **Returns**

  Type: *bool*

### *class method* `json(cls, json_)` {#MiraiMessageSegment.json}

- **Arguments**

  - **json_** (*str*)

### *class method* `music_share(cls, kind, title, summary, jump_url, picture_url, music_url, brief)` {#MiraiMessageSegment.music_share}

- **Arguments**

  - **kind** (*str*)

  - **title** (*str*)

  - **summary** (*str*)

  - **jump_url** (*str*)

  - **picture_url** (*str*)

  - **music_url** (*str*)

  - **brief** (*str*)

### *class method* `plain(cls, text)` {#MiraiMessageSegment.plain}

- **Arguments**

  - **text** (*str*)

### *class method* `poke(cls, name)` {#MiraiMessageSegment.poke}

- **Arguments**

  - **name** (*str*)

### *class method* `quote(cls, id_, group_id, sender_id, target_id, origin)` {#MiraiMessageSegment.quote}

- **Arguments**

  - **id_** (*int*)

  - **group_id** (*int*)

  - **sender_id** (*int*)

  - **target_id** (*int*)

  - **origin** (*alicebot.adapter.mirai.message.MiraiMessage*)

### *class method* `source(cls, id_, time)` {#MiraiMessageSegment.source}

- **Arguments**

  - **id_** (*int*)

  - **time** (*int*)

### *class method* `voice(cls, voice_id = None, url = None, path = None)` {#MiraiMessageSegment.voice}

- **Arguments**

  - **voice_id** (*Optional[str]*)

  - **url** (*Optional[str]*)

  - **path** (*Optional[str]*)

### *class method* `xml(cls, xml)` {#MiraiMessageSegment.xml}

- **Arguments**

  - **xml** (*str*)