import fs from "fs";
import path from "path";
import { defineConfig, DefaultTheme } from "vitepress";

const baseDir: string = "docs";

export default defineConfig({
  lang: "zh-CN",
  title: "AliceBot",
  description: "简单的 Python 异步多后端聊天机器人框架",

  lastUpdated: true,

  head: [
    ["link", { rel: "icon", href: "/logo.png" }],
    ["link", { rel: "manifest", href: "/manifest.json" }],
    ["meta", { name: "theme-color", content: "#ffffff" }],
    ["meta", { name: "apple-mobile-web-app-capable", content: "yes" }],
    [
      "meta",
      { name: "apple-mobile-web-app-status-bar-style", content: "black" },
    ],
    ["link", { rel: "apple-touch-icon", href: "/icons/apple-touch-icon.png" }],
    ["link", { rel: "mask-icon", href: "/icons/safari-pinned-tab.svg" }],
    [
      "meta",
      { name: "msapplication-TileImage", content: "/icons/mstile-150x150.png" },
    ],
    ["meta", { name: "msapplication-TileColor", content: "#2d89ef" }],
  ],

  themeConfig: {
    logo: "/logo.png",
    nav: [
      { text: "主页", link: "/" },
      { text: "指南", link: "/guide/" },
      { text: "API", link: "/api/" },
      { text: "更新日志", link: "/changelog" },
    ],

    sidebar: {
      "/guide/": sidebarGuide(),
      "/api/": sidebarApi(),
    },

    editLink: {
      pattern:
        "https://github.com/AliceBotProject/alicebot/edit/master/docs/:path",
      text: "在 GitHub 上编辑此页",
    },

    lastUpdatedText: "上次更新",

    socialLinks: [
      {
        icon: "github",
        link: "https://github.com/AliceBotProject/alicebot",
      },
    ],

    footer: {
      message: "Released under the MIT License.",
      copyright: "Copyright © 2021-present st1020",
    },
  },
});

function getSidebarItem(file: string): DefaultTheme.SidebarItem {
  const content = fs.readFileSync(path.join(baseDir, file), "utf-8");
  const match = content.match(/^\s*#+\s+(.*)/m);
  if (match === null) {
    return {
      text: "",
      link: file,
    };
  }
  return {
    text: match[1].trim(),
    link: file,
  };
}

function getSidebarChildrenItems(dir: string): DefaultTheme.SidebarItem[] {
  try {
    let readme_flag = false;
    let temp = fs.readdirSync(path.join(baseDir, dir)).filter((name) => {
      if (name == "index.md") {
        readme_flag = true;
        return false;
      }
      return (
        !name.startsWith(".") &&
        fs.statSync(path.join(baseDir, dir, name)).isFile()
      );
    });
    if (readme_flag) temp.unshift("index.md");
    return temp.map((item) => getSidebarItem(path.join(dir, item)));
  } catch {
    return [];
  }
}

function sidebarGuide() {
  return [
    {
      text: "基础",
      collapsible: false,
      items: [
        "/guide/index.md",
        "/guide/getting-started.md",
        "/guide/basic-config.md",
        "/guide/plugin-basics.md",
      ].map(getSidebarItem),
    },
    {
      text: "进阶",
      collapsible: false,
      items: [
        "/guide/plugin-advanced.md",
        "/guide/builtin-message.md",
        "/guide/scheduler.md",
        "/guide/hook-function.md",
        "/guide/hot-reload.md",
      ].map(getSidebarItem),
    },
    {
      text: "协议适配器",
      collapsible: false,
      items: [
        "/guide/cqhttp-adapter.md",
        "/guide/mirai-adapter.md",
        "/guide/dingtalk-adapter.md",
      ].map(getSidebarItem),
    },
  ];
}

function sidebarApi() {
  return [
    {
      text: "AliceBot Api Reference",
      items: [
        ...getSidebarChildrenItems("/api/"),
        getSidebarItem("/api/adapter/index.md"),
        {
          text: "alicebot.adapter.utils",
          link: "/api/adapter/utils.md",
        },
        {
          text: "alicebot.adapter.cqhttp",
          link: "/api/adapter/cqhttp/index.md",
          items: getSidebarChildrenItems("/api/adapter/cqhttp/"),
        },
        {
          text: "alicebot.adapter.mirai",
          link: "/api/adapter/mirai/index.md",
          items: getSidebarChildrenItems("/api/adapter/mirai/"),
        },
        {
          text: "alicebot.adapter.dingtalk",
          link: "/api/adapter/dingtalk/index.md",
          items: getSidebarChildrenItems("/api/adapter/dingtalk/"),
        },
        {
          text: "alicebot.adapter.apscheduler",
          link: "/api/adapter/apscheduler/index.md",
          items: getSidebarChildrenItems("/api/adapter/apscheduler/"),
        },
      ],
    },
  ];
}
