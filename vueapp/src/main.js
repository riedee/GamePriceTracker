import { createApp } from 'vue'
import Search from './components/Search.vue'
import axios from 'axios';

Vue.prototype.$http = axios;

createApp(Search).mount('#app')
