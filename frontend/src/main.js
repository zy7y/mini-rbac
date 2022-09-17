import { createApp } from 'vue'

import App from './App.vue'
import router from './router'
import store from './stores'

import { userStore } from './stores/user'

import 'normalize.css'
import '@/assets/css/base.css'

import 'ant-design-vue/dist/antd.css'
import hasPermisson from '@/utils/directive'
import { registerFilter } from './utils'

const app = createApp(App)
// 权限校验自定义指令
hasPermisson(app)
// 注册全局filter函数
registerFilter(app)

app.use(store)

userStore().loadRoleRouter()
app.use(router)

app.mount('#app')
