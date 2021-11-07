## Intro

- `Vue.js`
  - 자바스크립트 프레임워크
- SPA
  - Single Page Application
  - 현재 페이지 동적 렌더링
  - 단일 페이지, 서버에서 최초에만 페이지 다운로드, 이후 동적으로 DOM 구성
    - 현재 페이지 중 필요 부분만 동적으로 재작성
  - 연속되는 페이지 간 사용자 경험 향상 : 모바일 최적화
  - CSR (Client Side Rendering) 구조
- CSR
  - 클라이언트에서 화면 구성
  - 최초 요청 시 뼈대만 받고 브라우저에서 동적으로 DOM 렌더링
    - HTML, CSS, JS 등 데이터 제외 리소스 응답 -> 이후 클라이언트에서 필요 데이터만 요청해서 JS로 DOM 렌더링
  - 장점
    - 서버 ~ 클라이언트 트래픽 감소 : 필요 데이터만 갱신
    - 사용자 경험 향상 : 변경되는 부분만 갱신
  - 단점
    - 전체 페이지 렌더링 시점 느림
    - SEO (검색 엔진 최적화) 어려움 : 최초 문서에 데이터 X
- SSR
  - Server Side Rendering
  - 서버에서 클라이언트 보여줄 페이지 모두 구성해서 전달
  - 장점
    - 초기 구동 속도 빠름
    - SEO 적합 : DOM에 이미 모든 데이터 작성
  - 단점
    - 모든 요청마다 새로운 페이지 구성 : 반복 새로고침으로 인한 사용자 경험 침해, 트래픽 많음

## Why Vue.js?

![image-20211103144544213](C:\Users\j2woo\AppData\Roaming\Typora\typora-user-images\image-20211103144544213.png)

```html
<form class="d-inline like-form" data-id="{{ article.pk }}">
    {% csrf_token %}
    {% if user in article.like_users.all %}
    	<button class="btn btn-link">
    		<i id="like-{{ article.pk }}" class="fas fa-heart fa-lg" style="color:crimson;"></i>        
	    </button>
    {% else %}
    	<button class="btn btn-link">
    		<i id="like-{{ article.pk }}" class="fas fa-heart fa-lg" style="color:black;"></i>        
	    </button>
    {% endif %}
</form>
<p>
    <span id="like-count-{{ article.pk }}"> <!-- 선택 : 무엇을 -->
    	{{ article.like_users.all|length }} 
    </span>명이 이 글을 좋아합니다.
</p>
```

```javascript
const forms = document.querySelectorAll('.like-form')  // 선택 - 잡는다

forms.forEach(function (form) {
    form.addEventListener('submit', function (event) {  // 이벤트 등록
        event.preventDefault()
        
        const articleId = event.target.dataset.articleId
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
        
        axios.post(`http://127.0.0.1:8000/articles/${articleId}/like/`, {}, {
            headers: {
                'X-CSRFToken': csrftoken
            }
        })
        .then(function (res) {
            const count = res.data.count
            const liked = res.data.liked
            
            const likeIconColor = document.querySelector(`#like-${articleId}`)
            const likeCount = document.querySelector(`#like-count-${articleId}`)
            
            likeCount.innerText = `${count} 명이 이 글을 좋아합니다.`  // 변경
            
            if (liked) {
                likeIconColor.style.color = 'crimson'
            } else{
                likeIconColor.style.color = 'black'
            }
        })
    })
})
```

- Vanilla JS
  - 한 유저가 100만 개의 게시글 작성 + 닉네임 변경 시 게시글 전부 작성자 이름 수정 ㅣㅍㄹ요
  - '모든 요소' 선택, '이벤트' 등록, 값 변경
- Vue.js
  - DOM ~ Data 연결 시 Data 변경하면 DOM은 알아서 변경 => **Data만 관리하면 된다**

## Concept

- MVVM Pattern : 애플리케이션 로직을 UI에서 분리
  - Model
    - JavaScript Object 자료 구조 -> View Instance 내부에서 data로 사용, 바뀌면 View (DOM) 반응
  - View
    - DOM (HTML) : Data 변화에 따라 바뀌는 대상
  - View Model
    - Vue Instance : View ~ Model 사이 Data, DOM 관련 모든 일 처리, 얼마만큼 잘 처리해서 보여줄지 (DOM) 고민

![image-20211103151642363](C:\Users\j2woo\AppData\Roaming\Typora\typora-user-images\image-20211103151642363.png)



## Quick Start

> https://kr.vuejs.org/v2/guide/

- Django 순서

  - 데이터 흐름
  - url -> views -> template

- Vue.js 순서

  - Data 변화 시 DOM 변경
  - Data 로직 작성 -> DOM 작성

- CDN 작성

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
  </head>
  <body>
    <!-- 1. Vue.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  </body>
  </html>
  ```

- 선언적 렌더링

  ```html
  <h2>선언적 렌더링</h2>
  <div id="app">
      {{ message }}
  </div>
  ```

  ```javascript
  var app = new Vue({
  	el: '#app',
  	data: {
  		message: '안녕하세요 Vue!'
  	}
  })
  ```

- Element 속성 바인딩

  ```html
  <h2>Element 속성 바인딩</h2>
  <div id="app-2">
      <span v-bind:title="message">
      	내 위에 잠시 마우스를 올리면 동적으로 바인딩 된 title을 볼 수 있습니다!
      </span>
  </div>
  ```

  ```javascript
  var app2 = new Vue({
  	el: '#app-2',
  	data: {
  		message: '이 페이지는 ' + new Date() + ' 에 로드 되었습니다'
  	}
  })
  ```

- 조건문

  ```html
  <h2>조건</h2>
  <div id="app-3">
      <p v-if="seen">
          이제 나를 볼 수 있어요
      </p>
  </div>
  ```

  ```javascript
  var app3 = new Vue({
  	el: '#app-3',
  	data: {
  		seen: true // false로 토글 가능
  	}
  })
  ```

- 반복문

  ```html
  <h2>반복</h2>
  <div id="app-4">
  	<ol>
          <li v-for="todo in todos">
          	{{ todo.text }}
          </li>
      </ol>
  </div>
  ```

  ```javascript
  var app3 = new Vue({
  	el: '#app-4',
  	data: {
  		todos: [
              { text: 'JavaScript 배우기' },
              { text: 'Vue 배우기' },
              { text: '무언가 멋진 것을 만들기' },
          ]
  	}
  })
  ```

- 사용자 입력 핸들링

  ```html
  <h2>사용자 입력 핸들링</h2>
  <div id="app-5">
  	<p>{{ message }}</p>
      <button v-on:click="reverseMessage">
          메시지 뒤집기
      </button>
  </div>
  ```

  ```javascript
  var app3 = new Vue({
  	el: '#app-5',
  	data: {
  		message: '안녕하세요! Vue.js!'
  	}
      methods: {
      	reverseMessage: function () {
      		this.message = this.message.split('').reverse().join('')
  		}
  	}
  })
  ```

## Basic Syntax

- Vue Instance

  ```javascript
  const app = new Vue({
      el: '#app'
  })
  ```

  - Vue 함수로 새 인스턴스 만들기
  - Option 객체 전달 필요

- Options / DOM - `el`

  ```javascript
  const app = new Vue({
      el: '#app'
  })
  ```

  - Vue 인스턴스에 연결할 기존 DOM element 필요
  - CSS 선택자, HTML Element로 작성

- Options / DOM - `data`

  ```javascript
  const app = new Vue({
      el: '#app'
      data: {
      	message: 'Hello',
  	}
  })
  ```

  - Vue 인스턴스 데이터 객체
  - Vue 인스턴스 상태 데이터 정의
  - 다른 함수에서 this 키워드로 접근 가능

- Options / DOM - `methods`

  ```javascript
  const app = new Vue({
      el: '#app'
      data: {
      	message: 'Hello',
  	}
      methods: {
      	greeting: function () {
      		console.log('hello')
  		}                
      }
  })
  ```

  - Vue 인스턴스에 추가할 메서드
  - 다른 함수에서 this 키워드로 접근 가능

- `this` 키워드

  ```html
  <div id="app">
      <button @click="myFunc">a</button>
      <button @click="yourFunc">b</button>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
  	const app = new Vue({
      	el: '#app'
      	data: {
      		a: 1,
  		}
          methods: {
              myFunc: function () {
          		console.log(this)  // Vue Instance
  		    }
      		yourFunc: () {
          		console.log(this)  // Window
  		    }
          }
      })
  </script>
  ```

## Template Syntax

- Template Syntax

  - 렌더링 된 DOM -> 기본 Vue 인스턴스 데이터에 선언적으로 바인딩할 수 있는 HTML 기반 템플릿 구문 사용

  - Interpolation (보간법)

    - Text

      ```vue
      <span>메시지: {{ msg }}</span>
      ```

    - Raw HTML

      ```vue
      <span v-html="rawHtml"></span>
      ```

    - Attributes

      ```vue
      <div v-bind:id="dynamicId"></div>
      ```

    - JS 표현식

      - `{{ number + 1}}`, `{{ message.split('').reverse().join('') }}`

  - Directive

    - v-접두사 특수 속성
    - 속성 값 : 단일 JS 표현식 : v-for 예외
    - 표현식 값 변경 시 DOM에 적용 역할
    - 전달인자 (Arguments) : `:`을 통해 전달인자 받기
    - 수식어 (Modifiers) : `.` 특수 접미사, 특별한 방법으로 바인딩 해야함 의미

    ```vue
    <a v-bind:href="url"></a>
    <a v-on:click="doSomething"></a>
    
    <form v-on:submit.prevent="onSubmit"></form>
    ```

- v-text

  - textContent 업데이트

## Lifecycle Hooks

## Lodash Library

