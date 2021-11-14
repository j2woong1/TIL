<template>
  <div>
    <h1>Video List</h1>
    <ul>
      <VideoListItem 
      v-for="(video, idx) in videoList" :key="idx"
      :video="video" />
    </ul>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  computed: {
    videoList: function () {
      return this.$store.state.searchResult
    }
  }
} 
</script>

<style>

</style>