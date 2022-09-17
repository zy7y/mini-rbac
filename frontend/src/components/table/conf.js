import { ref } from 'vue'

// 菜单类型映射
export const menuType = {
  0: '目录',
  1: '菜单',
  2: '按钮'
}

// 请求方法颜色映射
export const methodColor = {
  GET: '#61AFFE',
  POST: '#49CC90',
  DELETE: '#F93E3E',
  PUT: '#FCA130'
}

export const tableTree = () => {
  // 1.适配菜单表格
  // 展开行 https://blog.csdn.net/weixin_52691965/article/details/120494451
  const expandedRowKeys = ref([])
  const expand = (expanded, record) => {
    if (expandedRowKeys.value.length > 0) {
      let index = expandedRowKeys.value.indexOf(record.id)
      if (index > -1) {
        expandedRowKeys.value.splice(index, 1)
      } else {
        expandedRowKeys.value.splice(0, expandedRowKeys.value.length)
        expandedRowKeys.value.push(record.id)
      }
    } else {
      expandedRowKeys.value.push(record.id)
    }
  }
  return expand
}
