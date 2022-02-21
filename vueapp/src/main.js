import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios';

const Vue = window.vue;

Vue.prototype.$http = axios;

createApp(App).mount('#app')
