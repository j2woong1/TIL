<template>
<div>
  <input @keypress.enter="onInputKeyword" type="text">

</div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    onInputKeyword: function (event) {
      // console.log(event.target.value)
      this.$emit('input-search', event.target.value)
    }
  }
}
</script>

<style>

</style>