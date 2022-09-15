import request from '@/utils/request'

// 获取角色列表, 需要考虑创建用户选择角色应该是所有未被删除的情况
export function getMenus(params) {
  return request({
    url: '/menu',
    params
  })
}

// 条件查询
export function queryMenu(data) {
  return request({
    url: '/menu/query',
    method: 'post',
    data
  })
}

// 删除
export function delMenu(id) {
  return request({
    url: `/menu/${id}`,
    method: 'delete'
  })
}

// 创建
export function addMenu(data) {
  return request({
    url: '/menu',
    method: 'post',
    data
  })
}

// 修改
export function putMenu(id, data) {
  return request({
    url: `/menu/${id}`,
    method: 'put',
    data
  })
}
