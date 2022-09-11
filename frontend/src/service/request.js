import axios from "axios";
import {message, ElLoading} from 'element-plus'
import userStore from '@/stores/user'


const store = userStore()

export default (config) => {

    const instance = axios.create({
        baseURL: import.meta.env.VITE_BASE_URL,
        timeout: 5000,
    })

    instance.interceptors.request.use(config => {
        ElLoading.service({
            title: '请求中.'
        })
        config.headers.Authorization = store.accessToken
        return config
    })

    instance.interceptors.response.use(res => {
        if (res.data.code !== 20000 ){
            message.error(res.data.msg)
        }
        ElLoading.close()
        return res.data
    }, err => {
        message.error(err)
        ElLoading.close()
        return Promise.reject(err)
    })

    return instance(config)
}