<script setup>
import { useRoute } from 'vue-router'
import { computed } from 'vue'

const route = useRoute()
const cruPath = computed(() => {
  return route.path.substring(1, route.path.length).split('/')
})
</script>

<template>
  <div class="crumb">
    <a-breadcrumb>
      <a-breadcrumb-item href="">Home</a-breadcrumb-item>
      <template v-for="path in cruPath" :key="path">
        <a-breadcrumb-item>
          {{ path }}
        </a-breadcrumb-item>
      </template>
    </a-breadcrumb>
  </div>
</template>

<style scoped>
.crumb {
  display: flex;
  align-items: center;
  margin-left: 16px;
  font-size: 10px;
}
</style>
