import { createRouter, createWebHistory } from "vue-router";
import ChatApp from "@/components/ChatApp.vue";

const routes = [
    {
      path: '/',
      name: 'chatapp',
      component: ChatApp
    }
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
  });
  
  export default router;