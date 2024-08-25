import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

const apiUrl =
   "https://16d6c3fe-7242-4453-af5c-b75e3719c75c-dev.e1-eu-north-azure.choreoapis.dev/djangoreact/backend/v1";

const api = axios.create({
   baseURL: import.meta.env.VITE_API_URL
      ? import.meta.env.VITE_API_URL
      : apiUrl,
});

api.interceptors.request.use(
   (config) => {
      const token = localStorage.getItem(ACCESS_TOKEN);
      if (token) {
         config.headers.Authorization = `Bearer ${token}`;
      }
      return config;
   },
   (error) => {
      return Promise.reject(error);
   }
);
export default api;
