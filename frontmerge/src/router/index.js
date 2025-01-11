import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '@/views/HomeView.vue'

// import PageNotFoundView from '@/views/PageNotFoundView.vue'

const routes = [
  {
    path: '/',
    name: 'HomeLink',
    component: HomeView,
  },
  // {
  //   path: '/:pathMatch(.*)*',
  //   name: 'PageNotFoundLink',
  //   component: PageNotFoundView,
  // },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
})

export default router
