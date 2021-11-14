<template>
  <div>
    <input @keypress.enter="onSearch" v-model="query" type="text">
    <button @click="onSearch">Search</button>
    
  </div>
</template>

<script>
export default {
  name: 'VideoSearchBar',
  data: function () {
    return {
      query: '',
    }
  },
  methods: {
    onSearch: function () {
      // console.log(`${this.query} 검색 하세요.`)
      this.$store.dispatch('onSearch', this.query)
    }
  }
}
</script>

<style>

</style>