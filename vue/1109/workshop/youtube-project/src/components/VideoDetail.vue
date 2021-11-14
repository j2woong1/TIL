<template>
  <div v-if="video">
    <iframe :src="videoURL" frameborder="0"></iframe>
    <h2>title</h2>
    <p>desciption</p>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    video: {
      type: [String, Object], // 처음에 아무것도 안고른경우 
    }
  },
  computed: {
    videoURL: function () {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  }
}
</script>

<style>

</style>