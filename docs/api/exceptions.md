# alicebot.exceptions

AliceBot 异常。

下列是 AliceBot 运行过程中可能会抛出的异常。这些异常大部分不需要用户处理， AliceBot 会自动捕获并处理。
对于适配器开发者，所有适配器抛出的异常都应该继承自 `AdapterException` 。

## *class* `EventException`(self, /, *args, **kwargs) {#EventException}

Bases: `BaseException`

事件处理过程中由插件抛出的异常，用于控制事件的传播，会被 AliceBot 自动捕获并处理。

- **Arguments**

  - **args**

  - **kwargs**

## *class* `SkipException`(self, /, *args, **kwargs) {#SkipException}

Bases: `alicebot.exceptions.EventException`

跳过当前插件继续当前事件传播。

- **Arguments**

  - **args**

  - **kwargs**

## *class* `StopException`(self, /, *args, **kwargs) {#StopException}

Bases: `alicebot.exceptions.EventException`

停止当前事件传播。

- **Arguments**

  - **args**

  - **kwargs**

## *class* `AliceBotException`(self, /, *args, **kwargs) {#AliceBotException}

Bases: `Exception`

所有 AliceBot 发生的异常的基类。

- **Arguments**

  - **args**

  - **kwargs**

## *class* `GetEventTimeout`(self, /, *args, **kwargs) {#GetEventTimeout}

Bases: `alicebot.exceptions.AliceBotException`

当 get 方法超时使被抛出。

- **Arguments**

  - **args**

  - **kwargs**

## *class* `AdapterException`(self, /, *args, **kwargs) {#AdapterException}

Bases: `alicebot.exceptions.AliceBotException`

由适配器抛出的异常基类，所有适配器抛出的异常都应该继承自此类。

- **Arguments**

  - **args**

  - **kwargs**

## *class* `LoadModuleError`(self, /, *args, **kwargs) {#LoadModuleError}

Bases: `alicebot.exceptions.AliceBotException`

加载模块错误，在指定模块中找不到特定类型的类或模块中存在多个符合条件的类时抛出。

- **Arguments**

  - **args**

  - **kwargs**