import axios from 'axios'
import { message } from 'ant-design-vue'
import { userStore } from '@/stores/user'

export default (config) => {
  const instance = axios.create({
    baseURL: import.meta.env.VITE_BASE_URL,
    timeout: 10000
  })

  instance.interceptors.request.use((config) => {
    userStore().isLoading = !userStore().isLoading
    config.headers.Authorization = userStore().accessToken
    return config
  })

  instance.interceptors.response.use(
    (res) => {
      userStore().isLoading = !userStore().isLoading
      if (res.data.code !== 200) {
        message.error(res.data.msg)
      }
      console.log(res.data)
      return res.data
    },
    (err) => {
      userStore().isLoading = !userStore().isLoading
      if (err.response.data?.msg) {
        message.error(err.response.data.msg)
      } else if (err.response.data?.detail) {
        // 请求参数缺失
        message.error(err.response.data?.detail[0].msg)
      } else {
        message.error(err.message)
      }

      return Promise.reject(err)
    }
  )

  return instance(config)
}
