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
