<script setup>
import { ref, reactive, onMounted, toRefs } from 'vue'
import Table from '@/components/table/table.vue'

import { getRoles, queryRole, delRole } from '@/service/role'
import { columns } from './conf'
import RoleSearch from './role-search.vue'
import RoleModal from './role-modal.vue'

import { userStore } from '@/stores/user'
import { messageTip } from '@/utils'

const store = userStore()

store.$subscribe((mutation, state) => {
  if (state.isPush) {
    getPageData()
    state.isPush = false
  }
})

/**查询表单响应式数据 */

// 是否查询
const isQuery = ref(false)

// 列表数据
const dataSource = ref([])

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
    getRoles({ offset, limit }).then((res) => {
      dataSource.value = res.data.items
      pagination.total = res.data.total
    })
  } else {
    queryRole({ offset, limit, name: form?.name }).then((res) => {
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
  getPageData()
}

// 删除
const delClick = async (record) => {
  const res = await delRole(record.id)
  messageTip(res)
  getPageData()
}

// 新增

const modalRef = ref()
const modalConf = reactive({
  title: '',
  type: ''
})
const addClick = () => {
  // 弹出modal 并获取菜单树
  modalConf.title = '新增角色'
  modalConf.type = 'create'
  modalRef.value.showModal = true
}

const putClick = (record) => {
  modalConf.title = '编辑角色'
  modalConf.type = 'update'
  modalRef.value.openModal(record)
}

const { title, type } = toRefs(modalConf)
</script>

<template>
  <div class="role">
    <!-- 查询 -->

    <RoleSearch @query-click="clickQuery" @reset-click="resetQueryForm"></RoleSearch>

    <Table
      :columns="columns"
      :data-source="dataSource"
      :pagination="pagination"
      page-name="role"
      list-title="角色列表"
      @create-click="addClick"
      @update-click="putClick"
      @delete-click="delClick"
    >
    </Table>

    <RoleModal ref="modalRef" :modal-title="title" :modal-type="type" />
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
