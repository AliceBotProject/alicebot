<script setup lang="ts">
const props = defineProps(["pypi_name"]);
import { ref, onMounted } from "vue";
const version = ref("0.0.0");
onMounted(async () => {
  const _ = (await (await fetch("https://pypi.org/pypi/" + props.pypi_name + "/json")).json())["info"]["version"]
  !!_ && (version.value = _)
});
</script>

<template>
  <div>
    {{ version }}
  </div>
</template>
