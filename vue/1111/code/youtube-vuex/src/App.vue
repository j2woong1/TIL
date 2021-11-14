<template>
  <div id="app">
    <VideoSearchBar />
    <VideoDetail />
    <VideoList />
  </div>
</template>

<script>
import VideoSearchBar from '@/components/VideoSearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'



export default {
  name: 'App',
  components: {
    VideoSearchBar,
    VideoList,
    VideoDetail,
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
