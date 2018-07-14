import Vue from 'vue'
import Router from 'vue-router'
import index from '@/views/index'
import list from '@/components/section/list'
import detail from '@/components/section/detail'
import archive from '@/components/section/archive'

Vue.use(Router)

export default new Router({
  mode: 'history',
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
          path: 'article/:id',
          name: 'detail',
          components: {
            'section': detail
          },
          meta: {
            title: 'article'
          }
        },
        {
          path: 'category/:id',
          name: 'category',
          components: {
            'section': list
          }
        },
        {
          path: 'archive',
          name: 'archive',
          components: {
            'section': archive
          }
        }
      ]
    }
  ]
})
