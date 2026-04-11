import inspect
from collections.abc import Awaitable, Callable
from typing import Any, override

from anyio.lowlevel import checkpoint

from alicebot import Adapter, ConfigModel, Event, MessageEvent
from alicebot.plugin import Plugin
from alicebot.typing import AnyEvent

EventFactory = Callable[
    ["FakeAdapter"],
    Event["FakeAdapter"] | None | Awaitable[Event["FakeAdapter"] | None],
]


async def allow_schedule_other_tasks() -> None:
    """让出当前任务，允许其他任务执行。"""
    for _ in range(1000):
        await checkpoint()


class FakeAdapter(Adapter[AnyEvent, None]):
    """用于测试的适配器。"""

    name: str = "fake_adapter"
    event_factories: tuple[EventFactory, ...] = ()
    handle_get: bool = True

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

            # 发送一个事件后，等待完成必要的处理再发送下一个
            await allow_schedule_other_tasks()

        # 尽可能让其他任务执行完毕后再退出
        await allow_schedule_other_tasks()

        self.bot.exit()


def fake_adapter_class_factory(
    *event_factories: EventFactory, handle_get: bool = True
) -> type[FakeAdapter]:
    return type(
        "FakeAdapter",
        (FakeAdapter,),
        {"event_factories": event_factories, "handle_get": handle_get},
    )


class FakeMessageEvent(MessageEvent[FakeAdapter]):
    _adapter: FakeAdapter
    type: str
    message: str

    def __init__(
        self,
        adapter: FakeAdapter,
        type: str = "message",
        message: str = "test",
    ) -> None:
        self._adapter = adapter
        self.type = type
        self.message = message

    @property
    @override
    def adapter(self) -> "FakeAdapter":
        return self._adapter

    @override
    def get_sender_id(self) -> None:
        pass

    @override
    def get_plain_text(self) -> str:
        return self.message

    @override
    async def reply(self, message: str) -> None:
        pass


def fake_message_event_factor(
    adapter: FakeAdapter, message: str = "test"
) -> FakeMessageEvent:
    return FakeMessageEvent(adapter=adapter, type="message", message=message)


class BaseTestPlugin[StateT: Any = None, ConfigT: ConfigModel | None = None](
    Plugin[FakeMessageEvent, StateT, ConfigT],
):
    @override
    async def handle(self) -> None:
        pass

    @override
    async def rule(self) -> bool:
        return isinstance(self.event, FakeMessageEvent)
