"""用于发布新版本的脚本。"""
# ruff: noqa: S603, S607
import argparse
import json
import subprocess
from pathlib import Path

import tomlkit
from tomlkit.container import OutOfOrderTableProxy
from tomlkit.items import Array, Table

CHANGELOG_PREFIX = """---
sidebar: auto
---

# 更新日志


"""

parser = argparse.ArgumentParser(prog="release", description="AliceBot Release")
parser.add_argument("version", help="target version")
args = parser.parse_args()
version = args.version


def write_version_json(file: Path, version: str) -> None:
    """写入 package.json。

    Args:
        file: 文件路径。
        version: 版本信息。
    """
    with file.open(encoding="utf-8") as f:
        json_file = json.load(f)
    json_file["version"] = version
    with file.open("w", encoding="utf-8") as f:
        json.dump(json_file, f, indent=2)


def write_version_toml(file: Path, version: str, *, is_package: bool = False) -> None:
    """写入 pyproject.toml。

    Args:
        file: 文件路径。
        version: 版本信息。
        is_package: 是否是 packages 目录下的包。
    """
    with file.open(encoding="utf-8") as f:
        toml_file = tomlkit.load(f)
    project_table = toml_file["project"]
    assert isinstance(project_table, (OutOfOrderTableProxy, Table))
    project_table["version"] = version
    if is_package:
        dependencies_array = project_table["dependencies"]
        assert isinstance(dependencies_array, Array)
        dependencies_array[0] = f"alicebot=={version}"
    with file.open("w", encoding="utf-8") as f:
        tomlkit.dump(toml_file, f)


write_version_json(Path("package.json"), version)
write_version_toml(Path("pyproject.toml"), version)
for package in Path("packages").iterdir():
    if package.is_dir():
        write_version_toml(package / "pyproject.toml", version, is_package=True)
subprocess.run(["pdm", "update"], check=True)
subprocess.run(["pnpm", "run", "changelog"], check=True)
with Path("docs/changelog.md").open(encoding="utf-8") as f:
    changelog_file = f.read()
with Path("docs/changelog.md").open("w", encoding="utf-8") as f:
    f.write(
        CHANGELOG_PREFIX
        + (
            "\n".join(
                ("#" + x) if x.startswith("# ") else x
                for x in changelog_file.split("\n")
            )
        ).replace("_", "\\_")
    )
subprocess.run(["pnpm", "exec", "prettier", "--write", "docs/changelog.md"], check=True)
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "chore: 发布 " + version], check=True)
