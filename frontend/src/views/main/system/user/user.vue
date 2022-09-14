<script setup>
import { getUsers } from '@/service/user'
import { columns } from './conf'
import { formatTime } from '@/utils/format'

import { ref, reactive, onMounted } from 'vue'

import { PlusOutlined, SearchOutlined } from '@ant-design/icons-vue'

// 列表数据
const dataSource = ref([])

// 页面展示数据条数变化回调
const pageSizeChange = (current, size) => {
  console.log(current, size, '展示数量变化')
}

// 页码变化回调
const pageChange = (page, pageSize) => {
  console.log(page, pageSize, '页码变化')
}

//分页
const pagination = reactive({
  current: 1, //当前页
  pageSize: 10, // 每页数量
  showSizeChanger: true,
  total: 200,
  pageSizeOptions: ['10', '50', '100'],
  showTotal: (total) => `共${total}条数据`,
  onShowSizeChange: pageSizeChange,
  onChange: pageChange
})

onMounted(() => {
  getPageData()
})

const getPageData = () => {
  getUsers().then((res) => {
    dataSource.value = res.data.items
    pagination.total = res.data.total
  })
}
</script>

<template>
  <div class="user">
    <!-- 查询 -->
    <div class="search">
      <a-form layout="inline">
        <a-form-item label="用户名">
          <a-input placeholder="用户名"> </a-input>
        </a-form-item>
        <a-form-item label="昵称">
          <a-input placeholder="昵称"> </a-input>
        </a-form-item>
        <a-form-item>
          <a-button type="primary" v-per="'user:query'">
            <template #icon> <SearchOutlined /> </template>查询</a-button
          >
        </a-form-item>
      </a-form>
    </div>

    <!-- 列表 -->
    <div class="data">
      <a-card title="用户列表"
        ><template #extra>
          <a-button type="primary" v-per="'user:create'">
            <template #icon><plus-outlined /></template>
            新增</a-button
          >
        </template>

        <!-- 数据 -->
        <a-table :columns="columns" :data-source="dataSource" :pagination="pagination">
          <template #bodyCell="{ column, record }">
            <template v-if="column.key === 'status'">
              <a-tag :color="record.status !== 9 ? 'green' : 'red'">
                {{ record.status !== 9 ? '正常' : '已删除' }}
              </a-tag>
            </template>
            <template v-else-if="column.key === 'created'">
              {{ formatTime(record.created) }}
            </template>
            <template v-else-if="column.key === 'modified'">
              {{ formatTime(record.modified) }}
            </template>
            <template v-else-if="column.key === 'action'">
              <span>
                <a v-pre="'user:update'">修改</a>
                <a-divider type="vertical" />
                <template v-if="record.status !== 9">
                  <a v-per="'user:delete'">删除</a>
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
