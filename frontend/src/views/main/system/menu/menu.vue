<script setup>
import { ref } from 'vue'
import { PlusOutlined } from '@ant-design/icons-vue'

import { columns, menuType, methodColor } from './conf'
import { loadIconCpn } from '@/utils/loadCpn'
import { getMenus } from '@/service/menu'

// 列表数据
const dataSource = ref([])

getMenus().then((res) => (dataSource.value = res.data))

// 菜单类型隐射

// 展开行 https://blog.csdn.net/weixin_52691965/article/details/120494451
const expandedRowKeys = ref([])

const zi = (expanded, record) => {
  if (expandedRowKeys.value.length > 0) {
    let index = expandedRowKeys.value.indexOf(record.id)
    if (index > -1) {
      expandedRowKeys.value.splice(index, 1)
    } else {
      expandedRowKeys.value.splice(0, expandedRowKeys.value.length)
      expandedRowKeys.value.push(record.id)
    }
  } else {
    expandedRowKeys.value.push(record.id)
  }
}

//
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
    <!-- 列表 -->
    <div class="data">
      <a-card title="菜单列表"
        ><template #extra>
          <a-button type="primary" v-per="'role:create'" @click="addClick">
            <template #icon><plus-outlined /></template>
            新增</a-button
          >
        </template>

        <!-- 数据 -->
        <a-table
          :columns="columns"
          :scroll="{ x: 1600, y: 'calc(100vh - 380px)' }"
          :data-source="dataSource"
          :pagination="{
            hideOnSinglePage: true
          }"
          :row-key="(record) => record.id"
          @expand="zi"
          :expandedRowKeys="expandRowKeys"
        >
          <template #bodyCell="{ column, record }">
            <template v-if="column.key === 'meta'">
              <component :is="loadIconCpn(record.meta?.icon)"></component>
            </template>
            <template v-if="column.key === 'type'">
              {{ menuType[record.type] }}
            </template>
            <template v-if="column.key === 'method'">
              <template v-if="record.method">
                <a-tag :color="methodColor[record.method]">{{ record.method }}</a-tag>
              </template>
            </template>
            <template v-else-if="column.key === 'created'">
              {{ $formatTime(record.created) }}
            </template>
            <template v-else-if="column.key === 'modified'">
              {{ $formatTime(record.modified) }}
            </template>
            <template v-else-if="column.key === 'action'">
              <span>
                <a v-per="'role:update'" @click="putClick(record)">编辑</a>
                <a-divider type="vertical" />
                <template v-if="record.status !== 9">
                  <a v-per="'role:delete'" @click="delClick(record)">删除</a>
                </template>
              </span>
            </template>
          </template>
        </a-table>
      </a-card>
    </div>
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
