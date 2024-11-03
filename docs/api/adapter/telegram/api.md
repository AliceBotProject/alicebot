# alicebot.adapter.telegram.api

Telegram API 定义。

## _abstract class_ `TelegramAPIBase` {#TelegramAPIBase}

Bases: `abc.ABC`

Helper class that provides a standard way to create an ABC using

inheritance.

### _async method_ `call_api(self, api, *, response_type = None, **params)` {#TelegramAPIBase-call-api}

- **Arguments**

  - **api** (_str_)

  - **response\_type** (_Optional\[type\[~\_T\]\]_)

  - **params** (_Any_)

- **Returns**

  Type: _Any_

## _abstract class_ `TelegramAPI` {#TelegramAPI}

Bases: `alicebot.adapter.telegram.api.TelegramAPIBase`

Helper class that provides a standard way to create an ABC using

inheritance.

### _async method_ `add_sticker_to_set(self, *, user_id, name, sticker)` {#TelegramAPI-add-sticker-to-set}

- **Arguments**

  - **user\_id** (_int_)

  - **name** (_str_)

  - **sticker** (_alicebot.adapter.telegram.model.InputSticker_)

- **Returns**

  Type: _bool_

### _async method_ `answer_callback_query(self, *, callback_query_id, text = None, show_alert = None, url = None, cache_time = None)` {#TelegramAPI-answer-callback-query}

- **Arguments**

  - **callback\_query\_id** (_str_)

  - **text** (_Optional\[str\]_)

  - **show\_alert** (_Optional\[bool\]_)

  - **url** (_Optional\[str\]_)

  - **cache\_time** (_Optional\[int\]_)

- **Returns**

  Type: _bool_

### _async method_ `answer_inline_query(self, *, inline_query_id, results, cache_time = None, is_personal = None, next_offset = None, button = None)` {#TelegramAPI-answer-inline-query}

- **Arguments**

  - **inline\_query\_id** (_str_)

  - **results** (_list\[typing.Union\[alicebot.adapter.telegram.model.InlineQueryResultCachedAudio, alicebot.adapter.telegram.model.InlineQueryResultCachedDocument, alicebot.adapter.telegram.model.InlineQueryResultCachedGif, alicebot.adapter.telegram.model.InlineQueryResultCachedMpeg4Gif, alicebot.adapter.telegram.model.InlineQueryResultCachedPhoto, alicebot.adapter.telegram.model.InlineQueryResultCachedSticker, alicebot.adapter.telegram.model.InlineQueryResultCachedVideo, alicebot.adapter.telegram.model.InlineQueryResultCachedVoice, alicebot.adapter.telegram.model.InlineQueryResultArticle, alicebot.adapter.telegram.model.InlineQueryResultAudio, alicebot.adapter.telegram.model.InlineQueryResultContact, alicebot.adapter.telegram.model.InlineQueryResultGame, alicebot.adapter.telegram.model.InlineQueryResultDocument, alicebot.adapter.telegram.model.InlineQueryResultGif, alicebot.adapter.telegram.model.InlineQueryResultLocation, alicebot.adapter.telegram.model.InlineQueryResultMpeg4Gif, alicebot.adapter.telegram.model.InlineQueryResultPhoto, alicebot.adapter.telegram.model.InlineQueryResultVenue, alicebot.adapter.telegram.model.InlineQueryResultVideo, alicebot.adapter.telegram.model.InlineQueryResultVoice\]\]_)

  - **cache\_time** (_Optional\[int\]_)

  - **is\_personal** (_Optional\[bool\]_)

  - **next\_offset** (_Optional\[str\]_)

  - **button** (_Optional\[alicebot.adapter.telegram.model.InlineQueryResultsButton\]_)

- **Returns**

  Type: _bool_

### _async method_ `answer_pre_checkout_query(self, *, pre_checkout_query_id, ok, error_message = None)` {#TelegramAPI-answer-pre-checkout-query}

- **Arguments**

  - **pre\_checkout\_query\_id** (_str_)

  - **ok** (_bool_)

  - **error\_message** (_Optional\[str\]_)

- **Returns**

  Type: _bool_

### _async method_ `answer_shipping_query(self, *, shipping_query_id, ok, shipping_options = None, error_message = None)` {#TelegramAPI-answer-shipping-query}

- **Arguments**

  - **shipping\_query\_id** (_str_)

  - **ok** (_bool_)

  - **shipping\_options** (_Optional\[list\[alicebot.adapter.telegram.model.ShippingOption\]\]_)

  - **error\_message** (_Optional\[str\]_)

- **Returns**

  Type: _bool_

### _async method_ `answer_web_app_query(self, *, web_app_query_id, result)` {#TelegramAPI-answer-web-app-query}

- **Arguments**

  - **web\_app\_query\_id** (_str_)

  - **result** (_Union\[alicebot.adapter.telegram.model.InlineQueryResultCachedAudio, alicebot.adapter.telegram.model.InlineQueryResultCachedDocument, alicebot.adapter.telegram.model.InlineQueryResultCachedGif, alicebot.adapter.telegram.model.InlineQueryResultCachedMpeg4Gif, alicebot.adapter.telegram.model.InlineQueryResultCachedPhoto, alicebot.adapter.telegram.model.InlineQueryResultCachedSticker, alicebot.adapter.telegram.model.InlineQueryResultCachedVideo, alicebot.adapter.telegram.model.InlineQueryResultCachedVoice, alicebot.adapter.telegram.model.InlineQueryResultArticle, alicebot.adapter.telegram.model.InlineQueryResultAudio, alicebot.adapter.telegram.model.InlineQueryResultContact, alicebot.adapter.telegram.model.InlineQueryResultGame, alicebot.adapter.telegram.model.InlineQueryResultDocument, alicebot.adapter.telegram.model.InlineQueryResultGif, alicebot.adapter.telegram.model.InlineQueryResultLocation, alicebot.adapter.telegram.model.InlineQueryResultMpeg4Gif, alicebot.adapter.telegram.model.InlineQueryResultPhoto, alicebot.adapter.telegram.model.InlineQueryResultVenue, alicebot.adapter.telegram.model.InlineQueryResultVideo, alicebot.adapter.telegram.model.InlineQueryResultVoice\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.SentWebAppMessage_

### _async method_ `approve_chat_join_request(self, *, chat_id, user_id)` {#TelegramAPI-approve-chat-join-request}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **user\_id** (_int_)

- **Returns**

  Type: _bool_

### _async method_ `ban_chat_member(self, *, chat_id, user_id, until_date = None, revoke_messages = None)` {#TelegramAPI-ban-chat-member}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **user\_id** (_int_)

  - **until\_date** (_Optional\[int\]_)

  - **revoke\_messages** (_Optional\[bool\]_)

- **Returns**

  Type: _bool_

### _async method_ `ban_chat_sender_chat(self, *, chat_id, sender_chat_id)` {#TelegramAPI-ban-chat-sender-chat}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **sender\_chat\_id** (_int_)

- **Returns**

  Type: _bool_

### _async method_ `close(self)` {#TelegramAPI-close}

- **Returns**

  Type: _bool_

### _async method_ `close_forum_topic(self, *, chat_id, message_thread_id)` {#TelegramAPI-close-forum-topic}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **message\_thread\_id** (_int_)

- **Returns**

  Type: _bool_

### _async method_ `close_general_forum_topic(self, *, chat_id)` {#TelegramAPI-close-general-forum-topic}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

- **Returns**

  Type: _bool_

### _async method_ `copy_message(self, *, chat_id, from_chat_id, message_id, message_thread_id = None, caption = None, parse_mode = None, caption_entities = None, show_caption_above_media = None, disable_notification = None, protect_content = None, reply_parameters = None, reply_markup = None)` {#TelegramAPI-copy-message}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **from\_chat\_id** (_Union\[int, str\]_)

  - **message\_id** (_int_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **show\_caption\_above\_media** (_Optional\[bool\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_)

  - **reply\_markup** (_Union\[alicebot.adapter.telegram.model.InlineKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardRemove, alicebot.adapter.telegram.model.ForceReply, NoneType\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.MessageId_

### _async method_ `copy_messages(self, *, chat_id, from_chat_id, message_ids, message_thread_id = None, disable_notification = None, protect_content = None, remove_caption = None)` {#TelegramAPI-copy-messages}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **from\_chat\_id** (_Union\[int, str\]_)

  - **message\_ids** (_list\[int\]_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **remove\_caption** (_Optional\[bool\]_)

- **Returns**

  Type: _list\[alicebot.adapter.telegram.model.MessageId\]_

### _async method_ `create_chat_invite_link(self, *, chat_id, name = None, expire_date = None, member_limit = None, creates_join_request = None)` {#TelegramAPI-create-chat-invite-link}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **name** (_Optional\[str\]_)

  - **expire\_date** (_Optional\[int\]_)

  - **member\_limit** (_Optional\[int\]_)

  - **creates\_join\_request** (_Optional\[bool\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.ChatInviteLink_

### _async method_ `create_chat_subscription_invite_link(self, *, chat_id, subscription_period, subscription_price, name = None)` {#TelegramAPI-create-chat-subscription-invite-link}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **subscription\_period** (_int_)

  - **subscription\_price** (_int_)

  - **name** (_Optional\[str\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.ChatInviteLink_

### _async method_ `create_forum_topic(self, *, chat_id, name, icon_color = None, icon_custom_emoji_id = None)` {#TelegramAPI-create-forum-topic}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **name** (_str_)

  - **icon\_color** (_Optional\[int\]_)

  - **icon\_custom\_emoji\_id** (_Optional\[str\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.ForumTopic_

### _async method_ `create_invoice_link(self, *, title, description, payload, currency, prices, provider_token = None, max_tip_amount = None, suggested_tip_amounts = None, provider_data = None, photo_url = None, photo_size = None, photo_width = None, photo_height = None, need_name = None, need_phone_number = None, need_email = None, need_shipping_address = None, send_phone_number_to_provider = None, send_email_to_provider = None, is_flexible = None)` {#TelegramAPI-create-invoice-link}

- **Arguments**

  - **title** (_str_)

  - **description** (_str_)

  - **payload** (_str_)

  - **currency** (_str_)

  - **prices** (_list\[alicebot.adapter.telegram.model.LabeledPrice\]_)

  - **provider\_token** (_Optional\[str\]_)

  - **max\_tip\_amount** (_Optional\[int\]_)

  - **suggested\_tip\_amounts** (_Optional\[list\[int\]\]_)

  - **provider\_data** (_Optional\[str\]_)

  - **photo\_url** (_Optional\[str\]_)

  - **photo\_size** (_Optional\[int\]_)

  - **photo\_width** (_Optional\[int\]_)

  - **photo\_height** (_Optional\[int\]_)

  - **need\_name** (_Optional\[bool\]_)

  - **need\_phone\_number** (_Optional\[bool\]_)

  - **need\_email** (_Optional\[bool\]_)

  - **need\_shipping\_address** (_Optional\[bool\]_)

  - **send\_phone\_number\_to\_provider** (_Optional\[bool\]_)

  - **send\_email\_to\_provider** (_Optional\[bool\]_)

  - **is\_flexible** (_Optional\[bool\]_)

- **Returns**

  Type: _str_

### _async method_ `create_new_sticker_set(self, *, user_id, name, title, stickers, sticker_type = None, needs_repainting = None)` {#TelegramAPI-create-new-sticker-set}

- **Arguments**

  - **user\_id** (_int_)

  - **name** (_str_)

  - **title** (_str_)

  - **stickers** (_list\[alicebot.adapter.telegram.model.InputSticker\]_)

  - **sticker\_type** (_Optional\[str\]_)

  - **needs\_repainting** (_Optional\[bool\]_)

- **Returns**

  Type: _bool_

### _async method_ `decline_chat_join_request(self, *, chat_id, user_id)` {#TelegramAPI-decline-chat-join-request}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **user\_id** (_int_)

- **Returns**

  Type: _bool_

### _async method_ `delete_chat_photo(self, *, chat_id)` {#TelegramAPI-delete-chat-photo}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

- **Returns**

  Type: _bool_

### _async method_ `delete_chat_sticker_set(self, *, chat_id)` {#TelegramAPI-delete-chat-sticker-set}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

- **Returns**

  Type: _bool_

### _async method_ `delete_forum_topic(self, *, chat_id, message_thread_id)` {#TelegramAPI-delete-forum-topic}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **message\_thread\_id** (_int_)

- **Returns**

  Type: _bool_

### _async method_ `delete_message(self, *, chat_id, message_id)` {#TelegramAPI-delete-message}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **message\_id** (_int_)

- **Returns**

  Type: _bool_

### _async method_ `delete_messages(self, *, chat_id, message_ids)` {#TelegramAPI-delete-messages}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **message\_ids** (_list\[int\]_)

- **Returns**

  Type: _bool_

### _async method_ `delete_my_commands(self, *, scope = None, language_code = None)` {#TelegramAPI-delete-my-commands}

- **Arguments**

  - **scope** (_Union\[alicebot.adapter.telegram.model.BotCommandScopeDefault, alicebot.adapter.telegram.model.BotCommandScopeAllPrivateChats, alicebot.adapter.telegram.model.BotCommandScopeAllGroupChats, alicebot.adapter.telegram.model.BotCommandScopeAllChatAdministrators, alicebot.adapter.telegram.model.BotCommandScopeChat, alicebot.adapter.telegram.model.BotCommandScopeChatAdministrators, alicebot.adapter.telegram.model.BotCommandScopeChatMember, NoneType\]_)

  - **language\_code** (_Optional\[str\]_)

- **Returns**

  Type: _bool_

### _async method_ `delete_sticker_from_set(self, *, sticker)` {#TelegramAPI-delete-sticker-from-set}

- **Arguments**

  - **sticker** (_str_)

- **Returns**

  Type: _bool_

### _async method_ `delete_sticker_set(self, *, name)` {#TelegramAPI-delete-sticker-set}

- **Arguments**

  - **name** (_str_)

- **Returns**

  Type: _bool_

### _async method_ `delete_webhook(self, *, drop_pending_updates = None)` {#TelegramAPI-delete-webhook}

- **Arguments**

  - **drop\_pending\_updates** (_Optional\[bool\]_)

- **Returns**

  Type: _bool_

### _async method_ `edit_chat_invite_link(self, *, chat_id, invite_link, name = None, expire_date = None, member_limit = None, creates_join_request = None)` {#TelegramAPI-edit-chat-invite-link}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **invite\_link** (_str_)

  - **name** (_Optional\[str\]_)

  - **expire\_date** (_Optional\[int\]_)

  - **member\_limit** (_Optional\[int\]_)

  - **creates\_join\_request** (_Optional\[bool\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.ChatInviteLink_

### _async method_ `edit_chat_subscription_invite_link(self, *, chat_id, invite_link, name = None)` {#TelegramAPI-edit-chat-subscription-invite-link}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **invite\_link** (_str_)

  - **name** (_Optional\[str\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.ChatInviteLink_

### _async method_ `edit_forum_topic(self, *, chat_id, message_thread_id, name = None, icon_custom_emoji_id = None)` {#TelegramAPI-edit-forum-topic}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **message\_thread\_id** (_int_)

  - **name** (_Optional\[str\]_)

  - **icon\_custom\_emoji\_id** (_Optional\[str\]_)

- **Returns**

  Type: _bool_

### _async method_ `edit_general_forum_topic(self, *, chat_id, name)` {#TelegramAPI-edit-general-forum-topic}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **name** (_str_)

- **Returns**

  Type: _bool_

### _async method_ `edit_message_caption(self, *, business_connection_id = None, chat_id = None, message_id = None, inline_message_id = None, caption = None, parse_mode = None, caption_entities = None, show_caption_above_media = None, reply_markup = None)` {#TelegramAPI-edit-message-caption}

- **Arguments**

  - **business\_connection\_id** (_Optional\[str\]_)

  - **chat\_id** (_Union\[int, str, NoneType\]_)

  - **message\_id** (_Optional\[int\]_)

  - **inline\_message\_id** (_Optional\[str\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **show\_caption\_above\_media** (_Optional\[bool\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

- **Returns**

  Type: _Union\[alicebot.adapter.telegram.model.Message, bool\]_

### _async method_ `edit_message_live_location(self, *, latitude, longitude, business_connection_id = None, chat_id = None, message_id = None, inline_message_id = None, live_period = None, horizontal_accuracy = None, heading = None, proximity_alert_radius = None, reply_markup = None)` {#TelegramAPI-edit-message-live-location}

- **Arguments**

  - **latitude** (_float_)

  - **longitude** (_float_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **chat\_id** (_Union\[int, str, NoneType\]_)

  - **message\_id** (_Optional\[int\]_)

  - **inline\_message\_id** (_Optional\[str\]_)

  - **live\_period** (_Optional\[int\]_)

  - **horizontal\_accuracy** (_Optional\[float\]_)

  - **heading** (_Optional\[int\]_)

  - **proximity\_alert\_radius** (_Optional\[int\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

- **Returns**

  Type: _Union\[alicebot.adapter.telegram.model.Message, bool\]_

### _async method_ `edit_message_media(self, *, media, business_connection_id = None, chat_id = None, message_id = None, inline_message_id = None, reply_markup = None)` {#TelegramAPI-edit-message-media}

- **Arguments**

  - **media** (_Union\[alicebot.adapter.telegram.model.InputMediaAnimation, alicebot.adapter.telegram.model.InputMediaDocument, alicebot.adapter.telegram.model.InputMediaAudio, alicebot.adapter.telegram.model.InputMediaPhoto, alicebot.adapter.telegram.model.InputMediaVideo\]_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **chat\_id** (_Union\[int, str, NoneType\]_)

  - **message\_id** (_Optional\[int\]_)

  - **inline\_message\_id** (_Optional\[str\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

- **Returns**

  Type: _Union\[alicebot.adapter.telegram.model.Message, bool\]_

### _async method_ `edit_message_reply_markup(self, *, business_connection_id = None, chat_id = None, message_id = None, inline_message_id = None, reply_markup = None)` {#TelegramAPI-edit-message-reply-markup}

- **Arguments**

  - **business\_connection\_id** (_Optional\[str\]_)

  - **chat\_id** (_Union\[int, str, NoneType\]_)

  - **message\_id** (_Optional\[int\]_)

  - **inline\_message\_id** (_Optional\[str\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

- **Returns**

  Type: _Union\[alicebot.adapter.telegram.model.Message, bool\]_

### _async method_ `edit_message_text(self, *, text, business_connection_id = None, chat_id = None, message_id = None, inline_message_id = None, parse_mode = None, entities = None, link_preview_options = None, reply_markup = None)` {#TelegramAPI-edit-message-text}

- **Arguments**

  - **text** (_str_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **chat\_id** (_Union\[int, str, NoneType\]_)

  - **message\_id** (_Optional\[int\]_)

  - **inline\_message\_id** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **link\_preview\_options** (_Optional\[alicebot.adapter.telegram.model.LinkPreviewOptions\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

- **Returns**

  Type: _Union\[alicebot.adapter.telegram.model.Message, bool\]_

### _async method_ `export_chat_invite_link(self, *, chat_id)` {#TelegramAPI-export-chat-invite-link}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

- **Returns**

  Type: _str_

### _async method_ `forward_message(self, *, chat_id, from_chat_id, message_id, message_thread_id = None, disable_notification = None, protect_content = None)` {#TelegramAPI-forward-message}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **from\_chat\_id** (_Union\[int, str\]_)

  - **message\_id** (_int_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.Message_

### _async method_ `forward_messages(self, *, chat_id, from_chat_id, message_ids, message_thread_id = None, disable_notification = None, protect_content = None)` {#TelegramAPI-forward-messages}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **from\_chat\_id** (_Union\[int, str\]_)

  - **message\_ids** (_list\[int\]_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

- **Returns**

  Type: _list\[alicebot.adapter.telegram.model.MessageId\]_

### _async method_ `get_business_connection(self, *, business_connection_id)` {#TelegramAPI-get-business-connection}

- **Arguments**

  - **business\_connection\_id** (_str_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.BusinessConnection_

### _async method_ `get_chat(self, *, chat_id)` {#TelegramAPI-get-chat}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.ChatFullInfo_

### _async method_ `get_chat_administrators(self, *, chat_id)` {#TelegramAPI-get-chat-administrators}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

- **Returns**

  Type: _list\[typing.Union\[alicebot.adapter.telegram.model.ChatMemberOwner, alicebot.adapter.telegram.model.ChatMemberAdministrator, alicebot.adapter.telegram.model.ChatMemberMember, alicebot.adapter.telegram.model.ChatMemberRestricted, alicebot.adapter.telegram.model.ChatMemberLeft, alicebot.adapter.telegram.model.ChatMemberBanned\]\]_

### _async method_ `get_chat_member(self, *, chat_id, user_id)` {#TelegramAPI-get-chat-member}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **user\_id** (_int_)

- **Returns**

  Type: _Union\[alicebot.adapter.telegram.model.ChatMemberOwner, alicebot.adapter.telegram.model.ChatMemberAdministrator, alicebot.adapter.telegram.model.ChatMemberMember, alicebot.adapter.telegram.model.ChatMemberRestricted, alicebot.adapter.telegram.model.ChatMemberLeft, alicebot.adapter.telegram.model.ChatMemberBanned\]_

### _async method_ `get_chat_member_count(self, *, chat_id)` {#TelegramAPI-get-chat-member-count}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

- **Returns**

  Type: _int_

### _async method_ `get_chat_menu_button(self, *, chat_id = None)` {#TelegramAPI-get-chat-menu-button}

- **Arguments**

  - **chat\_id** (_Optional\[int\]_)

- **Returns**

  Type: _Union\[alicebot.adapter.telegram.model.MenuButtonCommands, alicebot.adapter.telegram.model.MenuButtonWebApp, alicebot.adapter.telegram.model.MenuButtonDefault\]_

### _async method_ `get_custom_emoji_stickers(self, *, custom_emoji_ids)` {#TelegramAPI-get-custom-emoji-stickers}

- **Arguments**

  - **custom\_emoji\_ids** (_list\[str\]_)

- **Returns**

  Type: _list\[alicebot.adapter.telegram.model.Sticker\]_

### _async method_ `get_file(self, *, file_id)` {#TelegramAPI-get-file}

- **Arguments**

  - **file\_id** (_str_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.File_

### _async method_ `get_forum_topic_icon_stickers(self)` {#TelegramAPI-get-forum-topic-icon-stickers}

- **Returns**

  Type: _list\[alicebot.adapter.telegram.model.Sticker\]_

### _async method_ `get_game_high_scores(self, *, user_id, chat_id = None, message_id = None, inline_message_id = None)` {#TelegramAPI-get-game-high-scores}

- **Arguments**

  - **user\_id** (_int_)

  - **chat\_id** (_Optional\[int\]_)

  - **message\_id** (_Optional\[int\]_)

  - **inline\_message\_id** (_Optional\[str\]_)

- **Returns**

  Type: _list\[alicebot.adapter.telegram.model.GameHighScore\]_

### _async method_ `get_me(self)` {#TelegramAPI-get-me}

- **Returns**

  Type: _alicebot.adapter.telegram.model.User_

### _async method_ `get_my_commands(self, *, scope = None, language_code = None)` {#TelegramAPI-get-my-commands}

- **Arguments**

  - **scope** (_Union\[alicebot.adapter.telegram.model.BotCommandScopeDefault, alicebot.adapter.telegram.model.BotCommandScopeAllPrivateChats, alicebot.adapter.telegram.model.BotCommandScopeAllGroupChats, alicebot.adapter.telegram.model.BotCommandScopeAllChatAdministrators, alicebot.adapter.telegram.model.BotCommandScopeChat, alicebot.adapter.telegram.model.BotCommandScopeChatAdministrators, alicebot.adapter.telegram.model.BotCommandScopeChatMember, NoneType\]_)

  - **language\_code** (_Optional\[str\]_)

- **Returns**

  Type: _list\[alicebot.adapter.telegram.model.BotCommand\]_

### _async method_ `get_my_default_administrator_rights(self, *, for_channels = None)` {#TelegramAPI-get-my-default-administrator-rights}

- **Arguments**

  - **for\_channels** (_Optional\[bool\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.ChatAdministratorRights_

### _async method_ `get_my_description(self, *, language_code = None)` {#TelegramAPI-get-my-description}

- **Arguments**

  - **language\_code** (_Optional\[str\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.BotDescription_

### _async method_ `get_my_name(self, *, language_code = None)` {#TelegramAPI-get-my-name}

- **Arguments**

  - **language\_code** (_Optional\[str\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.BotName_

### _async method_ `get_my_short_description(self, *, language_code = None)` {#TelegramAPI-get-my-short-description}

- **Arguments**

  - **language\_code** (_Optional\[str\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.BotShortDescription_

### _async method_ `get_star_transactions(self, *, offset = None, limit = None)` {#TelegramAPI-get-star-transactions}

- **Arguments**

  - **offset** (_Optional\[int\]_)

  - **limit** (_Optional\[int\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.StarTransactions_

### _async method_ `get_sticker_set(self, *, name)` {#TelegramAPI-get-sticker-set}

- **Arguments**

  - **name** (_str_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.StickerSet_

### _async method_ `get_updates(self, *, offset = None, limit = None, timeout = None, allowed_updates = None)` {#TelegramAPI-get-updates}

- **Arguments**

  - **offset** (_Optional\[int\]_)

  - **limit** (_Optional\[int\]_)

  - **timeout** (_Optional\[int\]_)

  - **allowed\_updates** (_Optional\[list\[str\]\]_)

- **Returns**

  Type: _list\[alicebot.adapter.telegram.model.Update\]_

### _async method_ `get_user_chat_boosts(self, *, chat_id, user_id)` {#TelegramAPI-get-user-chat-boosts}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **user\_id** (_int_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.UserChatBoosts_

### _async method_ `get_user_profile_photos(self, *, user_id, offset = None, limit = None)` {#TelegramAPI-get-user-profile-photos}

- **Arguments**

  - **user\_id** (_int_)

  - **offset** (_Optional\[int\]_)

  - **limit** (_Optional\[int\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.UserProfilePhotos_

### _async method_ `get_webhook_info(self)` {#TelegramAPI-get-webhook-info}

- **Returns**

  Type: _alicebot.adapter.telegram.model.WebhookInfo_

### _async method_ `hide_general_forum_topic(self, *, chat_id)` {#TelegramAPI-hide-general-forum-topic}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

- **Returns**

  Type: _bool_

### _async method_ `leave_chat(self, *, chat_id)` {#TelegramAPI-leave-chat}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

- **Returns**

  Type: _bool_

### _async method_ `log_out(self)` {#TelegramAPI-log-out}

- **Returns**

  Type: _bool_

### _async method_ `pin_chat_message(self, *, chat_id, message_id, business_connection_id = None, disable_notification = None)` {#TelegramAPI-pin-chat-message}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **message\_id** (_int_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **disable\_notification** (_Optional\[bool\]_)

- **Returns**

  Type: _bool_

### _async method_ `promote_chat_member(self, *, chat_id, user_id, is_anonymous = None, can_manage_chat = None, can_delete_messages = None, can_manage_video_chats = None, can_restrict_members = None, can_promote_members = None, can_change_info = None, can_invite_users = None, can_post_stories = None, can_edit_stories = None, can_delete_stories = None, can_post_messages = None, can_edit_messages = None, can_pin_messages = None, can_manage_topics = None)` {#TelegramAPI-promote-chat-member}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **user\_id** (_int_)

  - **is\_anonymous** (_Optional\[bool\]_)

  - **can\_manage\_chat** (_Optional\[bool\]_)

  - **can\_delete\_messages** (_Optional\[bool\]_)

  - **can\_manage\_video\_chats** (_Optional\[bool\]_)

  - **can\_restrict\_members** (_Optional\[bool\]_)

  - **can\_promote\_members** (_Optional\[bool\]_)

  - **can\_change\_info** (_Optional\[bool\]_)

  - **can\_invite\_users** (_Optional\[bool\]_)

  - **can\_post\_stories** (_Optional\[bool\]_)

  - **can\_edit\_stories** (_Optional\[bool\]_)

  - **can\_delete\_stories** (_Optional\[bool\]_)

  - **can\_post\_messages** (_Optional\[bool\]_)

  - **can\_edit\_messages** (_Optional\[bool\]_)

  - **can\_pin\_messages** (_Optional\[bool\]_)

  - **can\_manage\_topics** (_Optional\[bool\]_)

- **Returns**

  Type: _bool_

### _async method_ `refund_star_payment(self, *, user_id, telegram_payment_charge_id)` {#TelegramAPI-refund-star-payment}

- **Arguments**

  - **user\_id** (_int_)

  - **telegram\_payment\_charge\_id** (_str_)

- **Returns**

  Type: _bool_

### _async method_ `reopen_forum_topic(self, *, chat_id, message_thread_id)` {#TelegramAPI-reopen-forum-topic}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **message\_thread\_id** (_int_)

- **Returns**

  Type: _bool_

### _async method_ `reopen_general_forum_topic(self, *, chat_id)` {#TelegramAPI-reopen-general-forum-topic}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

- **Returns**

  Type: _bool_

### _async method_ `replace_sticker_in_set(self, *, user_id, name, old_sticker, sticker)` {#TelegramAPI-replace-sticker-in-set}

- **Arguments**

  - **user\_id** (_int_)

  - **name** (_str_)

  - **old\_sticker** (_str_)

  - **sticker** (_alicebot.adapter.telegram.model.InputSticker_)

- **Returns**

  Type: _bool_

### _async method_ `restrict_chat_member(self, *, chat_id, user_id, permissions, use_independent_chat_permissions = None, until_date = None)` {#TelegramAPI-restrict-chat-member}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **user\_id** (_int_)

  - **permissions** (_alicebot.adapter.telegram.model.ChatPermissions_)

  - **use\_independent\_chat\_permissions** (_Optional\[bool\]_)

  - **until\_date** (_Optional\[int\]_)

- **Returns**

  Type: _bool_

### _async method_ `revoke_chat_invite_link(self, *, chat_id, invite_link)` {#TelegramAPI-revoke-chat-invite-link}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **invite\_link** (_str_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.ChatInviteLink_

### _async method_ `send_animation(self, *, chat_id, animation, business_connection_id = None, message_thread_id = None, duration = None, width = None, height = None, thumbnail = None, caption = None, parse_mode = None, caption_entities = None, show_caption_above_media = None, has_spoiler = None, disable_notification = None, protect_content = None, message_effect_id = None, reply_parameters = None, reply_markup = None)` {#TelegramAPI-send-animation}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **animation** (_Union\[bytes, tuple\[str, bytes\], str\]_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **duration** (_Optional\[int\]_)

  - **width** (_Optional\[int\]_)

  - **height** (_Optional\[int\]_)

  - **thumbnail** (_Union\[bytes, tuple\[str, bytes\], str, NoneType\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **show\_caption\_above\_media** (_Optional\[bool\]_)

  - **has\_spoiler** (_Optional\[bool\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **message\_effect\_id** (_Optional\[str\]_)

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_)

  - **reply\_markup** (_Union\[alicebot.adapter.telegram.model.InlineKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardRemove, alicebot.adapter.telegram.model.ForceReply, NoneType\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.Message_

### _async method_ `send_audio(self, *, chat_id, audio, business_connection_id = None, message_thread_id = None, caption = None, parse_mode = None, caption_entities = None, duration = None, performer = None, title = None, thumbnail = None, disable_notification = None, protect_content = None, message_effect_id = None, reply_parameters = None, reply_markup = None)` {#TelegramAPI-send-audio}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **audio** (_Union\[bytes, tuple\[str, bytes\], str\]_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **duration** (_Optional\[int\]_)

  - **performer** (_Optional\[str\]_)

  - **title** (_Optional\[str\]_)

  - **thumbnail** (_Union\[bytes, tuple\[str, bytes\], str, NoneType\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **message\_effect\_id** (_Optional\[str\]_)

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_)

  - **reply\_markup** (_Union\[alicebot.adapter.telegram.model.InlineKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardRemove, alicebot.adapter.telegram.model.ForceReply, NoneType\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.Message_

### _async method_ `send_chat_action(self, *, chat_id, action, business_connection_id = None, message_thread_id = None)` {#TelegramAPI-send-chat-action}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **action** (_str_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **message\_thread\_id** (_Optional\[int\]_)

- **Returns**

  Type: _bool_

### _async method_ `send_contact(self, *, chat_id, phone_number, first_name, business_connection_id = None, message_thread_id = None, last_name = None, vcard = None, disable_notification = None, protect_content = None, message_effect_id = None, reply_parameters = None, reply_markup = None)` {#TelegramAPI-send-contact}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **phone\_number** (_str_)

  - **first\_name** (_str_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **last\_name** (_Optional\[str\]_)

  - **vcard** (_Optional\[str\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **message\_effect\_id** (_Optional\[str\]_)

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_)

  - **reply\_markup** (_Union\[alicebot.adapter.telegram.model.InlineKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardRemove, alicebot.adapter.telegram.model.ForceReply, NoneType\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.Message_

### _async method_ `send_dice(self, *, chat_id, business_connection_id = None, message_thread_id = None, emoji = None, disable_notification = None, protect_content = None, message_effect_id = None, reply_parameters = None, reply_markup = None)` {#TelegramAPI-send-dice}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **emoji** (_Optional\[str\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **message\_effect\_id** (_Optional\[str\]_)

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_)

  - **reply\_markup** (_Union\[alicebot.adapter.telegram.model.InlineKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardRemove, alicebot.adapter.telegram.model.ForceReply, NoneType\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.Message_

### _async method_ `send_document(self, *, chat_id, document, business_connection_id = None, message_thread_id = None, thumbnail = None, caption = None, parse_mode = None, caption_entities = None, disable_content_type_detection = None, disable_notification = None, protect_content = None, message_effect_id = None, reply_parameters = None, reply_markup = None)` {#TelegramAPI-send-document}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **document** (_Union\[bytes, tuple\[str, bytes\], str\]_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **thumbnail** (_Union\[bytes, tuple\[str, bytes\], str, NoneType\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **disable\_content\_type\_detection** (_Optional\[bool\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **message\_effect\_id** (_Optional\[str\]_)

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_)

  - **reply\_markup** (_Union\[alicebot.adapter.telegram.model.InlineKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardRemove, alicebot.adapter.telegram.model.ForceReply, NoneType\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.Message_

### _async method_ `send_game(self, *, chat_id, game_short_name, business_connection_id = None, message_thread_id = None, disable_notification = None, protect_content = None, message_effect_id = None, reply_parameters = None, reply_markup = None)` {#TelegramAPI-send-game}

- **Arguments**

  - **chat\_id** (_int_)

  - **game\_short\_name** (_str_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **message\_effect\_id** (_Optional\[str\]_)

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.Message_

### _async method_ `send_invoice(self, *, chat_id, title, description, payload, currency, prices, message_thread_id = None, provider_token = None, max_tip_amount = None, suggested_tip_amounts = None, start_parameter = None, provider_data = None, photo_url = None, photo_size = None, photo_width = None, photo_height = None, need_name = None, need_phone_number = None, need_email = None, need_shipping_address = None, send_phone_number_to_provider = None, send_email_to_provider = None, is_flexible = None, disable_notification = None, protect_content = None, message_effect_id = None, reply_parameters = None, reply_markup = None)` {#TelegramAPI-send-invoice}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **title** (_str_)

  - **description** (_str_)

  - **payload** (_str_)

  - **currency** (_str_)

  - **prices** (_list\[alicebot.adapter.telegram.model.LabeledPrice\]_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **provider\_token** (_Optional\[str\]_)

  - **max\_tip\_amount** (_Optional\[int\]_)

  - **suggested\_tip\_amounts** (_Optional\[list\[int\]\]_)

  - **start\_parameter** (_Optional\[str\]_)

  - **provider\_data** (_Optional\[str\]_)

  - **photo\_url** (_Optional\[str\]_)

  - **photo\_size** (_Optional\[int\]_)

  - **photo\_width** (_Optional\[int\]_)

  - **photo\_height** (_Optional\[int\]_)

  - **need\_name** (_Optional\[bool\]_)

  - **need\_phone\_number** (_Optional\[bool\]_)

  - **need\_email** (_Optional\[bool\]_)

  - **need\_shipping\_address** (_Optional\[bool\]_)

  - **send\_phone\_number\_to\_provider** (_Optional\[bool\]_)

  - **send\_email\_to\_provider** (_Optional\[bool\]_)

  - **is\_flexible** (_Optional\[bool\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **message\_effect\_id** (_Optional\[str\]_)

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.Message_

### _async method_ `send_location(self, *, chat_id, latitude, longitude, business_connection_id = None, message_thread_id = None, horizontal_accuracy = None, live_period = None, heading = None, proximity_alert_radius = None, disable_notification = None, protect_content = None, message_effect_id = None, reply_parameters = None, reply_markup = None)` {#TelegramAPI-send-location}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **latitude** (_float_)

  - **longitude** (_float_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **horizontal\_accuracy** (_Optional\[float\]_)

  - **live\_period** (_Optional\[int\]_)

  - **heading** (_Optional\[int\]_)

  - **proximity\_alert\_radius** (_Optional\[int\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **message\_effect\_id** (_Optional\[str\]_)

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_)

  - **reply\_markup** (_Union\[alicebot.adapter.telegram.model.InlineKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardRemove, alicebot.adapter.telegram.model.ForceReply, NoneType\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.Message_

### _async method_ `send_media_group(self, *, chat_id, media, business_connection_id = None, message_thread_id = None, disable_notification = None, protect_content = None, message_effect_id = None, reply_parameters = None)` {#TelegramAPI-send-media-group}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **media** (_Union\[list\[alicebot.adapter.telegram.model.InputMediaAudio\], list\[alicebot.adapter.telegram.model.InputMediaDocument\], list\[alicebot.adapter.telegram.model.InputMediaPhoto\], list\[alicebot.adapter.telegram.model.InputMediaVideo\]\]_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **message\_effect\_id** (_Optional\[str\]_)

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_)

- **Returns**

  Type: _list\[alicebot.adapter.telegram.model.Message\]_

### _async method_ `send_message(self, *, chat_id, text, business_connection_id = None, message_thread_id = None, parse_mode = None, entities = None, link_preview_options = None, disable_notification = None, protect_content = None, message_effect_id = None, reply_parameters = None, reply_markup = None)` {#TelegramAPI-send-message}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **text** (_str_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **link\_preview\_options** (_Optional\[alicebot.adapter.telegram.model.LinkPreviewOptions\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **message\_effect\_id** (_Optional\[str\]_)

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_)

  - **reply\_markup** (_Union\[alicebot.adapter.telegram.model.InlineKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardRemove, alicebot.adapter.telegram.model.ForceReply, NoneType\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.Message_

### _async method_ `send_paid_media(self, *, chat_id, star_count, media, business_connection_id = None, payload = None, caption = None, parse_mode = None, caption_entities = None, show_caption_above_media = None, disable_notification = None, protect_content = None, reply_parameters = None, reply_markup = None)` {#TelegramAPI-send-paid-media}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **star\_count** (_int_)

  - **media** (_list\[typing.Union\[alicebot.adapter.telegram.model.InputPaidMediaPhoto, alicebot.adapter.telegram.model.InputPaidMediaVideo\]\]_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **payload** (_Optional\[str\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **show\_caption\_above\_media** (_Optional\[bool\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_)

  - **reply\_markup** (_Union\[alicebot.adapter.telegram.model.InlineKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardRemove, alicebot.adapter.telegram.model.ForceReply, NoneType\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.Message_

### _async method_ `send_photo(self, *, chat_id, photo, business_connection_id = None, message_thread_id = None, caption = None, parse_mode = None, caption_entities = None, show_caption_above_media = None, has_spoiler = None, disable_notification = None, protect_content = None, message_effect_id = None, reply_parameters = None, reply_markup = None)` {#TelegramAPI-send-photo}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **photo** (_Union\[bytes, tuple\[str, bytes\], str\]_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **show\_caption\_above\_media** (_Optional\[bool\]_)

  - **has\_spoiler** (_Optional\[bool\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **message\_effect\_id** (_Optional\[str\]_)

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_)

  - **reply\_markup** (_Union\[alicebot.adapter.telegram.model.InlineKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardRemove, alicebot.adapter.telegram.model.ForceReply, NoneType\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.Message_

### _async method_ `send_poll(self, *, chat_id, question, options, business_connection_id = None, message_thread_id = None, question_parse_mode = None, question_entities = None, is_anonymous = None, type = None, allows_multiple_answers = None, correct_option_id = None, explanation = None, explanation_parse_mode = None, explanation_entities = None, open_period = None, close_date = None, is_closed = None, disable_notification = None, protect_content = None, message_effect_id = None, reply_parameters = None, reply_markup = None)` {#TelegramAPI-send-poll}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **question** (_str_)

  - **options** (_list\[alicebot.adapter.telegram.model.InputPollOption\]_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **question\_parse\_mode** (_Optional\[str\]_)

  - **question\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **is\_anonymous** (_Optional\[bool\]_)

  - **type** (_Optional\[str\]_)

  - **allows\_multiple\_answers** (_Optional\[bool\]_)

  - **correct\_option\_id** (_Optional\[int\]_)

  - **explanation** (_Optional\[str\]_)

  - **explanation\_parse\_mode** (_Optional\[str\]_)

  - **explanation\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **open\_period** (_Optional\[int\]_)

  - **close\_date** (_Optional\[int\]_)

  - **is\_closed** (_Optional\[bool\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **message\_effect\_id** (_Optional\[str\]_)

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_)

  - **reply\_markup** (_Union\[alicebot.adapter.telegram.model.InlineKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardRemove, alicebot.adapter.telegram.model.ForceReply, NoneType\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.Message_

### _async method_ `send_sticker(self, *, chat_id, sticker, business_connection_id = None, message_thread_id = None, emoji = None, disable_notification = None, protect_content = None, message_effect_id = None, reply_parameters = None, reply_markup = None)` {#TelegramAPI-send-sticker}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **sticker** (_Union\[bytes, tuple\[str, bytes\], str\]_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **emoji** (_Optional\[str\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **message\_effect\_id** (_Optional\[str\]_)

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_)

  - **reply\_markup** (_Union\[alicebot.adapter.telegram.model.InlineKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardRemove, alicebot.adapter.telegram.model.ForceReply, NoneType\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.Message_

### _async method_ `send_venue(self, *, chat_id, latitude, longitude, title, address, business_connection_id = None, message_thread_id = None, foursquare_id = None, foursquare_type = None, google_place_id = None, google_place_type = None, disable_notification = None, protect_content = None, message_effect_id = None, reply_parameters = None, reply_markup = None)` {#TelegramAPI-send-venue}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **latitude** (_float_)

  - **longitude** (_float_)

  - **title** (_str_)

  - **address** (_str_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **foursquare\_id** (_Optional\[str\]_)

  - **foursquare\_type** (_Optional\[str\]_)

  - **google\_place\_id** (_Optional\[str\]_)

  - **google\_place\_type** (_Optional\[str\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **message\_effect\_id** (_Optional\[str\]_)

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_)

  - **reply\_markup** (_Union\[alicebot.adapter.telegram.model.InlineKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardRemove, alicebot.adapter.telegram.model.ForceReply, NoneType\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.Message_

### _async method_ `send_video(self, *, chat_id, video, business_connection_id = None, message_thread_id = None, duration = None, width = None, height = None, thumbnail = None, caption = None, parse_mode = None, caption_entities = None, show_caption_above_media = None, has_spoiler = None, supports_streaming = None, disable_notification = None, protect_content = None, message_effect_id = None, reply_parameters = None, reply_markup = None)` {#TelegramAPI-send-video}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **video** (_Union\[bytes, tuple\[str, bytes\], str\]_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **duration** (_Optional\[int\]_)

  - **width** (_Optional\[int\]_)

  - **height** (_Optional\[int\]_)

  - **thumbnail** (_Union\[bytes, tuple\[str, bytes\], str, NoneType\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **show\_caption\_above\_media** (_Optional\[bool\]_)

  - **has\_spoiler** (_Optional\[bool\]_)

  - **supports\_streaming** (_Optional\[bool\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **message\_effect\_id** (_Optional\[str\]_)

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_)

  - **reply\_markup** (_Union\[alicebot.adapter.telegram.model.InlineKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardRemove, alicebot.adapter.telegram.model.ForceReply, NoneType\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.Message_

### _async method_ `send_video_note(self, *, chat_id, video_note, business_connection_id = None, message_thread_id = None, duration = None, length = None, thumbnail = None, disable_notification = None, protect_content = None, message_effect_id = None, reply_parameters = None, reply_markup = None)` {#TelegramAPI-send-video-note}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **video\_note** (_Union\[bytes, tuple\[str, bytes\], str\]_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **duration** (_Optional\[int\]_)

  - **length** (_Optional\[int\]_)

  - **thumbnail** (_Union\[bytes, tuple\[str, bytes\], str, NoneType\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **message\_effect\_id** (_Optional\[str\]_)

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_)

  - **reply\_markup** (_Union\[alicebot.adapter.telegram.model.InlineKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardRemove, alicebot.adapter.telegram.model.ForceReply, NoneType\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.Message_

### _async method_ `send_voice(self, *, chat_id, voice, business_connection_id = None, message_thread_id = None, caption = None, parse_mode = None, caption_entities = None, duration = None, disable_notification = None, protect_content = None, message_effect_id = None, reply_parameters = None, reply_markup = None)` {#TelegramAPI-send-voice}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **voice** (_Union\[bytes, tuple\[str, bytes\], str\]_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **message\_thread\_id** (_Optional\[int\]_)

  - **caption** (_Optional\[str\]_)

  - **parse\_mode** (_Optional\[str\]_)

  - **caption\_entities** (_Optional\[list\[alicebot.adapter.telegram.model.MessageEntity\]\]_)

  - **duration** (_Optional\[int\]_)

  - **disable\_notification** (_Optional\[bool\]_)

  - **protect\_content** (_Optional\[bool\]_)

  - **message\_effect\_id** (_Optional\[str\]_)

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_)

  - **reply\_markup** (_Union\[alicebot.adapter.telegram.model.InlineKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardRemove, alicebot.adapter.telegram.model.ForceReply, NoneType\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.Message_

### _async method_ `set_chat_administrator_custom_title(self, *, chat_id, user_id, custom_title)` {#TelegramAPI-set-chat-administrator-custom-title}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **user\_id** (_int_)

  - **custom\_title** (_str_)

- **Returns**

  Type: _bool_

### _async method_ `set_chat_description(self, *, chat_id, description = None)` {#TelegramAPI-set-chat-description}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **description** (_Optional\[str\]_)

- **Returns**

  Type: _bool_

### _async method_ `set_chat_menu_button(self, *, chat_id = None, menu_button = None)` {#TelegramAPI-set-chat-menu-button}

- **Arguments**

  - **chat\_id** (_Optional\[int\]_)

  - **menu\_button** (_Union\[alicebot.adapter.telegram.model.MenuButtonCommands, alicebot.adapter.telegram.model.MenuButtonWebApp, alicebot.adapter.telegram.model.MenuButtonDefault, NoneType\]_)

- **Returns**

  Type: _bool_

### _async method_ `set_chat_permissions(self, *, chat_id, permissions, use_independent_chat_permissions = None)` {#TelegramAPI-set-chat-permissions}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **permissions** (_alicebot.adapter.telegram.model.ChatPermissions_)

  - **use\_independent\_chat\_permissions** (_Optional\[bool\]_)

- **Returns**

  Type: _bool_

### _async method_ `set_chat_photo(self, *, chat_id, photo)` {#TelegramAPI-set-chat-photo}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **photo** (_Union\[bytes, tuple\[str, bytes\]\]_)

- **Returns**

  Type: _bool_

### _async method_ `set_chat_sticker_set(self, *, chat_id, sticker_set_name)` {#TelegramAPI-set-chat-sticker-set}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **sticker\_set\_name** (_str_)

- **Returns**

  Type: _bool_

### _async method_ `set_chat_title(self, *, chat_id, title)` {#TelegramAPI-set-chat-title}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **title** (_str_)

- **Returns**

  Type: _bool_

### _async method_ `set_custom_emoji_sticker_set_thumbnail(self, *, name, custom_emoji_id = None)` {#TelegramAPI-set-custom-emoji-sticker-set-thumbnail}

- **Arguments**

  - **name** (_str_)

  - **custom\_emoji\_id** (_Optional\[str\]_)

- **Returns**

  Type: _bool_

### _async method_ `set_game_score(self, *, user_id, score, force = None, disable_edit_message = None, chat_id = None, message_id = None, inline_message_id = None)` {#TelegramAPI-set-game-score}

- **Arguments**

  - **user\_id** (_int_)

  - **score** (_int_)

  - **force** (_Optional\[bool\]_)

  - **disable\_edit\_message** (_Optional\[bool\]_)

  - **chat\_id** (_Optional\[int\]_)

  - **message\_id** (_Optional\[int\]_)

  - **inline\_message\_id** (_Optional\[str\]_)

- **Returns**

  Type: _Union\[alicebot.adapter.telegram.model.Message, bool\]_

### _async method_ `set_message_reaction(self, *, chat_id, message_id, reaction = None, is_big = None)` {#TelegramAPI-set-message-reaction}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **message\_id** (_int_)

  - **reaction** (_Optional\[list\[Union\[alicebot.adapter.telegram.model.ReactionTypeEmoji, alicebot.adapter.telegram.model.ReactionTypeCustomEmoji, alicebot.adapter.telegram.model.ReactionTypePaid\]\]\]_)

  - **is\_big** (_Optional\[bool\]_)

- **Returns**

  Type: _bool_

### _async method_ `set_my_commands(self, *, commands, scope = None, language_code = None)` {#TelegramAPI-set-my-commands}

- **Arguments**

  - **commands** (_list\[alicebot.adapter.telegram.model.BotCommand\]_)

  - **scope** (_Union\[alicebot.adapter.telegram.model.BotCommandScopeDefault, alicebot.adapter.telegram.model.BotCommandScopeAllPrivateChats, alicebot.adapter.telegram.model.BotCommandScopeAllGroupChats, alicebot.adapter.telegram.model.BotCommandScopeAllChatAdministrators, alicebot.adapter.telegram.model.BotCommandScopeChat, alicebot.adapter.telegram.model.BotCommandScopeChatAdministrators, alicebot.adapter.telegram.model.BotCommandScopeChatMember, NoneType\]_)

  - **language\_code** (_Optional\[str\]_)

- **Returns**

  Type: _bool_

### _async method_ `set_my_default_administrator_rights(self, *, rights = None, for_channels = None)` {#TelegramAPI-set-my-default-administrator-rights}

- **Arguments**

  - **rights** (_Optional\[alicebot.adapter.telegram.model.ChatAdministratorRights\]_)

  - **for\_channels** (_Optional\[bool\]_)

- **Returns**

  Type: _bool_

### _async method_ `set_my_description(self, *, description = None, language_code = None)` {#TelegramAPI-set-my-description}

- **Arguments**

  - **description** (_Optional\[str\]_)

  - **language\_code** (_Optional\[str\]_)

- **Returns**

  Type: _bool_

### _async method_ `set_my_name(self, *, name = None, language_code = None)` {#TelegramAPI-set-my-name}

- **Arguments**

  - **name** (_Optional\[str\]_)

  - **language\_code** (_Optional\[str\]_)

- **Returns**

  Type: _bool_

### _async method_ `set_my_short_description(self, *, short_description = None, language_code = None)` {#TelegramAPI-set-my-short-description}

- **Arguments**

  - **short\_description** (_Optional\[str\]_)

  - **language\_code** (_Optional\[str\]_)

- **Returns**

  Type: _bool_

### _async method_ `set_passport_data_errors(self, *, user_id, errors)` {#TelegramAPI-set-passport-data-errors}

- **Arguments**

  - **user\_id** (_int_)

  - **errors** (_list\[typing.Union\[alicebot.adapter.telegram.model.PassportElementErrorDataField, alicebot.adapter.telegram.model.PassportElementErrorFrontSide, alicebot.adapter.telegram.model.PassportElementErrorReverseSide, alicebot.adapter.telegram.model.PassportElementErrorSelfie, alicebot.adapter.telegram.model.PassportElementErrorFile, alicebot.adapter.telegram.model.PassportElementErrorFiles, alicebot.adapter.telegram.model.PassportElementErrorTranslationFile, alicebot.adapter.telegram.model.PassportElementErrorTranslationFiles, alicebot.adapter.telegram.model.PassportElementErrorUnspecified\]\]_)

- **Returns**

  Type: _bool_

### _async method_ `set_sticker_emoji_list(self, *, sticker, emoji_list)` {#TelegramAPI-set-sticker-emoji-list}

- **Arguments**

  - **sticker** (_str_)

  - **emoji\_list** (_list\[str\]_)

- **Returns**

  Type: _bool_

### _async method_ `set_sticker_keywords(self, *, sticker, keywords = None)` {#TelegramAPI-set-sticker-keywords}

- **Arguments**

  - **sticker** (_str_)

  - **keywords** (_Optional\[list\[str\]\]_)

- **Returns**

  Type: _bool_

### _async method_ `set_sticker_mask_position(self, *, sticker, mask_position = None)` {#TelegramAPI-set-sticker-mask-position}

- **Arguments**

  - **sticker** (_str_)

  - **mask\_position** (_Optional\[alicebot.adapter.telegram.model.MaskPosition\]_)

- **Returns**

  Type: _bool_

### _async method_ `set_sticker_position_in_set(self, *, sticker, position)` {#TelegramAPI-set-sticker-position-in-set}

- **Arguments**

  - **sticker** (_str_)

  - **position** (_int_)

- **Returns**

  Type: _bool_

### _async method_ `set_sticker_set_thumbnail(self, *, name, user_id, format, thumbnail = None)` {#TelegramAPI-set-sticker-set-thumbnail}

- **Arguments**

  - **name** (_str_)

  - **user\_id** (_int_)

  - **format** (_str_)

  - **thumbnail** (_Union\[bytes, tuple\[str, bytes\], str, NoneType\]_)

- **Returns**

  Type: _bool_

### _async method_ `set_sticker_set_title(self, *, name, title)` {#TelegramAPI-set-sticker-set-title}

- **Arguments**

  - **name** (_str_)

  - **title** (_str_)

- **Returns**

  Type: _bool_

### _async method_ `set_webhook(self, *, url, certificate = None, ip_address = None, max_connections = None, allowed_updates = None, drop_pending_updates = None, secret_token = None)` {#TelegramAPI-set-webhook}

- **Arguments**

  - **url** (_str_)

  - **certificate** (_Union\[bytes, tuple\[str, bytes\], NoneType\]_)

  - **ip\_address** (_Optional\[str\]_)

  - **max\_connections** (_Optional\[int\]_)

  - **allowed\_updates** (_Optional\[list\[str\]\]_)

  - **drop\_pending\_updates** (_Optional\[bool\]_)

  - **secret\_token** (_Optional\[str\]_)

- **Returns**

  Type: _bool_

### _async method_ `stop_message_live_location(self, *, business_connection_id = None, chat_id = None, message_id = None, inline_message_id = None, reply_markup = None)` {#TelegramAPI-stop-message-live-location}

- **Arguments**

  - **business\_connection\_id** (_Optional\[str\]_)

  - **chat\_id** (_Union\[int, str, NoneType\]_)

  - **message\_id** (_Optional\[int\]_)

  - **inline\_message\_id** (_Optional\[str\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

- **Returns**

  Type: _Union\[alicebot.adapter.telegram.model.Message, bool\]_

### _async method_ `stop_poll(self, *, chat_id, message_id, business_connection_id = None, reply_markup = None)` {#TelegramAPI-stop-poll}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **message\_id** (_int_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **reply\_markup** (_Optional\[alicebot.adapter.telegram.model.InlineKeyboardMarkup\]_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.Poll_

### _async method_ `unban_chat_member(self, *, chat_id, user_id, only_if_banned = None)` {#TelegramAPI-unban-chat-member}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **user\_id** (_int_)

  - **only\_if\_banned** (_Optional\[bool\]_)

- **Returns**

  Type: _bool_

### _async method_ `unban_chat_sender_chat(self, *, chat_id, sender_chat_id)` {#TelegramAPI-unban-chat-sender-chat}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **sender\_chat\_id** (_int_)

- **Returns**

  Type: _bool_

### _async method_ `unhide_general_forum_topic(self, *, chat_id)` {#TelegramAPI-unhide-general-forum-topic}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

- **Returns**

  Type: _bool_

### _async method_ `unpin_all_chat_messages(self, *, chat_id)` {#TelegramAPI-unpin-all-chat-messages}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

- **Returns**

  Type: _bool_

### _async method_ `unpin_all_forum_topic_messages(self, *, chat_id, message_thread_id)` {#TelegramAPI-unpin-all-forum-topic-messages}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **message\_thread\_id** (_int_)

- **Returns**

  Type: _bool_

### _async method_ `unpin_all_general_forum_topic_messages(self, *, chat_id)` {#TelegramAPI-unpin-all-general-forum-topic-messages}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

- **Returns**

  Type: _bool_

### _async method_ `unpin_chat_message(self, *, chat_id, business_connection_id = None, message_id = None)` {#TelegramAPI-unpin-chat-message}

- **Arguments**

  - **chat\_id** (_Union\[int, str\]_)

  - **business\_connection\_id** (_Optional\[str\]_)

  - **message\_id** (_Optional\[int\]_)

- **Returns**

  Type: _bool_

### _async method_ `upload_sticker_file(self, *, user_id, sticker, sticker_format)` {#TelegramAPI-upload-sticker-file}

- **Arguments**

  - **user\_id** (_int_)

  - **sticker** (_Union\[bytes, tuple\[str, bytes\]\]_)

  - **sticker\_format** (_str_)

- **Returns**

  Type: _alicebot.adapter.telegram.model.File_
