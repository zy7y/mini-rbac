<script setup>
import { onUnmounted, reactive, toRefs } from 'vue'

import EachartView from '@/components/echart/eachart-view.vue'
import MarkdownView from '@/components/markdown/preview-view.vue'

/** websocket */
let ws = new WebSocket(import.meta.env.VITE_WS)

// 响应式数据
const data = reactive({
  systemUsage: {
    cpu: '0',
    momery: '0',
    disk: '0'
  },
  performance: {
    rps: [],
    time: [],
    user: []
  }
})

// 接收消息
ws.onmessage = (e) => {
  const wsData = JSON.parse(e.data)
  data.systemUsage = wsData.usage
  data.performance.rps.push({
    value: [Date.now(), wsData.performance.rps]
  })
  data.performance.time.push({
    value: [Date.now(), wsData.performance.time]
  })
  data.performance.user.push({
    value: [Date.now(), wsData.performance.user]
  })
}

const { systemUsage, performance } = toRefs(data)

onUnmounted(() => {
  ws.close()
})
</script>

<template>
  <div class="about">
    <EachartView :performance="performance" :system-usage="systemUsage" />
    <MarkdownView class="footer" />
  </div>
</template>

<style scoped>
.footer {
  margin: 20px 0px;
}
</style>
