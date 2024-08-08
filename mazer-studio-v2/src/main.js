import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueMarkdownEditor from '@kangc/v-md-editor';
import vuepressTheme from '@kangc/v-md-editor/lib/theme/vuepress.js';

import './assets/style.scss'
import "@popperjs/core"
import 'bootstrap'
import 'flag-icon-css/css/flag-icons.css'
import '@kangc/v-md-editor/lib/style/base-editor.css';
import '@kangc/v-md-editor/lib/theme/style/vuepress.css';

import Prism from 'prismjs';

VueMarkdownEditor.use(vuepressTheme, {
    Prism,
});

const app = createApp(App)

app.use(router)
app.use(VueMarkdownEditor)

app.mount('#app')

app.config.globalProperties.$server = 'http://127.0.0.1:5000';