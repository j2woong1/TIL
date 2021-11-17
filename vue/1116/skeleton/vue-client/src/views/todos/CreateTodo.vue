<template>
  <div>
    <input type="text" v-model.trim="title" @keypress.enter="createTodo">
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
import axios from'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: '',
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem("jwt")

      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        }
      }

      return config
    },

    createTodo: function () {
      const config = this.setToken()

      const todoItem = {
        title: this.title,
      }

      if (todoItem.title) {
        axios.post(`${SERVER_URL}/todos/`, todoItem, config)
          .then((res) => {
            console.log(res)
            this.$router.push({ name: 'TodoList' })
          })
          .catch((err) => {
            console.log(err)
          })
        }
    },
  }
}
</script>