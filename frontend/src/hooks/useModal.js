import { ref } from 'vue'
export default () => {
  // 控制modal显示
  const showModal = ref(false)
  // 编辑数据时需要的 数据id
  const updateId = ref()
  // 表单ref对象
  const formRef = ref()
  return { showModal, updateId, formRef }
}
