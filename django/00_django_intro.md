[TOC]

# 00_django_intro

## Intro

> 프로젝트 시작 전 항상 가상환경 설정하기

**설치**

```bash
$ pip install django
```

- 설치 확인

  ```bash
  $ pip list
  ```

<br>

**프로젝트 생성**

> [주의]
>
> project 를 생성할 때, Python 이나 Django 에서 사용중인 이름은 피해야 한다. 
>
> `-` 도 사용할 수 없다. (ex. django, test, class, django-test...)

```bash
$ django-admin startproject first_project
```

<br>

**서버 실행**

```bash
$ python manage.py runserver
```

<br>

**프로젝트 구조**

- `__init__.py`
  - 빈 파일
  - Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시
- `settings.py`
  - 웹사이트의 모든 설정을 포함
  - 우리가 만드는 어떤 application이라도 등록이 되는 곳이며, static files의 위치, database 세부 설정 등이 작성
- `urls.py`
  - 사이트의 url와 view의 연결을 지정
- `wsgi.py`
  - Web Server Gateway Interface
  - 장고 어플리케이션이 웹서버와 연결 및 소통하는 것을 도움
- `asgi.py`
  - new in 3.0
  - Asynchronous Server Gateway Interface
  - 장고 어플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움

<br>

**Application 생성**

```bash
$ python manage.py startapp articles
```

<br>

**Application (app)**

- 실제로 어떠한 역할을 해주는 친구가 app.
- 프로젝트는 이러한 app의 집합이고, 실제 요청을 처리하고 페이지를 보여주고 하는 것들은 이 app의 역할.
- 하나의 프로젝트는 여러 개의 app을 가질 수 있다.
  - app은 하나의 역할 및 기능 단위로 쪼개는 것이 일반적
  - 그러나 작은 규모의 서비스에서는 잘 나누지 않으며 반드시 이렇게 나눠야 한다 같은 기준 또한 없다.
- **일반적으로 app 이름은 `복수형`으로 작성 하는 것을 권장한다.**

<br>

**Application 구조**

- `admin.py`
  - 관리자용 페이지 관련 기능을 작성 하는 곳.
- `apps.py`
  - 앱의 정보가 있는 곳. 
  - 우리는 수정할 일이 없다.
- `models.py`
  - 앱에서 사용하는 Model(Database)를 정의하는 곳.
- `tests.py`
  - 테스트 코드를 작성하는 곳.
- `views.py`
  - view가 정의 되는 곳. 

<br>

**Application 등록**

> 반드시 **app 생성 후 등록** 순서를 지켜야한다.

- 방금 생성한 app을 사용하려면 프로젝트에 등록 해야 한다.

  ```python
  # settings.py
  
  INSTALLED_APPS = [
  	'articles',
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  ```

  > INSTALLED_APPS의 app order
  >
  > ```python
  > INSTALLED_APPS = [
  >     # Local apps
  >     'blogs',
  > 
  >     # Third party apps
  >     'haystack',
  > 
  >     # Django apps
  >     'django.contrib.admin',
  >     'django.contrib.auth',
  >     'django.contrib.contenttypes',
  >     'django.contrib.sessions',
  >     'django.contrib.sites',
  > ]
  > ```

<br>

**MTV 패턴**

![img_02](00_django_intro.assets/img_02.png)

**model**

- 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)

**template**

- 파일의 구조나 레이아웃을 정의
- 실제 내용을 보여주는 데 사용 (presentation)

**view**

- HTTP 요청을 수신하고 HTTP 응답을 반환
- Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
- 그리고 탬플릿에게 응답의 서식 설정을 맡김

<br>

**.py 3대장 기억하기**

- `urls.py` : 주소(URL) 관리
- `views.py` : 페이지 관리 (페이지 하나 당, 하나의 함수)
- `models.py` : 데이터베이스 관리

<br>

**Internationalization**

> https://docs.djangoproject.com/en/3.2/topics/i18n/
>
> http://www.i18nguy.com/unicode/language-identifiers.html
>
> https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

```python
# settings.py

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```

<br>

`runserver` **Automatic reloading**

- 개발 서버는 요청이 들어올 때마다(코드가 저장될 때 마다) 자동으로 Python 코드를 다시 불러온다. 
- 코드의 변경사항을 반영하기 위해서 굳이 서버를 재가동 하지 않아도 된다. 
- 그러나, 파일을 추가하는 등의 몇몇의 동작(커스텀 필터, 새로운 모듈 추가 등)은 개발 서버가 자동으로 
  인식하지 못하기 때문에, 이런 상황에서는 서버를 재가동 해야 적용되는 경우도 있다.

<br>

---

<br>

### 요청과 응답

**urls.py**

- 장고 서버로 요청(request)이 들어오면, 그 요청이 어디로 가야하는지 인식하고 관련된 함수(view)로 넘겨준다.

- `views.py` 에서 만든 함수를 연결시켜준다.

  ```python
  # first_project/urls.py
  
  from django.contrib import admin
  from django.urls import path
  from articles import views
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('index/', views.index),
  ]
  ```


<br>

**views.py**

- HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성
- Model을 통해 요청에 맞는 필요 데이터에 접근
- tempate에게 HTTP 응답 서식을 맡김

```python
# articles/views.py

def index(request): # 첫번째 인자는 반드시 request
    return render(request, 'index.html') # render의 첫번째 인자도 반드시 request
```

<br>

**Templates**

- `views.py`에서 지정한 `index.html` 파일을 만들자.

- Django에 설정된 template의 기본 경로는 **app 폴더안의 templates 폴더**이다.

  ```html
  <!-- articles/templates/index.html -->
  
  <h1>만나서 반갑습니다!</h1>
  ```

<br>

---

<br>

## Template

> https://docs.djangoproject.com/en/3.2/topics/templates/#module-django.template
>
> 데이터 표현을 제어하는 도구이자 표현에 관련된 로직

<br>

### Django template language

> https://docs.djangoproject.com/en/3.2/ref/templates/language/
>
> https://docs.djangoproject.com/ko/3.2/ref/templates/builtins/#built-in-template-tags-and-filters

- django template에서 사용하는 built-in template system
- 조건, 반복, 변수 치환, 필터 등의 기능을 제공
- Django 템플릿 시스템은 단순히 Python이 HTML에 포함 된 것이 아님
  - 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것
- 파이썬처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만 이건 **Python 코드로 실행되는 것이 아님**

<br>

**syntax**

1. variables

- `{{ variables }}`

- 변수명은 영,숫자와 밑줄(_)의 조합으로 구성될 수 있으나 밑줄로는 시작 할 수 없음
- 변수명에 공백이나 구두점 문자를 사용할 수 없음
- `dot(.)`를 사용하여 변수 속성에 접근

<br>

2. Filters

- `{{ variable|filter }}`
- 표시할 변수를 수정
- 파이프(|)를 사용하여 적용

<br>

3. Tags

- `{% tag %}`
- 출력 테스트를 만들거나 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 보다 복잡한 일들을 수행
- 일부 태그는 시작과 종료 태그가 필요(`{% tag %}` ... `{% endtag %}`)

<br>

4. Comments

- `{# lorem #}`

<br>

### Template inheritance

> https://docs.python.org/ko/3.9/library/pathlib.html#module-pathlib

- 템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춤

- 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하고, 
  하위 템플릿이 재정의(override) 할 수있는 블록을 정의하는 기본 “skeleton” 템플릿을 만들 수 있음
  
  ```python
  # settings.py
  
  TEMPLATES = [
      {
          ...,
          'DIRS': [BASE_DIR / 'templates'],
  ...
  ]
  ```
  
  - `app_name/templates` 기본경로 외 추가 경로 설정하기

<br>

**`extends` tag**

- 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림
- 반드시 템플릿 최상단에 위치해야 함(== 템플릿의 첫번째 템플릿 태그여야 함)
  - 즉, 2개 이상 사용할 수 없음

<br>

**`block` tag**

- 하위 템플릿에서 재지정(overriden)할 수 있는 블록을 정의

- 하위 템플릿이 채울 수 있는 공간

- 가독성을 높이기 위해 선택적으로 `{% endblock %}` 태그에 이름 지정

  ```django
  {% block content %}
  {% endblock content %}
  ```

<br>

**Template system**

>https://docs.djangoproject.com/ko/3.2/misc/design-philosophies/#template-system

1. 표현과 로직(view)을 분리

- 우리는 템플릿 시스템이 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐이라고 봅니다. 
- 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야 합니다.

2. 중복을 배제

- 대다수의 동적 웹사이트는 공통 헤더, 푸터, 네이게이션 바 같은 사이트 공통 디자인을 갖습니다. 
- Django 템플릿 시스템은 이러한 요소를 한 곳에 저장하기 쉽게 하여 중복 코드를 없애야 합니다. 

<br>

## HTML Form

<br>

**throw & catch**

- throw

  ```python
  # first_project/urls.py
  
  path('throw/', views.throw),
  ```

  ```python
  # articles/views.py 
  
  def throw(request):
      return render(request, 'throw.html')
  ```

  ```html
  <!-- articles/templates/throw.html -->
  
  <form action="/catch/" method="GET">
    <label for="message">Throw</label>
    <input type="text" id="message" name="message">
    <input type="submit">
  </form>
  ```

- catch

  ```python
  # first_project/urls.py
  
  path('catch/', views.catch),
  ```

  ```python
  # articles/views.py
  
  def catch(request):
      message = request.GET.get('message')
      context = {
          'message': message,
      }
      return render(request, 'catch.html', context)
  ```

  ```django
  <!-- articles/templates/catch.html -->
  
  <h1>너가 던져서 내가 받은건 {{ message }}야!</h1>
  <a href="/throw/">뒤로</a>
  ```

<br>

---

<br>

## URLs

> 웹 어플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작

<br>

### Variable routing

- 동적 라우팅

- URL 주소를 변수로 사용하는 것
- URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음
- 즉, 변수 값에 따라 하나의 `path()`에 여러 페이지를 연결 시킬 수 있음

```python
# urls.py

urlpatterns = [
    ...,
    # path('hello/<name>/', views.hello),
    path('hello/<str:name>/', views.hello),
]
```

```python
# views.py

def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)
```

```django
<!-- hello.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>만나서 반가워요 {{ name }}님!</h1>
{% endblock %}
```

<br>

**URL Path converters**

> [https://docs.djangoproject.com/en/3.2/topics/http/urls/#path-converters](https://docs.djangoproject.com/en/3.2/topics/http/urls/)

- str
  - `/` 를 제외하고 비어 있지 않은 모든 문자열과 매치
  - 작성하지 않을 경우 기본 값
- int
  - 0 또는 양의 정수와 매치
- slug
- uuid
- path

<br>

### App URL mapping

> 하나의 프로젝트의 여러 앱이 존재한다면, 
> 각각의 앱 안에 urls.py을 만들고 프로젝트 urls.py에서 각 앱의 urls.py 파일로 URL 매핑을 위탁하게 가능

**두번째 app 생성 및 등록**

```bash
$ python manage.py startapp pages
```

```python
INSTALLED_APPS = [
    'articles',
    'pages',
    ...,
]
```

<br>

```python
# articles/urls.py

from django.urls import path
from . import views 


urlpatterns = [
    path('index/', views.index),
    path('greeting/', views.greeting),
    path('dinner/', views.dinner),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<str:name>/', views.hello),
]
```

```python
# pages/urls.py

from django.urls import path


urlpatterns = [

]
```

> [주의] urlpatterns list를 작성하지 않으면 에러가 발생한다.

- django는 명시적 상대경로(`from .module import ..`)를 권장한다.

<br>

### Including other URLconfs

```python
# firstpjt/urls.py

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
```

<br>

`include()`

- 다른 URLconf(app1/urls.py)들을 참조할 수 있도록 도움
- 함수 include()를 만나게 되면, URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달

<br>

### Naming URL patterns

- Django는 URL에 이름을 지정하는 방법을 제공하므로써 뷰 함수와 템플릿에서 특정 주소를 쉽게 참조할 수 있도록 도움

```python
# articles/urls.py

urlpatterns = [
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.hello, name='hello'),
]
```

<br>

**url tag 사용하기**

```django
<!-- index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>만나서 반가워요!</h1>
  <a href="{% url 'greeting' %}">greeting</a>
  <a href="{% url 'dinner' %}">dinner</a>
  <a href="{% url 'throw' %}">throw</a>
{% endblock %}
```

<br>

`{$ url '' %}`

- 주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소를 반환
- 템플릿에 URL을 하드 코딩하지 않고도 DRY 원칙을 위반하지 않고 링크를 출력하는 방법

<br>

---

## Namespace

> 개체를 구분할 수 있는 범위를 나타내는 namespace

**두번째 app의 index 페이지 작성**

```python
# pages/urls.py

from django.urls import path
from . import views 


urlpatterns = [
    path('index/', views.index, name='index'),
]
```

```python
# pages/views.py

def index(request):
    return render(request, 'index.html')
```

```django
<!-- pages/templates/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>두번째 앱의 index</h1>
{% endblock %}
```

```django
<!-- articles/templates/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>만나서 반가워요!</h1>
  <a href="{% url 'greeting' %}">greeting</a>
  <a href="{% url 'dinner' %}">dinner</a>
  <a href="{% url 'dtl_practice' %}">dtl-practice</a>
  <a href="{% url 'throw' %}">throw</a>

  <h2><a href="{% url 'index' %}">두번째 앱 index로 이동</a></h2>
{% endblock %}
```

<br>

**2가지 문제**

1. articles app index 페이지에서 두번째 앱 index로 이동 하이퍼 링크를 클릭 시 현재 페이지로 이동
   - URL namespace
2. pages app index url로 이동해도 articles app의 index 페이지가 출력됨
   - Template namespace

<br>

### URL namespace

**app_name attribute 작성**

```python
# pages/urls.py

app_name = 'pages'
urlpatterns = [
    path('index/', views.index, name='index'),
]
```

```python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    ...,
]
```

<br>

**`app_name` attribute**

- URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용 할 수 있음
- urls.py에 `app_name` attribute 값 작성

<br>

**참조**

- `:` 연산자를 사용하여 지정
  - 예를들어, app_name이 `articles`이고 URL name이 `index`인 주소 참조는 `articles:index`

<br>

**URL tag 변경**

```django
<!-- articles/templates/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>만나서 반가워요!</h1>
  <a href="{% url 'articles:greeting' %}">greeting</a>
  <a href="{% url 'articles:dinner' %}">dinner</a>
  <a href="{% url 'articles:throw' %}">throw</a>

  <h2><a href="{% url 'pages:index' %}">두번째 앱 index로 이동</a></h2>
{% endblock %}
```

<br>

### Template namespace

- Django는 기본적으로 `app_name/templates/` 경로에 있는 templates 파일들만 찾을 수 있으며, INSTALLED_APPS에 작성한 app 순서로 tamplate을 검색 후 렌더링 함

- templates의 폴더 구조를 `app_name/templates/app_name` 형태로 변경해 
  임의로 물리적인 이름 공간을 생성 후 변경된 경로로 수정
  
  ```python
  # articles/views.py
  
  return render(request, 'articles/index.html')
  ```
  
  ```python
  # pages/views.py
  
  return render(request, 'pages/index.html')
  ```