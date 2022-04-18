# alicebot.utils

## *class* `Condition`(self) {#Condition}

Bases: `object`

类似于 asyncio.Condition ，但允许在 notify() 时传递值，并由 wait() 返回。

### *method* `notify(self, value=None, n=1)` {#Condition.notify}

- **Arguments**

  - **value**

  - **n**

### *method* `notify_all(self, value=None)` {#Condition.notify_all}

- **Arguments**

  - **value**

### *async method* `wait(self)` {#Condition.wait}

### *async method* `wait_for(self, predicate)` {#Condition.wait_for}

- **Arguments**

  - **predicate**