<script setup>
import { tableTree } from './conf'
import { menuType, methodColor } from '@/views/main/system/menu/conf'

/**接受父组件传递过来的值 */
defineProps({
  // 列配置
  columns: {
    type: Array,
    require: true,
    default: () => []
  },
  // 数据源
  dataSource: {
    type: Array,
    require: true,
    default: () => []
  },
  // 分页器配置 非必须
  pagination: {
    type: Object,
    default: () => ({
      // 默认不要分页器
      hideOnSinglePage: true
    })
  },
  // 页面名称小写-主要用于权限校验
  pageName: {
    type: String,
    default: 'user'
  },
  listTitle: {
    type: String
  }
})

// 子组件事件, 父组件可通过 @updateClick进行绑定
const emits = defineEmits(['createClick', 'updateClick', 'deleteClick'])

// 事件
const createEvent = () => {
  emits('createClick')
}

const updateEvent = (record) => {
  emits('updateClick', record)
}

const deleteEvent = (record) => {
  emits('deleteClick', record)
}

const expand = tableTree()
</script>

<template>
  <div class="list">
    <a-card :title="listTitle"
      ><template #extra>
        <a-button type="primary" v-per="`${pageName}:create`" @click="createEvent">
          <template #icon>
            <component :is="$loadIconCpn('PlusOutlined')"></component>
          </template>
          新增</a-button
        >
      </template>
      <a-table
        :columns="columns"
        :scroll="{ y: 'calc(100vh - 420px)' }"
        :data-source="dataSource"
        :pagination="pagination"
        :row-key="(record) => record.id"
        @expand="expand"
      >
        <template #bodyCell="{ column, record }">
          <!-- 适配菜单表格 -->
          <template v-if="column.key === 'icon'">
            <component :is="$loadIconCpn(record.icon)"></component>
          </template>
          <template v-if="column.key === 'type'">
            {{ menuType[record.type] }}
          </template>
          <template v-if="column.key === 'method'">
            <template v-if="record.method">
              <a-tag :color="methodColor[record.method]">{{ record.method }}</a-tag>
            </template>
          </template>

          <!-- 一般表格 -->
          <template v-if="column.key === 'status'">
            <a-tag :color="record.status !== 9 ? 'green' : 'red'">
              {{ record.status !== 9 ? '正常' : '删除' }}
            </a-tag>
          </template>
          <template v-else-if="column.key === 'created'">
            {{ $formatTime(record.created) }}
          </template>
          <template v-else-if="column.key === 'modified'">
            {{ $formatTime(record.modified) }}
          </template>

          <template v-else-if="column.key === 'action'">
            <span>
              <a v-per="`${pageName}:update`" @click="updateEvent(record)">编辑</a>
              <a-divider type="vertical" />
              <template v-if="record.status !== 9">
                <a v-per="`${pageName}:delete`" @click="deleteEvent(record)">删除</a>
              </template>
            </span>
          </template>
        </template>
      </a-table>
    </a-card>
  </div>
</template>

<style scoped>
.list {
  margin-top: 20px;
}
</style>
