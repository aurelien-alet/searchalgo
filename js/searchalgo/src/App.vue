<template>
  <div id="app">
    <h3>SearchAlgo</h3>
    <div>{{ test }}</div>
    <page></page>
  </div>
</template>

<script>
import Page from './components/Page.vue'

export default {
  name: 'app',
  components: {
    Page
  },
  data() {
      return {
          test: "ok"
      }
  }
}
</script>

<style>
  @import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
</style>
