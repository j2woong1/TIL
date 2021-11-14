<template>
  <li @click="selectVideo">
    <img :src="youtubeImageSrc">
    {{ video.snippet.title | stringUnescape }}  
  </li>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  methods: {
    selectVideo: function () {
      this.$emit('select-video', this.video)
    }
  },
  props: {
    video: {
      type: Object,
    }
  },
  computed: {
    youtubeImageSrc: function () {
      return this.video.snippet.thumbnails.default.url
    }
  },
  filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText)
    }
  }
}
</script>

<style>

</style>