import { message } from 'ant-design-vue'

import { formatTime } from './format'
import { loadIconCpn } from './loadCpn'

export const registerFilter = (app) => {
  app.config.globalProperties.$formatTime = (value) => formatTime(value)
  app.config.globalProperties.$loadIconCpn = (value) => loadIconCpn(value)
}

// 响应msg
export const messageTip = (res) => {
  if (res.code === 200) {
    message.success(res.msg)
  }
}
