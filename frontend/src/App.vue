<script setup>
import { RouterView } from 'vue-router'
import { Spin } from 'ant-design-vue'
import { userStore } from './stores/user'
</script>

<template>
  <Spin :spinning="userStore().isLoading" tip="数据请求中" size="large">
    <RouterView />
  </Spin>
</template>

<style>
.ant-spin-nested-loading,
.ant-spin-container {
  width: 100%;
  height: 100%;
}
</style>
