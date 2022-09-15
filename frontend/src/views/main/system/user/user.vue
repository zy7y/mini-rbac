<script setup>
import { ref, reactive, onMounted } from 'vue'

import { PlusOutlined } from '@ant-design/icons-vue'

import { getUsers, queryUser, delUser, addUser, getUserInfo, putUser } from '@/service/user'
import { getRoles } from '@/service/role'
import { columns, addUserRules, putUserRules } from './conf'
import { formatTime } from '@/utils/format'
import { message } from 'ant-design-vue'
import { userStore } from '@/stores/user'
import router from '@/router'

/**查询表单响应式数据 */
const queryFormRef = ref()

const queryForm = reactive({
  username: '',
  nickname: ''
})

// 是否查询
const isQuery = ref(false)

// 列表数据
const dataSource = ref([])

//分页响应式配置
const pagination = reactive({
  current: 1, //当前页
  pageSize: 5, // 每页数量
  // showSizeChanger: true,
  total: 0,
  pageSizeOptions: ['5', '10', '50'],
  showTotal: (total) => `共 ${total} 条数据`,
  onChange: (page, pageSize) => {
    pagination.current = page
    pagination.pageSize = pageSize
    getPageData()
  }
})

onMounted(() => {
  getPageData()
})

// 获取页面数据
const getPageData = () => {
  let offset = pagination.current
  let limit = pagination.pageSize
  if (!isQuery.value) {
    getUsers({ offset, limit }).then((res) => {
      dataSource.value = res.data.items
      pagination.total = res.data.total
    })
  } else {
    queryUser({ offset, limit, username: queryForm.username, nickname: queryForm.nickname }).then(
      (res) => {
        dataSource.value = res.data.items
        pagination.total = res.data.total
      }
    )
  }
}

// 点击查询事件
const clickQuery = () => {
  isQuery.value = true
  getPageData()
}

// 重置搜索框
const resetQueryForm = () => {
  queryFormRef.value.resetFields()
  isQuery.value = false
  getPageData()
}

// 删除
const delClick = (record) => {
  delUser(record.id)
  getPageData()
}

/**新增用户 */
const addVisible = ref(false)
const formRef = ref(null)
const newUserForm = reactive({
  username: '',
  nickname: '',
  password: '',
  roles: []
})
// 选择角色
const roleOptions = ref([])

const addClick = () => {
  addVisible.value = !addVisible.value
  // 请求角色信息
  getRoles({ limit: 100 }).then((res) => {
    roleOptions.value = res.data.items.map((e) => ({ label: e.name, value: e.id }))
  })
}

// 新增modal 确定的回调
const onOk = () => {
  formRef.value.validateFields().then(() => {
    // 表单验证通过
    const { username, nickname, password, roles } = newUserForm
    let rids = roles.map((e, i) => ({ rid: e, status: i === 0 ? 5 : 1 }))
    addUser({ username, nickname, password, rids }).then((res) => {
      if (res.msg === '请求成功') {
        message.success('新增成功')
        // 1. 关闭 modal
        addVisible.value = !addVisible.value
        // 2. 重置响应式数据
        formRef.value.resetFields()
        // 3. 刷新页面数据
        getPageData()
      }
    })
  })
}

// 新增modal 取消回调
const onCancel = () => {
  // 2. 重置响应式数据
  formRef.value.resetFields()
}

/**更新用户 */

const putClick = (record) => {
  // 打开编辑的modal
  putVisible.value = !putVisible.value
  // 请求所有角色信息
  getRoles({ limit: 100 }).then((res) => {
    roleOptions.value = res.data.items.map((e) => ({ label: e.name, value: e.id }))
  })
  putId.value = record.id
  // 加载当前用户id 具备的用户角色
  getUserInfo(record.id).then((res) => {
    // 角色信息
    putUserForm.roles = res.data.roles.map((e) => e.id)
    // 昵称信息
    putUserForm.nickname = res.data.nickname
    putUserForm.password = '加密之后的密码'
  })
}

const putVisible = ref(false)

const putUserFormRef = ref()
const putUserForm = reactive({
  nickname: '',
  password: '',
  roles: []
})
const putId = ref()

//modal 事件
const onOkPut = () => {
  //校验数据
  putUserFormRef.value.validateFields().then(() => {
    //验证通过
    const { nickname, password, roles } = putUserForm
    let rids = roles.map((e, i) => ({ rid: e, status: i === 0 ? 5 : 1 }))
    putUser(putId.value, { nickname, password, rids }).then((res) => {
      if (res.msg === '请求成功') {
        message.success('修改成功')
        // 1. 关闭 modal
        putVisible.value = !putVisible.value
        // 2. 重置响应式数据
        putUserFormRef.value.resetFields()
        if (putId.value === userStore().userInfo.id) {
          // 改了自己
          message.warning('修改了自己，请重新登录')
          userStore().$reset()
          router.push('/login')
        } else {
          // 3. 刷新页面数据
          getPageData()
        }
      }
    })
  })
}

const onCancelPut = () => {
  putUserFormRef.value.resetFields()
}
</script>

<template>
  <div class="user">
    <!-- 查询 -->
    <div class="search">
      <a-form ref="queryFormRef" layout="inline" :model="queryForm">
        <a-form-item label="用户名" name="username">
          <a-input placeholder="用户名" v-model:value="queryForm.username"> </a-input>
        </a-form-item>
        <a-form-item label="昵称" name="nickname">
          <a-input placeholder="昵称" v-model:value="queryForm.nickname"> </a-input>
        </a-form-item>
        <a-form-item v-per="'user:query'">
          <a-button type="primary" @click="clickQuery">查询</a-button>
          <a-button style="margin-left: 10px" @click="resetQueryForm">重置</a-button>
        </a-form-item>
      </a-form>
    </div>

    <!-- 列表 -->
    <div class="data">
      <a-card title="用户列表"
        ><template #extra>
          <a-button type="primary" v-per="'user:create'" @click="addClick">
            <template #icon><plus-outlined /></template>
            新增</a-button
          >
        </template>

        <!-- 数据 -->
        <a-table
          :columns="columns"
          :scroll="{ y: 'calc(100vh - 460px)' }"
          :data-source="dataSource"
          :pagination="pagination"
        >
          <template #bodyCell="{ column, record }">
            <template v-if="column.key === 'status'">
              <a-tag :color="record.status !== 9 ? 'green' : 'red'">
                {{ record.status !== 9 ? '正常' : '删除' }}
              </a-tag>
            </template>
            <template v-else-if="column.key === 'created'">
              {{ formatTime(record.created) }}
            </template>
            <template v-else-if="column.key === 'modified'">
              {{ formatTime(record.modified) }}
            </template>
            <template v-else-if="column.key === 'action'">
              <span>
                <a v-per="'user:update'" @click="putClick(record)">编辑</a>
                <a-divider type="vertical" />
                <template v-if="record.status !== 9">
                  <a v-per="'user:delete'" @click="delClick(record)">删除</a>
                </template>
              </span>
            </template>
          </template>
        </a-table>
      </a-card>
    </div>

    <!-- 新增 用户-->
    <a-modal
      v-model:visible="addVisible"
      title="新建用户"
      ok-text="创建"
      cancel-text="取消"
      @ok="onOk"
      @cancel="onCancel"
    >
      <a-form ref="formRef" :model="newUserForm" :rules="addUserRules">
        <a-form-item name="username" label="账号">
          <a-input v-model:value="newUserForm.username" placeholder="用于登录" />
        </a-form-item>
        <a-form-item name="nickname" label="昵称">
          <a-input v-model:value="newUserForm.nickname" />
        </a-form-item>
        <a-form-item name="password" label="密码">
          <a-input-password v-model:value="newUserForm.password" autocomplete="on" />
        </a-form-item>
        <a-form-item name="roles" label="角色">
          <a-select
            v-model:value="newUserForm.roles"
            mode="multiple"
            style="width: 100%"
            placeholder="默认激活第一个角色"
            :options="roleOptions"
          ></a-select>
        </a-form-item>
      </a-form>
    </a-modal>

    <!-- 修改用户 -->
    <a-modal
      v-model:visible="putVisible"
      title="编辑用户"
      ok-text="确认"
      cancel-text="取消"
      @ok="onOkPut"
      @cancel="onCancelPut"
    >
      <a-form ref="putUserFormRef" :model="putUserForm" :rules="putUserRules">
        <a-form-item name="nickname" label="昵称">
          <a-input v-model:value="putUserForm.nickname" />
        </a-form-item>
        <a-form-item name="password" label="密码">
          <a-input-password v-model:value="putUserForm.password" autocomplete="on" />
        </a-form-item>
        <a-form-item name="roles" label="角色">
          <a-select
            v-model:value="putUserForm.roles"
            mode="multiple"
            style="width: 100%"
            placeholder="默认激活第一个角色"
            :options="roleOptions"
          ></a-select>
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<style scoped>
.search {
  display: flex;
  /* justify-content: center; */
  align-content: center;
  margin-bottom: 16px;
  padding: 24px;
  background: #fff;
}
.data {
  margin-top: 20px;
}
</style>
