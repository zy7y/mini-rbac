import { createApp } from 'vue'

import App from './App.vue'
import router from './router'
import store from './stores'

import { userStore } from './stores/user'

import 'normalize.css'
import '@/assets/css/base.css'

import 'ant-design-vue/dist/antd.css'
import hasPermisson from '@/utils/directive'
import { formatTime } from './utils/format'

const app = createApp(App)
hasPermisson(app)
app.config.globalProperties.$formatTime = (value) => formatTime(value)
app.use(store)

userStore().loadRoleRouter()
app.use(router)

app.mount('#app')
