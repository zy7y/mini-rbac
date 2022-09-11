import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const userStore = defineStore('user', () => {
  const info = ref({})
  const token = ref("")
  const accessToken = computed(() => 'Bearer ' + token)

  return { info, token, accessToken }
}, {
    persist: true,
  })

// export const userStore = defineStore('user',{
//     state: () => ({
//         token: ""
//     }),
//     getters: {
//         accessToken() {
//             return `Bearer ${this.token}`
//         }
//     }
// })