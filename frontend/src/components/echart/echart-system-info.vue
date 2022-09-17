<script setup>
import Echart from './echart.vue'
import { computed } from 'vue'

const props = defineProps({
  cpuValue: {
    type: String,
    require: true
  },
  memoryValue: {
    type: String,
    require: true
  },
  diskValue: {
    type: String,
    require: true
  },
  style: {
    type: Object
  }
})

const options = computed(() => {
  const gaugeData = [
    {
      value: props.cpuValue,
      name: 'CPU',
      title: {
        offsetCenter: ['-60%', '80%']
      },
      detail: {
        offsetCenter: ['-60%', '95%']
      }
    },
    {
      value: props.memoryValue,
      name: 'MEMORY',
      title: {
        offsetCenter: ['0%', '80%']
      },
      detail: {
        offsetCenter: ['0%', '95%']
      }
    },
    {
      value: props.diskValue,
      name: 'DISK',
      title: {
        offsetCenter: ['60%', '80%']
      },
      detail: {
        offsetCenter: ['60%', '95%']
      }
    }
  ]
  return {
    series: [
      {
        type: 'gauge',
        anchor: {
          show: true,
          showAbove: true,
          size: 18,
          itemStyle: {
            color: '#FAC858'
          }
        },
        pointer: {
          icon: 'path://M2.9,0.7L2.9,0.7c1.4,0,2.6,1.2,2.6,2.6v115c0,1.4-1.2,2.6-2.6,2.6l0,0c-1.4,0-2.6-1.2-2.6-2.6V3.3C0.3,1.9,1.4,0.7,2.9,0.7z',
          width: 8,
          length: '80%',
          offsetCenter: [0, '8%']
        },
        progress: {
          show: true,
          overlap: true,
          roundCap: true
        },
        axisLine: {
          roundCap: true
        },
        data: gaugeData,
        title: {
          fontSize: 14
        },
        detail: {
          width: 40,
          height: 14,
          fontSize: 14,
          color: '#fff',
          backgroundColor: 'inherit',
          borderRadius: 3,
          formatter: '{value}%'
        }
      }
    ]
  }
})
</script>

<template>
  <div class="system-info">
    <Echart :options="options" :style="style" />
  </div>
</template>

<style scoped></style>
