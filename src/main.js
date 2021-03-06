// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Decks from './components/Decks'
import Info from './components/Info'
// import router from './router'
import './styles.scss'

Vue.config.devtools = true
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  // template: '<App/>',
  render: function (createElement) {
    return createElement('App', {})
  }
})

new Vue({
  el: '#decks',
  components: { Decks },
  render: function (createElement) {
    return createElement('Decks', {})
  }
})

new Vue({
  el: '#info',
  components: { Info },
  render: function (createElement) {
    return createElement('Info', {})
  }
})
