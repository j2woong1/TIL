<template>
  <div id="app">
    <!-- 3. 사용한다 -->
    <h1>App</h1>
    <p>AddData: {{ appData }}</p>
    <input v-model="appData" type="text">
    <p>ParentData: {{ parentData }}</p>
    <p>ChildData: {{ childData }}</p>
    <Parent :appData="appData" @parent-input="inputParent" @child-input="inputChild"/>
  </div>
</template>

<script>
// 1. 불러온다
import Parent from './components/Parent.vue'

export default {
  name: 'App',
  // 2. 등록한다
  components: {
    Parent,
  },
  data: function () {
    return {
      appData: '',
      parentData: '',
      childData: '',
    }
  },
  methods: {
    inputParent: function (data) {
      this.parentData = data
    },
    inputChild: function (data) {
      this.childData = data
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
