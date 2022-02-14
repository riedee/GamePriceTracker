<template>
  <div>
    <div v-for="post in posts" v-bind:key="post.id">
      <h2>{{ post.title }}</h2>
      <p>{{ post.body }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      posts: [],
    };
  },

  methods: {
    async getData() {
      try {
        const response = await this.$http.get(
          "https://www.google.com/search?q=video+games&rlz=1C1CHBF_enUS864US864&oq=video+games&aqs=chrome.0.0i433i512l2j0i131i433i512j0i433i512j46i512j0i512j0i457i512j0i402l2j0i131i433i512.2867j0j7&sourceid=chrome&ie=UTF-8"
        );
        // JSON responses are automatically parsed.
        this.posts = response.data;
      } catch (error) {
        console.log(error);
      }
    },

    created() {
      this.getData();
    }
  },
};
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
