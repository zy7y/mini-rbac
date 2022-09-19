import { ref } from 'vue'
export default (emits, queryForm) => {
  const formRef = ref()

  const queryEvent = () => {
    emits('queryClick', queryForm)
  }

  const resetEvent = () => {
    formRef.value.resetFields()
    emits('resetClick')
  }
  return { formRef, queryEvent, resetEvent }
}
