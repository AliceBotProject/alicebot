# alicebot.adapter.telegram

Telegram 协议适配器。

本适配器适配了 Telegram Bot API 协议。
协议详情请参考：[Telegram Bot API](https://core.telegram.org/bots/api)。

## _class_ `TelegramAdapter` {#TelegramAdapter}

Bases: `alicebot.adapter.Adapter`, `alicebot.adapter.telegram.api.TelegramAPI`

Telegram 协议适配器。

- **Attributes**

  - **session** (_aiohttp.client.ClientSession_)

  - **app** (_Optional\[aiohttp.web\_app.Application\]_)

  - **runner** (_Optional\[aiohttp.web\_runner.AppRunner\]_)

  - **site** (_Optional\[aiohttp.web\_runner.TCPSite\]_)

### _class_ `Config` {#Config}

Bases: `alicebot.config.ConfigModel`

Telegram 适配器配置

- **Attributes**

  - **adapter\_type** (_Literal\['polling', 'webhook'\]_) - 适配器运行模式

  - **bot\_token** (_str_) - 从 `BotFather` 获取的 token 值。
  参考：https://core.telegram.org/bots#how-do-i-create-a-bot

  - **api\_server** (_str_) - 自定义 API 服务器

  - **webhook\_host** (_Optional\[str\]_) - 自定义 Webhook 服务器地址

  - **webhook\_port** (_Optional\[int\]_) - 自定义 Webhook 服务器端口

  - **webhook\_url** (_Optional\[str\]_) - 自定义 Webhook 服务器路径

  - **proxy** (_Optional\[str\]_) - 代理服务器地址，为空时表示不使用代理

  - **api\_timeout** (_int_) - 进行 API 调用时等待返回响应的超时时间。

### _async method_ `call_api(self, api, *, response_type = None, **params)` {#TelegramAdapter-call-api}

调用 Telegram Bot API，协程会等待直到获得 API 响应。

- **Arguments**

  - **api** (_str_) - API 名称。

  - **response\_type** (_Optional\[type\[~\_T\]\]_) - API 响应类型。

  - **\*\*params** (_Any_) - API 参数。

- **Returns**

  Type: _Optional\[~\_T\]_

  API 响应。

- **Raises**

  - **NetworkError** - 网络错误。

  - **ActionFailed** - API 请求响应 failed，API 操作失败。

### _async method_ `handle_response(self, request)` {#TelegramAdapter-handle-response}

处理响应。

- **Arguments**

  - **request** (_aiohttp.web\_request.Request_)

- **Returns**

  Type: _aiohttp.web\_response.StreamResponse_

### _async method_ `handle_telegram_event(self, update)` {#TelegramAdapter-handle-telegram-event}

处理 Telegram 事件。

- **Arguments**

  - **update** (_alicebot.adapter.telegram.model.Update_) - 接收到的信息。

- **Returns**

  Type: _None_

### _async method_ `on_tick(self)` {#TelegramAdapter-on-tick}

当轮询发生。

- **Returns**

  Type: _None_

### _async method_ `run(self)` {#TelegramAdapter-run}

适配器运行方法，适配器开发者必须实现该方法。

适配器运行过程中保持保持运行，当此方法结束后，AliceBot 不会自动重新启动适配器。

- **Returns**

  Type: _None_

### _async method_ `send(self, message, chat_id, disable_notification = None, protect_content = None, message_effect_id = None, reply_parameters = None, reply_markup = None, **kwargs)` {#TelegramAdapter-send}

Call `seedMessage` etc. APIs to send message.

- **Arguments**

  - **message** (_Union\[str, alicebot.adapter.telegram.message.TelegramMessage, alicebot.adapter.telegram.media.TelegramMedia\]_) - The message, can be `str`, `TelegramMessage` or `TelegramMedia`.

  - **chat\_id** (_Union\[int, str\]_) - Unique identifier for the target chat or username of the target
  channel (in the format `@channelusername`).

  - **disable\_notification** (_Optional\[bool\]_) - Sends the message silently.
  Users will receive a notification with no sound.

  - **protect\_content** (_Optional\[bool\]_) - Protects the contents of the sent message from forwarding
  and saving.

  - **message\_effect\_id** (_Optional\[str\]_) - Unique identifier of the message effect to be added to
  the message; for private chats only.

  - **reply\_parameters** (_Optional\[alicebot.adapter.telegram.model.ReplyParameters\]_) - Description of the message to reply to.

  - **reply\_markup** (_Union\[alicebot.adapter.telegram.model.InlineKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardMarkup, alicebot.adapter.telegram.model.ReplyKeyboardRemove, alicebot.adapter.telegram.model.ForceReply, NoneType\]_) - Additional interface options. A JSON-serialized object for an
  inline keyboard,custom reply keyboard, instructions to remove a reply
  keyboard or to force a reply from the user.

  - **\*\*kwargs** (_Any_) - Additional API parameters.

- **Returns**

  Type: _Any_

  API Response.

- **Raises**

  - **...** - See `call_api()`.

### _async method_ `shutdown(self)` {#TelegramAdapter-shutdown}

在适配器结束运行时运行的方法，用于安全地关闭适配器。

AliceBot 在接收到系统的结束信号后先发送 cancel 请求给 run 任务。
在所有适配器都停止运行后，会依次运行并等待所有适配器的 `shutdown()` 方法。
当强制退出时此方法可能未被执行。

- **Returns**

  Type: _None_

### _async method_ `startup(self)` {#TelegramAdapter-startup}

在适配器开始运行前运行的方法，用于初始化适配器。

AliceBot 依次运行并等待所有适配器的 `startup()` 方法，待运行完毕后再创建 `run()` 任务。

- **Returns**

  Type: _None_
