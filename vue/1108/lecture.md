## Vue CLI

### SFC

- Component
  - 기본 HTML element 확장 -> 재사용 가능 코드 캡슐화 => 유지보수
  - 재사용성
  - Vue Component === Vue Instance
- SFC (Single File Component)
  - `.vue` 확장자 가진 싱글 파일 컴포넌트 통한 개발 방식
  - 특정 영역 HTML, CSS, JavaScript 코드를 하나 파일에서 관리

### Vue CLI

- Quick Start

  ```bash
  $ npm install -g @vue/cli
  $ vue create 프로젝트이름
  Default ([vue 2] babel, eslint)
  $ cd 프로젝트이름
  $ npm run serve
  ```

### Babel & Webpack

![image-20211110133732297](C:\Users\j2woo\Desktop\ssafy6\TIL\img\image-20211110133732297.png)

- Node.js
  - JavaScript Runtime Environment -> JS 브라우저 밖에서 실행 가능한 환경
- Babel
  - Compiler -> ES2015+ JS 코드를 구 버전 JS로 바꾸는 도구
- Webpack
  - Module Bundler -> 모듈 간 의존성 문제 해결
- 프로젝트 구조
  - `node_modules` : node.js 환경 의존성 모듈
  - `public/index.html` : Vue 앱 뼈대, 실제 제공 단일 html 파일
  - `src/assets` : webpack에 의해 빌드 된 정적 파일
  - `src/components` : 하위 컴포넌트 위치
  - `src/App.vue` : 최상위 컴포넌트
  - `src/main.js` : webpack 빌드 시작 시 가장 먼저 불러오는 entry point, DOM ~ data 연결과 동일 작업, vue 전역에서 활용할 모듈 등록
  - `babel.config.js`
  - `package.json` : 프로젝트 종속성 목록, 지원 브라우저 구성 옵션 포함
  - `package-lock.json` : `node_modules`에 설치되는 모듈 관련 의존성 설정, 관리, 팀원/배포 환경에서 동일 종속성 설치 보장, 사용 패키지 버전 고정, 개발 과정 간 의존성 패키지 충돌 방지

### Pass Props & Emit Events

- 컴포넌트 작성

  - 부모 : 자식에게 데이터 전달 (Pass props) / 자식 : 메시지 부모에게 알림 (Emit event)

- Props

  - `prop-data-name="value"`

  - Static Props

    ```vue
    // App.vue
    <template>
    	<div id="app">
            <img alt="Vue logo" src="./assets/logo.png">
            <about my-message="This is prop data"></about>
        </div>
    </template>
    
    // About.vue
    
    <template>
    	<div>
            <h1>About</h1>
            <h2>{{ mymessage }}</h2>
        </div>
    </template>
    
    <script>
    export default {
        name: 'About',
        props: {
            myMessage: String,
        }
    }
    </script>
    ```

  - Dynamic Props

    - v-bind directive

    ```vue
    // App.vue
    <template>
    	<div id="app">
            <img alt="Vue logo" src="./assets/logo.png">
            <about my-message="This is prop data" :parent-data="parentData"></about>
        </div>
    </template>
    
    <script>
    import About from './components/About.vue'
        
    export default {
        name: 'App',
        components: {
            About
        },
        data: function () {
            return {
                parentData: 'This is parent Data by v-bind'
            }
        }
    }
    </script>
    
    // About.vue
    
    <template>
    	<div>
            <h1>About</h1>
            <h2>{{ mymessage }}</h2>
            <h2>{{ parentData }}</h2>
        </div>
    </template>
    
    <script>
    export default {
        name: 'About',
        props: {
            myMessage: String,
            parentData: String,
        }
    }
    </script>
    ```

  - 이름 컨벤션

    - during declaration (선언 시) : camelCase
    - in template (HTML) : kebab-case

  - data: 함수 (function)

  - 단방향 데이터 흐름 : 부모 컴포넌트 업데이트될 때마다 자식 요소 모든 prop 업데이트

- Emit

  - `$emit(eventName)` : 부모 -> v-on

    ```vue
    // About.vue
    
    <template>
    	<div>
            <h1>About</h1>
            <h2>{{ mymessage }}</h2>
            <h2>{{ parentData }}</h2>
            <input type="text" @keyup.enter="childInputChange" v-model="childInputData">
        </div>
    </template>
    
    <script>
    export default {
        name: 'About',
        data: function () {
            return {
                childInputData: null,
            }
        },
        props: {
            myMessage: String,
            parentData: String,
        },
        methods: {
            childInputChange: function () {
                this.$emit('child-input-change', this.childInputData)
            }
        }
    }
    </script>
    
    // App.vue
    <template>
    	<div id="app">
            <img alt="Vue logo" src="./assets/logo.png">
            <about my-message="This is prop data" 
                   :parent-data="parentData" @child-input-change="parentGetChange"></about>
        </div>
    </template>
    
    <script>
    import About from './components/About.vue'
        
    export default {
        name: 'App',
        components: {
            About
        },
        data: function () {
            return {
                parentData: 'This is parent Data by v-bind'
            }
        },
        methods: {
            parentGetChange: function (inputData) {
                console.log('About으로부터 ${inputData}를 받음!')
            }
        }
    }
    </script>
    ```

  - event 이름 컨벤션 : kebab-case

### Vue Router

- 설치

  ```bash
  $ vue create 프로젝트이름
  $ cd 프로젝트이름
  $ vue add router
  WARN There are uncommitted changes in the current repository, its recommend to commit or stash them first. ? Still proceed? Yes
  ? Use history mode for router? (Requires proper server setup for index fallback in production) (Y/n)
  Yes
  ```

- 변화

  ```vue
  // App.vue
  
  <template>
  	<div id="app">
          <div id="nav">
      		<router-link to="/">Home</router-link>
              <router-link to="/about">About</router-link>
  	    </div>
      </div>
  </template>
  ```

  ![image-20211110155424827](C:\Users\j2woo\Desktop\ssafy6\TIL\img\image-20211110155424827.png)

  - `router-link`
    - 사용자 내비게이션 가능하게 하는 component
    - 목표 경로 : `to` prop
    - 클릭 이벤트 차단 -> 리로드 X
    - 기본 GET 요청 이벤트 제거 형태로 구성

- Named Routes

  ```javascript
  // index.js
  
  import Vue from 'vue'
  import VueRouter from 'vue-router'
  import Home from './views/Home.vue'
  import About from '@/views.About.vue'
  
  Vue.use(VueRouter)
  
  const routes = [
      {
          path: '/',
          name: 'Home',
          component: Home
      },
      {
          path: '/about',
          name: 'About',
          component: About
      }
  ]
  ```

  ```vue
  // App.vue
  
  <template>
  	<div id="app">
          <div id="nav">
      		<router-link :to="{ name: 'Home' }">Home</router-link>
              <router-link :to="{ name: 'About' }">About</router-link>	        
  	    </div>
      </div>
  </template>
  ```

- 프로그래밍 방식 내비게이션

  - 선언적 방식 : `<router-link to ="..."`
  - 프로그래밍 방식 : `$router.push(...)`

  ```vue
  // literal string path
  router.push('home')
  
  // object
  router.push({ path: 'home'})
  
  // named route
  router.push({ name: 'user', params: { userId: '123' }})
  
  // with query, resulting in /register?plan=private
  router.push({ name: 'register', query: { plan: 'private' }})
  ```

  ```vue
  // About.vue
  
  <template>
  	<div class="about">
          <h1>This is an about page</h1>
          <button @click="moveToHome">Home으로 이동</button>
      </div>
  </template>
  
  <script>
  export default {
      name: 'About',
      methods: {
          moveToHome: function () {
              // this.$router.push('/')
              this.$router.push({ name: 'Home' })
          }
      }
  }
  </script>
  ```

- Dynamic Route Matching

  - 동적 인자 전달 : 주어진 패턴 가진 라우트 -> 동일 컴포넌트에 매핑 시

  ```javascript
  const routes = [
      {
          path: '/user/:userId',
          name: 'User',
          component: User
      }
  ]
  ```

  |              pattern               |     matched path      |            $route.params            |
  | :--------------------------------: | :-------------------: | :---------------------------------: |
  |          /user/:userName           |      /user/john       |        { username: 'john' }         |
  | /user/:userName/article/:articleId | /user/john/article/12 | { username: 'john', articleId: 12 } |

- Component, Views

  - App.vue : 최상위 컴포넌트
  - views/
    - router (index.js)에 매핑되는 컴포넌트 모아두는 폴더
  - components/
    - router에 매핑된 컴포넌트 내부에 작성하는 컴포넌트 모아두는 폴더

