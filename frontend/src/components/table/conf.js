import { ref } from 'vue'

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
