<script setup>
import { ref, onMounted, watchEffect } from 'vue'
import * as echarts from 'echarts'

const props = defineProps({
  options: {
    type: Object,
    require: true
  },
  style: {
    type: Object,
    default: () => ({
      width: '100%',
      height: '360px'
    })
  }
})

const echartRef = ref()

onMounted(() => {
  const instance = echarts.init(echartRef.value)

  // props 变化就重新设置值
  watchEffect(() => {
    instance.setOption(props.options)
  })
})
</script>

<template>
  <div class="echart">
    <div ref="echartRef" :style="style"></div>
  </div>
</template>

<style scoped></style>
