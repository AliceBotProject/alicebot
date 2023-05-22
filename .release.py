import json
import argparse
import subprocess
from pathlib import Path

import tomlkit

CHANGELOG_PREFIX = """---
sidebar: auto
---

# 更新日志


"""

parser = argparse.ArgumentParser(prog="release", description="AliceBot Release")
parser.add_argument("version", help="target version")
args = parser.parse_args()
version = args.version


def write_version_json(file: Path, version: str):
    with open("package.json", encoding="utf-8") as f:
        json_file = json.load(f)
    json_file["version"] = version
    with open("package.json", "w", encoding="utf-8") as f:
        json.dump(json_file, f, indent=2)


def write_version_toml(file: Path, version: str, *, is_package: bool = False):
    with open(file, encoding="utf-8") as f:
        toml_file = tomlkit.load(f)
    toml_file["tool"]["poetry"]["version"] = version  # type: ignore
    if is_package:
        toml_file["tool"]["poetry"]["dependencies"]["alicebot"] = version  # type: ignore
    with open(file, "w", encoding="utf-8") as f:
        tomlkit.dump(toml_file, f)


write_version_json(Path("package.json"), version)
write_version_toml(Path("pyproject.toml"), version)
for package in Path("packages").iterdir():
    if package.is_dir():
        write_version_toml(package / "pyproject.toml", version, is_package=True)

subprocess.run(["pnpm", "run", "changelog"])
with open("docs/changelog.md", encoding="utf-8") as f:
    changelog_file = f.read()
with open("docs/changelog.md", "w", encoding="utf-8") as f:
    f.write(
        CHANGELOG_PREFIX
        + (
            "\n".join(
                map(
                    lambda x: ("#" + x) if x.startswith("# ") else x,
                    changelog_file.split("\n"),
                )
            )
        ).replace("_", "\\_")
    )
subprocess.run(["pnpm", "exec", "prettier", "--write", "docs/changelog.md"])
subprocess.run(["git", "tag", "-d", "v" + version])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "chore: 发布 " + version])
subprocess.run(["git", "tag", "v" + version])
