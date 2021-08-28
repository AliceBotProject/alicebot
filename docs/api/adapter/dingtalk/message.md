# alicebot.adapter.dingtalk.message

## DingTalk 消息


## _class_ `DingTalkMessage`

基类：[`alicebot.message.MessageSegment`](../../message.md#alicebot.message.MessageSegment)[`None`]

DingTalk 消息


### `as_dict()`

返回符合钉钉消息标准的消息字段字典。


* **返回**

    符合钉钉消息标准的消息字段字典。



* **返回类型**

    Dict[str, Dict[str, Any]]



### _classmethod_ `raw(data)`

DingTalk 原始消息


### _classmethod_ `text(content)`

DingTalk text 消息


### _classmethod_ `link(text, title, message_url, pic_url=None)`

DingTalk link 消息


### _classmethod_ `markdown(title, text)`

DingTalk markdown 消息


### _classmethod_ `action_card_single_btn(title, text, single_title, single_url, btn_orientation='0')`

DingTalk 整体跳转 actionCard 消息


### _classmethod_ `action_card_multi_btns(title, text, btns, btn_orientation='0')`

DingTalk 独立跳转 actionCard 消息


### _classmethod_ `feed_card(links)`

DingTalk feedCard 消息


### _classmethod_ `at(at_mobiles=None, at_user_ids=None, is_at_all=False)`

DingTalk At 信息
