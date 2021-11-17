## Vue with server

### 1. Todo 데이터를 가져오는 과정에서 발생하는 CORS Policy 관련 이슈 해결

```bash
$ pip install django-cors-headers
```

```python
# server/settings.py
INSTALLED_APPS = [
    'corsheaders',...
]
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', ....
]

CORS_ALLOW_ALL_ORIGINS = True
```



### 2. Todo Create & Read

> - CreateTodo 컴포넌트의 createTodo 메서드 작성
> - Todo 작성이 성공하면 Vue Router 를 사용해 TodoList 컴포넌트로 이동
> - Get Todos 버튼을 클릭하지 않고도 TodoList 컴포넌트가 생성될 때 Todo 목록을 가져올 수 있도록 수정

```vue
// views/todos/CreateTodo.vue
createTodo: function () {
    const todoItem = {
        title: this.title,
    }

    if (todoItem.title) {
        axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/todos/',
            data: todoItem
        })
            .then(res => {
            console.log(res)
            this.$router.push({ name: 'TodoList' })
        })
            .catch(err => {
            console.log(err)
        })
    }
}
```



### 3. Todo Delete

> - TodoList 컴포넌트의 deleteTodo 메서드 작성
> - Todo 삭제가 성공하면 별도의 새로고침 없이 업데이트 된 Todo 목록을 보여줄 수 있도록 함

```vue
// views/todos/TodoList.vue
deleteTodo: function (todo) {
    axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/todos/${todo.id}/`
    })
        .then(res => {
        console.log(res)
        this.getTodos()
    })
        .catch(err => {
        console.log(err)
    })
},
```



### 4. Todo Update (+ 실시간 취소선 toggle)

> - TodoList 컴포넌트의 updateTodo 메서드 작성
> - Todo status 가 변경되면 별도의 새로고침 없이 취소선이 toggle 될 수 있도록 함

```vue
// views/todos/TodoList.vue
    updateTodoStatus: function (todo) {
      // 4번 문제
      const todoItem = {
        ...todo,
        is_completed: !todo.is_completed
      }

      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/todos/${todo.id}/`,
        data: todoItem,
      })
        .then(res => {
          console.log(res)
          todo.is_completed = !todo.is_completed
        })
      },
    },
  created: function () {
    this.getTodos()
  }
```

