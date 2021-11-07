## 기초

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

  ![image-20211028091351384](C:\Users\j2woo\AppData\Roaming\Typora\typora-user-images\image-20211028091351384.png)

  - 해석

    - 파싱 (Parsing)
      - 구문 분/해석
      - 브라우저 : 문자열 해석 -> DOM Tree 제작 과정

  - 조작

    ![image-20211028091534729](C:\Users\j2woo\AppData\Roaming\Typora\typora-user-images\image-20211028091534729.png)

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

  ![image-20211028144204853](C:\Users\j2woo\AppData\Roaming\Typora\typora-user-images\image-20211028144204853.png)

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

  