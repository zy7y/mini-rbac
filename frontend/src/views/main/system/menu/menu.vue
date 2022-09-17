<script setup>
import { ref } from 'vue'

import { columns } from './conf'
import { getMenus } from '@/service/menu'

import Table from '@/components/table/table.vue'

// 列表数据
const dataSource = ref([])

getMenus().then((res) => (dataSource.value = res.data))

// 新增
const addClick = () => {
  console.log('点击')
}

//
const putClick = () => {
  console.log('点击')
}

const delClick = () => {
  console.log('点击')
}
</script>

<template>
  <div class="user">
    <Table
      :columns="columns"
      :data-source="dataSource"
      page-name="menu"
      list-title="菜单列表"
      @create-click="addClick"
      @update-click="putClick"
      @delete-click="delClick"
    >
    </Table>
  </div>
</template>

<style scoped>
.search {
  display: flex;
  /* justify-content: center; */
  align-content: center;
  margin-bottom: 16px;
  padding: 24px;
  background: #fff;
}
.data {
  margin-top: 20px;
}
</style>
