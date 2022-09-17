import { formatTime } from './format'
import { loadIconCpn } from './loadCpn'

export const registerFilter = (app) => {
  app.config.globalProperties.$formatTime = (value) => formatTime(value)
  app.config.globalProperties.$loadIconCpn = (value) => loadIconCpn(value)
}
