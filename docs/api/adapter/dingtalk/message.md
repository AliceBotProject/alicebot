# alicebot.adapter.dingtalk.message

DingTalk 适配器消息。

## *class* `DingTalkMessage`(self, type, data = <factory>) {#DingTalkMessage}

Bases: `alicebot.message.MessageSegment`

DingTalk 消息

- **Arguments**

  - **type** (*str*)

  - **data** (*Dict[str, Any]*)

### *class method* `action_card_multi_btns(cls, title, text, btns, btn_orientation = '0')` {#DingTalkMessage.action_card_multi_btns}

DingTalk 独立跳转 actionCard 消息

- **Arguments**

  - **title** (*str*)

  - **text** (*str*)

  - **btns** (*list*)

  - **btn_orientation** (*str*)

### *class method* `action_card_single_btn(cls, title, text, single_title, single_url, btn_orientation = '0')` {#DingTalkMessage.action_card_single_btn}

DingTalk 整体跳转 actionCard 消息

- **Arguments**

  - **title** (*str*)

  - **text** (*str*)

  - **single_title** (*str*)

  - **single_url** (*str*)

  - **btn_orientation** (*str*)

### *method* `as_dict(self)` {#DingTalkMessage.as_dict}

返回符合钉钉消息标准的消息字段字典。

- **Returns**

  Type: *Dict[str, Dict[str, Any]]*

  符合钉钉消息标准的消息字段字典。

### *class method* `at(cls, at_mobiles = None, at_user_ids = None, is_at_all = False)` {#DingTalkMessage.at}

DingTalk At 信息

- **Arguments**

  - **at_mobiles** (*Optional[List[str]]*)

  - **at_user_ids** (*Optional[List[str]]*)

  - **is_at_all** (*bool*)

### *class method* `feed_card(cls, links)` {#DingTalkMessage.feed_card}

DingTalk feedCard 消息

- **Arguments**

  - **links** (*list*)

### *class method* `link(cls, text, title, message_url, pic_url = None)` {#DingTalkMessage.link}

DingTalk link 消息

- **Arguments**

  - **text** (*str*)

  - **title** (*str*)

  - **message_url** (*str*)

  - **pic_url** (*Optional[str]*)

### *class method* `markdown(cls, title, text)` {#DingTalkMessage.markdown}

DingTalk markdown 消息

- **Arguments**

  - **title** (*str*)

  - **text** (*str*)

### *class method* `raw(cls, data)` {#DingTalkMessage.raw}

DingTalk 原始消息

- **Arguments**

  - **data** (*Dict[str, Any]*)

- **Returns**

  Type: *DingTalkMessage*

### *class method* `text(cls, content)` {#DingTalkMessage.text}

DingTalk text 消息

- **Arguments**

  - **content** (*str*)

- **Returns**

  Type: *DingTalkMessage*