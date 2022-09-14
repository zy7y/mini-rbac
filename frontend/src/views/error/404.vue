<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const toHome = () => {
  router.push('/')
}
</script>

<template>
  <div>
    <a-result status="404" title="404" sub-title="页面找不到~">
      <template #extra>
        <a-button type="primary" @click="toHome"> Back Home </a-button>
      </template>
    </a-result>
  </div>
</template>

<style scoped></style>
