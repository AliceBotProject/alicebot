# alicebot.dependencies

AliceBot 依赖注入。

实现依赖注入相关功能。

## *function* `Depends(dependency = None, *, use_cache = True)` {#Depends}

子依赖装饰器。

- **Arguments**

  - **dependency** (*Union[Type[Union[~T, AsyncContextManager[~T], ContextManager[~T]]], Callable[[], AsyncGenerator[~T, NoneType]], Callable[[], Generator[~T, NoneType, NoneType]], NoneType]*) - 依赖类。如果不指定则根据字段的类型注释自动判断。

  - **use_cache** (*bool*) - 是否使用缓存。默认为 `True`。

- **Returns**

  Type: *~T*

  返回内部子依赖对象。