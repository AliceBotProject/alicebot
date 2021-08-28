# alicebot.adapter.apscheduler

## APScheduler 适配器

本适配器用于实现定时任务，适配器将使用 APScheduler 实现定时任务，在设定的时间产生一个事件供插件处理。
APScheduler 使用方法请参考: [APScheduler](https://apscheduler.readthedocs.io/) 。


## `scheduler_decorator(trigger, trigger_args, override_rule=False)`

用于为插件类添加计划任务功能的装饰器。


* **参数**

    
    * **trigger** – APScheduler 触发器。


    * **trigger_args** – APScheduler 触发器参数。


    * **override_rule** – 是否重写 rule() 方法，若为 True，则会在 rule() 方法中添加处理本插件定义的计划任务事件的逻辑。
