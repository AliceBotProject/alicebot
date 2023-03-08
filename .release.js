import { writeFile } from "fs";
import { promisify } from "util";
import { Writable } from "stream";
import conventionalChangelog from "conventional-changelog";

const fileName = "docs/changelog.md";
const prefix = `---
sidebar: auto
---

# 更新日志


`;

const version = process.env.npm_package_version;
const exec = promisify(require("child_process").exec);

conventionalChangelog({
  preset: "angular",
  releaseCount: 0,
}).pipe(
  new Writable({
    async write(chunk, _encoding, callback) {
      if (this.s === undefined) {
        await exec("git tag v" + version);
        this.s = prefix;
      }
      let temp = chunk.toString();
      if (temp.startsWith("# ")) {
        temp = "#" + temp;
      }
      this.s += temp;
      callback();
    },
    async destroy() {
      writeFile(fileName, this.s.replaceAll("_", "\\_"), (err) =>
        err ? console.log(err) : null
      );
      console.log("成功写入文件");
      await exec("git tag -d v" + version);
      await exec("git add .");
      await exec('git commit -m "chore: 发布 ' + version + '"');
      await exec("git tag v" + version);
    },
  })
);
