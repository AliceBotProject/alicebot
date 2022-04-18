# alicebot.load_module

## *class* `ModulePathFinder`(self, /, *args, **kwargs) {#ModulePathFinder}

Bases: `importlib.abc.MetaPathFinder`

用于查找 AliceBot 组件的元路径查找器。

- **Attributes**

  - **path** (*List[str]*)

### *method* `find_spec(self, fullname, path=None, target=None)` {#ModulePathFinder.find_spec}

- **Arguments**

  - **fullname**

  - **path**

  - **target**

## *function* `load_module(name, module_class_type, try_instantiate_class = False, *args, **kwargs)` {#load_module}

从模块中查找指定类型的类和 `Config` 。若模块中存在多个符合条件的类，则抛出错误。

- **Arguments**

  - **name** (*str*) - 模块名称，格式和 Python `import` 语句相同。

  - **module_class_type** (*Type[~_T]*) - 要查找的类型。

  - **try_instantiate_class** (*bool*) - 是否尝试实例化类，当为 True 时，查找到指定的类后会尝试使用指定参数示例化类，仅返回成功被实例化的对象。

  - ***args** - 实例化类时使用的参数，仅当 `try_instantiate_class` 为 True 时生效。

  - ****kwargs** - 实例化类时使用的参数，仅当 `try_instantiate_class` 为 True 时生效。

- **Returns**

  Type: *Tuple[Union[Type[~_T], ~_T], Optional[Type[pydantic.main.BaseModel]]]*

  `(class, config)` 返回符合条件的类和配置类组成的元组，当 `try_instantiate_class` 为 True 时，返回 `(object, config)` 。

- **Raises**

  - **LoadModuleError** - 当找不到符合条件的类或者模块中存在多个符合条件的类。

## *function* `load_modules_from_dir(_module_path_finder, path, module_class_type)` {#load_modules_from_dir}

从指定路径列表中的所有模块中查找指定类型的类和 `Config` ，以 `_` 开头的插件不会被导入。路径可以是相对路径或绝对路径。

- **Arguments**

  - **_module_path_finder** (*alicebot.load_module.ModulePathFinder*) - 用于查找 AliceBot 组件的元路径查找器。

  - **path** (*Iterable[str]*) - 由储存模块的路径文本组成的列表。 例如 `['path/of/plugins/', '/home/xxx/alicebot/plugins']` 。

  - **module_class_type** (*Type[~_T]*) - 要查找的类型。

- **Returns**

  Type: *List[Tuple[Type[~_T], Optional[Type[pydantic.main.BaseModel]], ModuleInfo]]*

  `[(class, config, module_info), ...]` 返回由符合条件的类、配置类和 `ModuleInfo` 组成的元组组成的列表。