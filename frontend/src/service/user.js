import request from "./request";

export function login(data) {
  return request({
    url: "/login",
    method: 'post',
    data
  });
}
