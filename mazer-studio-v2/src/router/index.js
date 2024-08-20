import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HomeArticleMainView from '../views/HomeArticleMainView.vue'
import MyProfileView from '../views/MyProfileView.vue'
import EditorView from '../views/EditorView.vue'
import AllArticleView from '../views/AllArticleView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/article',
      name: 'article',
      component: HomeArticleMainView
    },
    {
      path: '/profile',
      name: 'profile',
      component: MyProfileView
    },
    {
      path: '/editor',
      name: 'editor',
      component: EditorView
    },
    {
      path: '/all',
      name: 'all',
      component: AllArticleView
    }
  ]
})

export default router
