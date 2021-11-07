## Vue 기초

> - Vue를 활용하여 todo list 앱을 완성하시오
>   - select 요소를 통해 todo list 의 상태를 설정할 수 있다
>     - 상태 종류 - 전체, 진행중, 완료
>   - computed를 통해 상태별로 표시되는 todo list를 계산하고 화면에 todo list를 표시한다
>   - Todo item의 체크박스를 통해 할 일의 완료 여부를 설정할 수 있다
>   - "완료된 할 일 지우기" 버튼을 누르면 모든 완료된 todo item을 삭제한다
>   - Local Storage 를 활용하여 브라우저 종료 시에도 데이터가 사라지지 않는다

```html
  <div id="app">
    <select v-model="status">
      <option value="all">전체</option>
      <option value="inProgress">진행 중</option>
      <option value="completed">완료</option>
    </select>
    <input v-model="content" @keyup.enter="addTodo" type="text"> <!-- 엔터 눌렀다가 떼면 -->
    <button @click="addTodo">+</button>
    <br>
    <ul>
      <li v-for="todo in todoListByStatus" :key="todo.date">
        <input type="checkbox" :checked="todo.completed" @click="toggleTodo(todo)">
        <span :class="{ completed: todo.completed }"> {{ todo.content }} </span>
      </li>
    </ul>

    <button @click="deleteCompleted">완료된 할 일 지우기</button>
    
  </div>

  <!-- vue.js -->
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <!-- Lodash -->
  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  <script>
    const STORAGE_KEY = 'vue-todo-app'
    const todoStorage = {
      fetch: function () {
        return JSON.parse(localStorage.getItem(STORAGE_KEY)) || []
      },
      save: function (todoList) {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(todoList))
      },
    }


    const app = new Vue({
      el: '#app',
      data: {
        content: '',
        todoList: todoStorage.fetch(),
        status: 'all',
      },
      methods: {
        addTodo: function () {
          const todo = {
            content: this.content, // 할 일
            completed: false, // 완료 여부
            date: new Date().getTime(), //PK로 활용
          }
          this.todoList.push(todo)
          this.content = ''
        },
        toggleTodo: function (todo) {
          todo.completed = !todo.completed // true <-> false 뒤집기
        },
        deleteCompleted: function () {
          this.todoList = this.todoList.filter(todo => !todo.completed)
        },
      },
      computed: {
        todoListByStatus: function () {
          return this.todoList.filter(todo => {
            if (this.status === 'inProgress') {
              return !todo.completed // 해야할 일들(todo.completed ->false)에 해당하는 것만 모아서 리스트로 만듬
            }
            if (this.status === 'completed') {
              return todo.completed // 완료된 일(todo.completed -> true)
            }
            return true
          })
        }
      },
      watch: {
        todoList: {
          handler: function (todoList) {
            todoStorage.save(todoList)
          },
          deep: true,
        }
      }
    })
  </script>
```

![image-20211104161955273](C:\Users\j2woo\AppData\Roaming\Typora\typora-user-images\image-20211104161955273.png)

