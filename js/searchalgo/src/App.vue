<template>
  <div id="app">
    <h1 class="text-centered">SearchAlgo</h1>
    <page></page>
  </div>
</template>

<script>
import Page from './components/Page.vue'
import '../node_modules/bootstrap/dist/js/bootstrap.min.js';

export default {
  name: 'app',
  components: {
    Page
  },
  data() {
      return {

      }
  }
}
</script>

<style>
  @import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
  @import "./style.css";
</style>
