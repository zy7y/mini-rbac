<script setup>
    import { User, Lock } from '@element-plus/icons-vue'
    import {ref,reactive} from 'vue'

    import { userStore } from '@/stores/user';

    const store = userStore()
    // 表单配置
    const rules = {
        username: [
            {required: true, message: '请输入用户名', trigger: 'blur'},
            {min:5, max:20, message: '5~20', trigger: 'blur'}
        ],
        password: [
            {required: true, message: '请输入密码', trigger: 'blur'},
            {min:6, max:12, message: '6~12', trigger: 'blur'}
        ]
    }

    // 响应式数据
    const formRef = ref()
    const formData = reactive({
        username: 'admin',
        password: '123456'
    })

    // 事件
    const submitForm = (formEl) => {
        if (!formEl) return
        formEl.validate( valid => {
            if (valid) {
                // 验证通过，执行登录逻辑
                store.loginAction(formData)
            }
        })
    }
    
</script>

<template>
  <div class="login">
    <div class="continer">
      <h1>Mini RBAC</h1>
      <el-form ref="formRef" :model="formData" :rules="rules" status-icon>
        <el-form-item prop="username">
          <el-input placeholder="用户名" clearable :prefix-icon="User"
          v-model.trim="formData.username"/>
        </el-form-item>
        <el-form-item prop="password">
          <el-input placeholder="密码" show-password :prefix-icon="Lock"
          v-model.trim="formData.password"/>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm(formRef)" >登录</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<style scoped>
.login {
  display: flex;
  background-color: #2d3a4b;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  width: 100%;
  height: 100%;
}
.continer {
  width: 300px;
  height: 300px;
}
.continer h1{
    color: #fff;
}
.continer .el-button {
  width: 100%;
}
</style>
