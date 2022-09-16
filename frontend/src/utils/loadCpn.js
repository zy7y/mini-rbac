// 动态加载组件
import * as icons from '@ant-design/icons-vue'
import router from '@/router'

/**
 * 动态加载antd icon
 * @param {*} iconName
 * @returns 组件对象
 * jsx：使用 h(loadIconCpn('UserField'))
 * template: 使用 <component :is="loadIconCpn("UserField")">
 */
function loadIconCpn(iconName) {
  return icons[iconName]
}

// 拿到views下所有.vue文件
const modules = import.meta.glob('../views/**/**.vue')

function loadRouter(menus) {
  for (const menu of menus) {
    //   type 为1 菜单组件
    if (menu.type === 1 && menu.path !== '') {
      const cnpPath = `../views/main${menu.component}`

      router.addRoute('main', {
        path: menu.path,
        name: menu.name,
        // 映射取值
        component: modules[/* @vite-ignore */ cnpPath],
        meta: menu.meta
      })
    } else if (menu.children) {
      loadRouter(menu.children)
    }
  }
}

// 获取按钮权限列表，和第一个选中菜单
function getPermissions(menuArr) {
  let arr = []
  let firstMenu = null

  function _forMenu(menus) {
    for (const menu of menus) {
      if (menu.type === 1 && firstMenu === null) {
        firstMenu = menu
      }
      if (menu.type !== 2 && menu.children) {
        _forMenu(menu.children)
      } else {
        arr.push(menu.identifier)
      }
    }
  }

  _forMenu(menuArr)
  return [arr.filter((e) => e !== null), firstMenu]
}

export { loadIconCpn, loadRouter, getPermissions }
