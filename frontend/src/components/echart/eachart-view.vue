<script setup>
import Card from '@/components/card/card.vue'
import EchartSystemInfo from './echart-system-info.vue'
import EachartPerResult from './eachart-per-result.vue'

defineProps({
  performance: {
    type: Object
  },
  systemUsage: {
    type: Object
  }
})
</script>

<template>
  <div class="echart-data">
    <Card title="资源使用率" class="left">
      <EchartSystemInfo
        :cpu-value="systemUsage.cpu"
        :disk-value="systemUsage.disk"
        :memory-value="systemUsage.memory"
        :style="{ width: '100%', height: '300px' }"
      />
    </Card>
    <Card title="压测结果">
      <EachartPerResult
        :rps="performance.rps"
        :time="performance.time"
        :user="performance.user"
        :style="{ width: '100%', height: '300px' }"
      />
    </Card>
  </div>
</template>

<style scoped>
.echart-data {
  display: flex;
  width: 100%;
  justify-content: space-around;
}
.left {
  width: 40%;
}
</style>
