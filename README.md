# Mini RBAC
仅保留核心权限控制的极简后台管理系统。
## 进度
## 权限控制
- [x] 前端菜单权限控制
- [x] 前端路由权限控制
- [x] 前端按钮权限控制
- [x] 后端接口权限控制

## 功能导向
- [x] 登录、退出
- [ ] 用户管理
- [ ] 角色管理
- [ ] 菜单管理
# 技术实现
## 前端 `node 16.15 LTS`
```json
{
    "ant-design-vue": "^3.2.12",
    "axios": "^0.27.2",
    "moment": "^2.29.4",
    "pinia": "^2.0.21",
    "pinia-plugin-persistedstate": "^2.2.0",
    "vue": "^3.2.38",
    "vue-router": "^4.1.5",
    "vite": "^3.0.9"
}
```
## 后端 `Python 3.9.7`
```
bcrypt==4.0.0
fastapi==0.82.0
passlib==1.7.4
python-jose==3.3.0
tomli==2.0.1
tortoise-orm==0.19.2
uvicorn==0.18.3
```
