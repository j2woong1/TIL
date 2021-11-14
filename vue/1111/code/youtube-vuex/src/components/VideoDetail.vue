<template>
  <div v-if="isSelected">
    <iframe :src="videoUrl" frameborder="0"></iframe>
    <h2>{{ videoTitle }}</h2>
    <p>{{ videoDesc }}</p>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  computed: {
    isSelected: function () {
      return this.$store.getters.isSelected
    },
    videoUrl: function () {
      return this.$store.getters.videoUrl
    },
    videoTitle: function () {
      return this.$store.getters.videoTitle
    },
    videoDesc: function () {
      return this.$store.getters.videoDesc
    },
  }
}
</script>

<style>

</style>