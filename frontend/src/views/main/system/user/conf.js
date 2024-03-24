// 表格数据列 表头配置
export const columns = [
    {
        title: '用户ID',
        dataIndex: 'id',
        key: 'id',
    },
    {
        title: '用户名',
        dataIndex: 'username',
        key: 'username',
    },
    {
        title: '昵称',
        dataIndex: 'nickname',
        key: 'nickname',
    },
    {
        title: '状态',
        dataIndex: 'status',
        key: 'status',
    },
    {
        title: '创建时间',
        dataIndex: 'created',
        key: 'created',
    },
    // {
    //     title: '更新时间',
    //     dataIndex: 'modified',
    //     key: 'modified',
    // },
    {
        title: '限制时间',
        dataIndex: 'limit_time',
        key: 'limit_time',
    },
    {
        title: '操作',
        key: 'action',
    },
]

// 新增用户的校验配置
export const addUserRules = {
    username: [
        { required: true, message: '请输入用户名', trigger: 'blur' },
        { min: 2, max: 20, message: '2~20', trigger: 'blur' },
    ],
    password: [
        { required: true, message: '请输入密码', trigger: 'blur' },
        { min: 6, max: 12, message: '6~12', trigger: 'blur' },
    ],
    // limit_time: [{ required: true }],
    nickname: [
        { required: true, message: '请输入昵称', trigger: 'blur' },
        { min: 2, max: 20, message: '2~20', trigger: 'blur' },
    ],
    roles: [{ required: true, message: '请配置角色', trigger: 'blur' }],
}

// 编辑用户的校验配置
export const putUserRules = {
    password: [
        { required: true, message: '请输入密码', trigger: 'blur' },
        { min: 6, max: 12, message: '6~12', trigger: 'blur' },
    ],
    nickname: [
        { required: true, message: '请输入昵称', trigger: 'blur' },
        { min: 2, max: 20, message: '2~20', trigger: 'blur' },
    ],
    roles: [{ required: true, message: '请配置角色', trigger: 'blur' }],
}
