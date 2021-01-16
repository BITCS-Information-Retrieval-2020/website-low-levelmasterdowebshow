import Vue from 'vue'
import Router from 'vue-router'
import index from '@/views/index'
import integrated_search from '@/views/integrated_search'
import advanced_search from '@/views/advanced_search'
import search_list from '@/views/search_list'
import paper_details from '@/views/paper_details'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'integrated-search',
      component: integrated_search
    },
    {
      path: '/integrated-search',
      // path: '/',
      name: 'integrated-search',
      // meta:{
      //   navShow: true
      // },
      component: integrated_search
    },
    {
      path: '/advanced-search',
      name: 'advanced-search',
      // meta:{
      //   navShow: true
      // },
      component: advanced_search
    },
    {
      path: '/seach-list',
      name: 'search-list',
      // meta:{
      //   navShow: true
      // },
      component: search_list
    },
    // {
    //   path: '/search-list',
    //   name: 'search-list',
    //   // meta:{
    //   //   navShow: true
    //   // },
    //   component: () => 
    //     import('../views/search_list.vue'),
    //   beforeEnter: (to, from, next) => {
    //     const query = to.query;
    //     next('/')
    //   }
    // },
    {
      path: '/paper-details',
      name: 'paper-details',
      // meta:{
      //   navShow: true
      // },
      component: paper_details
    }
  ]
})
