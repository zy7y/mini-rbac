import request from '@/utils/request'

// 获取角色列表, 需要考虑创建用户选择角色应该是所有未被删除的情况
export function getRoles(params) {
  return request({
    url: '/role',
    params
  })
}

// 条件查询
export function queryRole(data) {
  return request({
    url: '/role/query',
    method: 'post',
    data
  })
}

// 删除
export function delRole(id) {
  return request({
    url: `/role/${id}`,
    method: 'delete'
  })
}

// 创建
export function addRole(data) {
  return request({
    url: '/role',
    method: 'post',
    data
  })
}

// 修改
export function putRole(id, data) {
  return request({
    url: `/role/${id}`,
    method: 'put',
    data
  })
}
