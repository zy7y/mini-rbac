<script setup>
import { ref, reactive, onMounted } from 'vue'
import Table from '@/components/table/table.vue'

import { getRoles, queryRole, delRole, putRole, addRole } from '@/service/role'
import { getMenus } from '@/service/menu'
import { columns, rules, treeFieldNames } from './conf'
import { message } from 'ant-design-vue'
import { getMenus as getRoleMenu } from '@/service/user'
import RoleSearch from './role-search.vue'

/**查询表单响应式数据 */

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
const getPageData = (form = null) => {
  let offset = pagination.current
  let limit = pagination.pageSize
  if (!isQuery.value) {
    getRoles({ offset, limit }).then((res) => {
      dataSource.value = res.data.items
      pagination.total = res.data.total
    })
  } else {
    queryRole({ offset, limit, name: form?.name }).then((res) => {
      dataSource.value = res.data.items
      pagination.total = res.data.total
    })
  }
}

// 点击查询事件
const clickQuery = (form) => {
  isQuery.value = true
  getPageData(form)
}

// 重置搜索框
const resetQueryForm = () => {
  isQuery.value = false
  getPageData()
}

// 删除
const delClick = (record) => {
  delRole(record.id)
  getPageData()
}

/**新增角色 */
const addVisible = ref(false)
const formRef = ref(null)
const newRoleForm = reactive({
  name: '',
  remark: '',
  menus: []
})

// 记录选中的子节点
const checkedKeys = ref([])
// 展开的节点
const expandedKeys = ref([])
// 选中事件
const check = (checkedKeys, e) => {
  newRoleForm.menus = [...e.halfCheckedKeys, ...checkedKeys]
}

const addClick = () => {
  addVisible.value = !addVisible.value
  // 弹出modal 并获取菜单树
  getMenus().then((res) => (treeData.value = res.data))
}

// 新增modal 确定的回调
const onOk = () => {
  formRef.value.validateFields().then(() => {
    // 表单验证通过
    addRole(newRoleForm).then((res) => {
      if (res.msg === '请求成功') {
        message.success('新增成功')
        // 1. 关闭 modal
        addVisible.value = !addVisible.value
        // 2. 重置响应式数据
        formRef.value.resetFields()
        checkedKeys.value = []
        expandedKeys.value = []
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
  checkedKeys.value = []
  expandedKeys.value = []
}

/**更新 */

/**
 * 编辑时获取数据 回显到put modal
 * @param {} record  行数据
 */

// modal 里表达响应式数据
const putRoleForm = reactive({
  name: '',
  remark: '',
  menus: []
})

// 点击编辑弹modal事件
const putClick = (record) => {
  putVisible.value = !putVisible.value
  console.log(record, '父组件')
  getPutModalData(record)
}

const getPutModalData = (record) => {
  // 打开编辑的modal
  getMenus().then((res) => (treeData.value = res.data))
  // 通过角色获取菜单, 已有菜单
  getRoleMenu(record.id).then((res) => {
    function _mids(menus) {
      for (const menu of menus) {
        if (menu.children) {
          _mids(menu.children)
        } else {
          putRoleForm.menus.push(menu.id)
        }
      }
    }
    _mids(res.data)
  })
  putId.value = record.id
  putRoleForm.name = record.name
  putRoleForm.remark = record.remark
}

// modal 是否显示
const putVisible = ref(false)

// modal 里的 表单 对象
const putRoleFormRef = ref()

// 记录 数据的 id 方便修改
const putId = ref()

//modal 事件
const onOkPut = () => {
  //校验数据
  putRoleFormRef.value.validateFields().then(() => {
    //验证通过
    putRole(putId.value, putRoleForm).then((res) => {
      if (res.msg === '请求成功') {
        message.success('修改成功')
        // 1. 关闭 modal
        putVisible.value = !putVisible.value
        // 2. 重置响应式数据
        putRoleFormRef.value.resetFields()
        // 3. 重新拉取数据
        getPageData()
      }
    })
  })
}

const onCancelPut = () => {
  putRoleFormRef.value.resetFields()
}

// tree
const treeData = ref()
</script>

<template>
  <div class="role">
    <!-- 查询 -->

    <RoleSearch @query-click="clickQuery" @reset-click="resetQueryForm"></RoleSearch>

    <Table
      :columns="columns"
      :data-source="dataSource"
      :pagination="pagination"
      page-name="role"
      list-title="角色列表"
      @create-click="addClick"
      @update-click="putClick"
      @delete-click="delClick"
    >
    </Table>
    <!-- 新增 -->
    <a-modal
      v-model:visible="addVisible"
      title="新建角色"
      ok-text="创建"
      cancel-text="取消"
      @ok="onOk"
      @cancel="onCancel"
    >
      <a-form ref="formRef" :model="newRoleForm" :rules="rules">
        <a-form-item name="name" label="名称">
          <a-input v-model:value="newRoleForm.name" />
        </a-form-item>
        <a-form-item name="remark" label="描述">
          <a-input v-model:value="newRoleForm.remark" />
        </a-form-item>
        <a-form-item name="menus" label="菜单">
          <a-tree
            checkable
            :tree-data="treeData"
            :fieldNames="treeFieldNames"
            @check="check"
            v-model:checkedKeys="checkedKeys"
            v-model:expandedKeys="expandedKeys"
          >
          </a-tree>
        </a-form-item>
      </a-form>
    </a-modal>

    <!-- 修改 -->
    <a-modal
      v-model:visible="putVisible"
      title="编辑角色"
      ok-text="确认"
      cancel-text="取消"
      @ok="onOkPut"
      @cancel="onCancelPut"
    >
      <a-form ref="putRoleFormRef" :model="putRoleForm" :rules="rules">
        <a-form-item name="name" label="名称">
          <a-input v-model:value="putRoleForm.name" />
        </a-form-item>
        <a-form-item name="remark" label="描述">
          <a-input v-model:value="putRoleForm.remark" />
        </a-form-item>
        <a-form-item name="menus" label="菜单">
          <a-tree
            checkable
            :tree-data="treeData"
            :fieldNames="treeFieldNames"
            v-model:checkedKeys="putRoleForm.menus"
          ></a-tree>
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
