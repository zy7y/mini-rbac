<script setup>
import { PlusOutlined } from '@ant-design/icons-vue'

import { columns } from './conf'
import { formatTime } from '@/utils/format'
import { userStore } from '@/stores/user'
import { loadIconCpn } from '@/utils/loadCpn'

// 列表数据
const dataSource = userStore().userMenus

// 菜单类型隐射

const menuType = {
  0: '目录',
  1: '菜单',
  2: '按钮'
}

const methodColor = {
  GET: '#61AFFE',
  POST: '#49CC90',
  DELETE: '#F93E3E',
  PUT: '#FCA130'
}

//
const addClick = () => {
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
        >
          <template #bodyCell="{ column, record }">
            <template v-if="column.key === 'meta'">
              <component :is="loadIconCpn(record.meta?.icon)"></component>
            </template>
            <template v-if="column.key === 'type'">
              {{ menuType[record.type] }}
            </template>
            <template v-if="column.key === 'method'">
              <a-tag :color="methodColor[record.method]">{{ record.method }}</a-tag>
            </template>
            <template v-else-if="column.key === 'created'">
              {{ formatTime(record.created) }}
            </template>
            <template v-else-if="column.key === 'modified'">
              {{ formatTime(record.modified) }}
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
