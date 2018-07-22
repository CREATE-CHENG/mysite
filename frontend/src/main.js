// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import App from './App'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueTimeago from 'vue-timeago'
import store from './store/store'
import './axios/interceptors'
import VueCookies from 'vue-cookies'
// import mavonEditor from 'mavon-editor'
// import 'mavon-editor/dist/css/index.css'
// import 'github-markdown-css/github-markdown.css'
import 'font-awesome/css/font-awesome.css'

Vue.use(VueCookies)

Vue.config.productionTip = false
Vue.config.devtools = true

Vue.use(BootstrapVue)

// Vue.use(mavonEditor)

Vue.use(VueTimeago, {
  name: 'Timeago', // Component name, `Timeago` by default
  locale: undefined, // Default locale
  locales: {
    'zh-CN': require('date-fns/locale/zh_cn')
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: {
    App
  }
})
