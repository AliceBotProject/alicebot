---
sidebar: auto
---

# 更新日志


## [0.6.2](https://github.com/AliceBotProject/alicebot/compare/v0.6.1...v0.6.2) (2023-04-25)


### Bug Fixes

* 修复 Hook 函数类型注解错误 ([b39865a](https://github.com/AliceBotProject/alicebot/commit/b39865a62148e292a86b7f1750e53a10b6c5335c))
* 修复 WebSocketAdapter 在还没有连接直接 shutdown 时的异常 ([c1a7599](https://github.com/AliceBotProject/alicebot/commit/c1a7599a52f9785eafc9d1558db42cd53b6e673c))
* **bot:** 修复热更新启动时适配器相关配置被改变不会自动重启 Bot 的错误 ([aa0ca73](https://github.com/AliceBotProject/alicebot/commit/aa0ca735e53ce3f9422b1f1ef23b7b070047a9a5))
* **cqhttp:** 修复 CQHTTPAdapter 类 call\_api 方法的类型注解错误 ([0d87850](https://github.com/AliceBotProject/alicebot/commit/0d87850403c92dd75dac5952137712fe1d57acae))
* **mirai:** 修复 MiraiAdapter 类 call\_api 方法的类型注解错误 ([c37a4f3](https://github.com/AliceBotProject/alicebot/commit/c37a4f37481bde18522263aa638409bac29e2b7d))
* **mirai:** 修复 MiraiMessageSegment 类进行相加等操作时的错误 ([f5df7ba](https://github.com/AliceBotProject/alicebot/commit/f5df7bafa792779efd56e5d6ca335385e406a999))
* **mirai:** 修改部分群事件的 operator 参数类型为可选类型 ([1986b0f](https://github.com/AliceBotProject/alicebot/commit/1986b0f6f25497ee80e864d8909cbb1a4523d34a))


### Features

* 添加 py.typed 标记 ([17f9216](https://github.com/AliceBotProject/alicebot/commit/17f92162d33b66f41fdc2da38c7e64e4b6189495))
* 完善类型注解并修改部分代码 ([393a105](https://github.com/AliceBotProject/alicebot/commit/393a10544f203341d4de0096388268082af8ee98))
* 修改 Bot 的 bot\_exit\_hook 接受的函数为异步函数 ([8490a0f](https://github.com/AliceBotProject/alicebot/commit/8490a0fdc5930864c44252f184de41004f2f5107))
* 移动示例适配器到 tests 中 ([8789b47](https://github.com/AliceBotProject/alicebot/commit/8789b47675051897ccc30eccb25c8c459e0f2e4c))
* Bot 类的 get\_adapter 方法支持传入适配器类 ([081f909](https://github.com/AliceBotProject/alicebot/commit/081f909af7fa2467c1150408130653906a8a31eb))
* **bot:** 添加从目录中加载插件 import 失败时的日志 ([ad91735](https://github.com/AliceBotProject/alicebot/commit/ad9173548e70943245f5c39e2ffb3e092538b3c9))
* **cqhttp:** CQHTTPAdapter 新增用于添加用户自定义事件模型的 add\_event\_model() 类方法 ([3eb0617](https://github.com/AliceBotProject/alicebot/commit/3eb0617d331beae672d1b32a4ae4fe113f440c09))


### BREAKING CHANGES

* bot\_exit\_hook 钩子函数要求为异步函数



## [0.6.1](https://github.com/AliceBotProject/alicebot/compare/v0.6.0...v0.6.1) (2022-12-03)


### Bug Fixes

* **bot:** 修复 Bot 类 get\_loaded\_adapter\_by\_name 方法错误 ([2b682b8](https://github.com/AliceBotProject/alicebot/commit/2b682b8f2aa9294f1c0e03fcd082e4d4ffed97d7))
* **mirai:** 修复 Mirai 适配器初始化错误 ([0d875bd](https://github.com/AliceBotProject/alicebot/commit/0d875bd0f9b5b002b09b70a3bb5b53e623eda6e0))


### Features

* **bot:** 修改 Bot 类 get\_loaded\_adapter\_by\_name 方法的名称为 get\_adapter ([2257674](https://github.com/AliceBotProject/alicebot/commit/225767456246618356373f2baf714d6695748e25))
* **bot:** Bot 类添加 get\_plugin() 方法 ([a434bf8](https://github.com/AliceBotProject/alicebot/commit/a434bf82cb541812adc75546aae696ab3deeb682))


### BREAKING CHANGES

* **bot:** 修改 Bot 类 get\_loaded\_adapter\_by\_name 方法的名称为 get\_adapter



## [0.6.0](https://github.com/AliceBotProject/alicebot/compare/v0.5.1...v0.6.0) (2022-11-26)


### Bug Fixes

* **bot:** 修复 docstring 错误 ([95521b0](https://github.com/AliceBotProject/alicebot/commit/95521b0ad125a7eb8240495b8ae3c8032c09c779))
* **bot:** 修复加载 json 配置文件出错时的日志等级错误 ([b9bbfff](https://github.com/AliceBotProject/alicebot/commit/b9bbfff85fdc9d060612110595f30ab1f1aa27e5))
* **bot:** 修复热更新时不会监控使用 load\_plugins\_from\_dirs() 方法程序式加载的插件目录的错误 ([500c2bc](https://github.com/AliceBotProject/alicebot/commit/500c2bc3cfd5aee0e3014818bf9363794bd78f75))


### Features

* 调整项目结构，增加 alicebot 模块对子模块的快捷导入 ([c482e7f](https://github.com/AliceBotProject/alicebot/commit/c482e7ffc9ec6c5348c776451721acfe2c06a333))
* 修改插件和适配器的定义为 Plugin 或 Adapter 的子类，而非一个 Python 模块，修改配置类的定义方式，并修改 Bot 的大量与加载插件和适配器相关的公开方法 ([759216a](https://github.com/AliceBotProject/alicebot/commit/759216a856caed514ee221ec474c18467d826e00))
* **adapter:** 为 Adapter 类添加泛型支持，并添加 config 属性 ([cf629da](https://github.com/AliceBotProject/alicebot/commit/cf629da89b3efa349e36f130315440264570816a))
* **bot:** 添加 toml 格式配置文件支持，并作为默认配置文件格式 ([207275d](https://github.com/AliceBotProject/alicebot/commit/207275daa92e8c34160d61e7a66327bd339c366c))
* **config:** 新增 ConfigModel 类，要求所有配置类必须是 ConfigModel 的子类 ([eec7cae](https://github.com/AliceBotProject/alicebot/commit/eec7caebc283e8e4d75d58a7768bf89511285592))
* **config:** 修改配置模型，允许配置发生改变时不一定重新启动 Bot ([9c471c3](https://github.com/AliceBotProject/alicebot/commit/9c471c340677657473616f978e43484a6971b52b))
* **cqhttp:** 完善配置类的类型注解 ([bf04235](https://github.com/AliceBotProject/alicebot/commit/bf04235bbe79a09fad572026725ee13038999a3f))
* **mirai:** 完善配置类的类型注解 ([bebf36d](https://github.com/AliceBotProject/alicebot/commit/bebf36d154f9e7bd41870e9fd25d025ddc2ed0e0))
* **plugin:** 修改 Plugin 类的 config 属性的定义为插件配置，并修改 Plugin 类的泛型参数 ([35576fa](https://github.com/AliceBotProject/alicebot/commit/35576fa6419782ae58b8a6148294a5231151162a))


### BREAKING CHANGES

* **config:** 修改配置模型
* **plugin:** 修改 Plugin 类的 config 属性的定义为插件配置而非 "self.bot.config" 的别名，并修改 Plugin 类的泛型参数
* **config:** 要求所有配置类必须是 ConfigModel 的子类，而非仅仅是 pydantic.BaseModel 的子类
* **bot:** Bot 的默认配置配置文件名修改为 config.toml
* 修改插件和适配器的定义为 Plugin 或 Adapter 的子类，修改插件和适配器配置类的定义方式，删除 Bot 类中程序化加载插件和适配器的所有方法，替换为 load\_plugins(), load\_plugins\_from\_dirs(), load\_adapters() 方法



## [0.5.1](https://github.com/AliceBotProject/alicebot/compare/v0.5.0...v0.5.1) (2022-09-11)


### Bug Fixes

* **adapter:** 修复 test 适配器中的错误 ([fabeb24](https://github.com/AliceBotProject/alicebot/commit/fabeb2490c13c36e30112cc7c3f5d799e6245a6b))
* **bot:** 修复 Adapter 类的 get 方法的 func 参数为协程时出现的错误 ([4e022fb](https://github.com/AliceBotProject/alicebot/commit/4e022fbad415b7006a08947d1d4ef895560d0232))
* **bot:** 修复调用 Bot 类的 reload\_plugins() 方法后适配器配置错误 ([a01676e](https://github.com/AliceBotProject/alicebot/commit/a01676e0bcdf00552edce0058c1bf04177c97ac5))
* **bot:** 修复热重载启用时之前因为某些原因未被成功过加载为插件的文件触发修改后无法被重新加载的错误 ([4c00b35](https://github.com/AliceBotProject/alicebot/commit/4c00b358c66fadec59a94f387e64e9339f48ebf5))
* **plugin:** 修复 Plugin 类 block 属性的潜在错误 ([3f76fd4](https://github.com/AliceBotProject/alicebot/commit/3f76fd4b90a239cdc47909c577d3d54aa61ef7c7))
* **utils:** 引入 typing-extensions，修复在 Python 3.10 以下版本中的运行异常 ([fcd4d43](https://github.com/AliceBotProject/alicebot/commit/fcd4d431590d2cc0dbd7e9916f077f4ee3b31d40))


### Features

* **bot:** 修改热更新文件修改相关日志 ([3d587b3](https://github.com/AliceBotProject/alicebot/commit/3d587b3d7557956b5e46a6475e11888c6b88e8c6))
* **utils:** 修改 load\_module\_from\_name() 函数的行为，保证只会引发 ImportError、 LoadModuleError 和 KeyboardInterrupt 异常 ([54af514](https://github.com/AliceBotProject/alicebot/commit/54af514144236adad80e62953a311011fb784755))



## [0.5.0](https://github.com/AliceBotProject/alicebot/compare/v0.4.0...v0.5.0) (2022-08-21)


### Bug Fixes

* **bot:** 修复部分情况下热更新时出现的导入错误 ([7977dfc](https://github.com/AliceBotProject/alicebot/commit/7977dfc0f3274e9fb939fc866484ea13c96b607a))
* **bot:** 修复部分情况下热重载时配置加载错误 ([24cd51c](https://github.com/AliceBotProject/alicebot/commit/24cd51c61d1d5262987c98673e8c6f7e32c07138))
* **bot:** 修复删除插件不触发热重载的错误 ([e97f244](https://github.com/AliceBotProject/alicebot/commit/e97f2447fc7ae938e15c21675341aa2e4f6e6832))


### Features

* **bot:** 添加加载同名插件时的警告 ([c008711](https://github.com/AliceBotProject/alicebot/commit/c00871168711c85227e06dbabf09ad64bd5657ec))
* **utils:** 删除 utils.Condition 类，改用标准库中的 asyncio.Condition 类 ([3e9db43](https://github.com/AliceBotProject/alicebot/commit/3e9db43a59fb1e6659836b7ca2cc15b064b71cef))


### BREAKING CHANGES

* **utils:** 删除 utils.Condition 类



## [0.4.0](https://github.com/AliceBotProject/alicebot/compare/v0.3.1...v0.4.0) (2022-08-19)


### Bug Fixes

* **bot:** 避免强制退出时 bot\_exit\_hook 重复触发 ([d5134fc](https://github.com/AliceBotProject/alicebot/commit/d5134fcf589accfa52d1990b994a4c3d45f8147b))
* **bot:** 修复热重载更新插件时插件优先级不会同步更新的错误及其他热重载相关错误 ([010ec49](https://github.com/AliceBotProject/alicebot/commit/010ec49eb0e909ec0c2470333797a27e5740e393))


### Features

* 对 Bot 类添加 reload\_plugins 方法用于手动重新加载所有插件，删除 load\_plugin\_from\_class 方法，并在程序式地导入插件或适配器时改变 config ([4eb1634](https://github.com/AliceBotProject/alicebot/commit/4eb1634ae812ba0ec92261d600bd0814f708aff0))
* 删除 hot\_reload 配置项，热重载启用方式更改为实例化 Bot 时传入参数 ([87976de](https://github.com/AliceBotProject/alicebot/commit/87976de50cf315a517832aa03fc73e409d2fd34a))
* 添加热重载功能，修改 utils 模块中 load\_module 相关函数的行为 ([576958f](https://github.com/AliceBotProject/alicebot/commit/576958f394aa80f7684e803e4d0c8e345286e30a))
* 修改 load\_module 相关函数的签名 ([300e09a](https://github.com/AliceBotProject/alicebot/commit/300e09a250281ee96696960d657767f5fb67ade0))
* 修改 load\_module 相关函数的行为 ([be20985](https://github.com/AliceBotProject/alicebot/commit/be2098555113c143b8ebeb0b33f92bbb9b568d28))
* 修改部分日志文本，修改 load\_modules\_from\_dir 函数的返回值 ([c6eb684](https://github.com/AliceBotProject/alicebot/commit/c6eb684aa0e07f219468edf4e0c2b7291d49e0ba))
* **bot:** 热重载时会检测配置文件的更新并自动重新运行 ([dbb0b50](https://github.com/AliceBotProject/alicebot/commit/dbb0b505ce3388d5d44a6ab9071b4100276208e0))
* **bot:** 热重载时会自动更新配置 ([e28c9b3](https://github.com/AliceBotProject/alicebot/commit/e28c9b3c3d50c8b7280370e4c7ecf961cef4d79b))
* **bot:** 删除 config\_file 和 config\_dict 属性并修改配置加载相关行为，添加 restart 方法用于重新运行 AliceBot ([956e2ea](https://github.com/AliceBotProject/alicebot/commit/956e2ead6e9ccd3e58d6dae218743787ffade217))
* **log:** 添加 verbose\_exception\_log 配置项，提供可选的详细异常记录 ([1565f42](https://github.com/AliceBotProject/alicebot/commit/1565f42a755f8e9cb173f5760070f5864bca1f3e))
* **plugin:** 修改 plugin\_state 的 key 为 plugin name ([f849743](https://github.com/AliceBotProject/alicebot/commit/f849743d06cda31f1111e1fa35a77f94f0552bf3))


### BREAKING CHANGES

* Plugin 和 Adapter 等类必须直接定义于导入的模块中



## [0.3.1](https://github.com/AliceBotProject/alicebot/compare/v0.3.0...v0.3.1) (2022-06-08)


### Bug Fixes

* 修复 load\_plugins\_from\_dir 方法不会导入配置类的问题 ([bc6dc1a](https://github.com/AliceBotProject/alicebot/commit/bc6dc1a0f8f209388d76cd927504da05d2c97160))


### Features

* 添加部分 docstring ([4d07ac2](https://github.com/AliceBotProject/alicebot/commit/4d07ac2bb9dd46e3b13816df5e983a02507dcba0))



## [0.3.0](https://github.com/AliceBotProject/alicebot/compare/v0.2.1...v0.3.0) (2022-05-04)


### Bug Fixes

* **bot:** 修复 Windows 系统下退出时出现异常 ([bc86eed](https://github.com/AliceBotProject/alicebot/commit/bc86eed8e21c7a674c751b4b9a20475bc8b663ca))
* **mirai:** 修复 GroupMemberInfo 类的类型错误 ([c96ca40](https://github.com/AliceBotProject/alicebot/commit/c96ca40f2fa0a3cc89f16e7077f2fb0fcfe61175))
* **utils:** 修复 python 3.10 下无法运行的问题 ([094ac04](https://github.com/AliceBotProject/alicebot/commit/094ac047e7d1b0f5c1d671f712378de67cc19085))


### Features

* 添加 state 状态存储功能 ([d94a3fe](https://github.com/AliceBotProject/alicebot/commit/d94a3fe2ff23f613fd8c42c5f251f7159f37950f))
* 添加 typing 模块，将所有类型变量定义转移到 alicebot.typing 模块中 ([eea30ed](https://github.com/AliceBotProject/alicebot/commit/eea30ed9718451b18423a335427a39cf896487ec))
* 为大多数模块添加 \_\_all\_\_ 属性 ([d58ad7e](https://github.com/AliceBotProject/alicebot/commit/d58ad7e91f583384d23e6bf800d68c9952810878))
* 为各个适配器添加泛型 Event 支持 ([aeb9ee1](https://github.com/AliceBotProject/alicebot/commit/aeb9ee15795493ff5fb7bd164ddc5d8dedff6c96))
* 修改 Bot 的 should\_exit 类型为 asyncio.Event ([4e9fdf1](https://github.com/AliceBotProject/alicebot/commit/4e9fdf1cf05fd4350c1d5313008f691af8d03e30))
* 移除 Bot 类的 loop 属性，并且不再使用低层级事件循环 API 启动 Bot 的运行 ([be46f5a](https://github.com/AliceBotProject/alicebot/commit/be46f5a89595c83765c4eefe54e839d0d7e5337b))
* **adapter.utils:** 添加 WebSocketAdapter 适配器 ([710ab13](https://github.com/AliceBotProject/alicebot/commit/710ab13bb897c1daea8716c11a08fd948477e07f))
* **adapter:** 添加 test 适配器 ([1c5f08b](https://github.com/AliceBotProject/alicebot/commit/1c5f08b0a943c573da2785c64f2b8e6a7723e023))
* **adapter:** 修改开发模式环境变量名称为 ALICEBOT\_DEV ([ae457d9](https://github.com/AliceBotProject/alicebot/commit/ae457d9dbcd13db41df9b1ee9ee24d465604b007))
* **alicebot:** 重命名 Bot 对象的 \_\_init\_\_() 方法参数为 config\_file ([e0c2c5e](https://github.com/AliceBotProject/alicebot/commit/e0c2c5e8a266d825a675cb083169b7f058728144))
* **bot:** 修改 Bot 类的部分类型提示 ([b87d8e4](https://github.com/AliceBotProject/alicebot/commit/b87d8e410440df2a3a4896f01b868522c3e9d87a))
* **bot:** Bot 的 handle\_exit 方法设为非公开方法，并部分调整代码格式 ([6a92fb5](https://github.com/AliceBotProject/alicebot/commit/6a92fb5e780b93d0ea8d394060040913d16ad4d8))
* **bot:** Bot 类 \_\_init\_\_() 方法添加 config\_dict 参数 ([832f42c](https://github.com/AliceBotProject/alicebot/commit/832f42ccf6959b0fdf43aa2baa17017764a03954))
* **bot:** Bot 类添加 load\_plugin\_from\_class() 方法 ([f00bbab](https://github.com/AliceBotProject/alicebot/commit/f00bbab6f440db68578c519deb9d3bd1f069a606))
* **config:** 不再使用上下文变量隐式传递 config 对象，删除 dev\_env 配置项 ([53a9191](https://github.com/AliceBotProject/alicebot/commit/53a91912649720d8ffca4e9186c0d3f5fb398055))
* **cqhttp:** 更新 cqhttp 适配器 ([0703c4b](https://github.com/AliceBotProject/alicebot/commit/0703c4b9f1bbaac05562659c41ccf6c415f24d9c))
* DataclassEncoder 类移动到 utils 模块中 ([293f571](https://github.com/AliceBotProject/alicebot/commit/293f5718e3494e84415014762566d8a9cd130cc7))
* **event:** 为 Event 类添加泛型支持 ([8fb3601](https://github.com/AliceBotProject/alicebot/commit/8fb36013559d3e875bb974f28522867692b58975))
* **event:** 修改 Event 类的部分行为 ([0635be7](https://github.com/AliceBotProject/alicebot/commit/0635be7a9a5ef01fb47e8aa92a5797eea8ace847))
* **event:** 重命名 Event 类的 handled 属性为 \_\_handled\_\_ ([4617bd1](https://github.com/AliceBotProject/alicebot/commit/4617bd15346d4a65f1e7ce5b572b1aad0ffbe812))
* **event:** event 模块不再是包 ([83899ba](https://github.com/AliceBotProject/alicebot/commit/83899ba0bb7e00c671814af4f503cacba5551d61))
* **exceptions:** 删除 AdapterTimeout 异常类，并新增 GetEventTimeout 类，get 方法不再抛出 AdapterTimeout 而是 GetEventTimeout ([0d7f6fa](https://github.com/AliceBotProject/alicebot/commit/0d7f6fa87a285f89dfa5a89cae37eb5cda0023cd))
* **exceptions:** 使 EventException 继承自 BaseException 以防止被用户捕获 ([9a2f45e](https://github.com/AliceBotProject/alicebot/commit/9a2f45e71c9ae6b8105871417e83ae7c40d8c390))
* get 方法和相关逻辑从 Adapter 类移动到 Bot 类并删除 BaseAdapter 类 ([662a9f6](https://github.com/AliceBotProject/alicebot/commit/662a9f6f7477bfe85002b84269ae6c26ca249846))
* **message:** Message 类添加 is\_text(), get\_plain\_text(), replace() 等方法 ([92188fc](https://github.com/AliceBotProject/alicebot/commit/92188fc19c0579e72dea321a904eb850764194ca))
* **mirai:** 更新 mirai-api-http 适配器 ([cfca9e0](https://github.com/AliceBotProject/alicebot/commit/cfca9e047b8940514432e53602c48f3e9538471e))
* **plugin:** 删除 Plugin 类的 send() 方法和 adapter 属性，更改 get() 方法为 Bot 类的 get() 方法的别名，相应修改测试插件 ([0ae3533](https://github.com/AliceBotProject/alicebot/commit/0ae3533c7578cc56808cff4c1f6500c708ee1e06))
* **plugin:** 添加判断防止 Plugin 的 priority 和 block 属性不存在 ([cd4c7dd](https://github.com/AliceBotProject/alicebot/commit/cd4c7dd6df2857a6dd46a71c5deb18ecb91db9a7))
* **plugin:** 为 Plugin 类添加泛型支持 ([0cca087](https://github.com/AliceBotProject/alicebot/commit/0cca087c060543ee24a0f22dfa3bb1311c616c38))
* **utils:** 删除 load\_module 模块，将其代码移动到 utils 模块中 ([fcf96ee](https://github.com/AliceBotProject/alicebot/commit/fcf96eed2bbc7ee7bf1928b8d9058dadec3a3fbe))
* **utils:** 删除无用的 LinkedQueue 类 ([f7a0b5b](https://github.com/AliceBotProject/alicebot/commit/f7a0b5bdbb3f65e672e4af9448c0537f2781700b))
* **utils:** 为 Condition 类添加泛型支持 ([3e2d6ef](https://github.com/AliceBotProject/alicebot/commit/3e2d6ef6fe0bd16752261ab2ef43be860c0dc784))


### BREAKING CHANGES

* **event:** Event 类实例化时必须指定 adapter 参数
* **plugin:** 删除 Plugin 类的 send() 方法和 adapter 属性，更改 get() 方法定义
* 删除 BaseAdapter 类
* **exceptions:** 删除 AdapterTimeout 异常类，并新增 GetEventTimeout 类，get 方法不再抛出 AdapterTimeout 而是 GetEventTimeout
* DataclassEncoder 类移动到 utils 模块中
* 所有类型变量定义转移到 alicebot.typing 模块中
* 修改 Bot 的 should\_exit 类型为 asyncio.Event
* 移除 Bot 类的 loop 属性
* **adapter:** 开发模式环境变量名称从 dev\_env 改为 ALICEBOT\_DEV
* **config:** 删除 dev\_env 配置项



## [0.2.1](https://github.com/AliceBotProject/alicebot/compare/v0.2.0...v0.2.1) (2021-09-12)


### Bug Fixes

* **cqhttp, mirai, dingtalk:** 修复 message 类型的 event 的 reply() 方法错误拼写为 replay 的错误 ([bf4c6be](https://github.com/AliceBotProject/alicebot/commit/bf4c6be83ff12b4072260927d0b73e2d5f77d67b))
* **load\_module:** 修复 ModulePathFinder 在部分情况下可能出现的错误 ([71a7366](https://github.com/AliceBotProject/alicebot/commit/71a736694179cc39ee157e637864a779792f8b1b))


### Features

* **load\_module:** load\_module() 函数添加不导入显式继承自 ABC 的类的功能 ([b018aaa](https://github.com/AliceBotProject/alicebot/commit/b018aaa3aa6c259ae080513eb8e85afe79309961))
* **message:** 增加 Message 类对 Iterable[Union[T\_MessageSegment, str, Mapping]] 类型的处理能力 ([1dc35cb](https://github.com/AliceBotProject/alicebot/commit/1dc35cb103fda5ee6bd4efa3e45ebc4cc38e0302))


### BREAKING CHANGES

* **cqhttp, mirai, dingtalk:** 所有适配器中 message 类型的 event 的 replay() 方法重命名为 reply()



## [0.2.0](https://github.com/AliceBotProject/alicebot/compare/v0.1.0...v0.2.0) (2021-09-04)


### Bug Fixes

* **.:** 修复 bot\_exit\_hook() 方法错误的类型提示 ([6add388](https://github.com/AliceBotProject/alicebot/commit/6add3883be4cce21fd7a731b872da71e1ec6b440))
* **.:** 修复当插件抛出 StopException 时会不执行其余同优先级的插件的 bug ([0d9eadc](https://github.com/AliceBotProject/alicebot/commit/0d9eadccabd0b7dac93943df4280626713ab57dd))
* **.:** 修复了当插件进行事件处理过程中出现错误时，插件的 block 属性会被忽略的 bug ([df71ffa](https://github.com/AliceBotProject/alicebot/commit/df71ffa14cdc1cd37128e717e4214a4895f11e6a))
* **adapter.cqhttp, adapter.utils:** 解决了 WebSocket 连接时无法关闭 AliceBot 的问题 ([aba36fd](https://github.com/AliceBotProject/alicebot/commit/aba36fdba96245fbf466142a240190be77891dd1))
* **cqhttp, adapter.utils:** 修复未进行 websocket 连接时直接关闭 alicebot 时报错的 bug ([157928d](https://github.com/AliceBotProject/alicebot/commit/157928d460a4b159960e4183eae2a79a3975e8a1))
* **cqhttp:** 为 api\_response 设置最大长度，解决潜在的内存泄露问题 ([96d0ed0](https://github.com/AliceBotProject/alicebot/commit/96d0ed06d32df65524371eab4b3cbf38ddd247f5))
* **message:** 修复 AbstractAdapter.get() 方法出现 KeyError 的 bug ([1f74906](https://github.com/AliceBotProject/alicebot/commit/1f749064aa0adcd5ed88ddd6981d730853f80cf3))


### Code Refactoring

* **message:** 修改 Message 和 MessageSegment 的子类继承方式。 ([d10a089](https://github.com/AliceBotProject/alicebot/commit/d10a0893e444d75a7ed99252d87cdfc2aa9ff5c4))


### Features

* **.:** 添加钩子函数 ([fa31d8e](https://github.com/AliceBotProject/alicebot/commit/fa31d8e4dbdb8524a356514a4af97d31d0e4cd4d))
* **adapter, config:** 添加 max\_event\_queue\_len 配置项，修改 adapter 的 max\_event\_queue\_len 从 Config 中获取 ([d1e41c0](https://github.com/AliceBotProject/alicebot/commit/d1e41c02be00b13aa339f3e9ba20068b446727d1))
* **adapter:** 将 Adapter 类抽象出 BaseAdapter 类，BaseAdapter 仅实现最基础的功能，Adapter 类在此基础上实现 handle\_event() 和 get() 等方法 ([2661929](https://github.com/AliceBotProject/alicebot/commit/26619299b8cdcd1df47c94567088dd0ebbde3b66))
* **adapter:** 添加从环境变量中获取 dev\_env 的值判断是否使用 pkg\_resources 风格的命名空间包的功能 ([d101fcf](https://github.com/AliceBotProject/alicebot/commit/d101fcfe2350bb1628f417a6e5d47b3046c24bd3))
* **adapter:** 重构事件分发的处理逻辑，修改 get() 方法，不再需要事件队列，而是使用 Condition 对象，提高性能，解决 get() 方法相关的潜在问题 ([8ed2a0d](https://github.com/AliceBotProject/alicebot/commit/8ed2a0d90f696939631affb7b42fa14dc2961e68))
* **apscheduler:** 添加 apscheduler 定时任务适配器 ([2498bf5](https://github.com/AliceBotProject/alicebot/commit/2498bf528dd5e26be2b4ac328e588826ad2a9bb3))
* **apscheduler:** 添加 scheduler\_decorator() 装饰器 ([09747a2](https://github.com/AliceBotProject/alicebot/commit/09747a2109b6a9185a012cf1c620252797aa2dd2))
* **dingtalk:** 添加 send() 方法，修改回复消息的方式，使用 webhook 地址回复；完善注释文档和异常处理 ([74030df](https://github.com/AliceBotProject/alicebot/commit/74030df1bfca675d2e7fdb0234c2b41c939d0d30))
* **dingtalk:** 新增钉钉协议适配器 alicebot-adapter-dingtalk ([785fac6](https://github.com/AliceBotProject/alicebot/commit/785fac640c7e4a7abded0bbcb58b318d5bc308ef))
* **message:** 添加了 Message 类 startswith()、endswith() 方法对 T\_MessageSegment 类型的支持 ([6e65316](https://github.com/AliceBotProject/alicebot/commit/6e653160750c97ae76299f4e204c214526b26fde))
* **mirai:** 添加 mirai-api-http 的 Websocket Adapter 模式 ([94be1b4](https://github.com/AliceBotProject/alicebot/commit/94be1b43c1cb324c3e6b696e376d3020d5415676))
* **mirai:** 添加支持 mirai-api-http 的 Reverse Websocket Adapter 的 mirai 适配器 ([01231dc](https://github.com/AliceBotProject/alicebot/commit/01231dca57c077d9e66606eacc9e059195edc592))
* **plugin:** 添加了 \_\_post\_init\_\_() 方法用于初始化后处理 ([6ffca3c](https://github.com/AliceBotProject/alicebot/commit/6ffca3cdc0842d05789f28ba00882145b55889c0))


### Performance Improvements

* **adapter, event:** 使用链队列代替列表作为事件队列，优化 get() 方法的性能 ([fecc7b1](https://github.com/AliceBotProject/alicebot/commit/fecc7b1287e799a02a0bb0c149d058b8db39e221))


### BREAKING CHANGES

* **message:** Message 的子类不再需要重写 \_construct() 方法，而需要重写 \_set\_message\_segment\_class() 和 \_str\_to\_message\_segment() 方法。
    MessageSegment 则需要重写 \_set\_message\_class() 方法。
refactor(cqhttp.message): 适配上述修改。
* **.:** 当超时时不再返回 None，而是抛出 AdapterTimeout 异常



## 0.1.0 (2021-07-24)



