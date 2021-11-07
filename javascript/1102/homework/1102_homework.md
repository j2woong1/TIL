## JavaScript 심화

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오

> - Event Loop는 Call Stack이 비워지면 Task Queue의 함수를 Call Stack으로 할당하는 역할을 한다
> - XMLHttpRequest (XHR)는 AJAX 요청 instance를 생성하는 JavaScript API이다. XHR의 메서드로 브라우저와 서버 간의 네트워크 요청을 전송할 수 있다
> - axios는 XHR(XMLHttpRequest)을 보내고 응답 결과를 Promise 객체로 반환해주는 라이브러리이다

- T
- T
- T



### 2. 아래의 코드가 실행되었을 때 Web API, Task Queue, Call Stack 그리고 Event Loop 에서 어떤 동작이 일어나는지 서술하시오

> ```javascript
> console.log('HELLO SSAFY!')
> 
> setTimeout(function () {
>     console.log('I am from setTimeout')
> }, 1000)
> 
> console.log('BYE SSAFT!')
> ```

1. `console.log('Hello SSAFY!')` 이 **Call Stack**에 push, `Hello SSAFY!`를 출력, pop -> **Call Stack** 빔
2. `setTimeout` **Web API**로 호출, **Call Stack**에서 push, 호출 완료 후 **pop**
3. `console.log('Bye SSAFY!')` 이 **Call Stack**에 push, `Bye SSAFY!` 출력 후 pop, **Web API**에서 setTimeout 1초 대기 중
4. **Web API** 작동 후 callback 함수(`function () { console.log('I am from setTimeout') }`)를 **Task Queue** 에 들어옴
5. **Event Loop**이 **Call Stack**이 비어있으면 **Task Queue**의 첫번째 요소를 **Call Stack**에 넣음
6. `console.log('I am from setTimeout')` 실행 후 pop



### 3. JS는 Event loop를 기반으로 하는 Concurrency model을 가지고 있다고 한다. Concurrency 키워드의 특징을 작성하고 이와 비슷한 키워드로 비교되는 Parallelism의 개념과 두 개념의 차이점을 서술하시오

- `Concurrency model` : Event Loop 기반 동시성 모델, 순서 보장 X
- `Parallelism` : 병렬처리 (Promise)
- `Promise` 콜백은 event queue에 배치되는 엄격한 순서로 호출
  - 각 콜백은 주어진 순서대로 하나씩 실행된다. (Chaining)