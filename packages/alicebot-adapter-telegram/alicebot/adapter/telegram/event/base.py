"""事件基类。"""

from typing import TYPE_CHECKING

from alicebot.event import Event

from ..model import Update  # noqa: TID252

if TYPE_CHECKING:
    from .. import TelegramAdapter  # noqa: TID252


class TelegramEvent(Event["TelegramAdapter"]):
    """Telegram Event Baseclass."""

    __event_type__: str = ""

    update: Update

    @property
    def update_id(self) -> int:
        """The update's unique identifier."""
        return self.update.update_id
