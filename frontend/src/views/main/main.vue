<script setup>
import { ref } from 'vue'

import SiderMenu from '@/components/layout/sider-menu.vue'
import Header from '@/components/layout/header.vue'

// a-ayout-sider 折叠状态响应式数据
const collapsed = ref(false)

// header组件 折叠按钮事件 触发a-layout-sider折叠
const changeSiderFold = (subValue) => {
  collapsed.value = subValue
}
</script>

<template>
  <div class="main">
    <a-layout>
      <a-layout-sider v-model:collapsed="collapsed" :trigger="null" collapsible>
        <!-- 动态菜单 -->
        <SiderMenu />
      </a-layout-sider>
      <a-layout>
        <a-layout-header style="background: #fff; padding: 0">
          <!-- 页头 -->
          <Header @changeFold="changeSiderFold" />
        </a-layout-header>
        <a-layout-content
          class="content"
          :style="{
            margin: '24px 16px',
            background: '#F0F2F5',
            minHeight: '280px'
          }"
        >
          <router-view />
        </a-layout-content>
      </a-layout>
    </a-layout>
  </div>
</template>

<style scoped>
.main {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.ant-layout {
  width: 100%;
  height: 100%;
}

#components-layout-demo-custom-trigger .trigger {
  font-size: 18px;
  line-height: 64px;
  padding: 0 24px;
  cursor: pointer;
  transition: color 0.3s;
}

#components-layout-demo-custom-trigger .trigger:hover {
  color: #1890ff;
}

#components-layout-demo-custom-trigger .logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.3);
  margin: 16px;
}

.site-layout .site-layout-background {
  background: #fff;
}
</style>
