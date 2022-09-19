<script setup>
import { ref, reactive, watch } from 'vue'
import { rules, treeFieldNames } from './conf'
import { addRole, putRole } from '@/service/role'
import { getMenus as getRoleMenu } from '@/service/user'
import { getMenus } from '@/service/menu'
import { userStore } from '@/stores/user'

import useModal from '@/hooks/useModal'
import { messageTip } from '@/utils'

const props = defineProps({
  modalTitle: {
    // modal 右上角显示的title
    type: String
  },
  modalType: {
    // create or update
    type: String,
    default: 'create'
  }
})

const { showModal, updateId, formRef } = useModal()

const roleForm = reactive({
  name: '',
  remark: '',
  menus: []
})

// menu数据
const treeData = ref()

const treeRef = ref()

watch(showModal, async (newValue) => {
  if (newValue) {
    const res = await getMenus()
    treeData.value = res.data
  }
})

// 记录选中的子节点
const checkedKeys = ref([])
// 展开的节点
const expandedKeys = ref([])
// 选中事件
const check = (checkedKeys, e) => {
  roleForm.menus = [...e.halfCheckedKeys, ...checkedKeys]
}

// 获取当前角色 实际上传是 用的menus  和 展示在tree中的选中menus
const getCurrentMenu = (record) => {
  let allMenus = []
  let checkMenus = []
  getRoleMenu(record.id).then((res) => {
    function _mids(menus) {
      for (const menu of menus) {
        allMenus.push(menu.id)
        if (menu.children) {
          _mids(menu.children)
        } else {
          checkMenus.push(menu.id)
        }
      }
    }
    _mids(res.data)
  })
  return { allMenus, checkMenus }
}

// 编辑角色时调用
const openModal = (record) => {
  showModal.value = true
  const { allMenus, checkMenus } = getCurrentMenu(record)
  updateId.value = record.id
  roleForm.name = record.name
  roleForm.remark = record.remark
  checkedKeys.value = checkMenus
  roleForm.menus = allMenus
}

// 新增成功 和关闭modal时重置数据
const resetData = () => {
  formRef.value.resetFields()
  checkedKeys.value = []
  expandedKeys.value = []
}

const onOk = () => {
  formRef.value.validateFields().then(async () => {
    // 表单验证通过
    let res
    if (props.modalType === 'create') {
      res = await addRole(roleForm)
    } else {
      res = await putRole(updateId.value, roleForm)
    }
    messageTip(res)
    resetData()
    showModal.value = !showModal.value
    userStore().isPush = true
  })
}

const onCancel = () => {
  resetData()
}

defineExpose({ showModal, openModal })
</script>

<template>
  <div class="modal">
    <a-modal
      v-model:visible="showModal"
      :title="modalTitle"
      ok-text="确认"
      cancel-text="取消"
      @ok="onOk"
      @cancel="onCancel"
    >
      <a-form ref="formRef" :model="roleForm" :rules="rules">
        <a-form-item name="name" label="名称">
          <a-input v-model:value="roleForm.name" />
        </a-form-item>
        <a-form-item name="remark" label="描述">
          <a-input v-model:value="roleForm.remark" />
        </a-form-item>
        <a-form-item name="menus" label="菜单">
          <a-tree
            ref="treeRef"
            checkable
            :tree-data="treeData"
            :fieldNames="treeFieldNames"
            @check="check"
            v-model:checkedKeys="checkedKeys"
            v-model:expandedKeys="expandedKeys"
          >
          </a-tree>
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<style scoped></style>
