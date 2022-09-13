import { createRouter, createWebHistory } from "vue-router";
import { message } from "ant-design-vue";
import { userStore } from "@/stores/user";

const routes = [
  {
    path: "/",
    redirect: "/main",
  },
  {
    path: "/login",
    meta: { title: "登录页" },
    component: () => import("@/views/login.vue"),
  },
  {
    path: "/main",
    meta: { title: "主页" },
    component: () => import("@/views/main.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
});

// 导航守卫
router.beforeEach((to) => {
  // 修改页面标题
  if (to.meta.title) {
    document.title = to.meta.title;
  }

  if (to.path !== "/login") {
    if (userStore().token) {
      return;
    }
    message.warning("请登录");
    return "/login";
  }
});

export default router;
