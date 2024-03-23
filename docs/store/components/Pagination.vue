<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{ total: number }>()
const model = defineModel<number>({ required: true })

function rangeList(start: number, end: number) {
  return Array.from({ length: end - start + 1 }, (_, i) => i + start)
}

const pageNumberArray = computed<(number | string)[]>(() => {
  const current = model.value
  const total = props.total
  const size = 4 // size hear must greater than 4
  if (total <= size)
    return rangeList(1, total)
  if (current < size - 2)
    return [...rangeList(1, size - 2), '...', total]
  if (current > total - size + 3)
    return [1, '...', ...rangeList(total - size + 3, total)]
  return [1, '...', ...rangeList(current - Math.floor((size - 4) / 2), current + Math.ceil((size - 4) / 2)), '...', total]
})
</script>

<template>
  <div>
    <div v-if="props.total > 1" class="my-4 w-full flex justify-center gap-x-2">
      <div
        class="h-8 w-8 flex cursor-pointer items-center justify-center rounded bg-vp-bg-soft hover:bg-vp-brand-soft hover:text-vp-brand-1"
        @click="model = Math.max(1, model - 1)"
      >
        &lt;
      </div>
      <div
        v-for="(item, index) in pageNumberArray"
        :key="index"
        class="h-8 w-8 flex cursor-pointer items-center justify-center rounded bg-vp-bg-soft hover:bg-vp-brand-soft hover:text-vp-brand-1"
        :class="item === model ? 'bg-vp-brand-soft text-vp-brand-1' : ''"
        @click=" () => { if (typeof item === 'number') model = item }"
      >
        {{ item }}
      </div>
      <div
        class="h-8 w-8 flex cursor-pointer items-center justify-center rounded bg-vp-bg-soft hover:bg-vp-brand-soft hover:text-vp-brand-1"
        @click="model = Math.min(total, model + 1)"
      >
        &gt;
      </div>
    </div>
  </div>
</template>
