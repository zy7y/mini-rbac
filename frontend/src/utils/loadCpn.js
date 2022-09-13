// 动态加载组件
import { h } from "vue";
import * as icons from "@ant-design/icons-vue";

/**
 * 动态加载antd icon
 * @param {*} iconName
 * @returns 组件对象
 * jsx：使用 h(loadIconCpn('UserField'))
 * template: 使用 <component :is="loadIconCpn("UserField")">
 */
function loadIconCpn(iconName) {
  return icons[iconName];
}

export { loadIconCpn };
