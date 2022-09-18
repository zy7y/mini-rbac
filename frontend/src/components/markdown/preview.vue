<script setup>
import VMdPreview from '@kangc/v-md-editor/lib/preview'
import '@kangc/v-md-editor/lib/style/preview.css'
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js'
import '@kangc/v-md-editor/lib/theme/style/github.css'
import createEmojiPlugin from '@kangc/v-md-editor/lib/plugins/emoji/index'
import '@kangc/v-md-editor/lib/plugins/emoji/emoji.css'

// highlightjs
import hljs from 'highlight.js'

VMdPreview.use(githubTheme, {
  Hljs: hljs
})
VMdPreview.use(createEmojiPlugin())

defineProps({
  text: {
    type: String
  }
})
</script>

<template>
  <v-md-preview :text="text"></v-md-preview>
</template>

<style scoped>
:deep(.github-markdown-body) {
  padding: 5px 20px !important;
  margin: 0px !important;
}
</style>
