<script setup>
import Markdown from '@/components/markdown/preview.vue'
import Card from '@/components/card/card.vue'

/**https://emoji6.com/emojiall/#symbols
 *
 * https://emojixd.com/
 */
const backend = `
ð¬ ç¼ç¨è¯­è¨ï¼ [Python 3.9](https://docs.python.org/zh-cn/3.9/)
ð Webæå¡ï¼ [FastAPI](https://fastapi.tiangolo.com/) + [Uvicorn](https://www.uvicorn.org/)
ð æ°æ®åºï¼ SQLite + [Tortoise ORM](https://tortoise.github.io/)
ð± å³æ¶éä¿¡ï¼ [Websockets](https://fastapi.tiangolo.com/advanced/websockets/)
ð JWTè®¤è¯ï¼[python-jose](https://python-jose.readthedocs.io/en/latest/)
`
const info = `
ð [MiniRBAC](https://github.com/zy7y/mini-rbac)
â åç«¯èåæé
â åç«¯è·¯ç±æé
â åç«¯æé®æé
â åç«¯æ¥å£æé
`

const forntend = `
ð¬ ç¼ç¨è¯­è¨ï¼Javascript
âï¸ æ¡æ¶ï¼[Vue](https://cn.vuejs.org/)
ðµð½ è·¯ç±ï¼[Vue Router](https://router.vuejs.org/zh/)
â»ï¸ ç¼å­ï¼[Pinia](https://pinia.vuejs.org/)
ð ï¸ æå»ºå·¥å·ï¼[Vite](https://cn.vitejs.dev/)
`
</script>

<template>
  <div class="content">
    <Card title="ð¥ï¸åç«¯">
      <Markdown :text="forntend" />
    </Card>
    <Card title="ð¯æ§å¶">
      <Markdown :text="info" />
    </Card>
    <Card title="ðåç«¯">
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
