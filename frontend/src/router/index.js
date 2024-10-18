// router/index.js

import { createRouter, createWebHistory } from "vue-router";
import ChatApp from "@/components/ChatApp.vue";
import StickyNote from "@/components/sticky_note/StickyNote.vue";
import LoginWindow from "@/components/LoginWindow.vue";
import Map from "@/components/map/Map.vue";

const routes = [
  {
    path: '/',
    redirect: '/chatapp',
  },
  {
    path: '/chatapp',
    name: 'chatapp',
    component: ChatApp,
    meta: { requiresAuth: true,
      title: '梅竹小天地 - 聊天室'
     },
  },
  {
    path: '/sticky_note',
    name: 'stickynote',
    component: StickyNote,
    meta: { requiresAuth: true,
      title: '梅竹小天地 - 留言板'
     },
  },
  {
    path: '/map',
    name: 'map',
    component: Map,
    meta: { requiresAuth: true,
      title: '梅竹小天地 - 活動與地圖'
     },
  },
  {
    path: '/login',
    name: 'login',
    component: LoginWindow,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Navigation Guard
router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('userName');
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login');
  } else if (to.path === '/login' && isAuthenticated) {
    next('/chatapp');
  } else {
    next();
  }
});

router.afterEach((to) => {
  document.title = to.meta.title || '梅竹小天地';
});

export default router;
