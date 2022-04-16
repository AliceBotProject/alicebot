---
sidebar: auto
---

# 更新日志

## 0.2.1 (2021-09-12)


### Bug Fixes

* **cqhttp, mirai, dingtalk:** 修复 message 类型的 event 的 reply() 方法错误拼写为 replay 的错误 ([bf4c6be](https://github.com/st1020/alicebot/commit/bf4c6be83ff12b4072260927d0b73e2d5f77d67b))
* **load_module:** 修复 ModulePathFinder 在部分情况下可能出现的错误 ([71a7366](https://github.com/st1020/alicebot/commit/71a736694179cc39ee157e637864a779792f8b1b))


### Features

* **load_module:** load_module() 函数添加不导入显式继承自 ABC 的类的功能 ([b018aaa](https://github.com/st1020/alicebot/commit/b018aaa3aa6c259ae080513eb8e85afe79309961))
* **message:** 增加 Message 类对 Iterable[Union[T_MessageSegment, str, Mapping]] 类型的处理能力 ([1dc35cb](https://github.com/st1020/alicebot/commit/1dc35cb103fda5ee6bd4efa3e45ebc4cc38e0302))


### BREAKING CHANGES

* **cqhttp, mirai, dingtalk:** 所有适配器中 message 类型的 event 的 replay() 方法重命名为 reply()

## 0.2.0


### Features

* **apscheduler:** 添加 apscheduler 定时任务适配器 ([2498bf5](https://github.com/st1020/alicebot/commit/2498bf528dd5e26be2b4ac328e588826ad2a9bb3))
* **dingtalk:** 新增钉钉协议适配器 alicebot-adapter-dingtalk ([785fac6](https://github.com/st1020/alicebot/commit/785fac640c7e4a7abded0bbcb58b318d5bc308ef))
* **mirai:** 添加 mirai-api-http 的 Websocket Adapter 模式 ([94be1b4](https://github.com/st1020/alicebot/commit/94be1b43c1cb324c3e6b696e376d3020d5415676))
* **mirai:** 添加支持 mirai-api-http 的 Reverse Websocket Adapter 的 mirai 适配器 ([01231dc](https://github.com/st1020/alicebot/commit/01231dca57c077d9e66606eacc9e059195edc592))
* **.:** 添加钩子函数 ([fa31d8e](https://github.com/st1020/alicebot/commit/fa31d8e4dbdb8524a356514a4af97d31d0e4cd4d))

此更新包含大量问题修复和功能增加，涉及大量不兼容变化，以上仅列举少量重要变化。

## 0.1.0

AliceBot 首个测试版。

