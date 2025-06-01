# 贡献指南

::: tip 注意
本文档适用于希望为 AliceBot 本身做出贡献的开发者。
:::

非常感谢您愿意为 AliceBot 项目贡献代码。

为了项目代码的质量和一致性，在正式开始您的贡献前，请先阅读本文档并遵循本文档的指引。

## 配置开发环境

### 安装依赖

AliceBot 使用 [uv](https://github.com/astral-sh/uv) 管理项目的依赖。

因此，你需要先根据 [uv](https://docs.astral.sh/uv/getting-started/installation/) 的指引安装 uv，之后在项目目录中执行以下命令：

```shell
uv sync --all-extras --dev
```

AliceBot 项目的文档使用 [VitePress](https://vitepress.dev/) 生成，如果你想要贡献 AliceBot 的文档，请额外安装 [pnpm](https://pnpm.io/)，并在项目目录中执行以下命令：

```shell
pnpm install
```

### 编辑器配置

虽然并非强制，但建议使用 VSCode 作为编辑器对 AliceBot 项目的代码进行编辑，因为 AliceBot 具有完全的类型注解，VSCode 的 BasedPyright 插件具有相对较好的静态类型检查效果。

如果你使用 VSCode 作为编辑器，需要安装 **Python**、**BasedPyright** 和 **Ruff** 插件，并进行以下配置：

```json
{
  "[python]": {
    "editor.formatOnPaste": false,
    "editor.formatOnSaveMode": "file",
    "editor.defaultFormatter": "charliermarsh.ruff"
  }
}
```

## 代码规范

### 代码质量

请确保你的代码风格和项目现有代码保持一致，变量命名清晰且符合规范，有适量的注释与测试代码，不要破坏现有功能。

### 代码风格

AliceBot 的代码风格遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 规范。

AliceBot 使用 [Ruff](https://docs.astral.sh/ruff/) 作为格式化工具，如果你已经按照上文配置了 VSCode，那么你应该很容易遵循此规范，否则请在提交前手动执行上述格式化工具。

### 类型注解

AliceBot 具有完全的类型注解。

在 [pyproject.toml](https://github.com/AliceBotProject/alicebot/blob/main/pyproject.toml) 文件中已经提供了针对 BasedPyright 和 MyPy 的配置，请确保你的代码能够通过这种严格程度的类型检查。

如果必要，你可以在代码中使用 `# type: ignore` 注释来抑制类型检查，但请注意，请将此作为最后手段，不要轻易使用。

### Docstring

AliceBot 中的全部函数、类、模块都具有 Docstring，AliceBot 的 Docstring 遵循 [Google 风格](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)，但请注意不需要在 Docstring 中添加类型。

```python
def foo(a: int, b: float) -> str:
    """错误的 Docstring。

    Args:
        a (int): 参数 a 的说明。
        b (float): 参数 b 的说明。

    Returns:
        str: 返回值的说明。
    """

def foo(a: int, b: float) -> str:
    """正确的 Docstring。

    Args:
        a: 参数 a 的说明。
        b: 参数 b 的说明。

    Returns:
        返回值的说明。
    """
```

## 贡献文档

AliceBot 使用使用 [VitePress](https://vitepress.dev/) 生成文档。API 文档则由 [Sophia-doc](https://github.com/st1020/sophia-doc) 自动生成。

在你修改完 AliceBot 的文档后，可以使用 pnpm 安装依赖后在开发模式下实时预览文档：

```shell
pnpm run docs:dev
```

## Commit 规范

请尽量使你的每一个 commit 都只做一件事。

AliceBot 的 commit message 格式遵循 [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) 规范。
