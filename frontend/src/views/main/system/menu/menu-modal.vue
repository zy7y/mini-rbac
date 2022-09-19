<script setup>
import { reactive, watch, toRefs } from 'vue'
import useModal from '@/hooks/useModal'
import { menuTypeMap, methodMap, iconMap, rules } from './conf'
import { getMenus, addMenu, putMenu } from '@/service/menu'
import { userStore } from '@/stores/user'
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

// 响应式数据
const data = reactive({
  // 表单响应式数据
  menuForm: {
    name: '',
    icon: null,
    path: null,
    type: 0,
    component: null,
    pid: 0,
    identifier: null,
    api: null,
    method: null
  },
  // 上层菜单列表
  menusOptions: []
})

//菜单筛选
const filterTreeNode = (inputValue, treeNode) => {
  return treeNode.name.toLowerCase().indexOf(inputValue.toLowerCase()) >= 0
}

// 图标筛选
const filterOption = (input, option) => {
  if (option.value) {
    return option.value.toLowerCase().indexOf(input.toLowerCase()) >= 0
  }
}
watch(showModal, async (newValue) => {
  if (newValue) {
    const res = await getMenus()
    data.menusOptions = res.data
    data.menusOptions.unshift({
      id: 0,
      name: '顶层菜单'
    })
  }
})

// 编辑
const openModal = (record) => {
  showModal.value = true
  updateId.value = record.id
  data.menuForm = record
}

const onOk = () => {
  //新增
  formRef.value.validateFields().then(async () => {
    let res
    if (props.modalType === 'create') {
      res = await addMenu(data.menuForm)
    } else {
      res = await putMenu(updateId.value, data.menuForm)
    }
    messageTip(res)
    formRef.value.resetFields()
    showModal.value = !showModal.value
    userStore().isPush = true
  })
}

const onCancel = () => {
  formRef.value.resetFields()
}

const { menuForm, menusOptions } = toRefs(data)

defineExpose({ openModal, showModal })
</script>

<template>
  <div class="menu-modal">
    <a-modal
      v-model:visible="showModal"
      :title="props.modalTitle"
      ok-text="确认"
      cancel-text="取消"
      @ok="onOk"
      @cancel="onCancel"
    >
      <a-form ref="formRef" :model="menuForm" class="form" :rules="rules">
        <a-form-item name="pid" label="上级菜单" class="item">
          <a-tree-select
            v-model:value="menuForm.pid"
            show-search
            style="width: 100%"
            :dropdown-style="{ maxHeight: '400px', overflow: 'auto' }"
            allow-clear
            :tree-data="menusOptions"
            :field-names="{
              children: 'children',
              label: 'name',
              value: 'id'
            }"
            :filterTreeNode="filterTreeNode"
          ></a-tree-select>
        </a-form-item>
        <a-form-item name="name" label="名称">
          <a-input v-model:value="menuForm.name" />
        </a-form-item>
        <a-form-item name="icon" label="图标">
          <a-select
            v-model:value="menuForm.icon"
            style="width: 100%"
            show-search
            :filterOption="filterOption"
          >
            <template v-for="option in iconMap()" :key="option.value">
              <a-select-option :value="option.value">
                <component :is="$loadIconCpn(option.label)"></component>
                {{ option.label }}
              </a-select-option>
            </template>
          </a-select>
        </a-form-item>
        <a-form-item name="path" label="路由">
          <a-input v-model:value="menuForm.path" />
        </a-form-item>
        <a-form-item name="type" label="类型">
          <a-select
            v-model:value="menuForm.type"
            style="width: 100%"
            :options="menuTypeMap()"
          ></a-select>
        </a-form-item>
        <a-form-item name="component" label="组件">
          <a-input v-model:value="menuForm.component" placeholder="views/main" />
        </a-form-item>
        <a-form-item name="identifier" label="权限">
          <a-input v-model:value="menuForm.identifier" />
        </a-form-item>
        <a-form-item name="api" label="接口">
          <a-input v-model:value="menuForm.api" />
        </a-form-item>
        <a-form-item name="method" label="方法">
          <a-select
            v-model:value="menuForm.method"
            style="width: 100%"
            :options="methodMap()"
          ></a-select>
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<style scoped>
.ant-form {
  display: flex;
  justify-content: space-between; /* 横向中间自动空间 */
  align-content: space-between; /* 竖向中间自动空间 */
  flex-wrap: wrap; /* 换行 */
}
.ant-form-item:nth-child(0) {
  width: 100%;
}

.ant-form-item {
  width: 48%;
}
.item {
  width: 100%;
}
</style>
