<template>
    <div class="sider-menu">
        <div class="logo"></div>
        <a-menu
            theme="dark"
            mode="inline"
            v-model:selectedKeys="store.selectKey"
        >
            <template v-for="menu in store.userMenus" :key="menu.id">
                <!-- 0 目录 顶层菜单 -->
                <template v-if="menu.type === 0">
                    <a-sub-menu :key="menu.id">
                        <template #icon>
                            <component
                                :is="$loadIconCpn(menu.icon)"
                            ></component>
                        </template>
                        <template #title>{{ menu.name }}</template>
                        <!-- 1 组件 子菜单项 -->
                        <template v-for="sub in menu.children" :key="sub.id">
                            <a-menu-item @click="menuClick(sub)">
                                <template #icon>
                                    <component
                                        :is="$loadIconCpn(sub.icon)"
                                    ></component>
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

<script setup>
import { useRouter } from 'vue-router'
import { userStore } from '@/stores/user'

const store = userStore()
const router = useRouter()

console.log('sider menu load')

// 菜单点击事件
const menuClick = (menu) => {
    router.push(menu.path)
}
</script>

<style scoped>
.logo {
    /* display: flex; */
    /* width: 100%; */
    height: 32px;
    background: rgba(255, 255, 255, 0.3) url('@/assets/img/fastapi.svg');
    margin: 16px;
    background-size: 100% 100%;
    color: white;
    font-size: 26px;
    text-align: center;
    font-weight: bold;
}
</style>
