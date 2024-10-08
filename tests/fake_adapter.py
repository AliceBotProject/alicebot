import inspect
from collections.abc import Awaitable
from typing import Any, Callable, ClassVar, Optional, Union
from typing_extensions import override

from anyio.lowlevel import checkpoint

from alicebot import Adapter, Event, MessageEvent


class FakeAdapter(Adapter[Event[Any], None]):
    """用于测试的适配器。"""

    EventFactory = Callable[
        ["FakeAdapter"],
        Union[
            Optional[Event["FakeAdapter"]],
            Awaitable[Optional[Event["FakeAdapter"]]],
        ],
    ]

    name: str = "fake_adapter"
    event_factories: ClassVar[tuple[EventFactory, ...]] = ()
    handle_get: ClassVar[bool] = True

    @override
    async def run(self) -> None:
        for event_factory in self.event_factories:
            event_factory_call = event_factory(self)
            if inspect.isawaitable(event_factory_call):
                event = await event_factory_call
            elif isinstance(event_factory_call, Event):
                event = event_factory_call
            else:
                continue

            if isinstance(event, Event):
                await self.handle_event(event, handle_get=self.handle_get)

        for _ in range(10):  # 尽可能让其他任务执行完毕后再退出
            await checkpoint()

        self.bot.exit()

    @classmethod
    def set_event_factories(cls, *event_factories: EventFactory) -> None:
        """设置适配器运行后将要产生的事件。"""
        cls.event_factories = event_factories


class FakeMessageEvent(MessageEvent[FakeAdapter]):
    message: str = "test"

    @override
    def get_sender_id(self) -> None:
        pass

    @override
    def get_plain_text(self) -> str:
        return self.message

    @override
    async def reply(self, message: str) -> None:
        pass
