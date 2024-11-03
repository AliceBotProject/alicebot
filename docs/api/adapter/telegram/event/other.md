# alicebot.adapter.telegram.event.other

Telegram 适配器事件。

## _class_ `EditedMessageEvent` {#EditedMessageEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

New version of a message that is known to the bot and was edited.

### _readonly property_ `edited_message` {#EditedMessageEvent-edited-message}

Type: _alicebot.adapter.telegram.model.Message_

The edited_message object.

## _class_ `ChannelPostEvent` {#ChannelPostEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

New incoming channel post of any kind - text, photo, sticker, etc..

### _readonly property_ `channel_post` {#ChannelPostEvent-channel-post}

Type: _alicebot.adapter.telegram.model.Message_

The channel_post object.

## _class_ `EditedChannelPostEvent` {#EditedChannelPostEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

New version of a channel post that is known to the bot and was edited.

### _readonly property_ `edited_channel_post` {#EditedChannelPostEvent-edited-channel-post}

Type: _alicebot.adapter.telegram.model.Message_

The edited_channel_post object.

## _class_ `BusinessConnectionEvent` {#BusinessConnectionEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

The bot was connected to or disconnected from a business account, or a user edited an existing connection with the bot.

### _readonly property_ `business_connection` {#BusinessConnectionEvent-business-connection}

Type: _alicebot.adapter.telegram.model.BusinessConnection_

The business_connection object.

## _class_ `BusinessMessageEvent` {#BusinessMessageEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

New message from a connected business account.

### _readonly property_ `business_message` {#BusinessMessageEvent-business-message}

Type: _alicebot.adapter.telegram.model.Message_

The business_message object.

## _class_ `EditedBusinessMessageEvent` {#EditedBusinessMessageEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

New version of a message from a connected business account.

### _readonly property_ `edited_business_message` {#EditedBusinessMessageEvent-edited-business-message}

Type: _alicebot.adapter.telegram.model.Message_

The edited_business_message object.

## _class_ `DeletedBusinessMessagesEvent` {#DeletedBusinessMessagesEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

Messages were deleted from a connected business account.

### _readonly property_ `deleted_business_messages` {#DeletedBusinessMessagesEvent-deleted-business-messages}

Type: _alicebot.adapter.telegram.model.BusinessMessagesDeleted_

The deleted_business_messages object.

## _class_ `MessageReactionEvent` {#MessageReactionEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

A reaction to a message was changed by a user.

### _readonly property_ `message_reaction` {#MessageReactionEvent-message-reaction}

Type: _alicebot.adapter.telegram.model.MessageReactionUpdated_

The message_reaction object.

## _class_ `MessageReactionCountEvent` {#MessageReactionCountEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

Reactions to a message with anonymous reactions were changed.

### _readonly property_ `message_reaction_count` {#MessageReactionCountEvent-message-reaction-count}

Type: _alicebot.adapter.telegram.model.MessageReactionCountUpdated_

The message_reaction_count object.

## _class_ `InlineQueryEvent` {#InlineQueryEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

New incoming inline query.

### _readonly property_ `inline_query` {#InlineQueryEvent-inline-query}

Type: _alicebot.adapter.telegram.model.InlineQuery_

The inline_query object.

## _class_ `ChosenInlineResultEvent` {#ChosenInlineResultEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

The result of an inline query that was chosen by a user and sent to their chat partner.

### _readonly property_ `chosen_inline_result` {#ChosenInlineResultEvent-chosen-inline-result}

Type: _alicebot.adapter.telegram.model.ChosenInlineResult_

The chosen_inline_result object.

## _class_ `CallbackQueryEvent` {#CallbackQueryEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

New incoming callback query.

### _readonly property_ `callback_query` {#CallbackQueryEvent-callback-query}

Type: _alicebot.adapter.telegram.model.CallbackQuery_

The callback_query object.

## _class_ `ShippingQueryEvent` {#ShippingQueryEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

New incoming shipping query.

### _readonly property_ `shipping_query` {#ShippingQueryEvent-shipping-query}

Type: _alicebot.adapter.telegram.model.ShippingQuery_

The shipping_query object.

## _class_ `PreCheckoutQueryEvent` {#PreCheckoutQueryEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

New incoming pre-checkout query.

### _readonly property_ `pre_checkout_query` {#PreCheckoutQueryEvent-pre-checkout-query}

Type: _alicebot.adapter.telegram.model.PreCheckoutQuery_

The pre_checkout_query object.

## _class_ `PurchasedPaidMediaEvent` {#PurchasedPaidMediaEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

A user purchased paid media with a non-empty payload sent by the bot in a non-channel chat.

### _readonly property_ `purchased_paid_media` {#PurchasedPaidMediaEvent-purchased-paid-media}

Type: _alicebot.adapter.telegram.model.PaidMediaPurchased_

The purchased_paid_media object.

## _class_ `PollEvent` {#PollEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

New poll state.

### _readonly property_ `poll` {#PollEvent-poll}

Type: _alicebot.adapter.telegram.model.Poll_

The poll object.

## _class_ `PollAnswerEvent` {#PollAnswerEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

A user changed their answer in a non-anonymous poll.

### _readonly property_ `poll_answer` {#PollAnswerEvent-poll-answer}

Type: _alicebot.adapter.telegram.model.PollAnswer_

The poll_answer object.

## _class_ `MyChatMemberEvent` {#MyChatMemberEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

The bot's chat member status was updated in a chat.

### _readonly property_ `my_chat_member` {#MyChatMemberEvent-my-chat-member}

Type: _alicebot.adapter.telegram.model.ChatMemberUpdated_

The my_chat_member object.

## _class_ `ChatMemberEvent` {#ChatMemberEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

A chat member's status was updated in a chat.

### _readonly property_ `chat_member` {#ChatMemberEvent-chat-member}

Type: _alicebot.adapter.telegram.model.ChatMemberUpdated_

The chat_member object.

## _class_ `ChatJoinRequestEvent` {#ChatJoinRequestEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

A request to join the chat has been sent.

### _readonly property_ `chat_join_request` {#ChatJoinRequestEvent-chat-join-request}

Type: _alicebot.adapter.telegram.model.ChatJoinRequest_

The chat_join_request object.

## _class_ `ChatBoostEvent` {#ChatBoostEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

A chat boost was added or changed.

### _readonly property_ `chat_boost` {#ChatBoostEvent-chat-boost}

Type: _alicebot.adapter.telegram.model.ChatBoostUpdated_

The chat_boost object.

## _class_ `RemovedChatBoostEvent` {#RemovedChatBoostEvent}

Bases: `alicebot.adapter.telegram.event.base.TelegramEvent`

A boost was removed from a chat.

### _readonly property_ `removed_chat_boost` {#RemovedChatBoostEvent-removed-chat-boost}

Type: _alicebot.adapter.telegram.model.ChatBoostRemoved_

The removed_chat_boost object.
