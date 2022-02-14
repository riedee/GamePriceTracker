@ -0,0 +1,26 @@
<template>
  <img alt="Vue logo" src="./assets/logo.png">
</template>

<script>
import GameDataBase from './components/GameDataBase.vue'
import GameDataGet from './components/GameDataGet.vue'
import GameDataPost from './components/GameDataPost.vue'

export default {
  name: 'App',
  components: {
    GameDataBase,
    GameDataGet,
    GameDataPost
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
