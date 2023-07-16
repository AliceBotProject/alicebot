# alicebot.adapter.cqhttp.message

CQHTTP 适配器消息。

## *class* `CQHTTPMessage`(self, message = None) {#CQHTTPMessage}

Bases: `alicebot.message.Message`

CQHTTP 消息。

- **Arguments**

  - **message** (*Union[Self, ~T_MessageSegment, str, Mapping[str, Any], Iterable[Union[~T_MessageSegment, str, Mapping[str, Any]]], NoneType]*) - 可以被转化为消息的数据。

  - ***args** - 其他参数。

## *class* `CQHTTPMessageSegment`(self, type, data = \<factory\>) {#CQHTTPMessageSegment}

Bases: `alicebot.message.MessageSegment`

CQHTTP 消息字段。

- **Arguments**

  - **type** (*str*)

  - **data** (*Dict[str, Any]*)

### *class method* `anonymous(cls, ignore = None)` {#CQHTTPMessageSegment.anonymous}

匿名发消息

- **Arguments**

  - **ignore** (*Optional[bool]*)

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `at(cls, qq)` {#CQHTTPMessageSegment.at}

@某人

- **Arguments**

  - **qq** (*Union[int, Literal['all']]*)

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `contact(cls, type_, id_)` {#CQHTTPMessageSegment.contact}

推荐好友/推荐群

- **Arguments**

  - **type_** (*Literal['qq', 'group']*)

  - **id_** (*int*)

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `contact_friend(cls, id_)` {#CQHTTPMessageSegment.contact_friend}

推荐好友

- **Arguments**

  - **id_** (*int*)

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `contact_group(cls, id_)` {#CQHTTPMessageSegment.contact_group}

推荐好友

- **Arguments**

  - **id_** (*int*)

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `dice(cls)` {#CQHTTPMessageSegment.dice}

掷骰子魔法表情

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `face(cls, id_)` {#CQHTTPMessageSegment.face}

QQ 表情

- **Arguments**

  - **id_** (*int*)

- **Returns**

  Type: *CQHTTPMessageSegment*

### *method* `get_cqcode(self)` {#CQHTTPMessageSegment.get_cqcode}

获取此消息字段的 CQ 码形式。

- **Returns**

  Type: *str*

  此消息字段的 CQ 码形式。

### *class method* `image(cls, file, type_ = None, cache = True, proxy = True, timeout = None)` {#CQHTTPMessageSegment.image}

图片

- **Arguments**

  - **file** (*str*)

  - **type_** (*Optional[Literal['flash']]*)

  - **cache** (*bool*)

  - **proxy** (*bool*)

  - **timeout** (*Optional[int]*)

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `json_message(cls, data)` {#CQHTTPMessageSegment.json_message}

JSON 消息

- **Arguments**

  - **data** (*str*)

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `location(cls, lat, lon, title, content = None)` {#CQHTTPMessageSegment.location}

位置

- **Arguments**

  - **lat** (*float*)

  - **lon** (*float*)

  - **title** (*Optional[str]*)

  - **content** (*Optional[str]*)

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `music(cls, type_, id_)` {#CQHTTPMessageSegment.music}

音乐分享

- **Arguments**

  - **type_** (*Literal['qq', '163', 'xm']*)

  - **id_** (*int*)

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `music_custom(cls, url, audio, title, content = None, image = None)` {#CQHTTPMessageSegment.music_custom}

音乐自定义分享

- **Arguments**

  - **url** (*str*)

  - **audio** (*str*)

  - **title** (*str*)

  - **content** (*Optional[str]*)

  - **image** (*Optional[str]*)

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `node(cls, id_)` {#CQHTTPMessageSegment.node}

合并转发节点

- **Arguments**

  - **id_** (*int*)

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `node_custom(cls, user_id, nickname, content)` {#CQHTTPMessageSegment.node_custom}

合并转发自定义节点

- **Arguments**

  - **user_id** (*int*)

  - **nickname** (*str*)

  - **content** (*CQHTTPMessage*)

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `poke(cls, type_, id_)` {#CQHTTPMessageSegment.poke}

戳一戳

- **Arguments**

  - **type_** (*str*)

  - **id_** (*int*)

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `record(cls, file, magic = False, cache = True, proxy = True, timeout = None)` {#CQHTTPMessageSegment.record}

语音

- **Arguments**

  - **file** (*str*)

  - **magic** (*bool*)

  - **cache** (*bool*)

  - **proxy** (*bool*)

  - **timeout** (*Optional[int]*)

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `reply(cls, id_)` {#CQHTTPMessageSegment.reply}

回复

- **Arguments**

  - **id_** (*int*)

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `rps(cls)` {#CQHTTPMessageSegment.rps}

猜拳魔法表情

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `shake(cls)` {#CQHTTPMessageSegment.shake}

窗口抖动（戳一戳）

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `share(cls, url, title, content = None, image = None)` {#CQHTTPMessageSegment.share}

链接分享

- **Arguments**

  - **url** (*str*)

  - **title** (*str*)

  - **content** (*Optional[str]*)

  - **image** (*Optional[str]*)

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `text(cls, text)` {#CQHTTPMessageSegment.text}

纯文本

- **Arguments**

  - **text** (*str*)

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `video(cls, file, cache = True, proxy = True, timeout = None)` {#CQHTTPMessageSegment.video}

短视频

- **Arguments**

  - **file** (*str*)

  - **cache** (*bool*)

  - **proxy** (*bool*)

  - **timeout** (*Optional[int]*)

- **Returns**

  Type: *CQHTTPMessageSegment*

### *class method* `xml_message(cls, data)` {#CQHTTPMessageSegment.xml_message}

XML 消息

- **Arguments**

  - **data** (*str*)

- **Returns**

  Type: *CQHTTPMessageSegment*

## *function* `escape(s, *, escape_comma = True)` {#escape}

对 CQ 码中的特殊字符进行转义。

- **Arguments**

  - **s** (*str*) - 待转义的字符串。

  - **escape_comma** (*bool*) - 是否转义 `,`。

- **Returns**

  Type: *str*

  转义后的字符串。