<script setup>
import { computed } from 'vue'
import Echart from './echart.vue'

const props = defineProps({
    rps: {
        type: Object,
    },
    time: {
        type: Object,
    },
    user: {
        type: Object,
    },
})

const options = computed(() => {
    return {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                animation: false,
            },
        },
        xAxis: {
            type: 'time',
            splitLine: {
                show: false,
            },
        },
        yAxis: {
            type: 'value',
            boundaryGap: [0, '100%'],
            splitLine: {
                show: false,
            },
        },
        series: [
            {
                name: '数学',
                type: 'line',
                zlevel: 0,
                z: 2,
                showSymbol: false,
                data: props.rps,
            },
            {
                name: '英语',
                type: 'line',
                zlevel: 0,
                z: 2,
                showSymbol: false,
                data: props.time,
            },
            {
                name: '计算机',
                type: 'line',
                zlevel: 0,
                z: 2,
                showSymbol: false,
                data: props.user,
            },
        ],
    }
})
</script>

<template>
    <div class="result">
        <Echart :options="options"></Echart>
    </div>
</template>

<style scoped></style>
