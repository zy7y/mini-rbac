import request from "@/utils/request";

export function login(data) {
  return request({
    url: "/login",
    method: "post",
    data,
  });
}

// 获取用户信息
export function getUserInfo(uid) {
  return request({
    url: `/user/${uid}`,
  });
}

// 获取权限信息
export function getMenus(rid) {
  return request({
    url: `/role/${rid}/menu`,
  });
}

// 修改用户信息
export function selectRole(rid) {
  return request({
    url: `/user/role/${rid}`,
    method: "put",
  });
}

// 获取用户列表
export function getUsers() {
  return request({
    url: "/user",
  });
}
