<script setup>
import useModal from '@/hooks/useModal'

const props = defineProps({
  modalTitle: {
    // modal 右上角显示的title
    type: String
  },
  modalType: {
    // create or update
    type: String,
    default: 'create'
  }
})

const { showModal, updateId, formRef } = useModal()

// 编辑
const openModal = (record) => {
  showModal.value = true

  updateId.value = record.id
}

const onOk = () => {
  //新增
  console.log(props)
}

const onCancel = () => {}

defineExpose({ openModal, showModal })
</script>

<template>
  <div class="menu-modal">
    <a-modal
      v-model:visible="showModal"
      :title="props.modalTitle"
      ok-text="确认"
      cancel-text="取消"
      @ok="onOk"
      @cancel="onCancel"
    >
      <a-form ref="formRef">
        <a-form-item>
          <a-input></a-input>
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<style scoped></style>
