# alicebot.dependencies

AliceBot 依赖注入。

实现依赖注入相关功能。

## _function_ `Depends(dependency = None, *, use_cache = True)` {#Depends}

子依赖装饰器。

- **Arguments**

  - **dependency** (_Union\[type\[Union\[~\_T, contextlib.AbstractAsyncContextManager\[~\_T\], contextlib.AbstractContextManager\[~\_T\]\]\], Callable\[\[\], collections.abc.AsyncGenerator\[~\_T, None\]\], Callable\[\[\], collections.abc.Generator\[~\_T, None, None\]\], NoneType\]_) - 依赖类。如果不指定则根据字段的类型注释自动判断。

  - **use\_cache** (_bool_) - 是否使用缓存。默认为 `True`。

- **Returns**

  Type: _~\_T_

  返回内部子依赖对象。
