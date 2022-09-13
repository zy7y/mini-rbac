<script setup>
    import router from '@/router';
import { userStore } from '@/stores/user';
    const store = userStore()

    const logout = () => {
        store.$reset()
        router.push('/login')
    }
</script>

<template>
    <div class="main">
        <el-container>
      <el-aside width="200px">Aside</el-aside>
      <el-container>
        <el-header>Header <el-button @click="logout">
            注销
        </el-button></el-header>
        <el-main>Main</el-main>
        <el-footer>Footer</el-footer>
      </el-container>
    </el-container>
    </div>
</template>

<style scoped>
.main {
    height: 100%;
}
.layout-container-demo .el-header {
  position: relative;
  background-color: var(--el-color-primary-light-7);
  color: var(--el-text-color-primary);
}
.layout-container-demo .el-aside {
  color: var(--el-text-color-primary);
  background: var(--el-color-primary-light-8);
}
.layout-container-demo .el-menu {
  border-right: none;
}
.layout-container-demo .el-main {
  padding: 0;
}
.layout-container-demo .toolbar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  right: 20px;
}
</style>
