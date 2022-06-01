"""AliceBot 事件。

事件类的基类。适配器开发者应实现此事件类基类的子类。
"""
from abc import ABC
from typing import Any, Generic, Optional

from pydantic import BaseModel, PrivateAttr

from alicebot.message import Message
from alicebot.typing import T_Adapter
from alicebot.utils import DataclassEncoder

__all__ = ["Event"]


class Event(ABC, BaseModel, Generic[T_Adapter]):
    """事件类的基类。

    Attributes:
        adapter: 产生当前事件的适配器对象。
        type: 事件类型。
        __handled__: 表示事件是否被处理过了，用于适配器处理。
            警告：请勿手动更改此属性的值。
    """

    adapter: Any
    # 这里的 adapter 类型定义只是为了 IDE 的类型检查工具能够正常工作，这个字段将永远不会被实际使用
    # IDE 对 BaseModel 实例化时的提示会将 BaseModel 视为 dataclasses，而忽略 __init__ 定义
    # 因此需要此定义防止类型提示出错
    # 参考：
    # https://pydantic-docs.helpmanual.io/visual_studio_code/#technical-details
    # https://koxudaxi.github.io/pydantic-pycharm-plugin/ignore-init-arguments/

    type: Optional[str]

    _adapter: Optional[T_Adapter] = PrivateAttr()  # adapter 实际上放在这里
    __handled__: bool = PrivateAttr(default=False)

    def __init__(self, **data):
        if "adapter" in data:
            self._adapter = data.pop("adapter")
        else:
            raise ValueError('"adapter" argument must be set')
        super().__init__(**data)

    @property
    def adapter(self) -> T_Adapter:
        """产生当前事件的适配器对象。"""
        return self._adapter

    def __str__(self) -> str:
        return f"Event<{self.type}>"

    def __repr__(self) -> str:
        return self.__str__()

    class Config:
        extra = "allow"
        json_encoders = {Message: DataclassEncoder}
