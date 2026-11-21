import {createRouter, createWebHistory} from "vue-router";
import Layout from "@/layouts/Layout.vue";
import Register from "@/views/Register.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes:
    [
    {path: '/', redirect: '/manager/home'},
    {
      path: '/manager',
      name: 'Layout',
      component: () => import('@/layouts/Layout.vue'),
      children: [
        {path: 'home', name: 'home', component: () => import('@/views/HomeView.vue')},
        {path: 'Lab', name: 'Lab', component: () => import('@/views/Lab.vue')},
        {path: 'User', name: 'User', component: () => import('@/views/User.vue')},
        {path: 'device', name: 'device', component: () => import('@/views/device.vue')},
      ]
    },
    {path: '/login', name: 'Login', component: () => import('@/views/Login.vue')},
    {path:'/register', name:'register',component:() => import('@/views/Register.vue')},
  ]
})
export default router
