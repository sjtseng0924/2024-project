import { createRouter, createWebHistory } from "vue-router";
import ChatApp from "@/components/ChatApp.vue";
import StickyNote from "@/components/sticky_note/StickyNote.vue";
import LoginWindow from "@/components/LoginWindow.vue";
import Map from "@/components/map/Map.vue";
const routes = [
  {
    path: '/',  // 根路徑
    redirect: '/chatapp'  // 重定向到 /chatapp
  },
  {
    path: '/chatapp',
    name: 'chatapp',
    component: ChatApp
  },
  {
    path: '/sticky_note',
    name: 'stickynote',
    component: StickyNote
  },
  {
    path: '/map',
    name: 'map',
    component: Map
  },
  {
    path: '/login',
    name: 'login',
    component: LoginWindow
  }
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
  });
  
  export default router;