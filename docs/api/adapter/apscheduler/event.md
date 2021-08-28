# alicebot.adapter.apscheduler.event

## APScheduler 事件


## _class_ `APSchedulerEvent`

基类：[`alicebot.event.Event`](../../event.md#alicebot.event.Event)

APSchedulerEvent 事件基类


### property `job: Job`


* **返回**

    产生当前事件的 APScheduler Job 对象。



### property `trigger: str`


* **返回**

    当前事件对应的 Plugin 的 trigger。



### property `trigger_args: Dict[str, Any]`


* **返回**

    当前事件对应的 Plugin 的 trigger_args。
