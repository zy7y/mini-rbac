export const columns = [
  {
    title: '名称',
    dataIndex: 'name',
    key: 'name',
    width: 120
  },
  {
    title: '图标',
    dataIndex: 'meta',
    key: 'meta',
    width: 60
  },
  {
    title: '路由',
    dataIndex: 'path',
    key: 'path',
    width: 120
  },
  {
    title: '类型',
    dataIndex: 'type',
    key: 'type',
    width: 80
  },
  {
    title: '组件路径',
    dataIndex: 'component',
    key: 'component',
    width: 120
  },
  {
    title: '权限标识',
    dataIndex: 'identifier',
    key: 'identifier',
    width: 120
  },
  {
    title: '请求接口',
    dataIndex: 'api',
    key: 'api',
    width: 80
  },
  {
    title: '请求方法',
    dataIndex: 'method',
    key: 'method',
    width: 80
  },
  {
    title: '创建时间',
    dataIndex: 'created',
    key: 'created',
    width: 80
  },
  {
    title: '更新时间',
    dataIndex: 'modified',
    key: 'modified',
    width: 80
  },
  {
    title: '操作',
    key: 'action',
    width: 120
  }
]

// 菜单类型映射
export const menuType = {
  0: '目录',
  1: '菜单',
  2: '按钮'
}
