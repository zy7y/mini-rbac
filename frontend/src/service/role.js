import request from '@/utils/request'

// 获取角色列表, 需要考虑创建用户选择角色应该是所有未被删除的情况
export function getRoles(parms) {
  return request({
    url: '/role',
    parms
  })
}
