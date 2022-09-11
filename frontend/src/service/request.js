import axios from "axios";
import { ElMessage, ElLoading } from 'element-plus'
import {userStore} from '@/stores/user'

let loading

export default (config) => {

    const instance = axios.create({
        baseURL: import.meta.env.VITE_BASE_URL,
        timeout: 10000,
    })

    instance.interceptors.request.use(config => {
        loading = ElLoading.service({
            lock: true,
            text: '请求中...',
            background: 'rabg(0,0,0,0.7)'
        })
        config.headers.Authorization = userStore().accessToken
        return config
    })

    instance.interceptors.response.use(res => {
        if (res.data.code !== 200 ){
            ElMessage.error(res.data.msg)
        }
        loading.close()
        return res.data
    }, err => {
        ElMessage.error(err)
        loading.close()
        return Promise.reject(err)
    })

    return instance(config)
}