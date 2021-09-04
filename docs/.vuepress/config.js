// const fs = require("fs");
// const path = require("path");
module.exports = {
  title: 'AliceBot',
  description: '简单的 Python 异步多后端聊天机器人框架',
  markdown: {
    lineNumbers: true
  },
  locales: {
    '/': {
      lang: 'zh-CN',
      title: 'AliceBot',
      description: '简单的 Python 异步多后端机器人框架'
    }
  },
  head: [
    ['link', {rel: 'icon', href: '/logo.png'}],
    ['link', {rel: 'manifest', href: '/manifest.json'}],
    ['meta', {name: 'theme-color', content: '#ffffff'}],
    ['meta', {name: 'apple-mobile-web-app-capable', content: 'yes'}],
    ['meta', {name: 'apple-mobile-web-app-status-bar-style', content: 'black'}],
    ['link', {rel: 'apple-touch-icon', href: '/icons/apple-touch-icon.png'}],
    ['link', {rel: 'mask-icon', href: '/icons/safari-pinned-tab.svg', color: '#5bbad5'}],
    ['meta', {name: 'msapplication-TileImage', content: '/icons/mstile-150x150.png'}],
    ['meta', {name: 'msapplication-TileColor', content: '#da532c'}]
  ],
  themeConfig: {
    logo: '/logo.png',
    repo: 'st1020/alicebot',
    editLinks: true,
    docsDir: 'docs',
    smoothScroll: true,
    locales: {
      '/': {
        label: '简体中文',
        selectText: '选择语言',
        ariaLabel: '选择语言',
        editLinkText: '在 GitHub 上编辑此页',
        lastUpdated: '上次更新',
        nav: [
          {text: '主页', link: '/'},
          {text: '指南', link: '/guide/'},
          {text: 'API', link: '/api/'},
          {text: '更新日志', link: '/changelog'}
        ],
        sidebarDepth: 2,
        sidebar: {
          '/guide/': [
            {
              title: '基础',
              collapsable: false,
              children: [
                '',
                'getting-started',
                'basic-config',
                'plugin-basics'
              ]
            },
            {
              title: '进阶',
              collapsable: false,
              children: [
                'plugin-advanced',
                'builtin-message',
                'scheduler',
                'hook-function'
              ]
            },
            {
              title: '协议适配器',
              collapsable: false,
              children: [
                'cqhttp-adapter',
                'mirai-adapter'
              ]
            }
          ],
          '/api/': [
            {
              title: 'AliceBot Api Reference',
              collapsable: false,
              children: [
                '',
                {title: 'alicebot.config', path: 'config'},
                {title: 'alicebot.event', path: 'event'},
                {title: 'alicebot.exception', path: 'exception'},
                {title: 'alicebot.load_module', path: 'load_module'},
                {title: 'alicebot.log', path: 'log'},
                {title: 'alicebot.message', path: 'message'},
                {title: 'alicebot.plugin', path: 'plugin'},
                {title: 'alicebot.adapter', path: 'adapter/'},
                {
                  title: 'alicebot.adapter.cqhttp',
                  collapsable: false,
                  path: '/api/adapter/cqhttp/',
                  children: [
                    {title: 'alicebot.adapter.cqhttp', path: 'adapter/cqhttp/'},
                    {title: 'alicebot.adapter.cqhttp.config', path: 'adapter/cqhttp/config'},
                    {title: 'alicebot.adapter.cqhttp.event', path: 'adapter/cqhttp/event'},
                    {title: 'alicebot.adapter.cqhttp.exception', path: 'adapter/cqhttp/exception'},
                    {title: 'alicebot.adapter.cqhttp.message', path: 'adapter/cqhttp/message'}
                  ]
                },
                {
                  title: 'alicebot.adapter.mirai',
                  collapsable: false,
                  path: '/api/adapter/mirai/',
                  children: [
                    {title: 'alicebot.adapter.mirai', path: 'adapter/mirai/'},
                    {title: 'alicebot.adapter.mirai.config', path: 'adapter/mirai/config'},
                    {title: 'alicebot.adapter.mirai.event', path: 'adapter/mirai/event'},
                    {title: 'alicebot.adapter.mirai.exception', path: 'adapter/mirai/exception'},
                    {title: 'alicebot.adapter.mirai.message', path: 'adapter/mirai/message'}
                  ]
                },
                {
                  title: 'alicebot.adapter.dingtalk',
                  collapsable: false,
                  path: '/api/adapter/dingtalk/',
                  children: [
                    {title: 'alicebot.adapter.dingtalk', path: 'adapter/dingtalk/'},
                    {title: 'alicebot.adapter.dingtalk.config', path: 'adapter/dingtalk/config'},
                    {title: 'alicebot.adapter.dingtalk.event', path: 'adapter/dingtalk/event'},
                    {title: 'alicebot.adapter.dingtalk.exception', path: 'adapter/dingtalk/exception'},
                    {title: 'alicebot.adapter.dingtalk.message', path: 'adapter/dingtalk/message'}
                  ]
                },
                {
                  title: 'alicebot.adapter.apscheduler',
                  collapsable: false,
                  path: '/api/adapter/apscheduler/',
                  children: [
                    {title: 'alicebot.adapter.apscheduler', path: 'adapter/apscheduler/'},
                    {title: 'alicebot.adapter.apscheduler.config', path: 'adapter/apscheduler/config'},
                    {title: 'alicebot.adapter.apscheduler.event', path: 'adapter/apscheduler/event'}
                  ]
                }
              ]
            }
          ]
        }
      }
    }
  },
  plugins: [
    ['@vuepress/back-to-top', true],
    ['@vuepress/pwa', {
      serviceWorker: true,
      updatePopup: true
    }],
    ['@vuepress/medium-zoom', true],
    ['container', {
      type: 'vue',
      before: '<pre class="vue-container"><code>',
      after: '</code></pre>'
    }]
  ]
}


// function getSideBar(folder) {
//   const extension = ['.md'];
//   return fs
//     .readdirSync(path.join(`${__dirname}/../${folder}`))
//     .filter(
//       (item) =>
//         item.toLowerCase() !== "readme.md" &&
//         fs.statSync(path.join(`${__dirname}/../${folder}`, item)).isFile() &&
//         extension.includes(path.extname(item))
//     );
// }