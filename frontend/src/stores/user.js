import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { ElMessage } from 'element-plus'
import {login} from '@/service/user'

export const userStore = defineStore('user', () => {
  const uid = ref(0)
  const token = ref("")
  const accessToken = computed(() => 'Bearer ' + token.value)

  // 非setup语法时的actions
  const loginAction = async (data) => {
    const res = await login(data)
    token.value = res.data.token
    uid.value = res.data.id
    // 弹框提示登录成功
    ElMessage.success("登录成功.")
  }

  return { uid, token, accessToken, loginAction }
}, {
    persist: true, // 解决pinia刷新时数据丢失问题
  })

// export const userStore = defineStore('user',{
//     state: () => ({
//         token: ""
//     }),
//     getters: {
//         accessToken() {
//             return `Bearer ${this.token}`
//         }
//     },
//     actions: {
//       async loginAction(data){
//         const res = await login(data)
//         console.log(res)
//         this.token = res.data.token
//         // uid.value = res.data.id
//       }
//     },
//     persist: true
// })