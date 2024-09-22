"""Telegram 协议适配器。

本适配器适配了 Telegram Bot API 协议。
协议详情请参考：[Telegram Bot API](https://core.telegram.org/bots/api)。
"""

import inspect
import json
import uuid
from typing import Any, Optional, TypeVar, Union
from typing_extensions import TypeGuard, override

import aiohttp
import structlog
from aiohttp import web
from anyio.lowlevel import checkpoint
from pydantic import TypeAdapter, ValidationError
from pydantic_core import to_jsonable_python

from alicebot.adapter import Adapter

from . import event
from .api import TelegramAPI
from .config import Config
from .event import TelegramEvent
from .exceptions import ActionFailed, NetworkError
from .media import TelegramMedia
from .message import TelegramMessage
from .model import (
    ForceReply,
    InlineKeyboardMarkup,
    InputFile,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ReplyParameters,
    Response,
    Update,
)

__all__ = ["TelegramAdapter"]

logger = structlog.stdlib.get_logger()

EventModels = dict[str, type[TelegramEvent]]

EVENT_MODELS: EventModels = {}
for _, model in inspect.getmembers(event, inspect.isclass):
    if issubclass(model, TelegramEvent):
        EVENT_MODELS[model.__event_type__] = model

_T = TypeVar("_T")


class TelegramAdapter(Adapter[TelegramEvent, Config], TelegramAPI):
    """Telegram 协议适配器。"""

    name = "telegram"
    Config = Config

    session: aiohttp.ClientSession
    app: Optional[web.Application]
    runner: Optional[web.AppRunner]
    site: Optional[web.TCPSite]

    _secret_token: Optional[str]
    _update_offset: Optional[int] = None

    @override
    async def startup(self) -> None:
        if self.config.adapter_type == "webhook":
            self.app = web.Application()
            assert self.config.webhook_url is not None
            self.app.add_routes(
                [web.post(self.config.webhook_url, self.handle_response)]
            )
            self._secret_token = uuid.uuid4().hex
        self.session = aiohttp.ClientSession()

    @override
    async def run(self) -> None:
        if self.config.adapter_type == "polling":
            while True:
                await checkpoint()
                await self.on_tick()
        elif self.config.adapter_type == "webhook":
            assert self.app is not None
            host = self.config.webhook_host
            port = self.config.webhook_port
            url = self.config.webhook_url
            assert self.app is not None
            if host is None or port is None or url is None:
                raise ValueError(
                    '"webhook_host", "webhook_port" and "webhook_url" must be set '
                    'when "adapter_type" is "webhook'
                )

            self.runner = web.AppRunner(self.app)
            await self.runner.setup()
            self.site = web.TCPSite(self.runner, host, port)
            await self.site.start()

            # 删除旧的 webhook 并设置新的 webhook
            await self.delete_webhook()
            logger.info("Setting webhook", host=host, port=port, url=url)
            await self.set_webhook(
                url=f"https://{host}:{port}{url}",
                secret_token=self._secret_token,
            )

    @override
    async def shutdown(self) -> None:
        if self.config.adapter_type == "webhook":
            await self.delete_webhook()
        await self.session.close()
        if self.runner is not None:
            await self.runner.cleanup()

    async def handle_response(self, request: web.Request) -> web.StreamResponse:
        """处理响应。"""
        secret_token = request.headers.get("X-Telegram-Bot-Api-Secret-Token")
        if secret_token == self._secret_token:
            update = Update.model_validate_json(await request.read())
            await self.handle_telegram_event(update)
            return web.Response(status=204)
        return web.Response(status=401)

    async def on_tick(self) -> None:
        """当轮询发生。"""
        try:
            updates = await self.get_updates(offset=self._update_offset, timeout=30)
            if self._update_offset is not None:
                for update in updates:
                    await self.handle_telegram_event(update)
            if updates:
                self._update_offset = updates[-1].update_id + 1
        except Exception:
            logger.exception("Failed to get updates")

    async def handle_telegram_event(self, update: Update) -> None:
        """处理 Telegram 事件。

        Args:
            update: 接收到的信息。
        """
        event_class_name = ""
        for k, v in update:
            if v is not None:
                event_class_name = k
        if event_class_name not in EVENT_MODELS:
            logger.warning(
                "Unknown event type",
                event_type=event_class_name,
                update=update,
            )
            return
        event_class = EVENT_MODELS[event_class_name]
        telegram_event = event_class(adapter=self, type=event_class_name, update=update)
        await self.handle_event(telegram_event)

    def _format_telegram_api_params(
        self, **params: Any
    ) -> Union[aiohttp.FormData, dict[str, Any]]:
        file_type_adapter: TypeAdapter[InputFile] = TypeAdapter(InputFile)

        def is_file(v: Any) -> TypeGuard[InputFile]:
            try:
                file_type_adapter.validate_python(v, strict=True)
            except ValidationError:
                return False
            return True

        if any(is_file(v) for v in params.values()):
            form_data = aiohttp.FormData()
            unnamed_file_count = 0
            for k, v in params.items():
                if v is None:
                    continue
                if is_file(v):
                    if isinstance(v, tuple):
                        filename, filedata = v
                        form_data.add_field(k, filedata, filename=filename)
                    elif isinstance(v, bytes):
                        form_data.add_field(
                            k, v, filename=f"upload_{unnamed_file_count}"
                        )
                else:
                    form_data.add_field(k, json.dumps(v, default=to_jsonable_python))
            return form_data

        return {
            k: to_jsonable_python(v, exclude_none=True)
            for k, v in params.items()
            if v is not None
        }

    @override
    async def call_api(
        self,
        api: str,
        *,
        response_type: Optional[type[_T]] = None,
        **params: Any,
    ) -> Optional[_T]:
        """调用 Telegram Bot API，协程会等待直到获得 API 响应。

        Args:
            api: API 名称。
            response_type: API 响应类型。
            **params: API 参数。

        Returns:
            API 响应。

        Raises:
            NetworkError: 网络错误。
            ActionFailed: API 请求响应 failed， API 操作失败。
        """
        if response_type is None:
            return_type_adapter = TypeAdapter(Response[Any])
        else:
            return_type_adapter = TypeAdapter(Response[response_type])

        data = self._format_telegram_api_params(**params)
        if isinstance(data, aiohttp.FormData):
            form_data, json_data = data, None
        else:
            form_data, json_data = None, data

        try:
            logger.debug(
                "Telegram API call", api=api, json_data=json_data, form_data=form_data
            )
            async with self.session.post(
                f"{self.config.api_server}bot{self.config.bot_token}/{api}",
                proxy=self.config.proxy,
                data=form_data,
                json=json_data,
            ) as resp:
                if not 200 <= resp.status < 300:  # noqa: PLR2004
                    raise ActionFailed(resp=await resp.json())
                resp_json = await resp.json()
                resp_model = return_type_adapter.validate_python(resp_json)
                if not resp_model.ok:
                    raise ActionFailed(resp=resp_model)
                return resp_model.result
        except (aiohttp.ClientError, ValidationError) as e:
            raise NetworkError from e

    async def send(
        self,
        message: Union[str, TelegramMessage, TelegramMedia],
        chat_id: Union[int, str],
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
        **kwargs: Any,
    ) -> Any:
        """Call `seedMessage` etc. APIs to send message.

        Args:
            message: The message, can be `str`, `TelegramMessage` or `TelegramMedia`.
            chat_id: Unique identifier for the target chat or username of the target
                channel (in the format `@channelusername`).
            disable_notification: Sends the message silently.
                Users will receive a notification with no sound.
            protect_content: Protects the contents of the sent message from forwarding
                and saving.
            message_effect_id: Unique identifier of the message effect to be added to
                the message; for private chats only.
            reply_parameters: Description of the message to reply to.
            reply_markup: Additional interface options. A JSON-serialized object for an
                inline keyboard,custom reply keyboard, instructions to remove a reply
                keyboard or to force a reply from the user.
            **kwargs: Additional API parameters.

        Returns:
            API Response.

        Raises:
            ...: See `call_api()`.
        """
        kwargs.update(
            {
                "protect_content": protect_content,
                "disable_notification": disable_notification,
                "message_effect_id": message_effect_id,
                "reply_parameters": reply_parameters,
                "reply_markup": reply_markup,
            }
        )
        if isinstance(message, str):
            return await self.send_message(chat_id=chat_id, text=message)
        if isinstance(message, TelegramMessage):
            return await self.send_message(
                chat_id=chat_id,
                text=message.to_text(),
                entities=message.to_entities(),
                **kwargs,
            )
        if isinstance(message, TelegramMedia):
            fields: dict[str, Any] = {}
            for k, v in message:
                if isinstance(v, TelegramMessage):
                    fields[k] = v.to_text()
                    fields[f"{k}_entities"] = v.to_entities()
                else:
                    fields[k] = v
            return await self.call_api(
                "send" + message.__class__.__name__,
                chat_id=chat_id,
                **fields,
                **kwargs,
            )
        raise TypeError("message must be str, TelegramMessage or TelegramMedia")
