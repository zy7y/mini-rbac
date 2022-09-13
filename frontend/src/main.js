import { createApp } from "vue";

import App from "./App.vue";
import router from "./router";
import store from "./stores";

import "normalize.css";
import "@/assets/css/base.css";

import "ant-design-vue/dist/antd.css";

const app = createApp(App);

app.use(store);
app.use(router);

app.mount("#app");
