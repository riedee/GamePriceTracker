import { createApp } from 'vue'
import Search from './components/Search.vue'
import axios from 'axios';

export const HTTP = axios.create({
  baseURL: `https://github.com/albert-marrero/video-games-data/tree/main/videogamegeek/games`
})

createApp(Search).mount('#app')
