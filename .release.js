const fs = require("fs")
const util = require("util")
const stream = require("stream")
const conventionalChangelog = require("conventional-changelog")

const fileName = "docs/changelog.md"
const prefix = `---
sidebar: auto
---

# 更新日志


`

const version = process.env.npm_package_version
const exec = util.promisify(require("child_process").exec)

conventionalChangelog({
  preset: "angular", releaseCount: 0,
}).pipe(new stream.Writable({
  async write(chunk, encoding, callback) {
    if (this.s === undefined) {
      await exec("git tag v" + version)
      this.s = prefix
    }
    let temp = chunk.toString()
    if (temp.startsWith("# ")) {
      temp = '#' + temp
    }
    this.s += temp
    callback()
  }, async destroy() {
    fs.writeFile(fileName, this.s, err => err ? console.log(err) : null)
    console.log("成功写入文件")
    await exec("git tag -d v" + version)
    await exec("git add .")
    await exec("git commit -m \"chore: 发布 " + version + "\"")
    await exec("git tag v" + version)
  }
}))
