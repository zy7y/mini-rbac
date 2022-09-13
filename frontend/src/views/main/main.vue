<script setup>
import { ref } from "vue";
import router from "@/router";

import { userStore } from "@/stores/user";

import SiderMenu from "@/components/layout/sider-menu.vue";
const store = userStore();

const collapsed = ref(false);

const logout = () => {
  store.$reset();
  router.push("/login");
};
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
          <a-button @click="logout">退出</a-button>
        </a-layout-header>
        <!-- 面包屑 -->
        <a-layout-content
          :style="{
            margin: '24px 16px',
            background: '#F0F2F5',
            minHeight: '280px',
          }"
        >
          <router-view />
        </a-layout-content>
      </a-layout>
    </a-layout>
  </div>
</template>

<style scoped>
.main,
.ant-layout {
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
