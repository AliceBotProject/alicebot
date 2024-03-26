# alicebot.adapter.dingtalk.message

DingTalk 适配器消息。

## _abstract class_ `DingTalkMessage` {#DingTalkMessage}

Bases: `alicebot.message.MessageSegment`

DingTalk 消息

### _method_ `__init__(self, /, **data)` {#BaseModel---init--}

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

- **Arguments**

  - **data** (_Any_)

- **Returns**

  Type: _None_

### _method_ `action_card_multi_btns(title, text, btns, btn_orientation = '0')` {#DingTalkMessage-action-card-multi-btns}

DingTalk 独立跳转 actionCard 消息

- **Arguments**

  - **text** (_str_)

  - **btns** (_List\[Any\]_)

  - **btn\_orientation** (_str_)

- **Returns**

  Type: _DingTalkMessage_

### _method_ `action_card_single_btn(title, text, single_title, single_url, btn_orientation = '0')` {#DingTalkMessage-action-card-single-btn}

DingTalk 整体跳转 actionCard 消息

- **Arguments**

  - **text** (_str_)

  - **single\_title** (_str_)

  - **single\_url** (_str_)

  - **btn\_orientation** (_str_)

- **Returns**

  Type: _DingTalkMessage_

### _method_ `at(at_mobiles = None, at_user_ids = None, is_at_all = False)` {#DingTalkMessage-at}

DingTalk At 信息

- **Arguments**

  - **at\_user\_ids** (_Optional\[List\[str\]\]_)

  - **is\_at\_all** (_bool_)

- **Returns**

  Type: _DingTalkMessage_

### _method_ `feed_card(links)` {#DingTalkMessage-feed-card}

DingTalk feedCard 消息

- **Returns**

  Type: _DingTalkMessage_

### _method_ `get_plain_text(self)` {#DingTalkMessage-get-plain-text}

获取消息中的纯文本部分。

- **Returns**

  Type: _str_

  消息中的纯文本部分。

### _method_ `get_segment_class()` {#DingTalkMessage-get-segment-class}

获取消息字段类。

- **Returns**

  Type: _None_

  消息字段类。

### _method_ `link(text, title, message_url, pic_url = None)` {#DingTalkMessage-link}

DingTalk link 消息

- **Arguments**

  - **title** (_str_)

  - **message\_url** (_str_)

  - **pic\_url** (_Optional\[str\]_)

- **Returns**

  Type: _DingTalkMessage_

### _method_ `markdown(title, text)` {#DingTalkMessage-markdown}

DingTalk markdown 消息

- **Arguments**

  - **text** (_str_)

- **Returns**

  Type: _DingTalkMessage_

### _method_ `raw(data)` {#DingTalkMessage-raw}

DingTalk 原始消息

- **Returns**

  Type: _DingTalkMessage_

### _method_ `ser_model(self)` {#DingTalkMessage-ser-model}

返回符合钉钉消息标准的消息字段字典。

- **Returns**

  Type: _Dict\[str, Any\]_

  符合钉钉消息标准的消息字段字典。

### _method_ `text(content)` {#DingTalkMessage-text}

DingTalk text 消息

- **Returns**

  Type: _DingTalkMessage_
