## AJAX

- AJAX

  - Asynchronous JavaScript And XML (비동기식 JavaScript와 XML)
  - 서버 통신 -> `XMLHttpRequest`

- 특징

  - 비동기성 : 전체 reload (새로고침) 안해도 수행
    - event 있으면 일부 업데이트 가능
  - 페이지 새로고침 없이 서버 요청
  - 서버에서 데이터 받고 작업 수행

- `XMLHttpRequest`

  - 전체 페이지 새로고침 없이 데이터 받음
  - 모든 종류 데이터 받기

  ```javascript
  const request = new XMLHttpRequest()
  const URL = 'https://jsonplaceholder.typicode.com/todos/1/'
  
  request.open('GET', URL)
  request.send()
  
  const todo = request.response
  console.log('data: ${todo}')
  ```

## Asynchronous JavaScript

- 동기식

  - 순차적, 직렬적 task 수행
  - 요청 보낸 후 응답 받아야지 다음 동작 : blocking

  ![image-20211101170836364](C:\Users\j2woo\AppData\Roaming\Typora\typora-user-images\image-20211101170836364.png)

  ```html
  <button>버튼</button>
  
  <script>
  	const btn = document.querySelector('button')
     	
      btn.addEventListener('click', function() {
          alert('You clicked me!')
          const pElem = document.createElement('p')
          pElem.innerText = 'sample text'
          document.body.appendChild(pElem)
      })
  </script>
  ```

  - 버튼 클릭 후 alert 메세지 확인 버튼 누를때까지 문장 X
    - alert 이후 코드 : alert 처리 끝날 때까지 실행 X
    - `JavaScript는 single threaded`

  ![image-20211101212427252](C:\Users\j2woo\AppData\Roaming\Typora\typora-user-images\image-20211101212427252.png)

- 비동기식

  - 병렬적 Task 수행 : non-blocking

  ![image-20211101212722053](C:\Users\j2woo\AppData\Roaming\Typora\typora-user-images\image-20211101212722053.png)

  ```javascript
  const request = new XMLHttpRequest()
  const URL = 'https://jsonplaceholder.typicpde.com/todos/1/'
  
  request.open('GET', URL)
  request.send() // XMLHttpRequest 요청
  
  const todo = request.response // 빈 응답 값 todo에 할당
  console.log('data: ${todo}') // console.log 실행
  ```

  ![image-20211101215533400](C:\Users\j2woo\AppData\Roaming\Typora\typora-user-images\image-20211101215533400.png)

  - 요청 보내고 응답 기다리지 않고 다음 코드 실행
  - 변수 todo -> 응답 데이터 할당 X, 빈 데이터 출력
  - 기다리는 방식으로 동작
    - `JavaScript는 single threaded`

- `JavaScript는 single threaded`

  - 여러 개의 CPU가 있어도 main thread 단일 스레드에서만 작업 수행
  - 이벤트 처리 Call Stack이 하나
    - 즉시 처리하지 못하는 이벤트 -> Web API에서 처리
    - 처리된 이벤트 -> Task Queue에서 대기
    - Call Stack이 비면 Event Loop가 Task Queue에서 Call Stack으로 보냄

- Concurrency model : Event Loop 기반 동시성 모델

  - Call Stack
    - 요청 올때마다 해당 요청 순차 처리 LIFO 형태 자료 구조
  - Web API (Browser API)
    - `setTimeout()`, DOM events, AJAX -> 데이터를 가져오는 시간이 소요되는 일 처리
  - Task Queue (Event Queue, Message Queue)
    - 비동기된 callback 함수가 대기하는 FIFO 형태 자료 구조
    - main thread 종료 후 실행 -> 후속 JavaScript 코드 차단 방지
  - Event Loop
    - Call Stack 비어있는지 확인
    - 비어있을 때 Task Queue에서 대기 중인 callback 함수 있는지 확인
    - 있으면 가장 앞 callback 함수 Call Stack으로 push

### callback Function

- Callback function
  - 다른 함수에 인자로 전달된 함수
  - 외부 함수 내에서 호출 
  - 비동기 콜백 (asynchronous callback) : 비동기 작업 완료 후 코드 실행 계속 사용
- 일급 객체 (First Class Object)
  - 일급 객체 (함수)
    - 다른 객체 적용 가능한 연산 모두 지원
  - 조건
    - 인자로 넘길 수 있어야 함
    - 함수 반환 값으로 사용 가능
    - 변수 할당 가능
- Async callbacks
  - 백그라운드에서 코드 실행 시작 함수 호출 시 인자로 지정된 함수
  - 백그라운드 코드 실행 종료 -> callback 함수 호출 => 작업 완료 알리거나 다음 작업 실행
- Callback
  - 특정 루틴, action에 의해 호출
- Callback Hell
  - 여러 개 연쇄 비동기 작업
  - 디버깅, 코드 가독성 문제
  - 해결 : Promise callbacks

### Promise

- Promise object

  ```javascript
  const myPromise = axios.get(URL)
  // console.log(myPromise) // Promise Object
  
  myPromise
  	.then(response => {
      	return response.data
  })
  
  // chaining
  axios.get(URL)
  	.then(response => {
      	return response.data
  	})
  	.then(response => {
      	return response.title
  	})
  	.catch(error => {
      	console.log(error)
  	})
  	.finally(function () {
      	console.log('나는 마지막에 무조건 시행')
  	})
  ```

  - 비동기 작업 최종 완료, 실패 나타내는 객체
    - 미래 완료, 실패, 그 결과 값
    - 미래 상황 약속
  - 성공 : `.then()`, 실패 : `.catch()`

- Promise methods

  - `.then(callback)`
    - 이전 작업 (promise) 성공/이행 시 수행 작업
    - 각 callback -> 이전 작업 성공 결과 인자로 전달 받음
    - 성공 시 코드 -> callback 함수 안
    - 여러 개 사용 (chaining) -> 연쇄 작업 가능 => 여러 비동기 작업 차례 수행 가능
  - `catch(callback)`
    - `.then` 하나라도 실패/거부 시 동작 -> `try - except`와 유사
  - 반환 값 필수
  - `.finally(callback)`
    - promise 객체 반환
    - 결과 상관 없이 지정된 callback 함수 실행
    - 어떤 인자도 전달받지 X : 성공 여부 모름
    - 무조건 실행되어야 하는 절 : 코드 중복 방지

- 보장

  - callback 함수: Event Loop가 현재 실행 중인 Call Stack 완료 이전 호출 X
  - `.then()` 여러 번 사용 -> 여러 개 callback 함수 추가 가능 : Chaining

### Axios

```javascript
axios.get('http://jsonplaceholder.typicode.com/todos/1/') // Promise return
	.then(...)
    .catch(...)
```

```javascript
// XMLHttpRequest -> Axios 변경
// XMLHttpRequest
const request = new XMLHttpRequest()
const URL = 'https://jsonplaceholder.typicode.com/todos/1/'

request.open('GET', URL)
request.send()

const todo = request.response
console.log(todo)

// Axios
const URL = 'https://jsonplaceholder.typicode.com/todos/1/'

axios.get(URL)
	.then(response => {
    	console.log(response.data)
	})
```

```javascript
// Axios 예시

const URL = 'https://jsonplaceholder.typicode.com/todos/1/'

axios.get(URL)
	.then(function (response) {
    	console.log(response)
    	return response.data
	})
	.then(function (data) {
    	return data.title
	})
    .then(function (title) {
        console.log(title)
    })
	.catch(function (error) {
    	console.log(error)
	})
	.finally(function () {
    	console.log('나는 마지막에 무조건 시행')
	})
```

