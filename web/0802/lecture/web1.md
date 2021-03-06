# Web

- WHATWG : Apple, Google, Microsoft, Mozilla (브라우저)

# HTML 

## Hyper Text Markup Language

- Hyper : 정보가 다중으로 연결
- Hyper Text : 참조(하이퍼링크)를 통해 한 문서에서 다른 문서로 즉시 접근 가능한 텍스트 (비선형적 텍스트)
- Markup 
- Language : 태그를 이용하여 데이터 구조 명시 -> HTML, Markdown

**웹 컨텐츠의 의미와 구조 정의**

# HTML 기본 구조

```html
<!DOCTYPE html>
<html lang="ko">
<head> <!-- 문서 정보, 브라우저에서 보이지 X, CSS 선언, 외부 로딩 파일 지정 -->
    <meta charset="UTF-8"
    <title>Document</title>
</head>
<body> <!-- 브라우저에 보임, 실제 내용 -->
    
</body>
</html>
```

- HTML 요소 : 최상위 요소, 문서 root -> head, body

## Open Graph Protocol

- HTML 문서 메타 데이터를 통해 정보 전달
- 페이스북 제작, 제목, 설명

## DOM(Document Object Model) 트리

- 구조화된 표현 (Structured Representation) 제공, 언어가 DOM 구조에 접근 방법 제공 -> 문서 구조, 스타일 내용 변경
- 동일한 문서 표현, 저장, 조작 방법 제공
- Web Page의 객체 지향 제공

## 요소 (Element)

```html
<h1>contents</h1> <!-- 여는/시작 태그, 닫는/종료 태그 -->
```

- 태그와 내용
- 태그 : 내용을 감싸는 것, 정보 성격과 의미 정의
- 내용 X 태그 : br, hr, img, input, link, meta
- 중첩 가능 : 오류 반환 X, 레이아웃이 깨진 상태로 출력 -> 디버깅 힘듦

## 속성 (Attribute)

```html
< a href="https://google.com"></a> <!-- 속성명="속성값", 공백 X, "" -->
```

- 태그 부가적인 정보 설정 -> 경로, 크기
- 요소 시작 태그에 작성, 이름과 값이 한 개의 쌍
- 태그와 상관 없이 사용 가능한 속성 (HTML Global Attribute)
  - id, class / hidden / lang / style / tabindex / title

https://developer.mozilla.org/ko/docs/Web/HTML

```html
<!DOCTYPE html> <!-- 이 문서가 HTML 5다 -->
<html>
    
<head>
    <meta charset="UTF-8">
    <title>타이틀입니다.</title>
</head>
    
<body>
    <h1>나의 첫번째 HTML</h1>
    <a href="https://google.com">구글로 고고!</a> <!-- 하이퍼링크 -->
</body>
    
</html>
```

## 시맨틱 태그

- non semantic : div, span
- header (머릿말), nav (내비게이션), aside (사이드, 메인과 관련성 적은), section (일반적인 구분, 컨텐츠 그룹 표현), article (독립적으로 구분되는 영역), footer (마지막 부분)
- '의미' -> 가독성, 유지 보수

## 시맨틱 웹

- 메타데이터 부여
- 데이터 집합인 웹페이지를 의미와 관련성을 가지는 DB로 구축

# HTML 문서 구조화

## 인라인/블록

- 인라인 : span
- 블록 : div

## 그룹

- p
- hr
- ol, ul
- pre, blackquote
- div

## 텍스트

- a
- b : 표현 상 굵게, strong : 강조
- i, em (웹 접근성)
- span, br (new line), img

## 테이블

## Form

- 서버에서 처리될 데이터 제공 : 
- action : 어디로
- method 

## Input

- 입력 데이터 
- label : 캡션
- name, placeholder
- required
- autofocus

https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input



**HTML : 구조**

**CSS : 표현** 

**JavaScript : 동작, 기능 (행동)**



https://www.advancedwebranking.com/html/

# CSS

**CSS : Cascading Style Sheet**

스타일, 레이아웃을 통해 문서 표시 방법 지정

```css
h1 { /* 선택자 */
    color: blue /* 속성(property): 값(value) */
    font-size: 15px
}
```

## 선택자 (Selector)

- 범위가 좁은게 우선 순위 높음 : 모든 태그 -> 태그 -> 클래스 -> ID (같은 강도면 아래가 높음)
- 요소 : 직접 선택
- 클래스 : 마침표
- id : #

```css
<style>
    * { /* 전체 선택자 */
        color: red;
    }
    
    h2 { /* 요소 선택자 */
        color: orange;
    }
    
    h3, h4 {
        font-size: 10px;
    }
    
    .green { /* 클래스 선택자 */
        color: green;
    }
    
    #purple { /* id 선택자 */
        color: purple
    }
    
    .box > p { /* 자식 결합자 */
        font-size: 30px;
    }
    
    .box p { /* 자손 결합자 */
        color: blue;
    }
</style>
```

### 우선순위

- 중요도 : !important
- 우선순위 : inline > id 선택자 > class 선택자 > 요소 선택자
- 소스 순서

### 기본

- 전체, 요소
- 클래스, 아이디, 속성

### 결합자 (Combiantors)

- 자손 : 하위 모든 요소
- 자식 : 바로 아래 요소

```css
div span { /* 자손 결합자 */
	color: red;
}

div > span { /* 자식 결합자 */
    color: red;
}
```

- 일반 형제 : 형제 요소 중 뒤 모든 요소
- 인접 형제 : 형제 요소 중 바로 뒤 요소

```css
p ~ span { /* 일반 형제 결합자 */
    color: red;
}

p + span { /* 인접 형제 결합자 */
    color: red;
}
```

### 의사 클래스/요소 (pseudo class)

- 링크, 동적
- 구조적

### 결합자



## CSS 단위

### 크기

- px
- % : 가변적인 레이아웃
- em : 상속 영향, 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈
- rem : 상속 영향 X, 최상위 요소(html) 사이즈 기준 배수 단위
- viewport : 상대적인 사이즈 -> vw, vh, vmin, vmax

### 색상

- 색상 키워드
- RGB : 16진수 (# + 16진수) or 함수형 (rgb 함수형)
- HSL : 색상, 채도, 명도
- *a : alpha (투명도) 추가

## CSS Box Model

![image-20210804110722589](web1.assets/image-20210804110722589.png)

- box-sizing : content-box
  - padding 제외 순수한 contents 영역
- border-box로 설정

![image-20210804144701401](web1.assets/image-20210804144701401.png)

- 마진 상쇄 : block A top, block B bottom margin이 큰 margin value로 결합(겹침)

## CSS Display

### Display : Block

- 줄 바꿈
- 화면 크기 전체 가로 폭
- Block 안 Inline 가능

### Display : Inline

- 줄 바꿈 X
- Content 너비만큼 가로 폭
- width, height, margin-top, margin-bottom 지정 X
- 상하 여백 : line-height

### Display : Inline-Block

- block, inline 모두
- inline처럼 한 줄에 표시 가능
- block처럼 width, height, margin 모두 지정 O

### Display : None

- 화면에 표시 X, 공간 X
- hidden : 공간 O, 표시 O

## CSS Position

- static : 기본 값 (기준 위치)
- relative
  - 자기 자신 static 위치 기준
  - 차지 공간 : static과 same
- absolute
  - 공간 차지 X
  - 가장 가까이 있는 부모 요소 기준 이동
  - 과거 위치 공간 : 존재 X -> 독자적
  - 격리된 UI 기능 제작
- fixed
  - 공간 차지 X
  - Viewport 기준 이동
  - 스크롤 시에도 항상 같은 곳에 위치

https://emmet.io/

https://docs.emmet.io/cheat-sheet/

