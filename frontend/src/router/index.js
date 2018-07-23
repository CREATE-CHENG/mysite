import Vue from 'vue'
import Router from 'vue-router'
import index from '@/views/index'
import list from '@/components/section/list'
import detail from '@/components/section/detail'
import archive from '@/components/section/archive'
import nothing from '@/components/section/nothing'

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
          }
        },
        {
          path: 'article/:id',
          name: 'detail',
          components: {
            'section': detail
          }
        },
        {
          path: 'category/:name',
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
        },
        {
          path: '*',
          name: '404',
          components: {
            'section': nothing
          }
        }
      ]
    }
  ]
})
