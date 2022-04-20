"""AliceBot 事件。

事件类的基类。适配器开发者应实现此事件类基类的子类。
"""
from abc import ABC
from typing import Any, Optional, TypeVar

from pydantic import BaseModel

from alicebot.message import Message, DataclassEncoder

__all__ = ['T_Event', 'Event']

T_Event = TypeVar('T_Event', bound='Event')


class Event(ABC, BaseModel):
    """事件类的基类。

    Attributes:
        adapter: 产生当前事件的适配器对象。
        type: 事件类型。
        handled: 表示事件是否被处理过了，用于适配器处理。
            警告：请勿手动更改此属性的值。
    """
    adapter: Any
    type: Optional[str]
    handled: bool = False

    def __str__(self) -> str:
        return f'Event<{self.type}>'

    def __repr__(self) -> str:
        return self.__str__()

    class Config:
        extra = 'allow'
        json_encoders = {Message: DataclassEncoder}
