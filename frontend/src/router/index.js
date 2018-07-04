import Vue from 'vue'
import Router from 'vue-router'
import index from '@/views/index'
import list from '@/components/section/list'
import detail from '@/components/section/detail'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: index,
      children: [
        {
          path: '',
          name: 'index',
          components: {
            'section': list
          },
          meta: {
            title: '首页'
          }
        },
        {
          path: 'article/',
          name: 'detail',
          components: {
            'section': detail
          },
          meta: {
            title: 'article'
          }
        }
      ]
    }
  ]
})
