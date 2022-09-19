<script setup>
import { ref } from 'vue'
import UserInfo from '@/components/layout/right/info.vue'
import HeaderCrumb from './header-crumb.vue'

// 记录图标状态
const collapsed = ref(false)

const emits = defineEmits(['changeFold'])

// 修改图标状态同时传递参数给父组件让其变更菜单收缩
const clickMenuFold = () => {
  collapsed.value = !collapsed.value
  // 父组件需要绑定这个事件
  emits('changeFold', collapsed.value)
}
</script>

<template>
  <div class="header">
    <!-- 左侧菜单收缩控制 -->
    <component
      class="menu-fold"
      :is="$loadIconCpn(collapsed ? 'MenuUnfoldOutlined' : 'MenuFoldOutlined')"
      @click="clickMenuFold"
    >
    </component>

    <div class="right">
      <HeaderCrumb />
      <UserInfo class="info" />
    </div>
  </div>
</template>

<style scoped>
div {
  font-size: 20px;
}
.header {
  display: flex;
  width: 100%;
  height: 100%;
  padding: 0 16px;
}
.menu-fold {
  font-size: 24px;
  line-height: 64px;
}

.right {
  display: flex;
  flex: 1;
  justify-content: space-between;
}
</style>
