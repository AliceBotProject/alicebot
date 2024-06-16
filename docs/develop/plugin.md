# 发布插件

AliceBot 提供了一个商店，用于分享用户开发的插件。当你已经完成了自己的插件开发，并且希望将他分享给大家，那么本篇教程将会帮助你完成。

在阅读本插件开发指南前，请先确保你已经阅读了[指南](/guide/)中关于如何插件开发的部分，并且已经可以顺利开发一个自己的插件。

## 插件模板

AliceBot 提供了一个插件模版 [AliceBotProject/alicebot-plugin-template](https://github.com/AliceBotProject/alicebot-plugin-template)，为了避免不必要的麻烦，建议直接从插件模块开始你的插件。

```sh
git clone https://github.com/AliceBotProject/alicebot-plugin-template.git
```

### 开始

AliceBot 的插件的项目名建议以 `alicebot-plugin-` 开头，全部小写，例如 `alicebot-plugin-example`。项目名应该被用于 PyPI 的包名、代码仓库名等。对于模块名，则应按照 Python 语言的惯例，将项目名中的 `-` 替换为 `_`，例如 `alicebot_plugin_example`。

例如，我们将开发一个名为 `alicebot-plugin-hello` 的插件。

首先，修改 clone 下来的模版的目录名为 `alicebot-plugin-hello`，并修改其中的 `alicebot_plugin_template` 目录的目录名为 `alicebot_plugin_hello`。

编辑 `pyproject.toml` 文件，修改其中有 `# TODO` 注释的部分，将其修改为你的插件的对应信息。比如，现在我们需要将 `project.name` 从 `alicebot-plugin-template` 修改为 `alicebot-plugin-hello`。

```toml {2}
[project]
name = "alicebot-plugin-hello" # TODO
version = "0.1.0" # TODO
description = "AliceBot Plugin Template." # TODO
authors = [{ name = "AliceBot", email = "concontact@alicebot.dev" }] # TODO
license = { text = "MIT" } # TODO

# ...
```

之后编辑 `README.md` 文件和 `LICENSE` 文件，将其替换为你的插件的对应信息。

### 编写插件

AliceBot 插件模版使用 [PDM](https://pdm-project.org/) 作为依赖管理工具，因此，你需要先根据 [PDM](https://pdm-project.org/latest/#installation) 的指引安装 PDM，之后在项目目录中执行以下命令：

```sh
pdm install
```

如果你的插件依赖了其他包，可以使用以下命令添加依赖：

```sh
pdm add <package>
```

你的插件的代码应位于 `alicebot_plugin_<you_plugin_name>` 目录下，插件模板提供了一个简单的插件示例，你可以在此基础上进行修改。

### 发布插件

为了将你的插件提交到 AliceBot 的插件商店，你需要先将你的插件发布到 PyPI 上。

在上传之前，你应该首先检查：

1. 确保你的插件已经可以正常安装，并且可以运行。
2. 确保的你插件的信息无误，`pyproject.toml` 文件中的信息已经正确填写，`README.md` 文件和 `LICENSE` 文件已经替换为你自己的信息。

你可以参考 [PyPI 文档](https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives)和 [PDM 文档](https://pdm-project.org/latest/usage/publish/)的指引将你的插件发布到 PyPI 上。

简单来说，你需要注册一个 PyPI 账号，生成一个个人访问令牌 (Token)，最后使用 `pdm publish` 命令将你的插件发布到 PyPI 上。

完成 PyPI 的发布后就可以将你的插件发布在 AliceBot 的插件商店了。

你可以点击以下链接在 [AliceBotProject/alicebot-store](https://github.com/AliceBotProject/alicebot-store) 仓库新建一个 Issue：

<https://github.com/AliceBotProject/alicebot-store/issues/new/choose>

选择“Publish a plugin”，修改 Issue 的标题中的 `{name}` 为你的插件的名字，并在下方的表单中填写 `pypi_name` 和 `module_name`。

比如，对于之前提到的 `alicebot-plugin-hello` 这个插件来说，Issue 的标题应该是 `[plugin]: Hello`，`pypi_name` 应该填写 `alicebot-plugin-hello`，`module_name` 应该填写 `alicebot_plugin_hello`。

提交 Issue 后，机器人将开始自动验证，通过验证后将自动提交 PR，你只需要等待管理员合并 PR 即可将插件发布在 AliceBot 的插件商店。
