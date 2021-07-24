# alicebot.adapter.cqhttp.message

## CQHTTP 消息


## _class_ `CQHTTPMessage`

基类：[`alicebot.message.Message`](../../message.md#alicebot.message.Message)

CQHTTP 消息


### `is_text()`


* **返回**

    是否是纯文本消息。



### `get_plain_text()`

获取消息中的纯文本部分。


* **返回**

    消息中的纯文本部分。



* **返回类型**

    str



## _class_ `CQHTTPMessageSegment`

基类：[`alicebot.message.MessageSegment`](../../message.md#alicebot.message.MessageSegment)

CQHTTP 消息字段


### `is_text()`


* **返回**

    是否是纯文本消息字段。



* **返回类型**

    bool



### `get_cqcode()`


* **返回**

    此消息字段的 CQ 码形式。



* **返回类型**

    str



### _classmethod_ `text(text)`

纯文本


### _classmethod_ `face(id_)`

QQ 表情


### _classmethod_ `image(file, type_=None, cache=True, proxy=True, timeout=None)`

图片


### _classmethod_ `record(file, magic=False, cache=True, proxy=True, timeout=None)`

语音


### _classmethod_ `video(file, cache=True, proxy=True, timeout=None)`

短视频


### _classmethod_ `at(qq)`

@某人


### _classmethod_ `rps()`

猜拳魔法表情


### _classmethod_ `dice()`

掷骰子魔法表情


### _classmethod_ `shake()`

窗口抖动（戳一戳）


### _classmethod_ `poke(type_, id_)`

戳一戳


### _classmethod_ `anonymous(ignore=None)`

匿名发消息


### _classmethod_ `share(url, title, content=None, image=None)`

链接分享


### _classmethod_ `contact(type_, id_)`

推荐好友/推荐群


### _classmethod_ `contact_friend(id_)`

推荐好友


### _classmethod_ `contact_group(id_)`

推荐好友


### _classmethod_ `location(lat, lon, title, content=None)`

位置


### _classmethod_ `music(type_, id_)`

音乐分享


### _classmethod_ `music_custom(url, audio, title, content=None, image=None)`

音乐自定义分享


### _classmethod_ `reply(id_)`

回复


### _classmethod_ `node(id_)`

合并转发节点


### _classmethod_ `node_custom(user_id, nickname, content)`

合并转发自定义节点


### _classmethod_ `xml_message(data)`

XML 消息


### _classmethod_ `json_message(data)`

JSON 消息


## `escape(s, *, escape_comma=True)`

对 CQ 码中的特殊字符进行转义。


* **参数**

    
    * **s** – 待转义的字符串。


    * **escape_comma** – 是否转义 `,`。



* **返回**

    转义后的字符串。



* **返回类型**

    str
