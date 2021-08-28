# alicebot.event

## 事件

事件类的基类。适配器开发者应实现此事件类基类的子类。


## _class_ `Event`

基类：`abc.ABC`, `pydantic.main.BaseModel`

事件类的基类。


### `adapter`

产生当前事件的适配器对象。


### `type`

事件类型。


### `handled`

表示事件是否被处理过了，用于适配器处理。
警告：请勿手动更改此属性的值。
