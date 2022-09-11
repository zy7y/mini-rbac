import { createApp } from 'vue'

import App from './App.vue'
import router from './router'
import store from './stores'

import 'normalize.css'
import '@/assets/base.css'
import 'element-plus/theme-chalk/el-message.css'
import 'element-plus/theme-chalk/el-loading.css'

const app = createApp(App)

app.use(store)
app.use(router)

app.mount('#app')
