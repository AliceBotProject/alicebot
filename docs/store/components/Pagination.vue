<script setup lang="ts">
import { computed } from "vue";

const props = defineProps<{ modelValue: number; pageTotal: number }>();
const emit = defineEmits<{
  "update:modelValue": [v: number];
}>();

const onPrev = () => {
  if (props.modelValue <= 1) return;
  emit("update:modelValue", props.modelValue - 1);
};
const onNext = () => {
  if (props.modelValue >= props.pageTotal) return;
  emit("update:modelValue", props.modelValue + 1);
};
const setPageNum = (pageNum: number | string) => {
  if (typeof pageNum !== "number") return;
  if (pageNum < 1) return;
  if (pageNum > props.pageTotal) return;
  emit("update:modelValue", pageNum);
};

const genPageArray = (current: number, total: number, size: number) => {
  let arr: (string | number)[] = [];
  if (total < size + 2) {
    arr = Array.from({ length: total }, (_, k) => k + 1);
  } else if (current < size - 2) {
    arr = Array.from(
      (function* gen(i, l) {
        while (i < l) yield i++;
      })(1, size - 2 + 1)
    );
    arr.push("...");
    arr.push(total);
  } else if (total - current < size - 2) {
    arr.push(1);
    arr.push("...");
    arr = arr.concat(
      Array.from(
        (function* gen(i, l) {
          while (i < l) yield i++;
        })(total - size + 2, total + 1)
      )
    );
  } else {
    arr.push(1);
    arr.push("...");
    arr = arr.concat(
      Array.from(
        (function* gen(i, l) {
          while (i < l) yield i++;
        })(
          current - Math.floor((size - 4) / 2),
          current - Math.floor((size - 4) / 2) + size - 4 + 1
        )
      )
    );
    arr.push("...");
    arr.push(total);
  }
  return arr;
};

const pageArrayLg = computed<(number | string)[]>(() => {
  const current = props.modelValue;
  const total = props.pageTotal;
  return genPageArray(current, total, 17);
});
const pageArrayMd = computed<(number | string)[]>(() => {
  const current = props.modelValue;
  const total = props.pageTotal;
  return genPageArray(current, total, 10);
});
const pageArraySm = computed<(number | string)[]>(() => {
  const current = props.modelValue;
  const total = props.pageTotal;
  return genPageArray(current, total, 6);
});
</script>

<template>
  <div>
    <div class="container" v-if="props.pageTotal > 1">
      <div class="paper-item" @click="onPrev" style="display: flex">&lt;</div>
      <div
        v-for="(item, index) in pageArrayLg"
        :key="index"
        @click="setPageNum(item)"
        class="paper-item paper-lg"
        :class="{ active: item == props.modelValue }"
      >
        {{ item }}
      </div>
      <div
        v-for="(item, index) in pageArrayMd"
        :key="index"
        @click="setPageNum(item)"
        class="paper-item paper-md"
        :class="{ active: item == props.modelValue }"
      >
        {{ item }}
      </div>
      <div
        v-for="(item, index) in pageArraySm"
        :key="index"
        @click="setPageNum(item)"
        class="paper-item paper-sm"
        :class="{ active: item == props.modelValue }"
      >
        {{ item }}
      </div>
      <div class="paper-item" @click="onNext" style="display: flex">></div>
    </div>
  </div>
</template>

<style scoped>
.container {
  margin: 1rem 0;
  width: 100%;
  display: flex;
  justify-content: center;
}

@media screen and (min-width: 780px) {
  .paper-lg,
  .paper-sm {
    display: none;
  }

  .paper-md {
    display: flex;
  }
}

@media screen and (min-width: 1024px) {
  .paper-md,
  .paper-sm {
    display: none;
  }

  .paper-lg {
    display: flex;
  }
}

@media screen and (max-width: 780px) {
  .paper-lg,
  .paper-md {
    display: none;
  }

  .paper-sm {
    display: flex;
  }
}

.paper-item {
  height: 2rem;
  width: 2rem;
  margin: 0 0.5rem;
  padding: 0rem 0.25rem;
  align-items: center;
  justify-content: center;
  background-color: var(--vp-c-bg-soft);
  border-radius: 0.25rem;
  cursor: pointer;
}

.paper-item:hover,
.paper-item.active {
  background-color: var(--vp-c-brand-soft);
  --un-text-opacity: 1;
  color: var(--vp-c-brand-1);
}
</style>
