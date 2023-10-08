<script setup lang="ts">
import { ref, onMounted } from "vue";
import IconVerify from "./icons/IconVerify.vue";
import IconGithub from "./icons/IconGithub.vue";
import IconAuthor from "./icons/IconAuthor.vue";
import IconPypi from "./icons/IconPypi.vue";
import IconModule from "./icons/IconModules.vue";
import IconVersion from "./icons/IconVersion.vue";
import IconLicense from "./icons/IconLicense.vue";
import IconCopy from "./icons/IconCopy.vue";
const props = defineProps(["item"]);
const version = ref("0.0.0");
const openGithub = (url: string) => {
  window.open(url);
};
const copyText = () => {
  let input = document.createElement("textarea");
  input.style.cssText =
    "position: absolute; top: 0; left: 0; opacity: 0; z-index: -10;";
  input.value = "pip install " + props.item.pypi_name;
  document.body.appendChild(input);
  input.select();
  document.execCommand("copy");
  document.body.removeChild(input);
};
onMounted(async () => {
  const _ = (
    await (
      await fetch("https://pypi.org/pypi/" + props.item.pypi_name + "/json")
    ).json()
  )["info"]["version"];
  !!_ && (version.value = _);
});
</script>
<template>
  <div class="card">
    <div class="card-top">
      <div class="card-head">
        <div class="card-title">
          {{ item.name
          }}<IconVerify v-if="item.is_official" style="margin-left: 0.1rem" />
        </div>
        <div
          class="card-github"
          @click="openGithub(item.homepage)"
          v-if="!!item.homepage"
        >
          <IconGithub />
        </div>
      </div>
      <div class="card-des">{{ item?.description }}</div>
      <div class="card-tags">
        <div class="card-tag" v-for="(tag, index_) in item.tags" :key="index_">
          {{ tag }}
        </div>
      </div>
      <div class="card-details">
        <div class="card-detail" title="作者" v-if="!!item.author">
          <div class="card-icon">
            <IconAuthor />
          </div>
          <div class="card-text">{{ item.author }}</div>
        </div>
        <div class="card-detail" title="pypi" v-if="!!item.pypi_name">
          <div class="card-icon">
            <IconPypi />
          </div>
          <div class="card-text">{{ item.pypi_name }}</div>
        </div>
        <div class="card-detail" title="module" v-if="!!item.module_name">
          <div class="card-icon">
            <IconModule />
          </div>
          <div class="card-text">{{ item.module_name }}</div>
        </div>
        <div class="card-detail" title="版本" v-if="!!item.pypi_name">
          <div class="card-icon">
            <IconVersion />
          </div>
          <div class="card-text" :key="item.pypi_name">{{ version }}</div>
        </div>
        <div class="card-detail" title="license" v-if="!!item.license">
          <div class="card-icon">
            <IconLicense />
          </div>
          <div class="card-text">{{ item.license }}</div>
        </div>
      </div>
    </div>
    <div class="card-button" @click="copyText()">
      点击复制安装命令
      <div style="margin-left: 0.3rem">
        <IconCopy />
      </div>
    </div>
  </div>
</template>
<style scoped>
.card {
  border: 1px solid var(--card-border);
  border-radius: 0.5rem;
  padding: 1.5rem;
  width: 100%;
  height: 100%;
  transition: border-color 0.25s;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  max-width: 332px;
}

.card:hover {
  border: 1px solid var(--card-hover);
}

.card-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.card-title {
  display: flex;
  font-size: large;
  font-weight: bold;
  align-items: center;
}

.card-github {
  cursor: pointer;
  fill: var(--card-icon);
}

.card-github:hover {
  fill: var(--card-hover);
}

.card-des {
  color: var(--card-des);
  opacity: 0.7;
  font-size: 0.875rem;
  line-height: 1.25rem;
  margin-top: 0.3rem;
}

.card-tags {
  display: flex;
  flex-wrap: wrap;
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.card-tag {
  margin: 0.5rem 0.5rem 0 0;
  padding: 0 0.5rem;
  background-color: var(--card-tag);
  border-radius: 0.1875rem;
}

.card-tags .card-tag:first-child {
  margin-left: 0;
}

.card-details {
  margin: 0.8rem 0 0.5rem 0;
}

.card-text {
  margin-left: 0.5rem;
  font-size: 0.95rem;
  line-height: 1.5rem;
}

.card-detail {
  display: flex;
  align-items: center;
}

.card-button {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  padding: 0.4rem 1rem;
  background-color: var(--card-button);
  border-radius: 0.5rem;
  cursor: pointer;
}

.card-button:hover {
  color: var(--card-hover);
}

.card-button:hover {
  fill: var(--card-hover);
}
</style>
