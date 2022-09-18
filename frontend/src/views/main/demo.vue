<script setup>
import { ref } from 'vue'
import UserModal from './system/user/user-modal.vue'
import { getRoles } from '@/service/role'

const isShow = ref(false)
const title = ref()
const type = ref()
const roleOptions = ref([])

getRoles({ limit: 100 }).then((res) => {
  roleOptions.value = res.data.items.map((e) => ({ label: e.name, value: e.id }))
})

const add = () => {
  isShow.value = !isShow.value
  title.value = '新增用户'
}

const put = () => {
  console.log('put')
}

const ok = (formRef) => {
  formRef.value.validateFields().then(() => {})
}

const cancel = () => {
  console.log('cancel')
  isShow.value = !isShow.value
}
</script>

<template>
  <div>
    demo
    <a-button @click="add">新增</a-button>
    <a-button @click="put">更新</a-button>
    <UserModal
      :modal-title="title"
      :modal-type="type"
      :show-modal="isShow"
      :role-options="roleOptions"
      @modal-ok="ok"
      @modal-cancel="cancel"
    ></UserModal>
  </div>
</template>

<style scoped></style>
