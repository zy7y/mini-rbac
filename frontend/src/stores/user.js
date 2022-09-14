import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { message } from 'ant-design-vue'

import router from '@/router'
import { loadRouter, loadDefaultMenu } from '@/utils/loadCpn'
import { getMenus, getUserInfo, login, selectRole } from '@/service/user'

export const userStore = defineStore(
  'user',
  () => {
    const token = ref('')
    const userInfo = ref({})
    const userMenus = ref([])

    const selectKey = ref(null)

    const isLoading = ref(false)

    // getter
    const accessToken = computed(() => 'Bearer ' + token.value)

    // setup store 不提供$reset 需要自己重置
    // https://github.com/vuejs/pinia/issues/1056
    const $reset = () => {
      token.value = ''
      userInfo.value = {}
      userMenus.value = []
    }

    /**
     * 获取用户信息 & 菜单路由
     * @param {*} uid 用户id
     */
    const getUserData = async (uid) => {
      // 2. 获取用户信息
      const info = await getUserInfo(uid)
      userInfo.value = info.data

      // 3. 获取权限信息
      const menus = await getMenus(info.data.roles[0].id)
      userMenus.value = menus.data

      // 3.1 加载权限
      loadRouter(menus.data)

      // 3.2 默认跳转路由
      const defaultMenu = loadDefaultMenu(menus.data)

      selectKey.value = [defaultMenu.id]
      // 4. 跳转
      if (defaultMenu.path) {
        router.push(defaultMenu.path)
      } else {
        router.push('/main')
      }
    }

    const loginAction = async (data) => {
      // 1. 登录
      const res = await login(data)
      token.value = res.data.token
      await getUserData(res.data.id)
      // 弹框提示登录成功
      message.success('登录成功.')
    }

    // loadRouter 刷新问题
    const loadRoleRouter = () => {
      loadRouter(userMenus.value)
    }

    // 切换角色
    const userSelectRole = async (rid) => {
      await selectRole(rid)
      // 重新拿用户信息
      await getUserData(userInfo.value.id)
    }

    return {
      token,
      accessToken,
      userInfo,
      userMenus,
      isLoading,
      selectKey,
      $reset,
      loginAction,
      loadRoleRouter,
      userSelectRole
    }
  },
  {
    persist: true
  }
)
