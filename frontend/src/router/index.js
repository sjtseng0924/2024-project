// router/index.js

import { createRouter, createWebHistory } from "vue-router";
import ChatApp from "@/components/ChatApp.vue";
import StickyNote from "@/components/sticky_note/StickyNote.vue";
import LoginWindow from "@/components/LoginWindow.vue";

const routes = [
  {
    path: '/',
    redirect: '/chatapp',
  },
  {
    path: '/chatapp',
    name: 'chatapp',
    component: ChatApp,
    meta: { requiresAuth: true },
  },
  {
    path: '/sticky_note',
    name: 'stickynote',
    component: StickyNote,
    meta: { requiresAuth: true },
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

export default router;
