<script setup lang="ts">
import { ref, computed, onMounted } from "vue";
import IconSearch from "./icons/IconSearch.vue";
import Pagination from "./Pagination.vue";
import Card from "./Card.vue";
interface dataSchema {
  module_name: string; //导入时的模块名称
  pypi_name: string; // 在 PyPi 上的名称
  name: string; //插件名称
  description: string; //描述
  author: string; //作者
  license?: string; //Optional[str] 开源许可
  homepage?: string; //Github 链接，应该是 http 地址而非 ssh 地址
  tags: string[]; //list[str] Tag 列表
  is_official: boolean; // 是否为官方维护的插件
}
const URL = "https://store.alicebot.dev/";
const type = ref("plugins");
const initData = ref();
const searchText = ref("");
const searchedData = computed(() => {
  let _ = initData.value;
  if (!_) return [];
  if (!!searchText.value) {
    _ = _.filter(
      (item: { name: string | string[] }) =>
        item.name.indexOf(searchText.value) > -1
    );
  }
  _ = _.sort((a: { time: string }, b: { time: string }) => {
    return new Date(b.time).getTime() - new Date(a.time).getTime();
  });
  return _;
});
const onPagedData = computed(() => {
  if (searchedData.value.length === 0) return [];
  return searchedData.value.slice(
    (pageNum.value - 1) * pageSize,
    pageNum.value * pageSize
  );
});
const pageSize = 10; // 每页显示的数量
const pageNum = ref(1); // 当前页码
const pageTotal = computed(() => {
  // 总页数
  pageNum.value = 1;
  return Math.ceil(searchedData.value.length / pageSize);
});
const setType = async (type_: string) => {
  type.value = type_;
  const _: dataSchema = (
    await (await fetch(URL + type.value + ".json")).json()
  )[type.value];
  initData.value = _;
  searchText.value = "";
};

onMounted(async () => {
  const _: dataSchema = (
    await (await fetch(URL + type.value + ".json")).json()
  )[type.value];
  initData.value = _;
});
</script>

<template>
  <div>
    <div class="tab">
      <div opacity="80" text="sm">类型</div>
      <div class="select-list">
        <button
          class="select-button"
          @click="setType('plugins')"
          :class="{ active: type == 'plugins' }"
        >
          插件
        </button>
        <button
          class="select-button"
          @click="setType('adapters')"
          :class="{ active: type == 'adapters' }"
        >
          适配器
        </button>
        <button
          class="select-button"
          @click="setType('bots')"
          :class="{ active: type == 'bots' }"
        >
          机器人
        </button>
      </div>
    </div>
    <div class="search-bar">
      <div class="divider" style="margin-top: 1rem" />
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
      <div class="divider" style="margin-bottom: 1rem" />
    </div>
    <Pagination
      :pageTotal="pageTotal"
      v-model="pageNum"
      style="width: 100%"
      key="topPagination"
    />
    <div class="card-list">
      <Card
        v-for="(item, index) in onPagedData"
        :key="index"
        :item="item"
      ></Card>
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
  background-color: var(--button-background);
  padding: 0.125rem 0.5rem;
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.select-button:hover {
  cursor: pointer;
  background-color: var(--button-background-hover);
}

.select-button.active {
  background-color: var(--button-background-active);
  --un-text-opacity: 1;
  color: var(--button-color-active);
}

.divider {
  background-color: var(--divider);
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
