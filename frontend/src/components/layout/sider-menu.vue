<script setup>
import { useRouter } from "vue-router";
import { userStore } from "@/stores/user";
import { loadIconCpn } from "@/utils/loadCpn";

const store = userStore();
</script>

<template>
  <div class="sider-menu">
    <div class="logo"></div>
    <a-menu theme="dark" mode="inline">
      <template v-for="menu in store.userMenus" :key="menu.id">
        <!-- 0 目录 顶层菜单 -->
        <template v-if="menu.type === 0">
          <a-sub-menu :key="`${menu.id}`">
            <template #icon>
              <component :is="loadIconCpn(menu.meta.icon)"></component>
            </template>
            <template #title>{{ menu.name }}</template>
            <!-- 1 组件 子菜单项 -->
            <template v-for="sub in menu.children" :key="sub.id">
              <a-menu-item>
                <template #icon>
                  <component :is="loadIconCpn(sub.meta.icon)"></component>
                </template>
                <span>{{ sub.name }}</span>
              </a-menu-item>
            </template>
          </a-sub-menu>
        </template>
      </template>
    </a-menu>
  </div>
</template>

<style scoped>
.logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.3);
  margin: 16px;
  background-size: 100% 100%;
}
</style>
