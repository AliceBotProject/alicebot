"""AliceBot 事件。

事件类的基类。适配器开发者应实现此事件类基类的子类。
"""
from abc import ABC
from typing import Any, Generic, Optional, Union

from pydantic import BaseModel

from alicebot.message import Message
from alicebot.typing import T_Adapter
from alicebot.utils import DataclassEncoder

__all__ = ['Event']


# 这里不能用 pydantic.generics.GenericModel，否则容易在编写适配器陷入循环引用，对适配器的编写造成困难
class Event(ABC, BaseModel, Generic[T_Adapter]):
    """事件类的基类。

    Attributes:
        adapter: 产生当前事件的适配器对象。
        type: 事件类型。
        __handled__: 表示事件是否被处理过了，用于适配器处理。
            警告：请勿手动更改此属性的值。
    """
    adapter: Union[Any, T_Adapter]  # Union[Any, ...] 等效与 Any，防止 pydantic 进行类型检验，但使静态类型检查工具可以识别到
    type: Optional[str]
    __handled__: bool = False

    def __str__(self) -> str:
        return f'Event<{self.type}>'

    def __repr__(self) -> str:
        return self.__str__()

    class Config:
        extra = 'allow'
        json_encoders = {Message: DataclassEncoder}
