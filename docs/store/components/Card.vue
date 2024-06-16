<script setup lang="ts">
import { onMounted, ref } from 'vue'
import type { MetaData, PyPIData } from './types'

const props = defineProps<{ item: MetaData }>()

const pypiJson = ref<PyPIData | undefined>(undefined)
const description = ref<string >()
const author = ref<string >('')
const homepage = ref<string >('')
const tags = ref<string[] >([])

const openHomepageLink = () => window.open(homepage.value)

async function copyInstallLink() {
  if ('pypi_name' in props.item)
    await navigator.clipboard.writeText(`pip install ${props.item.pypi_name}`)
}

onMounted(async () => {
  if (!('pypi_name' in props.item)) {
    description.value = props.item.description
    author.value = props.item.author
    homepage.value = props.item.homepage
    tags.value = props.item.tags.split(/[,\s]/).filter(tag => tag !== '')
    return
  }

  pypiJson.value = await (
    await fetch(`https://pypi.org/pypi/${props.item.pypi_name}/json`)
  ).json()
  if (pypiJson.value != null) {
    description.value = pypiJson.value.info.summary
    if (pypiJson.value.info.author?.length)
      author.value = pypiJson.value.info.author
    else
      author.value = pypiJson.value.info.author_email.match(/([^<>]*)<.*?>/)?.[1].trim() ?? ''
    homepage.value = pypiJson.value.info.project_urls.Repository ?? pypiJson.value.info.project_urls.Homepage ?? ''
    tags.value = pypiJson.value.info.keywords
      .split(/[,\s]/)
      .filter(tag => tag !== '') ?? []
  }
})
</script>

<template>
  <div
    class="h-full w-full flex flex-col border border-vp-bg-soft rounded-xl border-solid bg-vp-bg-soft p-6 duration-200 hover:border-vp-brand-1"
  >
    <div class="flex justify-between">
      <div class="flex items-center font-bold">
        {{ item.name }}
        <div v-if="item.is_official" class="i-mdi-check-decagram ml-1 h-5 w-5 text-vp-brand-1" />
      </div>
      <div class="i-mdi-github h-8 w-8 cursor-pointer text-vp-neutral hover:text-vp-brand-1" @click="openHomepageLink" />
    </div>
    <div class="my-1 text-sm text-vp-text-2">
      {{ description }}
    </div>
    <div v-if="tags?.length" class="mt-2 flex flex-wrap gap-2 text-sm">
      <div v-for="(tag, index) in tags" :key="index" class="rounded bg-vp-default-soft px-2 py-0.5">
        {{ tag }}
      </div>
    </div>
    <div class="mt-2 flex flex-col text-sm">
      <div class="h-6 flex items-center" title="author">
        <div class="i-mdi-account" />
        <div class="ml-2">
          {{ author }}
        </div>
      </div>
      <div v-if="'module_name' in item">
        <div class="h-6 flex items-center" title="license">
          <div class="i-mdi-scale-balance" />
          <div class="ml-2">
            {{ pypiJson?.info.license }}
          </div>
        </div>
        <div class="h-6 flex items-center" title="version">
          <div class="i-mdi-tag-multiple" />
          <div class="ml-2">
            {{ pypiJson?.info.version }}
          </div>
        </div>
        <div class="h-6 flex items-center" title="pypi">
          <div class="i-mdi-python" />
          <div class="ml-2">
            {{ item.pypi_name }}
          </div>
        </div>
        <div class="h-6 flex items-center" title="module">
          <div class="i-mdi-package-variant" />
          <div class="ml-2">
            {{ item.module_name }}
          </div>
        </div>
      </div>
      <div
        v-if="'module_name' in item"
        class="mt-2 w-full flex cursor-pointer items-center justify-center rounded-lg bg-vp-default-soft px-4 py-2 hover:fill-vp-brand-1 hover:text-vp-brand-1"
        @click="copyInstallLink"
      >
        点击复制安装命令
        <div class="i-mdi-package-down ml-1 h-5 w-5" />
      </div>
    </div>
  </div>
</template>
