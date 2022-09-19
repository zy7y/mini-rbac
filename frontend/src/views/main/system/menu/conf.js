import * as icons from '@ant-design/icons-vue'
export const columns = [
  {
    title: '名称',
    dataIndex: 'name',
    key: 'name',
    width: 120
  },
  {
    title: '图标',
    dataIndex: 'icon',
    key: 'icon',
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
  2: '按钮',
  3: '数据'
}

// 请求方法颜色映射
export const methodColor = {
  GET: '#61AFFE',
  POST: '#49CC90',
  DELETE: '#F93E3E',
  PUT: '#FCA130'
}

const nullOption = {
  label: null,
  value: null
}
// 转换成select 需要的options
export const menuTypeMap = () => {
  return Object.keys(menuType).map((k) => ({ label: menuType[k], value: parseInt(k) }))
}

export const methodMap = () => {
  let arr = Object.keys(methodColor).map((k) => ({ label: k, value: k }))
  arr.unshift(nullOption)
  return arr
}

export const iconMap = () => {
  let arr = Object.keys(icons)
    .filter((k) => k.indexOf('Outlined') !== -1)
    .map((k) => ({ label: k, value: k }))
  arr.unshift(nullOption)
  return arr
}

export const rules = {
  name: [
    { required: true, message: '请输入名称', trigger: 'blur' },
    { min: 3, max: 12, message: '3-12', trigger: 'blur' }
  ],
  path: [
    { required: true, message: '请输入路由', trigger: 'blur' },
    { min: 1, max: 20, message: '1~20', trigger: 'blur' }
  ]
}
