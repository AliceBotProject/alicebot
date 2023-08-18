<script setup lang="ts">
import Version from "./Version.vue";
import { ref } from "vue";
const props = defineProps(["item"]);
const openGithub = (url: string) => {
  window.open(url);
};
const copyText = ()=> {
    let input = document.createElement('textarea');
    input.style.cssText = 'position: absolute; top: 0; left: 0; opacity: 0; z-index: -10;';
    input.value = "pip install " + props.item.pypi_name;;
    document.body.appendChild(input);
    input.select();
    document.execCommand('copy');
    document.body.removeChild(input);
  }

</script>
<template>
  <div class="card">
    <div class="card-top">
      <div class="card-head">
        <div class="card-title">
          {{ item.name
          }}<svg v-if="item.is_official" xmlns="http://www.w3.org/2000/svg" width="21" height="21" viewBox="0 0 24 24"
            style="margin-left: 0.1rem">
            <path fill="#09f"
              d="m8.6 22.5l-1.9-3.2l-3.6-.8l.35-3.7L1 12l2.45-2.8l-.35-3.7l3.6-.8l1.9-3.2L12 2.95l3.4-1.45l1.9 3.2l3.6.8l-.35 3.7L23 12l-2.45 2.8l.35 3.7l-3.6.8l-1.9 3.2l-3.4-1.45l-3.4 1.45Zm2.35-6.95L16.6 9.9l-1.4-1.45l-4.25 4.25l-2.15-2.1L7.4 12l3.55 3.55Z" />
          </svg>
        </div>
        <div class="card-github" @click="openGithub(item.homepage)" v-if="!!item.homepage">
          <svg xmlns="http://www.w3.org/2000/svg" width="21" height="21" viewBox="0 0 16 16">
            <path
              d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59c.4.07.55-.17.55-.38c0-.19-.01-.82-.01-1.49c-2.01.37-2.53-.49-2.69-.94c-.09-.23-.48-.94-.82-1.13c-.28-.15-.68-.52-.01-.53c.63-.01 1.08.58 1.23.82c.72 1.21 1.87.87 2.33.66c.07-.52.28-.87.51-1.07c-1.78-.2-3.64-.89-3.64-3.95c0-.87.31-1.59.82-2.15c-.08-.2-.36-1.02.08-2.12c0 0 .67-.21 2.2.82c.64-.18 1.32-.27 2-.27c.68 0 1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82c.44 1.1.16 1.92.08 2.12c.51.56.82 1.27.82 2.15c0 3.07-1.87 3.75-3.65 3.95c.29.25.54.73.54 1.48c0 1.07-.01 1.93-.01 2.2c0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z" />
          </svg>
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
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 256 256">
              <path fill="#6e6e6e"
                d="M230.93 220a8 8 0 0 1-6.93 4H32a8 8 0 0 1-6.92-12c15.23-26.33 38.7-45.21 66.09-54.16a72 72 0 1 1 73.66 0c27.39 8.95 50.86 27.83 66.09 54.16a8 8 0 0 1 .01 8Z" />
            </svg>
          </div>
          <div class="card-text">{{ item.author }}</div>
        </div>
        <div class="card-detail" title="pypi" v-if="!!item.pypi_name">
          <div class="card-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24">
              <g fill="none">
                <g fill="#6e6e6e" clip-path="url(#akarIconsPythonFill0)">
                  <path
                    d="M11.914 0C5.82 0 6.2 2.656 6.2 2.656l.007 2.752h5.814v.826H3.9S0 5.789 0 11.969c0 6.18 3.403 5.96 3.403 5.96h2.03v-2.867s-.109-3.42 3.35-3.42h5.766s3.24.052 3.24-3.148V3.202S18.28 0 11.913 0ZM8.708 1.85c.578 0 1.046.47 1.046 1.052c0 .581-.468 1.051-1.046 1.051c-.579 0-1.046-.47-1.046-1.051c0-.582.467-1.052 1.046-1.052Z" />
                  <path
                    d="M12.087 24c6.092 0 5.712-2.656 5.712-2.656l-.007-2.752h-5.814v-.826h8.123s3.9.445 3.9-5.735c0-6.18-3.404-5.96-3.404-5.96h-2.03v2.867s.109 3.42-3.35 3.42H9.452s-3.24-.052-3.24 3.148v5.292S5.72 24 12.087 24Zm3.206-1.85c-.579 0-1.046-.47-1.046-1.052c0-.581.467-1.051 1.046-1.051c.578 0 1.046.47 1.046 1.051c0 .582-.468 1.052-1.046 1.052Z" />
                </g>
                <defs>
                  <clipPath id="akarIconsPythonFill0">
                    <path fill="#fff" d="M0 0h24v24H0z" />
                  </clipPath>
                </defs>
              </g>
            </svg>
          </div>
          <div class="card-text">{{ item.pypi_name }}</div>
        </div>
        <div class="card-detail" title="module" v-if="!!item.module_name">
          <div class="card-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24">
              <path fill="#6e6e6e"
                d="M20 4a2 2 0 0 0-2-2h-8L4 8v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V4M9 19H7v-2h2v2m8 0h-2v-2h2v2m-8-4H7v-4h2v4m4 4h-2v-4h2v4m0-6h-2v-2h2v2m4 2h-2v-4h2v4Z" />
            </svg>
          </div>
          <div class="card-text">{{ item.module_name }}</div>
        </div>
        <div class="card-detail" title="版本" v-if="!!item.pypi_name">
          <div class="card-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24">
              <g fill="none">
                <path
                  d="M24 0v24H0V0h24ZM12.593 23.258l-.011.002l-.071.035l-.02.004l-.014-.004l-.071-.035c-.01-.004-.019-.001-.024.005l-.004.01l-.017.428l.005.02l.01.013l.104.074l.015.004l.012-.004l.104-.074l.012-.016l.004-.017l-.017-.427c-.002-.01-.009-.017-.017-.018Zm.265-.113l-.013.002l-.185.093l-.01.01l-.003.011l.018.43l.005.012l.008.007l.201.093c.012.004.023 0 .029-.008l.004-.014l-.034-.614c-.003-.012-.01-.02-.02-.022Zm-.715.002a.023.023 0 0 0-.027.006l-.006.014l-.034.614c0 .012.007.02.017.024l.015-.002l.201-.093l.01-.008l.004-.011l.017-.43l-.003-.012l-.01-.01l-.184-.092Z" />
                <path fill="#6e6e6e"
                  d="M20.245 14.75c.935.614.892 2.037-.129 2.576l-7.181 3.796a2 2 0 0 1-1.87 0l-7.181-3.796c-1.02-.54-1.064-1.962-.129-2.576l.063.04l7.247 3.832a2 2 0 0 0 1.87 0l7.181-3.796a1.59 1.59 0 0 0 .13-.076Zm0-4a1.5 1.5 0 0 1 0 2.501l-.129.075l-7.181 3.796a2 2 0 0 1-1.707.077l-.162-.077l-7.182-3.796c-1.02-.54-1.064-1.962-.129-2.576l.063.04l7.247 3.832a2 2 0 0 0 1.708.077l.162-.077l7.181-3.796a1.59 1.59 0 0 0 .13-.076Zm-7.31-7.872l7.181 3.796c1.066.563 1.066 2.09 0 2.652l-7.181 3.796a2 2 0 0 1-1.87 0L3.884 9.327c-1.066-.563-1.066-2.089 0-2.652l7.181-3.796a2 2 0 0 1 1.87 0Z" />
              </g>
            </svg>
          </div>
          <Version class="card-text" :key="item.pypi_name" :pypi_name="item.pypi_name" />
        </div>
        <div class="card-detail" title="license" v-if="!!item.license">
          <div class="card-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 36 36">
              <path fill="#6e6e6e"
                d="M19 30H4a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h28a2 2 0 0 1 2 2v10.37a8.34 8.34 0 0 0-13.49 9.79l-.93 1.14ZM7 12v1.6h17V12Zm0 5.6h11V16H7Zm0 7h10V23H7Z"
                class="clr-i-solid clr-i-solid-path-1" />
              <path fill="currentColor"
                d="M33.83 23.59a6.37 6.37 0 1 0-10.77 4.59l-1.94 2.37l.9 3.61l3.66-4.46a6.26 6.26 0 0 0 3.55 0l3.66 4.46l.9-3.61l-1.94-2.37a6.34 6.34 0 0 0 1.98-4.59Zm-10.74 0a4.37 4.37 0 1 1 4.37 4.31a4.35 4.35 0 0 1-4.36-4.31Z"
                class="clr-i-solid clr-i-solid-path-2" />
              <path fill="none" d="M0 0h36v36H0z" />
            </svg>
          </div>
          <div class="card-text">{{ item.license }}</div>
        </div>
      </div>
    </div>
    <div class="card-button" @click="copyText()">
      点击复制安装命令
      <div style="margin-left: 0.3rem">
        <svg xmlns="http://www.w3.org/2000/svg" width="21" height="21" viewBox="0 0 48 48">
          <mask id="ipSInstall0">
            <g fill="none" stroke-linejoin="round" stroke-width="4">
              <path stroke="#fff" stroke-linecap="round" d="M41.4 11.551L36.333 5H11.667l-5.083 6.551" />
              <path fill="#fff" stroke="#fff"
                d="M6 13a2 2 0 0 1 2-2h32a2 2 0 0 1 2 2v27a3 3 0 0 1-3 3H9a3 3 0 0 1-3-3V13Z" />
              <path stroke="#000" stroke-linecap="round" d="m32 27l-8 8l-8-8m7.992-8v16" />
            </g>
          </mask>
          <path fill="currentColor" d="M0 0h48v48H0z" mask="url(#ipSInstall0)" />
        </svg>
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
