<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <about 
      my-message="this is prop data"
      :parent-data="parentData"
      @child-input-change="parentGetChange"
    >
    </about>
  </div>
</template>

<script>
import About from './components/About.vue'

export default {
  name: 'App',
  components: {
    About,
  },
  data: function () {
    return {
      parentData: 'This is parent data by v-bind',
    }
  },
  methods: {
    parentGetChange: function (inputData) {
      console.log(`About으로부터 ${inputData}를 받음!!!`)
    }
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
