# alicebot.load_module


## _class_ `ModulePathFinder`

基类：`importlib.abc.MetaPathFinder`

用于查找 AliceBot 组件的元路径查找器。


## `load_module(name, module_class_type, *args, **kwargs)`

从模块中查找指定类型的类和 `Config` 。
查找到指定的类后会尝试使用指定参数示例化类，仅返回能被实例化的类。
若模块中存在多个符合条件的类，则抛出错误。


* **参数**

    
    * **name** – 模块名称，格式和 Python `import` 语句相同。


    * **module_class_type** – 要查找的类型。


    * **args** – 实例化类时使用的参数。


    * **kwargs** – 实例化类时使用的参数。



* **返回**

    `(class, config)` 返回符合条件的类和配置类组成的元组。



* **返回类型**

    Tuple[Type[_T], Optional[Type[BaseModel]]]



* **引发**

    [**LoadModuleError**](exception.md#alicebot.exception.LoadModuleError) – 当找不到符合条件的类或者模块中存在多个符合条件的类。



## `load_modules_from_dir(_module_path_finder, path, module_class_type, *args, **kwargs)`

从指定路径列表中的所有模块中查找指定类型的类和 `Config` ，以 `_` 开头的插件不会被导入。
路径可以是相对路径或绝对路径。


* **参数**

    
    * **_module_path_finder** – 用于查找 AliceBot 组件的元路径查找器。


    * **path** – 由储存模块的路径文本组成的列表。 `['path/of/plugins/', '/home/xxx/alicebot/plugins']`


    * **module_class_type** – 要查找的类型。


    * **args** – 实例化类时使用的参数。


    * **kwargs** – 实例化类时使用的参数。



* **返回**

    `[(class, config, module_info), ...]` 返回由符合条件的类、配置类和 `ModuleInfo` 组成的元组组成的列表。
