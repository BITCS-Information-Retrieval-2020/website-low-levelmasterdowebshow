// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
import VideoPlayer from 'vue-video-player'
import qs from 'qs'

Vue.use(VideoPlayer)
require('vue-video-player/src/custom-theme.css')

var Instance = axios.create()
Vue.config.productionTip = false
// Instance.defaults.baseURL = 'http://47.95.200.233:8080'
Instance.defaults.baseURL = 'http://10.63.82.28:9001'
// Instance.defaults.baseURL = 'http://192.168.43.107:9001'
Vue.prototype.axios = Instance

Vue.prototype.$qs = qs;
Vue.use(ElementUI)
Vue.prototype.$axios = axios;
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
