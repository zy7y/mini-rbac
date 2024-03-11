<script setup>
import { ref, computed } from 'vue'
import { userStore } from '@/stores/user'
import { useRouter } from 'vue-router'

const store = userStore()
const router = useRouter()

const visible = ref(false)

const currentRoleId = ref(store.userInfo.roles[0].id)

// 角色列表选项
const options = computed(() => {
  return store.userInfo.roles.map((role) => ({
    label: role.name,
    value: role.id
  }))
})

const handleOk = () => {
  visible.value = !visible.value
  store.userSelectRole(currentRoleId.value)
  // 刷新组件 todo
  router.replace({
    path: '/back'
  })
  visible.value = !visible.value
}
const handleCancel = () => {
  visible.value = !visible.value
}

defineExpose({
  visible
})
</script>

<template>
  <div class="select-role">
    <a-modal v-model:visible="visible" title="切换角色">
      <template #footer>
        <a-button key="back" @click="handleCancel">取消</a-button>
        <a-button
          key="submit"
          type="primary"
          @click="handleOk"
          :disabled="currentRoleId === store.userInfo.roles[0]['id']"
          >确定</a-button
        >
      </template>
      <span>选择角色：</span>

      <a-space direction="vertical">
        <a-select
          v-model:value="currentRoleId"
          size="default"
          style="width: 400px"
          :options="options"
        ></a-select>
      </a-space>
    </a-modal>
  </div>
</template>

<style scoped></style>
