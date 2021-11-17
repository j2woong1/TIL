- 기초

  ### Intro

  - 브라우저
    - 웹 서버에서 이동, 클라이언트 ~ 서버 양방향 통신
    - HTML 문서, 파일 출력 GUI 기반 SW
    - 인터넷 컨텐츠 검색, 열람
  - JavaScript 필요성
    - 브라우저 화면 동적
    - 브라우저 조작 유일 언어
  - 브라우저 기능
    - DOM 조작
      - 문서 (HTML) 조작
    - BOM 조작
      - navigator, screen, location, frames, history, XHR
    - JavaScript Core (ECMAScript)
      - Data Structure (Object, Array), Conditional Expression, Iteration

  ### DOM (Document Object Model)

  - DOM

    - HTML, XML 문서 다루는 문서 프로그래밍 인터페이스
    - 문서 구조화, 구조화된 구성 요소 -> 하나 객체로 취급 : 논리적 트리 모델
    - 각 요소 -> 객체 (object) 취급
    - 단순 속성 접근, 메서드 활용 + 프로그래밍 언어적 특성 활용
    - 주요 객체
      - window : DOM 표현 창, 최상위 객체, 작성 시 생략 가능
      - document : 페이지 컨텐츠 Entry Point
      - navigator, location, history, screen

    ![image-20211028091351384](C:\Users\j2woo\Desktop\ssafy6\TIL\img\image-20211028091351384.png)

    - 해석

      - 파싱 (Parsing)
        - 구문 분/해석
        - 브라우저 : 문자열 해석 -> DOM Tree 제작 과정

    - 조작

      ![image-20211028091534729](C:\Users\j2woo\Desktop\ssafy6\TIL\img\image-20211028091534729.png)

  - BOM

    - Browser Object Model
    - 자바스크립트 ~ 브라우저 소통 모델

  ### DOM 조작

  - 개념

    - 순서
      - 선택 (Select)
      - 변경 (Manipulation)

  - 상속 구조

    - EventTarget
      - Event Listener 가질 수 있는 객체가 구현한 DOM 인터페이스
    - Node
      - 여러 가지 DOM 타입들이 상속하는 인터페이스
    - Element
      - Document 안 모든 객체 상속 -> 가장 범용적 기반 클래스
      - 부모 Node, 그 부모 EventTarget 속성 상속
    - Document
      - 브라우저 불러온 웹 페이지
      - DOM 트리 진입점 (entry point)
    - HTMLElement
      - 모든 종류 HTML
      - 부모 element 속성 상속

  - 선택 

    - 메서드
      - `Document.querySelector(selector)`
        - 제공한 선택자와 일치하는 element 하나 선택
        - 제공한 CSS selector 만족 -> 첫 번째 element 객체 반환, 없으면 null
      - `Document.querySelectorAll(selector)`
        - 제공한 선택자와 일치하는 여러 element 선택
        - 매칭할 하나 이상의 selector 포함한 유효한 CSS selector 인자
        - 지정된 selector 일치한 NodeList 반환
    - 메서드별 반환 타입
      - 단일 element
        - `getElementById()`
        - `querySelector()`
      - HTMLCollection
        - `getElementsByTagName()`
        - `getElementsByClassName()`
      - NodeList
        - `querySelectorAll()`
    - HTMLCollection & NodeList
      - 항목 접근 index 제공 : 유사 배열
      - HTMLCollection
        - name, id, index 속성으로 각 항목 접근 가능
        - Live Collection -> DOM 변경사항 실시간 반영
      - NodeList
        - index로만 각 항목 접근 가능
        - 다양한 메서드 사용 가능
        - Live Collection -> DOM 변경사항 실시간 반영
        - `querySelectorAll()` -> Static Collection => 실시간 반영 X
    - Collection
      - Live Collection
        - 실시간 업데이트
      - Static Collection
        - `querySelectorAll()` 반환 NodeList

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>
            .ssafy-location {
                color: blue;
            }
        </style>
    </head>
    <body>
        <h1>Hello SSAFY</h1>
       	<h2 id="location-header">Location</h2>
        <div>
            <ul>
                <li class="ssafy-location">서울</li>
                <li class="ssafy-location">대전</li>
                <li class="ssafy-location">광주</li>
                <li class="ssafy-location">구미</li>
                <li class="ssafy-location">부울경</li>
            </ul>
        </div>
    </body>
    </html>
    ```

    ![image-20211028144204853](C:\Users\j2woo\Desktop\ssafy6\TIL\img\image-20211028144204853.png)

  - 변경

    - Creation
      - `Document.createElement()` : 작성한 태그 명 HTML 생성 반환

  ### Event

  - `~하면 ~한다`

  - handler

    - `addEventListener()`
      - `EventTarget.addEventListener()`
        - 지정 이벤트가 대상 전달될 때마다 호출 함수 설정
      - `target.addEventListener(type, listener[, options])`
        - type
          - 반응 이벤트 유형 : 대소문자 구분 문자열
        - listener
          - 지정 타입 이벤트 발생 시 알림 수신 객체
          - EvenListener 인터페이스, JS function 객체 (콜백 함수)
      - 대상에 특정 이벤트가 발생하면 할 일을 등록하자
        - `EventTarget.addEventListener(type, listener)`
        - `EventTarget` : 대상
        - `type` : 특정 이벤트
        - `listener` : 할 일

  - 취소

    - `Event.preventDefault()`
    - 현재 이벤트 기본 동작 중단

  - 실습

    ```html
    <form action="/todo/">
        <input type="text">
        <button>Add</button>
    </form>
    <ul>
        
    </ul>
    ```

    ```javascript
    // 이벤트 타겟 설정
    const form = document.querySelector('form')
    
    function addTodo (event) {
        // event 기본 동작 X
        event.preventDefault()
        
        // input 요소 선택, value 값 저장
        const input = document.querySelector('input')
        const content = input.value
        
        if (content.trim()) {
            // 새로운 li 요소 생성, input value -> innerText
            const li = document.createElement('li')
            li.innerText = content
            
            // ul 요소 선택, ul 자식 요소 -> li 요소
            const ul = document.querySelector('ul')
            ul.appendChild(li)
        } else {
            alert('할 일을 입력해주세요')
        }
        event.target.reset()
    }
    
    form.addEventListener('submit', addTodo)
    ```

    

## ECMAScript 6

### Introduction

#### ECMA

- 정보 통신 표준 제정 비영리 표준화 기구

#### 세미콜론

- 선택적 사용 가능

- ASI 자동 삽입

  ```javascript
  // 세미콜론 O
  const greeting = 'Hello world!';
  console.log(greeting)
  
  // 세미콜론 X
  const greeting = 'Hello world!'
  console.log(greeting)
  ```



### 변수와 식별자

- 식별자 정의, 특징

  - 문자, `$`, `_`로 시작
  - 대소문자 구분, 클래스명 외 모두 소문자 시작
  - 예약어 사용 X (for, if, case)

- 작성 스타일

  - 카멜 케이스 (camelCase, lower-camel-case) : 변수, 객체, 함수

    ```javascript
    // 변수
    let dog
    let variableName
    
    // 객체
    const userInfo = { name: 'juan', age: 27 }
    
    // 함수
    function getPropertyName () {}
    function onClick () {}
    ```

  - 파스칼 케이스 (PascalCase, upper-camel-case) : 클래스, 생성자

    ```javascript
    // 클래스
    class User {
        constructor(options) {
            this.name = options.name
        }
    }
    
    // 생성자
    const good = new User ({
        name: '홍길동',
    })
    ```

  - 대문자 스네이크 케이스 (SNAKE_CASE) : 상수

    ```javascript
    // 상수
    const API_KEY = 'SOMEKEY'
    const PI = Math,PI
    
    // 상수 X
    const mutableCollection = new Set()
    ```

- 변수 선언 키워드

  |         const         |          let          |
  | :-------------------: | :-------------------: |
  | 재할당 X 변수 선언 시 | 재할당 O 변수 선언 시 |
  |       재선언 X        |       재선언 X        |
  |      블록 스코프      |      블록 스코프      |

  ```javascript
  let foo // 선언 (Declartion) : 변수 생성
  console.log(foo)  // undefined
  
  foo = 11  // 할당 (Assignment) : 선언 변수에 값 저장
  console.log(foo)  // 11
  
  let bar = 0  // 선언 + 할당
  console.log(bar) // 0
  
  // 초기회 (Initialization) : 선언 변수에 처음으로 값 저장
  ```

  ```javascript
  // let : 재할당 O
  let number = 10  // 1. 선언, 초기화 할당
  number = 10  // 2. 재할당
  
  console.log(number)  // 10
  
  // const : 재할당 X
  const number = 10  // 1. 선언, 초기화 할당
  number = 10  // 2. 재할당 불가능
  
  // Uncaught TypeError
  // : Assignment to constant variable
  ```

  ```javascript
  // let : 재선언 X
  let number = 10  // 1. 선언, 초기화 할당
  let number = 50  // 2. 재선언 X
  
  // Uncaught SyntaxError
  // : Identifier 'number' has already been declared
  
  // const : 재선언 X
  const number = 10  // 1. 선언, 초기화 할당
  const number = 50  // 2. 재선언 X
  
  // Uncaught SyntaxError
  // : Identifier 'number' has already been declared
  ```

  ```javascript
  let x = 1
  
  if (x === 1 ) {
      let x = 2  // 블록 스코프 (block scope) : 블록 바깥에서 접근 X
      console.log(x)  // 2
  }
  
  console.log(x)  // 1
  ```

  - var

    - 재선언, 재할당 O
    - 함수 스코프

    ```javascript
    var number = 10  // 1. 선언, 초기화 할당
    var number = 50  // 2. 재할당
    
    console.log(number) // 50
    ```

    ```javascript
    fuction foo() {
        var x = 5  // 함수 스코프 (function scope) : 함수 바깥에서 접근 X
        console.log(x)  // 5
    }
    
    // ReferenceError : x is not defined
    console.log(x)
    ```

    ```javascript
    console.log(username)  // undefined
    var username = '홍길동'
    
    console.log(email)  // Uncaught ReferenceError
    let email = 'gildong@gmail.com'
    
    console.log(age)  // Uncaught ReferenceError
    const age = 50
    
    // 호이스팅 (hoisting) : 변수 선언 이전 참조, 변수 선언 이전 위치에서 접근 시 undefined 반환
    ```



### 타입과 연산자

#### 데이터 타입

- 종류

  - 원시 타입 (Primitive Type)

    - 객체 (object) X 기본 타입
    - 변수 <- 해당 타입 값
    - 다른 변수 복사 시 실제 값 복사

    ```javascript
    const message = ['안녕하세요']  // 1. message 선언, 할당
    
    const greeting = message  // 2. greeting에 message 복사
    console.log(greeting)  // 3. '안녕하세요' 출력
    
    message[0] = 'Hello world!'  // 4. message 재할당
    console.log(greeting)  // 5. '안녕하세요' 출력
    
    // 해당 타입 값 저장
    ```

    - 숫자 타입 (Number)

      - 정/실수 구분 X
      - 보동소수점

      ```javascript
      const a = 13  // 양의 정수
      const b = -5  // 음의 정수
      const c = 3.14  // 실수
      const d = 2.998e8  // 거듭제곱
      const e = Infinity  // 양의 무한대
      const f = -Infinity  // 음의 무한대
      const g = NaN  // 산술 연산 불가
      ```

    - 문자열 타입 (String)

      - 텍스트 데이터
      - 유니코드 문자 집합
      - `''`, `""` 모두 가능
      - 템플릿 리터럴 (Template Literal)
        - ES6부터
        - 따옴표 대신 ``로 표현
        - `${ expression }` 형태로 표현식 삽입 가능

      ```javascript
      const firstName = 'Brandan'
      const lastName = 'Eich'
      const fullName = '${firstName} ${lastName}'
      
      console.log(fullName)  // Brandon Eich
      ```

    - undefined

      - 값 X
      - 직접 할당 X -> 자동 할당

      ```javascript
      let firstName
      console.log(firstName)  // undefined
      
      typeof undefined // undefined
      ```

    - null

      - 값 X 의도적 표현
      - typeof 연산자
        - 자료형 평가
        - 객체로 표현

      ```javascript
      let firstName = null
      console.log(firstName) // null
      
      typeof null // object
      ```

      |           undefined           |       null       |
      | :---------------------------: | :--------------: |
      |             빈 값             |      빈 값       |
      | 아무 것도 할당 X -> 자동 할당 | 의도적으로 필요  |
      |      typeof -> undefined      | typeof -> object |

      - Boolean

        - 논리적 참, 거짓
        - 조건, 반복문

        ```javascript
        let isAdmin = true
        console.log(isAdmin)  // true
        
        isAdmin = false
        console.log(isAdmin)  // false
        ```

        | 데이터 타입 |    거짓    |        참        |
        | :---------: | :--------: | :--------------: |
        |  Undefined  | 항상 거짓  |        X         |
        |    Null     | 항상 거짓  |        X         |
        |   Number    | 0, -0, NaN | 나머지 모든 경우 |
        |   String    | 빈 문자열  | 나머지 모든 경우 |
        |   Object    |     X      |     항상 참      |

  - 참조 타입 (Reference Type)

    - 객체 타입 자료형
    - 변수 <- 해당 객체 참조 값
    - 다른 변수 복사 시 참조 값 복사

    ```javascript
    const message = ['안녕하세요']  // 1. message 선언, 할당
    
    const greeting = message  // 2. greeting에 message 복사
    console.log(greeting)  // 3. ['안녕하세요'] 출력
    
    message[0] = 'Hello world!'  // 4. message 재할당
    console.log(greeting)  // 5. ['Hello world!'] 출력
    
    // 해당 객체 참조할 수 있는 참조 값 저장
    ```

    - 함수 (Functions), 배열 (Arrays), 객체 (Objects)

  ![image-20211101132932537](C:\Users\j2woo\AppData\Roaming\Typora\typora-user-images\image-20211101132932537.png)

#### 연산자

- 할당

  ```javascript
  let x = 0
  
  x += 10
  console.log(x) // 10
  
  x -= 3
  console.log(x) // 7
  
  x *= 10
  console.log(x) // 70
  
  x /= 10
  console.log(x) // 7
  
  x++
  console.log(x) // 8
  
  x--
  console.log(x) // 7
  ```

- 비교

  ```javascript
  const numOne = 1
  const numTwo = 100
  concole.log(numOne < numTwo) // true
  
  const charOne = 'a'
  const charTwo = 'z'
  console.log(charOne > charTwo) // false
  ```

- 동등 비교 `==`

  ```javascript
  const a = 1004
  const b = '1004'
  console.log(a == b) // true
  
  const c = 1
  const d = true
  console.log(c == d) // true
  
  // 자동 타입 변환
  console.log(a + b) // 10041004
  console.log(c + d) // 2
  ```

- 일치 비교 `===`

  ```javascript
  const a = 1004
  const b = '1004'
  console.log(a == b) // false
  
  const c = 1
  const d = true
  console.log(c == d) // false
  ```

- 논리

  ```javascript
  // and
  console.log(true && false) // false
  console.log(true && true) // true
  console.log(1 && 0) // 0
  console.log(4 && 7) // 7
  console.log('' && 5) // ''
  
  // or
  console.log(true || false) // true
  console.log(false || false) // false
  console.log(1 || 0) // 1
  console.log(4 || 7) // 4
  console.log('' || 5) // 5
  
  // not
  console.log(!true) // false
  console.log(!'Bonjour!') // false
  ```

- 삼항 (Trenary)

  - 가장 왼쪽 조건식
    - 참 -> : 앞
    - 거짓 -> : 뒤

  ```javascript
  console.log(true ? 1 : 2) // 1
  console.log(false ? 1 : 2) // 2
  
  const result = Math.PI > 4 ? 'Yes' : 'No'
  console.log(result) // None
  ```



### 조건문과 반복문

#### 조건문

- if statement

  - boolean 타입 변환 -> 참, 거짓 판단

  ```javascript
  if (condition) {
      // do something
  } else if (condition) {
      // do something
  } else {
      // do something
  }
  
  const nation = 'Korea'
  
  if (nation === 'Korea') {
      console.log('안녕하세요!')
  } else if (nation === 'France') {
     	console.log('Bonjour!')
  } else {
      console.log('Hello!')
  }
  ```

- switch statement

  - 어느 값 해당하는지 판별 (case)

  ```javascript
  switch(expression) {
      case 'first value': {
          // do something
          [break]
      }
      case 'second value': {
          // do something
          [break]
      }
      [default: {
       	// do something
       }]
  }
  
  // break O
  const nation = 'Korea'
  
  switch(nation) {
      case 'Korea': {
          console.log('안녕하세요!')
          [break]
      }
      case 'France': {
          console.log('Bonjour!')
          [break]
      }
      [default: {
       	console.log('Hello!')
       }]
  }
  
  // break X
  const nation = 'Korea'
  
  switch(nation) {
      case 'Korea': {
          console.log('안녕하세요!')
      }
      case 'France': {
          console.log('Bonjour!')
      }
      [default: {
       	console.log('Hello!')
       }]
  }
  ```

  ```javascript
  const numOne = 5
  const numTwo = 10
  let operator = '+'
  
  // if
  
  if (operator == '+') {
      console.log(numOne + numTwo)
  } else if (operator == '-') {
      console.log(numOne - numTwo)
  } else if (operator == '*') {
      console.log(numOne * numTwo)
  } else if (operator == '/') {
      console.log(numOne / numTwo)
  } else {
      console.log('유효하지 않은 연산자 입니다.')
  }
  
  // swtich
  
  switch(operator) {
      case '+': {
          console.log(numOne + numTwo)
          break
      }
      case '-': {
          console.log(numOne - numTwo)
          break
      }
      case '*': {
          console.log(numOne * numTwo)
          break
      }
      case '/': {
          console.log(numOne / numTwo)
          break
      }
      default: {
          console.log('유효하지 않은 연산자 입니다.')
      }
  }
  ```

#### 반복문

- while

  ```javascript
  while (condition) {
      // do something
  }
  
  let i = 0
  
  while (i < 6) {
      console.log(i) // 0, 1, 2, 3, 4, 5
      i += 1
  }
  ```

- for

  ```javascript
  for (initialization; condition; expression) {  // initialization : 최초 진입 시 1회, condition : 반복 전, expression : 반복 시행 이후
      // do something
  }
  
  for (let i = 0; i < 6; i++) {
      // 1. 반복문 진입, 변수 i 선언
      // 2. 조건문 평가 후 코드 블럭 실행
      // 3. 코드 블럭 실행 이후 i 값 증가
      console.log(i) // 0, 1, 2, 3, 4, 5
  }
  ```

- for...in

  - 객체 (object) 속성 순회

  ```javascript
  for (variable in object) {
      // do something
  }
  
  const = capitals = {
      Korea: '서울',
      France: '파리',
      USA: '워싱턴 D.C.'
  }
  
  for (let capital in capitals) {
      console.log(capital) // Korea, France, USA
  }
  ```

- for...of

  - 반복 가능한 (iterable) 객체 순회
  - array, map, set, string

  ```javascript
  for (variable of iterables) {
      // do something
  }
  
  const fruits = ['딸기', '바나나', '메론']
  
  for (let fruit of fruits) {
      console.log(fruit) // 딸기, 바나나, 메론
  }
  ```



### 함수

#### 활용법

- 정의 방법

  - 선언식 (declaration)

    - 이름 (name), 매개변수 (args), 몸통 (중괄호 내부)

    ```javascript
    function name(args) {
        // do something
    }
    
    function add(numOne, numTwo) {
        return numOne + numTwo
    }
    
    const result = add(1, 2)
    console.log(result) // 3
    ```

  - 표현식 (expression)

    - 이름 생략 후 익명 함수 정의 가능
    - 이름 (생략 가능), 매개변수 (args), 몸통 (중괄호 내부)

    ```javascript
    const myFunction = function (args) {
        // do something
    }
    
    const add = function (numOne, numTwo) {
        return numOne + numTwo
    }
    
    const result = add(1, 2)
    console.log(result) // 3
    ```

    - 기본인자

      - `=` 뒤 선언 가능

      ```javascript
      const greeting = function (name = 'noName') {
          console.log('hi ${name}')
      }
      
      greeting() // hi noName
      ```

- 선언식 vs 표현식

  |        |                       선언식                       |                       표현식                       |
  | :----: | :------------------------------------------------: | :------------------------------------------------: |
  | 공통점 | 데이터 타입, 함수 구성 요소 (이름, 매개변수, 몸통) | 데이터 타입, 함수 구성 요소 (이름, 매개변수, 몸통) |
  | 차이점 |              익명 함수 X, 호이스팅 O               |              익명 함수 O, 호이스팅 X               |

  - 타입

    ```javascript
    // 선언식
    function sub(args) {}
    
    // 표현식
    const add = function (args) {}
    
    const.log(typeof sub) // function
    const.log(typeof add) // function
    ```

  - 호이스팅

    - var로 정의한 변수처럼
    - 함수 호출 이후에 선언해도 동작

    ```javascript
    // 선언식
    sub(2, 7) // 9
    
    function sub (num1, num2) {
        return num1 + num2
    }
    
    // 표현식
    add(7, 2) // Uncaught ReferenceError : Cannot access 'sub' before initialization
    
    const add = function(num1, num2) {
        return num1 + num2
    }
    
    console.log(add)
    add(7, 2) // Uncaught TypeError: sub is not a function
    
    var sub = function (num1, num2) {
        return num1 - num2
    }
    ```

#### Arrow Function

- 화살표 함수

  - function 키워드 생략 O
  - 매개변수 하나 -> `( )` 생략 O
  - 몸통 표현식 하나 -> `{ }`, `return` 생략 O

  ```javascript
  const arrow = function (name) {
      return 'hello! ${name}'
  }
  
  // 1. function 키워드 삭제
  const arrow = (name) => { return 'hello! ${name}' }
  
  // 2. () 생략 : 매개변수 하나
  const arrow = name => { return 'hello! ${name}' }
  
  // 3. {}, return 생략 => 몸통 표현식 1개
  const arrow = name => 'hello! ${name}'
  ```



### 배열과 객체

#### 배열 (Arrays)

- 정의, 특징

  - 키, 속성 참조 타입 객체
  - 순서 보장
  - 0 포함 양의 정수 인덱스
  - 길이 : `array.length`

  ```javascript
  const numbers = [1, 2, 3, 4, 5]
  
  console.log(numbers[0]) // 1
  console.log(numbers[-1]) // undefined 
  console.log(numbers.length) // 5
  
  console.log(numbers[numbers.length - 1]) // 5
  console.log(numbers[numbers.length - 2]) // 4
  console.log(numbers[numbers.length - 3]) // 3
  console.log(numbers[numbers.length - 4]) // 2
  console.log(numbers[numbers.length - 5]) // 1
  ```

- 주요 메서드 기본

  |     메서드      |                  설명                  |         비고          |
  | :-------------: | :------------------------------------: | :-------------------: |
  |     reverse     |    원본 배열 요소 순서 반대로 정렬     |                       |
  |   push & pop    |      배열 가장 뒤 요소 추가, 제거      |                       |
  | unshift & shift |      배열 가장 앞 요소 추가, 제거      |                       |
  |    includes     | 배열 특정 값 존재 판별 후 참/거짓 반환 |                       |
  |     indexOf     | 배열 특정 값 존재 판별 후 인덱스 반환  |       없으면 -1       |
  |      join       |      배열 모든 요소 구분자로 연결      | 구분자 생략 시 , 기준 |

  - reverse

    ```javascript
    const numbers = [1, 2, 3, 4, 5]
    
    numbers.reverse()
    console.log(numbers) // [5, 4, 3, 2, 1]
    ```

  - push & pop

    ```javascript
    const numbers = [1, 2, 3, 4, 5]
    
    numbers.push(100)
    console.log(numbers) // [1, 2, 3, 4, 5, 100]
    
    numbers.pop()
    console.log(numbers) // [1, 2, 3, 4, 5]
    ```

  - unshift & shift

    ```javascript
    const numbers = [1, 2, 3, 4, 5]
    
    numbers.unshift(100)
    console.log(numbers) // [100, 1, 2, 3, 4, 5]
    
    numbers.shift()
    console.log(numbers) // [1, 2, 3, 4, 5]
    ```

  - includes

    ```javascript
    const numbers = [1, 2, 3, 4, 5]
    
    console.log(numbers.includes(1)) // true
    console.log(numbers.includes(100)) // false
    ```

  - indexOf

    ```javascript
    const numbers = [1, 2, 3, 4, 5]
    let result
    
    result = numbers.indexOf(3) // 2
    console.log(result)
    
    result = numbers.indexOf(100) // -1
    console.log(result)
    ```

  - join

    ```javascript
    const numbers = [1, 2, 3, 4, 5]
    let result
    
    result = numbers.join() // 1,2,3,4,5
    console.log(result)
    
    result = numbers.join('') // 12345
    console.log(result)
    
    result = numbers.join(' ') // 1 2 3 4 5
    console.log(result)
    
    result = numbers.join('-') // 1-2-3-4-5
    console.log(result)
    ```

- 주요 메서드 심화

  - 배열 순회

  - 메서드 호출 시 인자로 callback 함수 : 어던 함수 내부에서 실행 목적으로 인자 넘겨받는 함수

    | 메서드  |                       설명                       |   비고    |
    | :-----: | :----------------------------------------------: | :-------: |
    | forEach |       배열 각 요소에 콜백 함수 1번씩 실행        | 반환 값 X |
    |   map   |     콜백 함수 반환 값 요소 새로운 배열 반환      |           |
    | filter  |   콜백 함수 반환 값 참 요소만 새로운 배열 반환   |           |
    | reduce  | 콜백 함수 반환 값 하나의 값 (acc)에 누적 후 반환 |           |
    |  find   |     콜백 함수 반환 값 참이면 해당 요소 반환      |           |
    |  some   | 배열 요소 중 하나라도 판별 함수 통과 시 참 반환  |           |
    |  every  |     배열 모든 요소 판별 함수 통과 시 참 반환     |           |

    - foreach

      ```javascript
      array.forEach((element, index, array) => {
          // do something
      })
      
      const ssafy = ['광주', '대전', '구미', '서울']
      
      ssafy.forEach((region, index) => {
          console.log(region, index)
          // 광주 0
          // 대전 1
          // 구미 2
          // 서울 3
      })
      ```

    - map

      ```javascript
      array.map((element, index, array) => {
          // do something
      })
      
      const numbers = [1, 2, 3, 4, 5]
      
      const doubleNums = numbers.map((num) => {
          return num * 2
      })
      
      console.log(doubleNums) // [2, 4, 6, 8, 10]
      ```

    - filter

      ```javascript
      array.filter((element, index, array) => {
          // do something
      })
      
      const numbers = [1, 2, 3, 4, 5]
      
      const oddNums = numbers.filter((num, index) => {
          return num % 2
      })
      
      console.log(oddNums) // 1, 3, 5
      ```

    - reduce

      ```javascript
      array.reduce((acc, element, index, array) => { // acc : 이전 callback 함수 반환 값 누적 변수
          // do something
      }, initialValue) // 최소 callback 함수 호출 시 acc 할당 값, default 값 : 배열 첫번째 값
      
      const numbers = [1, 2, 3]
      
      const result = numbers.reduce((acc, num) => {
          return acc + num
      }, 0)
      
      console.log(result) // 6
      ```

    - find

      ```javascript
      arrays.find((element, index, array) => {
          // do something
      })
      
      const avengers = [
          { name: 'Tony Stark', age: 45 },
          { name: 'Steve Rogers', age: 32 },
          { name: 'Thor', age: 44 },
      ]
      
      const result = avengers.find((avenger) => {
          return avenger.name === 'Tony Stark'
      })
      
      console.log(result) // {name: "Tony Stark", age: 45}
      ```

    - some

      ```javascript
      array.some((element, index, array) => {
          // do something
      })
      
      const numbers = [1, 3, 5, 7, 9]
      
      const hasEvenNumber = numbers.some((num) => {
          return num % 2 === 0
      })
      console.log(hasEvenNumber) // false
      
      const hasOddNumber = numbers.some((num) => {
          return num % 2
      })
      console.log(hasOddNumber) // true
      ```

    - every

      ```javascript
      array.every((element, index, array) => {
          // do something
      })
      
      const numbers = [2, 4, 6, 8 ,10]
      
      const isEveryNumberEven = numbers.every((num) => {
          return num % 2 === 0
      })
      console.log(isEveryNumberEven) // true
      
      const isEveryNumberOdd = numbers.every((num) => {
          return num % 2 === 0
      })
      console.log(isEveryNumberOdd) // false
      ```

#### 객체 (Objects)

- 정의, 특징

  - 속성 (property) 집합, 중괄호 내부 key, value 쌍
  - key : 문자열 타입만 가능, 띄어쓰기 -> 따옴표 묶어서
  - value : 모든 타입 가능
  - 객체 요소 접근 : `.`, `""` - 띄어쓰기 구분자 -> 대괄호 접근만

  ```javascript
  const me = {
      name: '홍길동', // key 한 단어
      'phone number': '01012345678', // key 여러 단어
      samsungProducts: {
      	buds: 'Galaxy Buds Pro',
      	galaxy: 'Galaxy s21'
  	},
  }
  
  console.log(me.name) // 홍길동
  console.log(me['phone number']) // 01012345678
  console.log(me.samsungProducts) // {buds: "Galaxy Buds Pro", ...}
  console.log(me.samsungProducts.buds) // Galaxy Buds Pro
  ```

- ES6 문법

  - 속성명 축약 (shorthand) : key, 할당 변수 이름 같으면

    ```javascript
    let books = ['Learning JS', 'Eloquent JS']
    let magazines = null
    
    var bookShop = {
        books, // books: books,
        magazines, // magazines: magazines,
    }
    console.log(bookshop.books) // ['Learning JS', 'Eloquent JS']
    ```

  - 메서드명 축약 (shorthand) : 메서드 선언 시 function 키워드 생략

    ```javascript
    const newObj = {
        greeting() { // gretting: function ()
            console.log('Hi!')
        }
    };
    
    newObj.greeting() // Hi!
    ```

  - 계산된 속성 (computed property name) : key 이름 표현식으로 동적 생성

    ```javascript
    const key = 'regions'
    const value = ['광주', '대전', '구미', '서울']
    
    const ssafy = {
        [key]: value,
    }
    
    console.log(ssafy) // { regions: Array(4) }
    console.log(ssafy.regions) // ["광주", "대전", "구미", "서울"]
    ```

  - 구조 분해 할당 (destructing assignment) : 배열, 객체 분해 -> 속성 변수에 쉽게 할당

    ```javascript
    const userInformation = {
        name: 'ssafy kim',
        userId: 'ssafyStudent1234',
        phoneNumber: '010-1234-1234',
        email: 'ssafy@ssafy.com'
    }
    
    const { name } = userInformation
    const { userId } = userInformation
    const { phoneNumber } = userInformation
    const { email } = userInformation
    
    const { name, userId } = userInformation
    ```

- JSON (JavaScript Object Notation)

  - key-value 쌍 형태
  - 문자열 타입 -> 구문 분석 (parsing) 필수
  - `JSON.parse()` : JSON -> 자바스크립트 객체
  - `JSON.stringify()` : 자바스크립트 객체 -> JSON

  ```javascript
  // Object -> JSON
  const jsonData = JSON.stringify({
      coffee: 'Americano',
      iceCream: 'Cookie and cream',
  })
  
  console.log(jsonData) // "{"coffee":"Americano",...
  console.log(typeof jsonData) // string
  ```

  ```json
  // JSON -> Object
  
  const jsonData = JSON.stringify({
      coffee: 'Americano',
      iceCream: 'Cookie and cream',
  })
  
  const parsedData = JSON.parse(jsonData)
  
  console.log(parsedData) // {cofee: "Americano", ...}
  console.log(typeof parsedData) // object
  ```

  

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

  ![image-20211101170836364](C:\Users\j2woo\Desktop\ssafy6\TIL\img\image-20211101170836364.png)

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

  ![image-20211101212427252](C:\Users\j2woo\Desktop\ssafy6\TIL\img\image-20211101212427252.png)

- 비동기식

  - 병렬적 Task 수행 : non-blocking

  ![image-20211101212722053](C:\Users\j2woo\Desktop\ssafy6\TIL\img\image-20211101212722053.png)

  ```javascript
  const request = new XMLHttpRequest()
  const URL = 'https://jsonplaceholder.typicpde.com/todos/1/'
  
  request.open('GET', URL)
  request.send() // XMLHttpRequest 요청
  
  const todo = request.response // 빈 응답 값 todo에 할당
  console.log('data: ${todo}') // console.log 실행
  ```

  ![image-20211101215533400](C:\Users\j2woo\Desktop\ssafy6\TIL\img\image-20211101215533400.png)

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

