<script setup>
defineProps({
  title: { type: String },
  style: {
    default: () => ({
      padding: '0'
    })
  }
})
</script>

<template>
  <div class="card">
    <a-card :bodyStyle="style" :title="title">
      <slot></slot>
    </a-card>
  </div>
</template>

<style scoped>
.card {
  width: 100%;
  margin: 10px;
}
</style>
