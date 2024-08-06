import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import './assets/style.scss'
import "@popperjs/core"
import 'bootstrap'
import 'flag-icon-css/css/flag-icons.css'


const app = createApp(App)

app.use(router)

app.mount('#app')

app.config.globalProperties.$server = 'http://127.0.0.1:5000';