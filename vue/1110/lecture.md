[TOC]

## Vuex

### Vuex Intro

- Vuex

  - `Statement management pattern + Library` : 상태 관리 패턴 + 라이브러리
  - 상태 (state)를 전역 저장소로 관리할 수 있도록 지원하는 라이브러리
    - 예측 가능한 방식으로만 변경될 수 있도록 보장 규칙 설정
    - 모든 컴포넌트 중앙 집중식 저장소 역할

- State

  - 모든 상태 정보

- 상태 관리 패턴

  - 컴포넌트 공유 상태 추출 -> 전역에서 관리
  - 컴포넌트 : view, 트리 상관 없이 상태 액세스 / 동작 트리거
  - 상태 관리, 특정 규칙 적용 관련 개념 정의, 분리 -> 코드 구조, 유지 관리 기능 향상

- 기존 Pass props & Emit event

  - 단방향 흐름으로 부모 -> 자식 전달만 가능, 반대 : 이벤트 트리거
  - 장점 : 데이터 흐름 직관적 파악
  - 단점 : 컴포넌트 중첩 많아지면 동위 관계 컴포넌트로 데이터 전달 low

  ![image-20211114133136303](C:\Users\j2woo\Desktop\ssafy6\TIL\img\image-20211114133136303.png)

- Vuex management pattern

  - 중앙 저장소 (store)에 state 모아놓고 관리
  - 규모 클 때 (컴포넌트 중첩 많은) 효율적
  - 컴포넌트 : store state만 관리하면 됨 -> 동일 state 공유 컴포넌트 : 동기화

### Vuex Core Concepts

![image-20211114133416477](C:\Users\j2woo\Desktop\ssafy6\TIL\img\image-20211114133408079.png)

- State
  - 중앙에서 관리하는 모든 상태 정보 : data
    - single state tree
    - 모든 애플리케이션 상태 포함하는 **원본 소스 (single source of truth)**
    - 각 애플리케이션마다 하나 저장소
  - 여러 컴포넌트 내부 특정 state를 중앙에서 관리
- Mutations
  - state 변경
  - handler 함수는 반드시 동기적
    - 비동기 : state 변화 시점이 의도와 달라질 수 있음, 콜백 호출 시기 모름 (추적 X)
  - 첫번째 인자로 `state`
  - Action `commit()` 메서드로 호출
- Actions
  - 비동기 작업 포함 가능
  - `context` 객체 인자
  - 컴포넌트에서 `dispatch()` 메서드로 호출
- Getters
  - state 변경 안하고 계산 수행 : computed 유사
    - 실제 계산된 값을 사용하는 것처럼 -> state 기준 계산
  - state 종속성에 따라 캐시 (catched), 종속성 변경 시에만 재계산

### Vuex Todo App

![image-20211114134611507](C:\Users\j2woo\Desktop\ssafy6\TIL\img\image-20211114134611507.png)

#### Set Projects & Components

```bash
# Create Project
$ vue create todo-vuex-app
$ cd todo-vuex-app

# Add Vuex plugin in Vue CLI
$ vue add vuex

# Commit 여부 (Yes)
WARN There are uncommitted changes in the current repository, its recommdend to commit or stash them first. ? Still proceed? Yes
```

```javascript
// index.js
// Vuex core concepts

import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
    },
    mutations: {
    },
    actions: { 
    },
    modules: { 
    }
})
```

```vue
// components/TodoListItem.vue
// 개별 todo 컴포넌트, TodoList 컴포넌트 자식 컴포넌트

<template>
	<div>Todo</div>
</template>

<script>
export default {
    name: 'TodoListItem',
}
</script>

// components/TodoList.vue
// todo 목록 컴포넌트, TodoListItem 컴포넌트 부모 컴포넌트

<template>
	<div>
    	<todo-list-item></todo-list-item>
    </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'
    
export default {
    name: 'TodoList',
    components: {
        TodoListItem,
    }
}
</script>

// components/TodoForm.vue
// todo 데이터 입력 컴포넌트

<template>
	<div>Todo Form</div>
</template>

<script>
export default {
    name: 'TodoForm',
}
</script>

// App.vue
// 최상위 컴포넌트, TodoList, TodoForm 컴포넌트 부모 컴포넌트

<template>
	<div id="app">
    	<h1>Todo List</h1>
        <todo-list></todo-list>
        <todo-form></todo-form>
    </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'
    
export default {
    name: 'App',
    components: {
        TodoList,
        TodoForm
    }
}
</script>
```

#### Create Todo

```javascript
// index.jst
// state 작성

export default new.Vuex.Store({
    state: {
        todos: [
            {
                title: '할 일1',
                isCompleted: false,
                date: new Date().getTime(),
            },
            {
                title: '할 일2',
                isCompleted: false,
                date: new Date().getTime(),
            },
        ]
    }
})
```

```vue
// TodoList.vue
// 컴포넌트에서 Vuex Store의 state 접근 : 값 변경 X

<template>
	<div>
        <todo-list-item v-for="todo in $store.state.todos" :key="todo.date">
    	</todo-list-item>
    </div>
</template>

// TodoList.vue
// Computed로 변경 : 변경 사항 있을때만 새로 계산 값 반환 (computed)

<template>
	<div>
        <todo-list-item v-for="todo in todos" :key="todo.date">
    	</todo-list-item>
    </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'
    
export default {
    ...
    computed: {
        todos: function () {
            return this.$store.state.todos
        }
    }
}
</script>

// Pass Props
// TodoList.vue

<template>
	<div>
        <todo-list-item v-for="todo in todos" :key="todo.date" :todo="todo">
    	</todo-list-item>
    </div>
</template>

// TodoListItem.vue

<template>
	<div>{{ todo.title }}</div>
</template>

<script>
export default {
    name: 'TodoListItem',
    props: {
        todo: {
            type: Object,
        }
    }
}
</script>

// Actions, Mutations
// TodoForm.vue

<template>
	<div>
        <input type="text" v-model.trim="todoTitle" @keyup.enter="createTodo">
        <button @click="createTodo">Add</button>
    </div>
</template>

<script>
export default {
    ...
    methods: {
        createTodo: function () {
            const todoItem = {
                title: this.todoTitle,
                isCompleted: false,
                date: new Date().getTime(),
            }
            if (todoItem.title) {
                this.$store.dispatch('createTodo', todoItem)
            }
            this.todoTitle = null
        }
    }
}
</script>

// index.js
export default new Vuex.Store({
	state: {
		todos: [],
	}
	mutations: { // State todo 데이터 조작
		CREATE_TODO: function (state, todoItem) {
			state.todos.push(todoItem)
		}
	},
	actions: { // CREATE_TODO mutation 함수 호출
		createTodo: function (context, todoItem) {
			context.commit('CREATE_TODO', todoItem)
		}
	}
})
```

```javascript
// actions 변경
// 변경 전
actions: {
    createTodo: function (context, todoItem) {
        context.commit('CREATE_TODO', todoItem)
    }
},
    
// 변경 후
actions: {
    createTodo: function ({ commit }, todoItem) {
        commit('CREATE_TODO', todoItem)
    }
},
```

#### Delete Todo

```vue
// TodoListItem.vue
// 함수 호출

<template>
	<div>
        <div>
    		<span>{{ todo.title }}</span>        
	    </div>
        <button @click="deleteTodo">Delete</button>
    </div>
</template>

<script>
export default {
    name: 'TodoListItem',
    props: {
        todo: Object,
    },
    methods: {
        deleteTodo: function () {
            todo.$store.dispatch('deleteTodo', this.todo)
        }
    }
}
</script>
```

```javascript
// Actions & Mutations

actions: {
    ...
    deleteTodo: function ({ commit }, todoItem) {
        commit('DELETE_TODO', todoItem)
    }
},
mutations: {
    DELETE_TODO: function (state, todoItem) {
        // 1. todoItem이 첫 번째로 만나는 요소의 index
        const index = state.todos.indexOf(todoItem)
        
        // 2. 해당 index 1개만 삭제, 나머지 요소 새로운 배열 생성
        state.todos.splice(index, 1)
    }
}
```

#### Update Todo

```vue
// TodoListItem.vue
// 함수 호출

<template>
	<div>
        <span @click="updateTodoStatus">{{ todo.title }}</span>
        <button @click="deleteTodo">Delete</button>                
    </div>
</template>

<script></script>
```



#### Getters

#### Component Binding Helper

#### LocalStorage