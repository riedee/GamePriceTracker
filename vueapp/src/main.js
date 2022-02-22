import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios';

createApp(App).mount('#app')

const Vue = window.vue;

Vue.prototype.$http = axios;
