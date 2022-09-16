<script setup>
import { onUnmounted, ref } from 'vue'

import EchartSystemInfo from '@/components/echart/echart-system-info.vue'

/** websocket */
let ws = new WebSocket('ws://localhost:8000/ws')

const wsData = ref()
ws.onmessage = (e) => {
  // 接收消息
  wsData.value = JSON.parse(e.data)
}

onUnmounted(() => {
  ws.close()
})
</script>

<template>
  <div class="about">
    <a-card class="system">
      <template #title> 资源使用率(虚拟数据) </template>
      <EchartSystemInfo
        :cpu-value="wsData?.usage.cpu"
        :disk-value="wsData?.usage.disk"
        :memory-value="wsData?.usage.memory"
        :style="{ width: '100%', height: '300px' }"
      />
    </a-card>
  </div>
</template>

<style scoped>
.about {
  width: 100%;
  height: 100%;
}
.system {
  width: 50%;
}

.header .ant-card {
  width: 40%;
}
</style>
