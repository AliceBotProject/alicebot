# alicebot.event

AliceBot 事件。

事件类的基类。适配器开发者应实现此事件类基类的子类。

## *class* `Event`(__pydantic_self__, **data) {#Event}

Bases: `abc.ABC`, `pydantic.main.BaseModel`

事件类的基类。

- **Attributes**

  - **adapter** (*Any*) - 产生当前事件的适配器对象。

  - **type** (*Optional[str]*) - 事件类型。

  - **handled** (*bool*) - 表示事件是否被处理过了，用于适配器处理。
  警告：请勿手动更改此属性的值。

### *class* `Config`(self, /, *args, **kwargs) {#Event.Config}

Bases: `object`