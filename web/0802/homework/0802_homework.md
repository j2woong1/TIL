# 1. HTML 정의

(3) Hyper Text Markup Language



# 2. HTML 개념

- 웹 표준을 만드는 곳은 Mozilla 재단이다.

  - F : Apple, Google, Microsoft, Mozilla 모임

- 표(table) 을 만들 때에는 반드시 <th> 태그를 사용해야 한다.

  - F : <table>

  - | <table> | 테이블        |
    | ------- | ------------- |
    | <th>    | 테이블 - 헤더 |
    | <tr>    | 테이블 - 행   |
    | <td>    | 테이블 - 열   |

- 제목(Heading) 태그는 제목 이외에는 사용하지 않는 것이 좋다.

  - T

- 리스트를 나열하기 위해서는 <ul> 태그만 사용 할 수 있다.

  - F

  - | <ul> | 순서 필요 X             |
    | ---- | ----------------------- |
    | <ol> | 순서 O                  |
    | <dl> | 사전처럼 용어 설명      |
    | <li> | <ol>과 <ul>의 항목 나열 |

- HTML의 태그는 반드시 별도의 닫는 태그가 필요하다.

  - F : input, meta, img, link, etc - 닫는 태그 X



# 3. CSS 정의

(2) : Cascading Style Sheets



# 4. CSS 개념

- HTML과 CSS는 각자 문법을 갖는 별개의 언어이다.
  - T : HTML : Markup Language / CSS : Style Sheet Language -> 다른 언어지만 CSS 혼자서는 의미 X
- 웹 브라우저는 내장 기본 스타일이 있어 CSS가 없어도 작동한다.
  - T
- 자식 요소 프로퍼티는 부모의 프로퍼티를 모두 상속 받는다.
  - F : box model 관련 요소 상속 X, text 관련 요소 상속 O
- 디바이스마다 화면의 크기가 다른 것을 고려하여 상대 단위인 %를 사용한다.
  - F : viewport
- id 값은 유일해야 하므로 중복되어서는 안된다.
  - T -> 중복이면 class 이용



# 5. CSS 우선 순위

- !important
- Inline Style
- id 선택자
- class 선택자
- 요소 선택자
- 소스 순서