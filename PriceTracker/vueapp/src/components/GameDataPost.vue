<template>
  <div>
    <input type="text" v-model="postBody" @change="postPost()" />
    <ul v-if="errors && errors.length">
      <li v-for="error of errors">
        {{error.message}}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      postBody: '',
      errors: []
    }
  },

  methods: {
    // Pushes posts to the server when called.
    postPost() {
      axios.post(`https://raw.githubusercontent.com/albert-marrero/video-games-data/main/videogamegeek/games/2022-02-09.json`, {
        body: this.postBody
      })
      .then(response => {})
      .catch(e => {
        this.errors.push(e)
      })
    }
  }
}
</script>