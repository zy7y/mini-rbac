export const columns = [
  {
    title: 'ID',
    dataIndex: 'id',
    key: 'id'
  },
  {
    title: '名称',
    dataIndex: 'name',
    key: 'name'
  },
  {
    title: '描述',
    dataIndex: 'remark',
    key: 'remark'
  },
  {
    title: '状态',
    dataIndex: 'status',
    key: 'status'
  },
  {
    title: '创建时间',
    dataIndex: 'created',
    key: 'created'
  },
  {
    title: '更新时间',
    dataIndex: 'modified',
    key: 'modified'
  },
  {
    title: '操作',
    key: 'action'
  }
]

export const rules = {
  name: [
    { required: true, message: '请输入名称', trigger: 'blur' },
    { min: 3, max: 12, message: '3-12', trigger: 'blur' }
  ],
  remark: [
    { required: true, message: '请输入描述', trigger: 'blur' },
    { min: 1, max: 20, message: '1~20', trigger: 'blur' }
  ],
  menus: [{ required: true, message: '请选择菜单', trigger: 'blur' }]
}

// a-tree组件 字段替换 适配接口返回数据
export const treeFieldNames = {
  key: 'id',
  title: 'name',
  children: 'children'
}
