<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { userStore } from '@/stores/user'

import SelectRole from './select-role.vue'

const store = userStore()
const router = useRouter()

const roleChangeRef = ref()

const onClick = ({ key }) => {
  if (key === '1') {
    // 点击切换角色
    roleChangeRef.value?.showModal()
  } else {
    store.$reset()
    router.push('/login')
  }
}
</script>

<template>
  <div>
    <a-dropdown>
      <a class="ant-dropdown-link" @click.prevent>
        {{ store.userInfo.nickname }} - {{ store.userInfo.roles[0].name }}
      </a>
      <template #overlay>
        <a-menu @click="onClick">
          <a-menu-item key="1">切换角色</a-menu-item>
          <a-menu-item key="2">退出登录</a-menu-item>
        </a-menu>
      </template>
    </a-dropdown>
    <SelectRole ref="roleChangeRef" />
  </div>
</template>

<style scoped>
div {
  font-size: 16px;
}
</style>
