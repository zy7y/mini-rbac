<script setup>
import { ref } from "vue";
import UserInfo from "@/components/layout/layout-info/layout-info.vue";
import { MenuUnfoldOutlined, MenuFoldOutlined } from "@ant-design/icons-vue";

// 记录图标状态
const collapsed = ref(false);

const emits = defineEmits(["changeFold"]);

// 修改图标状态同时传递参数给父组件让其变更菜单收缩
const clickMenuFold = () => {
  collapsed.value = !collapsed.value;
  // 父组件需要绑定这个事件
  emits("changeFold", collapsed.value);
};
</script>

<template>
  <div class="header">
    <menu-unfold-outlined
      v-if="collapsed"
      class="trigger"
      @click="clickMenuFold"
    />
    <menu-fold-outlined v-else class="trigger" @click="clickMenuFold" />
    <UserInfo />
  </div>
</template>

<style scoped>
.trigger {
  margin-left: 16px;
  font-size: 24px;
}

.right {
  float: right;
  margin-right: 16px;
  font-size: 16px;
}
</style>
