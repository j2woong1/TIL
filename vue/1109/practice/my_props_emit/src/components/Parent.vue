<template>
<div>
  <h1>This is parent</h1>
  <p>ParentData: {{ parentData }}</p>
  <input v-model="parentData" type="text" @input="inputParentData">
  <p>appData: {{ appData }}</p>
  <p>ChildData: {{ childData }}</p>
  <Child :appData="appData" :parentData="parentData" @child-input="inputChildData"/>
</div>
</template>

<script>
import Child from './Child.vue'

export default {
  name: 'Parent',
  data: function () {
    return {
      parentData: '',
      childData: '',
    }
  },
  methods: {
    inputChildData: function (data) {
      this.childData = data
      this.$emit('child-input', this.childData)
      // console.log('!!!! text from child')
    },
    inputParentData: function () {
      this.$emit('parent-input', this.parentData)
    },
  },
  props: {
    appData: String,
  },
  components: {
    Child,
  }
}
</script>

<style>

</style>