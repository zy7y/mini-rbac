<script setup>
import { useRouter } from "vue-router";
import { userStore } from "@/stores/user";
import { loadIconCpn } from "@/utils/loadCpn";
import { ref } from "vue";

const store = userStore();
const router = useRouter();

// 菜单点击事件
const menuClick = (menu) => {
  router.push(menu.path);
};
</script>

<template>
  <div class="sider-menu">
    <div class="logo">
      <img src="@/assets/img/fastapi.svg" />
      <h1>Mini RBAC</h1>
    </div>
    <a-menu theme="dark" mode="inline" v-model:selectedKeys="store.selectKey">
      <template v-for="menu in store.userMenus" :key="menu.id">
        <!-- 0 目录 顶层菜单 -->
        <template v-if="menu.type === 0">
          <a-sub-menu :key="menu.id">
            <template #icon>
              <component :is="loadIconCpn(menu.meta.icon)"></component>
            </template>
            <template #title>{{ menu.name }}</template>
            <!-- 1 组件 子菜单项 -->
            <template v-for="sub in menu.children" :key="sub.id">
              <a-menu-item @click="menuClick(sub)">
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
  position: relative;
  display: flex;
  align-items: center;
  padding: 16px 16px;
  line-height: 32px;
  cursor: pointer;
}

.logo img {
  display: inline-block;
  height: 32px;
  vertical-align: middle;
  transition: height 0.2s;
}

.logo h1 {
  margin: 0 0 0 12px;
  overflow: hidden;
  color: #fff;
  font-weight: 600;
  font-size: 18px;
  line-height: 32px;
}
</style>
