<script setup>
import { reactive, ref, watch } from 'vue'
import { addUserRules, putUserRules } from './conf'

import { addUser, putUser, getUserInfo } from '@/service/user'
import { userStore } from '@/stores/user'
import { getRoles } from '@/service/role'
import useModal from '@/hooks/useModal'
import { messageTip } from '@/utils'
import { message } from 'ant-design-vue'

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

const store = userStore()

const { showModal, updateId, formRef } = useModal()

/** 页面数据 */

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

// 监听modal状态是否为打开 打开就请求数据
const roleOptions = ref([])
watch(showModal, async () => {
  if (showModal.value) {
    const res = await getRoles({ limit: 100 })
    roleOptions.value = res.data.items.map((e) => ({ label: e.name, value: e.id }))
  }
})

// 打开modal时的处理 - 更新
const openModal = async (record) => {
  // 打开编辑的modal
  showModal.value = !showModal.value
  updateId.value = record.id
  // 加载当前用户id 具备的用户角色
  const res = await getUserInfo(record.id)
  putUserForm.roles = res.data.roles.map((e) => e.id)
  // 昵称信息
  putUserForm.nickname = res.data.nickname
  putUserForm.password = '加密之后的密码'
}

// 点击modal 确定
const onOk = () => {
  formRef.value.validateFields().then(async () => {
    let res
    let flag = false
    if (props.modalType === 'create') {
      newUserForm.roles = newUserForm.roles.map((e, i) => ({ rid: e, status: i === 0 ? 5 : 1 }))
      res = await addUser(newUserForm)
    } else {
      const { nickname, password, roles } = putUserForm
      let rids = roles.map((e, i) => ({ rid: e, status: i === 0 ? 5 : 1 }))
      res = await putUser(updateId.value, {
        nickname,
        password,
        roles: rids
      })
      if (updateId.value === store.userInfo.id) {
        message.warning('修改登录用户信息，重新登录生效.')
        flag = true
      }
    }
    if (!flag) {
      messageTip(res)
    }

    formRef.value.resetFields()
    showModal.value = !showModal.value
    store.isPush = true
  })
}

// 点击modal 取消
const onCancel = () => {
  formRef.value.resetFields()
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
