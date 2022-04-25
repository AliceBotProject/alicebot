import * as fs from 'fs';
import * as path from 'path';
import type {SidebarConfig} from '@vuepress/theme-default'

function getChildren(dir: string, baseDir: string = 'docs'): string[] {
  let readme_flag = false
  let temp = fs.readdirSync(path.join(baseDir, dir)).filter(name => {
    if (name == 'README.md') {
      readme_flag = true
      return false
    }
    return !name.startsWith('.') && fs.statSync(path.join(baseDir, dir, name)).isFile()
  })
  if (readme_flag)
    temp.unshift('README.md')
  return temp.map(item => path.join(dir, item))
}

export const zh: SidebarConfig = {
  '/guide/': [
    {
      text: '基础',
      collapsible: false,
      children: [
        '/guide/README.md',
        '/guide/getting-started.md',
        '/guide/basic-config.md',
        '/guide/plugin-basics.md',
      ]
    },
    {
      text: '进阶',
      collapsible: false,
      children: [
        '/guide/plugin-advanced.md',
        '/guide/builtin-message.md',
        '/guide/scheduler.md',
        '/guide/hook-function.md',
      ]
    },
    {
      text: '协议适配器',
      collapsible: false,
      children: [
        '/guide/cqhttp-adapter.md',
        '/guide/mirai-adapter.md',
      ]
    }
  ],
  '/api/': [
    {
      text: 'AliceBot Api Reference',
      children: [
        ...getChildren('/api/'),
        '/api/plugin/README.md',
        '/api/adapter/README.md',
        {
          text: 'alicebot.adapter.cqhttp',
          link: '/api/adapter/cqhttp/README.md',
          children: getChildren('/api/adapter/cqhttp/'),
        },
        {
          text: 'alicebot.adapter.mirai',
          link: '/api/adapter/mirai/README.md',
          children: getChildren('/api/adapter/mirai/'),
        },
        {
          text: 'alicebot.adapter.dingtalk',
          link: '/api/adapter/dingtalk/README.md',
          children: getChildren('/api/adapter/dingtalk/'),
        },
        {
          text: 'alicebot.adapter.apscheduler',
          link: '/api/adapter/apscheduler/README.md',
          children: getChildren('/api/adapter/apscheduler/'),
        },
      ],
    },
  ],
}