import { userStore } from '@/stores/user'

export default (app) => {
  // 按钮权限
  app.directive('per', {
    mounted(el, binding) {
      console.log(el, binding.value)
      if (
        // 是否存在
        userStore().userInfo.permissions.indexOf(binding.value) === -1
      ) {
        // 删除元素
        el.parentNode && el.parentNode.removeChild(el)
      }
    }
  })
}
