---
title: 插件商店
editLink: false
aside: false
---

<script setup>
import { ref } from 'vue'
import PluginList from '../components/PluginList.vue'
// from '../components/test.json'
// import {data} from '../static/plugins.json'
</script>

# {{ $frontmatter.title }}
<Suspense><PluginList></PluginList></Suspense>
