<script setup>
import { ref, reactive, onMounted } from 'vue'

import Table from '@/components/table/table.vue'

import { getUsers, queryUser, delUser } from '@/service/user'

import { columns } from './conf'
import UserSearch from './user-search.vue'
import UserModal from './user-modal.vue'
import { userStore } from '@/stores/user'
import { messageTip } from '@/utils'

const store = userStore()

// 监听sotre 中的isPush 刷新页面数据
store.$subscribe((mutation, state) => {
  if (state.isPush) {
    getPageData()
    state.isPush = false
  }
})
// 是否查询
const isQuery = ref(false)

// 列表数据
const dataSource = ref([])

const modalRef = ref()

// modal 配置
const modalConf = reactive({
  title: '',
  type: ''
})

//分页响应式配置
const pagination = reactive({
  current: 1, //当前页
  pageSize: 5, // 每页数量
  // showSizeChanger: true,
  total: 0,
  pageSizeOptions: ['5', '10', '50'],
  showTotal: (total) => `共 ${total} 条数据`,
  onChange: (page, pageSize) => {
    pagination.current = page
    pagination.pageSize = pageSize
    getPageData()
  }
})

onMounted(() => {
  getPageData()
})

// 获取页面数据
const getPageData = (form = null) => {
  let offset = pagination.current
  let limit = pagination.pageSize
  if (!isQuery.value) {
    getUsers({ offset, limit }).then((res) => {
      dataSource.value = res.data.items
      pagination.total = res.data.total
    })
  } else {
    queryUser({ offset, limit, username: form?.username, nickname: form?.nickname }).then((res) => {
      dataSource.value = res.data.items
      pagination.total = res.data.total
    })
  }
}

// 点击查询事件
const clickQuery = (form) => {
  isQuery.value = true
  getPageData(form)
}

// 重置搜索框
const resetQueryForm = () => {
  isQuery.value = false
  store.isPush = true
}

// 删除
const delClick = async (record) => {
  const res = await delUser(record.id)
  messageTip(res)
  getPageData()
}

/**新增 */

const addClick = async () => {
  modalConf.title = '新增用户'
  modalConf.type = 'create'
  modalRef.value.showModal = !modalRef.value.showModal
}

/**编辑 */
const putClick = async (record) => {
  modalConf.title = '编辑用户'
  modalConf.type = 'update'
  modalRef.value.openModal(record)
}
</script>

<template>
  <div class="user">
    <!-- 查询 -->
    <UserSearch @query-click="clickQuery" @reset-click="resetQueryForm" />

    <!-- 列表数据 -->
    <Table
      :columns="columns"
      :data-source="dataSource"
      :pagination="pagination"
      page-name="user"
      list-title="用户列表"
      @create-click="addClick"
      @update-click="putClick"
      @delete-click="delClick"
    >
    </Table>

    <!-- 新增&编辑 -->
    <UserModal ref="modalRef" :modal-title="modalConf.title" :modal-type="modalConf.type" />
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
</style>
