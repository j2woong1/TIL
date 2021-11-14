<template>
  <div>
    <todo-list-item
      v-for="todo in todos"
      :key="todo.date"
      :todo="todo"
    >
    </todo-list-item>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  // 1. 과거
  // computed: {
  //   todos: function () {
  //     return this.$store.state.todos
  //   },
  // }
  // 2.
  // computed: mapState([
  //   'todos',
  // ]),
  // 3. 최종
  computed: {
    ...mapState([
      'todos'
    ])
  }
}
</script>

<style>

</style>