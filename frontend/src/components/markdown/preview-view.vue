<script setup>
import Markdown from '@/components/markdown/preview.vue'
import Card from '@/components/card/card.vue'

/**https://emoji6.com/emojiall/#symbols
 *
 * https://emojixd.com/
 */
const backend = `
💬 编程语言： [Python 3.9](https://docs.python.org/zh-cn/3.9/)
🌐 Web服务： [FastAPI](https://fastapi.tiangolo.com/) + [Uvicorn](https://www.uvicorn.org/)
📄 数据库： SQLite + [Tortoise ORM](https://tortoise.github.io/)
📱 即时通信： [Websockets](https://fastapi.tiangolo.com/advanced/websockets/)
🔐 JWT认证：[python-jose](https://python-jose.readthedocs.io/en/latest/)
`
const info = `
🎉 [MiniRBAC](https://github.com/zy7y/mini-rbac)
✅ 前端菜单权限
✅ 前端路由权限
✅ 前端按钮权限
✅ 后端接口权限
`

const forntend = `
💬 编程语言：Javascript
⚛️ 框架：[Vue](https://cn.vuejs.org/)
🚵🏽 路由：[Vue Router](https://router.vuejs.org/zh/)
♻️ 缓存：[Pinia](https://pinia.vuejs.org/)
🛠️ 构建工具：[Vite](https://cn.vitejs.dev/)
`
</script>

<template>
  <div class="content">
    <Card title="🖥️前端">
      <Markdown :text="forntend" />
    </Card>
    <Card title="🎯控制">
      <Markdown :text="info" />
    </Card>
    <Card title="🌐后端">
      <Markdown :text="backend" />
    </Card>
  </div>
</template>

<style scoped>
.content {
  display: flex;
  justify-content: space-between;
}
</style>
