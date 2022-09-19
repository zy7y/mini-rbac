import { createRouter, createWebHistory } from 'vue-router'
import { userStore } from '@/stores/user'

const routes = [
  {
    path: '/',
    redirect: '/main'
  },
  {
    path: '/login',
    meta: { title: '登录页' },
    component: () => import('@/views/login/login.vue')
  },
  {
    name: 'main',
    path: '/main',
    meta: { title: '主页' },
    component: () => import('@/views/main/main.vue')
  },
  {
    path: '/:pathMatch(.*)*',
    component: () => import('@/views/error/404.vue')
  },
  {
    path: '/back',
    component: () => import('@/views/error/back.vue')
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes
})

// 导航守卫
router.beforeEach((to) => {
  if (to.path !== '/login') {
    if (userStore().token) {
      return
    }
    return '/login'
  }
})

router.afterEach((next) => {
  // 修改页面标题
  document.title = next.name || 'Mini RBAC'
})

export default router
