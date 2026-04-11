"""事件基类。"""

from typing import TYPE_CHECKING, override

from pydantic import BaseModel, ConfigDict

from alicebot.event import Event

from ..model import Update  # noqa: TID252

if TYPE_CHECKING:
    from .. import TelegramAdapter  # noqa: TID252


class TelegramEvent(BaseModel, Event["TelegramAdapter"]):  # pyright: ignore[reportUnsafeMultipleInheritance]
    """Telegram Event Baseclass."""

    __event_type__: str = ""

    model_config = ConfigDict(extra="allow")

    _adapter: "TelegramAdapter"

    type: str
    update: Update

    @property
    @override
    def adapter(self) -> "TelegramAdapter":
        return self._adapter

    @adapter.setter
    def adapter(self, value: "TelegramAdapter") -> None:
        self._adapter = value

    @property
    def update_id(self) -> int:
        """The update's unique identifier."""
        return self.update.update_id

    @override
    def __str__(self) -> str:
        return (
            f"<{self.__class__.__name__} type={self.type}, update_id={self.update_id}>"
        )

    @override
    def __repr__(self) -> str:
        return self.__str__()
