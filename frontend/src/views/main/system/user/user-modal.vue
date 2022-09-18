<script setup>
import { reactive, ref } from 'vue'
import { message } from 'ant-design-vue'
import { addUserRules, putUserRules } from './conf'

import { addUser, putUser } from '@/service/user'
import { userStore } from '@/stores/user'

const props = defineProps({
  modalTitle: {
    // modal 右上角显示的title
    type: String
  },
  modalType: {
    // create or update
    type: String,
    default: 'create'
  },
  roleOptions: {
    // 角色列表
    type: Array,
    default: () => []
  },
  userId: {
    // 更新才会使用
    type: Number,
    require: false
  }
})

const emits = defineEmits(['modalCancel'])

const sotre = userStore()

/** 页面数据 */
const formRef = ref()

// create form
const newUserForm = reactive({
  username: '',
  nickname: '',
  password: '',
  roles: []
})

// update form
const putUserForm = reactive({
  nickname: '',
  password: '',
  roles: []
})

const onOk = () => {
  formRef.value.validateFields().then(async () => {
    let res
    if (props.modalType === 'create') {
      newUserForm.roles = newUserForm.roles.map((e, i) => ({ rid: e, status: i === 0 ? 5 : 1 }))
      res = await addUser(newUserForm)
    } else {
      const { nickname, password, roles } = putUserForm
      let rids = roles.map((e, i) => ({ rid: e, status: i === 0 ? 5 : 1 }))
      res = await putUser(props.userId, { nickname, password, roles: rids })
    }
    formRef.value.resetFields()
    showModal.value = !showModal.value
  })
}

const onCancel = () => {
  formRef.value.resetFields()
  emits('modalCancel')
}

const showModal = ref(false)

// 添加用户
const addUserAction = () => {
  formRef.value.validateFields().then(() => {
    // 表单验证通过
    newUserForm.roles = newUserForm.roles.map((e, i) => ({ rid: e, status: i === 0 ? 5 : 1 }))
    addUser(newUserForm).then((res) => {
      if (res.msg === '请求成功') {
        message.success('新增成功')
        // 2. 重置响应式数据
        formRef.value.resetFields()
        // 1. 关闭 modal
        showModal.value = !showModal.value
      }
    })
  })
}
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
      <!-- 新建 -->
      <template v-if="modalType === 'create'">
        <a-form ref="formRef" :model="newUserForm" :rules="addUserRules">
          <a-form-item name="username" label="账号">
            <a-input v-model:value="newUserForm.username" placeholder="用于登录" />
          </a-form-item>
          <a-form-item name="nickname" label="昵称">
            <a-input v-model:value="newUserForm.nickname" />
          </a-form-item>
          <a-form-item name="password" label="密码">
            <a-input-password v-model:value="newUserForm.password" autocomplete="on" />
          </a-form-item>
          <a-form-item name="roles" label="角色">
            <a-select
              v-model:value="newUserForm.roles"
              mode="multiple"
              style="width: 100%"
              placeholder="默认激活第一个角色"
              :options="roleOptions"
            ></a-select>
          </a-form-item>
        </a-form>
      </template>

      <!-- 编辑 -->
      <template v-else>
        <a-form ref="formRef" :model="putUserForm" :rules="putUserRules">
          <a-form-item name="nickname" label="昵称">
            <a-input v-model:value="putUserForm.nickname" />
          </a-form-item>
          <a-form-item name="password" label="密码">
            <a-input-password v-model:value="putUserForm.password" autocomplete="on" />
          </a-form-item>
          <a-form-item name="roles" label="角色">
            <a-select
              v-model:value="putUserForm.roles"
              mode="multiple"
              style="width: 100%"
              placeholder="默认激活第一个角色"
              :options="roleOptions"
            ></a-select>
          </a-form-item>
        </a-form>
      </template>
    </a-modal>
  </div>
</template>

<style scoped></style>
