<script setup lang="ts">
import { computed, ref, watchEffect } from 'vue'
import Pagination from './Pagination.vue'
import Card from './Card.vue'
import type { MetaData } from './types'

enum StoreType {
  Plugins = 'plugins',
  Adapters = 'adapters',
  Bots = 'bots',
}

const storeType = ref<StoreType>(StoreType.Plugins)
const dataItems = ref<MetaData[]>([])

const searchText = ref<string>('')
const searchedItems = computed<MetaData[]>(() => {
  if (searchText.value)
    return dataItems.value.filter(item => item.name.includes(searchText.value))
  return dataItems.value.toSorted((a, b) => b.time - a.time)
})

const pageSize = 10
const pageNumber = ref<number>(1)
const pageTotal = computed<number>(() => Math.ceil(searchedItems.value.length / pageSize))
const pageItems = computed(() => {
  if (searchedItems.value.length === 0)
    return []
  return searchedItems.value.slice(
    (pageNumber.value - 1) * pageSize,
    pageNumber.value * pageSize,
  )
})

watchEffect(async () => {
  dataItems.value = await (await fetch(`https://store.alicebot.dev/${storeType.value}.json`)).json()
  searchText.value = ''
})
</script>

<template>
  <div>
    <div class="mt-10 flex items-center text-sm text-vp-text-1">
      <div class="mr-8">
        类型
      </div>
      <div class="flex flex-wrap gap-2">
        <button
          class="cursor-pointer rounded bg-vp-bg-soft px-2 py-0.5 hover:bg-vp-brand-soft hover:text-vp-brand-1"
          :class="storeType === StoreType.Plugins ? 'bg-vp-brand-soft text-vp-brand-1' : ''"
          @click="storeType = StoreType.Plugins"
        >
          插件
        </button>
        <button
          class="cursor-pointer rounded bg-vp-bg-soft px-2 py-0.5 hover:bg-vp-brand-soft hover:text-vp-brand-1"
          :class="storeType === StoreType.Adapters ? 'bg-vp-brand-soft text-vp-brand-1' : ''"
          @click="storeType = StoreType.Adapters"
        >
          适配器
        </button>
        <button
          class="cursor-pointer rounded bg-vp-bg-soft px-2 py-0.5 hover:bg-vp-brand-soft hover:text-vp-brand-1"
          :class="storeType === StoreType.Bots ? 'bg-vp-brand-soft text-vp-brand-1' : ''"
          @click="storeType = StoreType.Bots"
        >
          机器人
        </button>
      </div>
    </div>
    <div class="my-4">
      <div class="h-px bg-neutral-700 opacity-15" />
      <div class="flex p-2">
        <div class="i-mdi-magnify mr-2 h-6 w-6" />
        <input
          v-model="searchText"
          class="my-auto w-full"
          type="text"
          role="search"
          placeholder="Search..."
        >
      </div>
      <div class="h-px bg-neutral-700 opacity-15" />
    </div>
    <Pagination key="topPagination" v-model="pageNumber" :total="pageTotal" />
    <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
      <Card v-for="(item, index) in pageItems" :key="index" :item="item" />
    </div>
    <Pagination key="bottomPagination" v-model="pageNumber" :total="pageTotal" />
  </div>
</template>
