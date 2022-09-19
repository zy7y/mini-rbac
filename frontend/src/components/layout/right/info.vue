<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { userStore } from '@/stores/user'
import { GithubOutlined } from '@ant-design/icons-vue'

import SelectRole from './select-role.vue'

const store = userStore()
const router = useRouter()

const roleChangeRef = ref()

const onClick = ({ key }) => {
  if (key === '1') {
    // 点击切换角色
    roleChangeRef.value.visible = true
  } else {
    store.$reset()
    router.push('/login')
  }
}

const visitGithub = () => {
  window.open('https://github.com/zy7y/mini-rbac', '_blank')
}
</script>

<template>
  <div class="inline">
    <github-outlined @click="visitGithub" />
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
span {
  padding: 0 16px;
}
</style>
