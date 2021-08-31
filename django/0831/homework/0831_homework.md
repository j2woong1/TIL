# 1. MTV

> Django는 MTV 디자인 패턴으로 이루어진 Web Framework 이다 . 여기서 MTV 는 무엇의 약자이며 각각 MVC 디자인 패턴과 어떻게 매칭이 되며 각 키워드가 django 에서 하는 역할을 간략히 서술하시오

- Model : 응용프로그램 데이터 구조 정의, DB 기록 관리 추가 , 수정 , 삭제
- Template : 파일의 구조, 레이아웃 정의, 실제 내용을 보여주기 (presentation)
- View : HTTP 요청 수신, 응답 반환, Model 을 통해 필요한 데이터에 접근, template 에게 응답의 서식 설정을 맡김



# 2. URL

> __(a)__는 Django 에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것을 의미한다 . (a) 는 무엇인지 작성하시오

- Variable Routing : <> 사용



# 3. Django Template Path

> Django 프로젝트는 render 할 template 파일들을 찾을 때 , 기본적으로 settings.py 에 등록된 각 앱 폴더 안의 __(a)__ 폴더 내부를 탐색한다 . (a) 에 들어갈 폴더 이름을 작성하시오

- templates



# 4. Django Template Language

## 1) menus 리스트를 반복문으로 출력하시오

```django
{% for menu in menus %}
	<p>{{ menu }}</p>
{% endfor %}
```

## 2) posts 리스트를 반목문을 활용하여 0 번 글부터 출력하시오

```django
{% for post in posts %}
	<p>{{ forloop.counter }}번 글 : {{ post }}</p>
{% endfor %}
```

## 3) users 리스트가 비어있다면 현재 가입한 유저가 없습니다 . 텍스트를 출력하시오

```django
{% for user in users %}
	<p>{{ user }}</p>
{% empty %}
	<p>현재 가입한 유저가 없습니다.</p>
{% endfor %}
```

## 4) 첫 번째 반복문일 때와 아닐 때를 조건문으로 분기처리 하시오

```django
{% if forloop.first %}
	<p>첫 번째 반복문 입니다.</p>
{% else %}
	<p>첫 번째 반복문이 아닙니다.</p>
{% endif %}
```

## 5) 출력된 결과가 주석과 같아지도록 하시오

```django
<!-- 5 -->
<p>{{ 'hello'|length}}</p>
<!-- My Name Is Tom -->
<p>{{ 'my name is tom'|capfirst}}</p>
```

## 6) 변수 today 에 datetime 객체가 들어있을 때 출력된 결과가 주석과 같아지도록 작성하시오

```django
<!-- 2020년 02월 02일 (Sun) PM 02:02 -->
{{today|date:"o년 m월 d일 (D) A H:i"}}
```



# 5. Form tag with Django

```django
<form action="/create" method="">
    <label for="title">Title : </label>
    <input type="text" name="title" id="title">
    <label for="content">Content : </label>
    <input type="text" name="content" id="content">
    <label for="my-site">My-Site : </label>
    <input type="text" name="my-site" id="my-site">
    <input type="submit">
</form>
```

## 1) 지문의 코드 중 form 태그의 속성인 action 의 역할에 대해 설명하시오

- 입력 데이터가 전송될 URL 지정

## 2) 지문의 코드 중 method 가 가질 수 있는 속성 값을 작성하시오

- `GET` : URL에 폼 데이터 추가
- `POST` : 폼 데이터 별도 첨부

## 3) input 태그에 각각 `안녕하세요 `, `반갑습니다 `, `파이팅 ` 문자열을 넣고
submit 버튼을 눌렀을 때 이동하는 url 경로를 작성하시오

- `create/?title=안녕하세요&content=반갑습니다&my-site=파이팅`



