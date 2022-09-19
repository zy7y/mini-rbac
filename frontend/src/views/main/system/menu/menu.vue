<script setup>
import { ref, reactive, toRefs, onMounted } from 'vue'

import { columns } from './conf'
import { delMenu, getMenus } from '@/service/menu'

import Table from '@/components/table/table.vue'
import MenuModal from './menu-modal.vue'
import { userStore } from '@/stores/user'
import { messageTip } from '@/utils'

const store = userStore()

store.$subscribe((mutation, state) => {
  if (state.isPush) {
    getPageData()
    state.isPush = false
  }
})

// 列表数据
const dataSource = ref([])

function getPageData() {
  getMenus().then((res) => (dataSource.value = res.data))
}

onMounted(() => {
  getPageData()
})

const modalRef = ref()
const modalConf = reactive({
  title: '',
  type: ''
})
// 新增
const addClick = () => {
  modalConf.title = '新增菜单'
  modalConf.type = 'create'
  modalRef.value.showModal = true
}

const putClick = (record) => {
  modalConf.title = '编辑菜单'
  modalConf.type = 'update'
  modalRef.value.openModal(record)
}

const delClick = async (record) => {
  const res = await delMenu(record.id)
  messageTip(res)
  getPageData()
}

const { title, type } = toRefs(modalConf)
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
    <MenuModal ref="modalRef" :modal-title="title" :modal-type="type"></MenuModal>
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
