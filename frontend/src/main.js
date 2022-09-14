import { createApp } from "vue";

import App from "./App.vue";
import router from "./router";
import store from "./stores";

import { userStore } from "./stores/user";

import "normalize.css";
import "@/assets/css/base.css";

import "ant-design-vue/dist/antd.css";
import hasPermisson from "@/utils/directive";

const app = createApp(App);
hasPermisson(app);
app.use(store);

userStore().loadRoleRouter();
app.use(router);

app.mount("#app");
