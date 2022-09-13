import axios from "axios";
import { message } from "ant-design-vue";
import { userStore } from "@/stores/user";

export default (config) => {
  const instance = axios.create({
    baseURL: import.meta.env.VITE_BASE_URL,
    timeout: 10000,
  });

  instance.interceptors.request.use((config) => {
    userStore().isLoading = !userStore().isLoading;
    config.headers.Authorization = userStore().accessToken;
    return config;
  });

  instance.interceptors.response.use(
    (res) => {
      userStore().isLoading = !userStore().isLoading;
      if (res.data.code !== 200) {
        message.error(res.data.msg);
      }

      return res.data;
    },
    (err) => {
      userStore().isLoading = !userStore().isLoading;
      message.error(err);
      return Promise.reject(err);
    }
  );

  return instance(config);
};
