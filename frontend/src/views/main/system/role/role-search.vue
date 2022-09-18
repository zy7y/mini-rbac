<script setup>
import { ref, reactive } from 'vue'

const emits = defineEmits(['queryClick', 'resetClick'])

const formRef = ref()

const queryForm = reactive({
  name: ''
})

const queryEvent = () => {
  emits('queryClick', queryForm)
}

const resetEvent = () => {
  formRef.value.resetFields()
  emits('resetClick')
}
</script>

<template>
  <div class="search">
    <a-form ref="formRef" layout="inline" :model="queryForm">
      <a-form-item label="名称" name="name">
        <a-input placeholder="角色名称" v-model:value="queryForm.name"> </a-input>
      </a-form-item>
      <a-form-item v-per="'role:query'">
        <a-button type="primary" @click="queryEvent">查询</a-button>
        <a-button style="margin-left: 10px" @click="resetEvent">重置</a-button>
      </a-form-item>
    </a-form>
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
</style>
