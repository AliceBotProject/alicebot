<script setup lang="ts">
import { ref, computed, onMounted } from "vue";
import IconSearch from "./icons/IconSearch.vue";
import Pagination from "./Pagination.vue";
import Card from "./Card.vue";

export interface DataItem {
  module_name?: string; // 导入时的模块名称
  pypi_name?: string; // 在 PyPi 上的名称
  name: string; // 名称
  description: string; // 描述
  author: string; // 作者
  license?: string; // 开源许可
  homepage?: string; // Github 链接
  tags: string[]; // Tag 列表
  is_official: boolean; // 是否为官方维护的插件
  time: number; // Unix timestamp
}

enum StoreType {
  Plugins = "plugins",
  Adapters = "adapters",
  Bots = "bots",
}

const URL = "https://store.alicebot.dev/";

const storeType = ref<StoreType>(StoreType.Plugins);
const dataItems = ref<DataItem[]>([]);

const searchText = ref<string>("");
const searchedData = computed<DataItem[]>(() => {
  let items = dataItems.value;
  if (!items) return [];
  if (!!searchText.value) {
    items = items.filter((item) => item.name.indexOf(searchText.value) > -1);
  }
  items = items.sort((a, b) => b.time - a.time);
  return items;
});

const pageSize = 10; // 每页显示的数量
const pageNum = ref<number>(1); // 当前页码
const pageTotal = computed<number>(() => {
  pageNum.value = 1;
  return Math.ceil(searchedData.value.length / pageSize);
}); // 总页数
const pageItems = computed(() => {
  if (searchedData.value.length === 0) return [];
  return searchedData.value.slice(
    (pageNum.value - 1) * pageSize,
    pageNum.value * pageSize
  );
});

const setType = async (type: StoreType) => {
  storeType.value = type;
  dataItems.value = await (await fetch(URL + storeType.value + ".json")).json();
  // dataItems.value = Array(50).fill({
  //   module_name: "alicebot_plugin_template",
  //   pypi_name: "alicebot-plugin-template",
  //   name: "alicebot-plugin-template",
  //   description: "AliceBot Plugin Template.",
  //   author: "st1020",
  //   license: "MIT",
  //   homepage: "https://github.com/",
  //   tags: ["alicebot", "bot", "chatbot", "tag1", "tag2"],
  //   is_official: false,
  //   time: 42,
  // });
  searchText.value = "";
};
onMounted(async () => await setType(StoreType.Plugins));
</script>

<template>
  <div>
    <div class="tab">
      <div opacity="80" text="sm">类型</div>
      <div class="select-list">
        <button
          class="select-button"
          @click="setType(StoreType.Plugins)"
          :class="{ active: storeType == StoreType.Plugins }"
        >
          插件
        </button>
        <button
          class="select-button"
          @click="setType(StoreType.Adapters)"
          :class="{ active: storeType == StoreType.Adapters }"
        >
          适配器
        </button>
        <button
          class="select-button"
          @click="setType(StoreType.Bots)"
          :class="{ active: storeType == StoreType.Bots }"
        >
          机器人
        </button>
      </div>
    </div>
    <div class="search-bar">
      <div class="divider" style="margin-top: 1rem"></div>
      <div class="search">
        <IconSearch class="icon" />
        <input
          class="search-input"
          type="text"
          role="search"
          placeholder="Search..."
          v-model="searchText"
        />
      </div>
      <div class="divider" style="margin-bottom: 1rem"></div>
    </div>
    <Pagination
      :pageTotal="pageTotal"
      v-model="pageNum"
      style="width: 100%"
      key="topPagination"
    />
    <div class="card-list">
      <Card v-for="(item, index) in pageItems" :key="index" :item="item" />
    </div>
    <Pagination
      :pageTotal="pageTotal"
      v-model="pageNum"
      style="width: 100%"
      key="bottomPagination"
    />
  </div>
</template>

<style scoped>
.tab {
  grid-row-gap: 0.5rem;
  row-gap: 0.5rem;
  margin-top: 2.5rem;
  grid-template-columns: 80px auto;
  display: grid;
}

.sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.select-list {
  grid-gap: 0.5rem;
  gap: 0.5rem;
  flex-wrap: wrap;
  display: flex;
  margin-bottom: 0.5rem;
}

.select-button {
  border-radius: 0.25rem;
  background-color: var(--vp-c-bg-soft);
  padding: 0.125rem 0.5rem;
  font-size: 0.875rem;
  line-height: 1.25rem;
  cursor: pointer;
}

.select-button:hover,
.select-button.active {
  background-color: var(--vp-c-brand-soft);
  --un-text-opacity: 1;
  color: var(--vp-c-brand-1);
}

.divider {
  background-color: rgba(60, 60, 67, 0.12);
  height: 1px;
}

.search {
  padding: 0.5rem;
  display: flex;
}

.icon {
  margin-right: 0.5rem;
}

.search-input {
  width: 100%;
  margin-top: auto;
  margin-bottom: auto;
}

.card-list {
  display: grid;
  gap: 1.5rem;
  grid-template-columns: repeat(auto-fit, minmax(18rem, 1fr));
}
</style>
