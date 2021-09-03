[TOC]

# 01_django_model

## Model

> 웹 어플리케이션의 데이터를 구조화하고 조작하기 위한 도구

**개념**

- 단일한 데이터에 대한 정보를 가짐
  - 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함
- 저장된 데이터베이스의 구조(layout) 
- django는 model을 통해 데이터에 접속하고 관리
- 일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑 됨

<br>

### Database

> 체계화된 데이터의 모임 (집합)

`쿼리(Query)`

- 데이터를 조회하기 위한 명령어
- (주로 테이블형 자료구조에서) 조건에 맞는 데이터를 추출하거나 조작하는 명령어

<br>

**기본 구조**

- `스키마 (Schema)` —> 뼈대(Structure)
  - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조
- `테이블 (Table)` —> 관계(Relation) —> 엑셀의 sheet
  - 열(column) : 필드(field) or 속성
  - 행(row) : 레코드(record) or 튜플

<br>

------

<br>

### ORM

> 객체-관계 매핑

**개념**

- Object-Relational-Mapping
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에(Django - SQL)데이터를 변환하는 프로그래밍 기술
- OOP 프로그래밍에서 RDBMS을 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법
- Django는 내장 Django ORM을 사용함

<br>

**장/단점**

- 장점
  - SQL을 잘 알지 못해도 DB 조작이 가능
  - SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성
- 단점
  - ORM 만으로 완전한 서비스를 구현하기 어려운 경우가 있음

<br>

**정리**

- 객체 지향 프로그래밍에서 DB를 편리하게 관리하게 위해 ORM 프레임워크를 도입
- **"우리는 DB를 객체(object)로 조작하기 위해 ORM을 사용한다."**

<br>

**models.py 정의**

```python
# articles/models.py

class Article(models.Model): # Model class 상속
    # id는 기본적으로 처음 테이블 생성시 자동으로 만들어진다.
    title = models.CharField(max_length=10) # 클래스 변수(DB의 필드)
    content = models.TextField() 
```

- DB 컬럼과 어떠한 타입으로 정의할 것인지에 대해 django.db 라는 모듈의 models 를 상속
  - 각 모델은 `django.db.models.Model` 클래스의 서브 클래스로 표현
- title과 content은 모델의 필드(컬럼)를 나타냄
  - 각 필드는 클래스 속성으로 지정되어 있으며, 각 속성은 각 데이터베이스의 열에 매핑

<br>

**사용 된 필드**

> [https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.CharField](https://docs.djangoproject.com/en/3.2/ref/models/fields/)

- `CharField(max_length=None, **options)`
  - 길이의 제한이 있는 문자열을 넣을 때 사용
  - CharField의 max_length는 필수 인자
    - **필드의 최대 길이(문자),** 데이터베이스 레벨과 Django의 유효성 검사(값을 검증하는 것)에서 활용
- `TextField(**options)`
  - max_length 옵션 작성시 자동 양식 필드인 textarea 위젯에 반영은 되지만
  - 모델과 데이터베이스 수준에는 적용되지 않음 
    - max_length 사용은 CharField에서 사용해야 함

<br>

------

<br>

## Migrations

>  “django가 model에 생긴 변화를 반영하는 방법”

<br>

**makemigrations**

> migration 파일은 데이터베이스 스키마를 위한 버전관리 시스템이라 생각하자

- 모델을 변경한 것에 기반한 새로운 migration(설계도, 이하 마이그레이션)만들 때 사용
- 모델을 활성화 하기 전에 DB 설계도(마이그레이션) 작성

```bash
$ python manage.py makemigrations
```

- `0001_initial.py` 생성 확인

<br>

**migrate**

> 설계도를 실제 DB에 반영하는 과정

- `migrate` 는 `makemigrations` 로 만든 설계도를 실제 `db.sqlite3` DB에 반영한다.

- 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룬다.

  ```bash
  $ python manage.py migrate
  ```

<br>

**sqlmigrate**

- 해당 migrations 설계도가 SQL 문으로 어떻게 해석되어서 동작할지 미리 확인 할 수 있다.

  ```bash
  $ python manage.py sqlmigrate app_name 0001
  ```

<br>

**showmigrations**

- migrations 설계도들이 migrate 됐는지 안됐는지 여부를 확인 할 수 있다.

  ```bash
  $ python manage.py showmigrations
  ```


<br>

**변경사항 반영**

```python
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```bash
$ python manage.py makemigrations
```

<br>

```bash
You are trying to add the field 'created_at' with 'auto_now_add=True' to article without a default; the database needs something to populate existing rows.

 1) Provide a one-off default now (will be set on all existing rows)
 2) Quit, and let me add a default in models.py
Select an option: 1
```

- `1` 입력 후 enter (추가된 필드에 대한 default 값 설정)

<br>

```bash
Please enter the default value now, as valid Python
You can accept the default 'timezone.now' by pressing 'Enter' or you can provide another value.
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
[default: timezone.now] >>>
```

- 그대로 `enter` (django가 timezone.now를 default 함수 값으로 자동 설정)

```bash
$ python manage.py migrate
```

<br>

`DateTimeField()`

- 최초 생성 일자: `auto_now_add=True`
  - django ORM이 최초 insert(테이블에 데이터 입력)시에만 현재 날짜와 시간으로 갱신
    (테이블에 어떤 값을 최초로 넣을 때)
- 최종 수정 일자: `auto_now=True`
  - django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신

<br>

**Model 작성 과정 3단계**

- `models.py` : 변경사항 발생 (생성 / 수정)
- `makemigrations` : migration 파일 만들기 (설계도)
- `migrate` : DB에 적용 (테이블 생성)

<br>

------

<br>

## Database API

> DB를 조작하기 위한 도구
>
> django가 기본적으로 orm을 제공함에 따른 것으로 db를 편하게 조작할 수 있도록 도와줌
>
> https://docs.djangoproject.com/en/3.2/topics/db/queries/

<br>

**DB API 구문**

> https://docs.djangoproject.com/en/3.2/ref/models/querysets/#queryset-api-reference
>
> https://docs.djangoproject.com/en/3.2/topics/db/queries/#making-queries

<img width="1517" alt="Screen Shot 2020-08-19 at 5 12 04 PM" src="https://user-images.githubusercontent.com/18046097/90609518-23395b80-e23f-11ea-8e04-abfc04a709f7.png">

<br>

**`objects` Manager**

> https://docs.djangoproject.com/en/3.2/topics/db/managers/#managers
>
> Django 모델에 데이터베이스 쿼리 작업이 제공되는 인터페이스

- Model Manager와 Django Model 사이의 **Query 연산의 인터페이스 역할** 을 해줌
- 즉, `models.py` 에 설정한 클래스(테이블)을 불러와서 사용할 때 DB와의 interface 역할을 하는 매니저
- Django는 기본적으로 모든 Django 모델 클래스에 대해 '`objects`' 라는 Manager(django.db.models.Manager) 객체를 자동으로 추가한다.
- Manager(objects)를 통해 특정 데이터를 조작(메서드)할 수 있다.

<br>

**QuerySet**

> 데이터베이스로부터 데이터를 읽고, 필터를 걸거나 정렬 등을 수행
>
> 쿼리(질문)를 DB에게 던져서 글을 읽거나, 생성하거나, 수정하거나, 삭제

- 데이터베이스로부터 전달받은 객체 목록
- queryset 안의 객체는 0개, 1개 혹은 여러 개일 수 있음
- 데이터베이스로부터 조회, 필터, 정렬 등을 수행 할 수 있음

<br>

### CRUD

> 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능인 
> Create(생성), Read(읽기), Update(갱신), Delete(삭제)를 묶어서 일컫는 말
>
> 이러한 4개의 조작을 모두 할 수 없다면 그 소프트웨어는 완전하다고 할 수 없다. 
>
> 이들 기능은 매우 기본적이기 때문에, 한 묶음으로 설명되는 경우가 많다.
>
> https://ko.wikipedia.org/wiki/CRUD

<br>

### Create

> django shell_plus에서 진행

<br>

`__str__`

- 모든 모델마다 표준 파이썬 클래스의 메소드인 **str**() 을 정의하여 
  각각의 object가 사람이 읽을 수 있는 문자열을 반환(return)하도록 한다.
  
  ```python
  # articles/models.py
  
  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      def __str__(self):
          return self.title
  ```

<br>

**`save()`**

> https://docs.djangoproject.com/en/3.2/ref/models/instances/#saving-objects

- Saving objects
- 객체를 데이터베이스에 저장함
- 데이터 생성 시 save()를 호출하기 전에는 객체의 ID 값이 무엇인지 알 수 없음
  - ID 값은 django가 아니라 DB에서 계산되기 때문
- 단순히 모델을 인스턴스화 하는 것은 DB에 영향을 미치지 않기 때문에 반드시 save()가 필요

<br>

### Read

`all()`

> https://docs.djangoproject.com/en/3.2/ref/models/querysets/#all

- 현재 QuerySet의 복사본을 반환

```python
Article.objects.all()
```

<br>

`get()`

>  https://docs.djangoproject.com/en/3.2/ref/models/querysets/#get

- 주어진 lookup 매개변수와 일치하는 객체를 반환
- 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectReturned 예외를 발생 시킴
- 위와 같은 특징을 가지고 있기 때문에 primary key와 같이 고유(unique)성을 보장하는 조회에서 사용해야 함

```python
>>> article = Article.objects.get(pk=100)
DoesNotExist: Article matching query does not exist.

>>> Article.objects.get(content='django!')
MultipleObjectsReturned: get() returned more than one Article -- it returned 2!
filter()
```

<br>

`filter()`

>  https://docs.djangoproject.com/en/3.2/ref/models/querysets/#filter

- 주어진 lookup 매개변수와 일치하는 객체를 포함하는 새 QuerySet을 반환


<br>

**Field lookups**

- SQL WHERE 절을 지정하는 방법

- QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인수로 지정

  ```python
  Article.objects.filter(pk__gt=1)
  ```

<br>

**The `pk` lookup shortcut**

> https://docs.djangoproject.com/en/3.2/topics/db/queries/#the-pk-lookup-shortcut

- 또한, 우리가 `.get(id=1)` 형태 뿐만 아니라 `.get(pk=1)` 로 사용할 수 있는 이유는(DB에는 id로 필드 이름이 지정 됨에도) `.get(pk=1)` 이`.get(id__exact=1)` 와 동일한 의미이기 때문이다. 

- pk는 `id__exact` 의 shortcut 이다.

  ```python
  >>> Blog.objects.get(id__exact=14) # Explicit form
  >>> Blog.objects.get(id=14) # __exact is implied
  >>> Blog.objects.get(pk=14) # pk implies id__exact
  ```

<br>

### Update

```python
>>> article = Article.objects.get(pk=1)
>>> article.title
'first'

# 값을 변경하고 저장
>>> article.title = 'byebye'
>>> article.save()

# 정상적으로 변경된 것을 확인
>>> article.title
'byebye'
```

<br>

### Delete

```python
>>> article = Article.objects.get(pk=1)

# 삭제
>>> article.delete()
(1, {'articles.Article': 1})

# 다시 1번 글을 찾으려고 하면 없다고 나온다.
>>> Article.objects.get(pk=1)
DoesNotExist: Article matching query does not exist.
```

<br>

---

<br>

[TOC]

# CRUD 실습

**`base.html` 설정**

```django
<!-- templates/base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <!-- Bootstrap CDN -->
</head>
<body>
  <div class="container">
    {% block content %}
    {% endblock %}
  </div>
  <!-- Bootstrap CDN -->
</body>
</html>
```

```python
# settings.py

'DIRS': [BASE_DIR / 'templates'],
```

<br>

**기본 페이지 설정**

```python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
]


# articles/views.py

def index(request):
    return render(request, 'articles/index.html')
```

```django
<!-- templates/articles/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
{% endblock %}
```

<br>

---

<br>

## READ

- 게시글 전체 조회

```python
# articles/views.py

from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
```

```django
<!--templates/articles/index.html-->

{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  <hr>
  {% for article in articles %}
    <p>글 번호: {{ article.pk }}</p>
    <p>글 제목: {{ article.title }}</p>
    <p>글 내용: {{ article.content }}</p>
    <hr>
  {% endfor %}
{% endblock %}
```

<br>

---

<br>

## CREATE

### New

```python
# articles/urls.py

path('new/', views.new, name='new'),
```

```python
# articles/views.py

def new(request):
    return render(request, 'articles/new.html')
```

```django
<!-- templates/articles/new.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>NEW</h1>
  <form action="#" method="GET">
    <label for="title">Title: </label>
    <input type="text" name="title"><br>
    <label for="content">Content: </label>
    <textarea name="content" cols="30" rows="5"></textarea><br>
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}
```

```django
<!-- templates/articles/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  <a href="{% url 'articles:new' %}">[new]</a>
  <hr>
{% endblock  %}
```

<br>

### Create

```python
# article/urls.py

path('create/', views.create, name='create'),
```

```python
def create(request):
    title = request.GET.get('title') 
    content = request.GET.get('content')
    
    article = Article(title=title, content=content)
    article.save()
    
    return render(request, 'articles/create.html')
```

```django
<!-- templates/articles/create.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>성공적으로 글이 작성되었습니다.</h1>
{% endblock %}
```

```django
<!-- templates/articles/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>NEW</h1>
  <form action="{% url 'articles:create' %}" method="GET">
    <label for="title">Title: </label>
    <input type="text" name="title"><br>
    <label for="content">Content: </label>
    <textarea name="content" cols="30" rows="5"></textarea><br>
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}
```

<br>

**게시글 정렬 순서 변경**

- `#1` - DB로 부터 받은 쿼리셋을 이후에 파이썬이 변경 (Python이 조작)
- `#2`-  처음부터 내림차순 쿼리셋으로 받음 (DB가 조작)

```python
# articles/views.py

def index(request):
    # 1. articles = Article.objects.all()[::-1]
    # 2. articles = Artile.objects.order_by('-pk')  
```

<br>

---

<br>

### Http Method - POST

> https://developer.mozilla.org/ko/docs/Web/HTTP/Methods/POST

- **3가지 이유에서 우리는 글을 작성할 때 GET 요청이 아닌 POST 요청을 해야 한다.**
1. 사용자는 Django에게 '**HTML 파일 줘(GET)**' 가 아니라 '**~한 레코드(글)을 생성해(POST)**' 이기 때문에 GET보다는 POST 요청이 맞다.
  
2. 데이터는 URL에 직접 노출되면 안된다. 
  (우리가 주소창으로 접근하는 방식은 모두 GET 요청) query의 형태를 통해 DB schema를 유추할 수 있다.
  
3. 모델(DB)을 건드리는 친구는 GET이 아닌 POST 요청! 왜? 중요하니까 **최소한의 신원 확인**이 필요하다!


<br>

**`POST`**

- 서버로 데이터를 전송할 때 사용
- 서버에 변경사항을 만듦
  - 때문에 요청자에 대한 최소한의 검증을 하지 않으면 부작용을 일으킬 수 있음
  - `csrf_token`을 통해서 요청자의 최소한의 신원확인
- 리소스를 생성/변경하기 위해 데이터를 HTTP body에 담아 전송
- CRUD에서 C/U/D 역할을 담당

<br>

**`GET`**

- 특정 리소스를 가져오도록 요청할 때 사용
- 반드시 데이터를 가져올 때만 사용해야 함
- DB에 변화를 주지 않음
- CRUD에서 R 역할을 담당

<br>

**DB 조작(GET/POST)**

- GET 요청은 DB에서 데이터를 꺼내서 가져온다. 즉, DB에 변화를 주는 게 아니다.
  - 즉, **GET**은 누가 요청해도 어차피 정보를 조회(HTML 파일을 얻는 것)하기 때문에 문제가 되지 않음.
- POST 요청은 DB에 조작(생성/수정/삭제)를 하는 것 (DB에 변화를 준다)
  - **POST**는 DB에 조작이 가해지기 때문에 요청자에 대한 최소한의 검증을 하지 않으면 아무나 DB에 접근해서 데이터에 조작을 가할 수 있다.
  - `csrf_token`을 통해서 요청자의 최소한의 신원확인을 한다.

<br>

**`new.html` 수정**

```django
<!-- templates/articles/new.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>NEW</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <label for="title">Title: </label>
    <input type="text" name="title"><br>
    <label for="content">Content: </label>
    <textarea name="content" cols="30" rows="5"></textarea><br>
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}
```

```python
# articles/views.py

def create(request):
    title = request.POST.get('title') 
    content = request.POST.get('content') 

    article = Article(title=title, content=content)
    article.save()
    return render(request, 'articles/index.html')
```

<br>

**CSRF Token**

> [https://ko.wikipedia.org/wiki/%EC%82%AC%EC%9D%B4%ED%8A%B8_%EA%B0%84_%EC%9A%94%EC%B2%AD_%EC%9C%84%EC%A1%B0](https://ko.wikipedia.org/wiki/사이트_간_요청_위조)

- 사이트 간 요청 위조(Cross-Site-Request-Fogery)

  - 웹 애플리케이션 취약점 중 하나로 **사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 한다거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법**을 의미한다.
  - `{% csrf_token %}` 을 설정하면 input type hidden 으로 특정한 hash 값이 들어있다.

- `{% csrf_token %}` 이 없다면?
- `403 forbidden` 에러: 서버에 요청은 도달했으나 서버가 접근을 거부할 때 반환하는 HTTP 응답 코드 / 오류 코드. 서버 자체 또는 서버에 있는 파일에 접근할 권한이 없을 경우에 발생
  - 이러한 접근을 할 수 있도록 하는 것이 `{% csrf_token %}` → 사내 인트라넷 서버를 사내가 아닌 밖에서 접속하려고 할 때도 해당 HTTP 응답 코드가 뜬다.
  

<br>

**게시글 작성 후 index로 되돌리기**

```python
# articles/views.py

def create(request):
    ...
    return render(request, 'articles/index.html')
```

- 문제점 발생
  1. 글을 작성 후 index 페이지가 출력되지만 게시글이 조회되지 않음

  2. URL은 여전이 create에 머물러 있음

     > 즉, 단순히 index 페이지만 render 되었을 뿐이고 url이 돌아가지 못했기 때문
     > index view 함수로 요청을 보내서 렌더링 된 것이 아님!


<br>

---

<br>

### Redirect

> Django shortcut function 중 하나이며 model, view name, absolute or relate URL을 인자로 받음
>
> 여기서 인자 view name은 URL pattern name으로 작성 될 수 있음

- POST 요청은 HTML 문서를 렌더링 하는 것이 아니라 **'~~ 좀 처리해줘(요청)'의 의미이기 때문에 요청을 처리하고 나서의 요청의 결과를 보기 위한 페이지로 바로 넘겨주는 것이 일반적**이다.

  ```python
  # articles/views.py
  
  from django.shortcuts import render, redirect
  
  
  def create(request):
      title = request.POST.get('title') 
      content = request.POST.get('content')
      
      article = Article(title=title, content=content)
      article.save()
      
      return redirect('articles:index')
  ```

<br>

**POST 요청으로 변경 후 변화하는 것**

- POST 요청을 하게 되면 form을 통해 전송한 데이터를 받을 때도 `request.POST.get()` 로 받아야 함
- 글이 작성되면 실제로 주소 창에 내가 넘긴 데이터가 나타나지 않는다. 
  (POST 요청은 HTTP body에 데이터를 전송함)
- POST는 html을 요청하는 것이 아니기 때문에 html 파일을 받아볼 수 있는 곳으로 다시 redirect 한다.

<br>

---

<br>

## DETAIL

**urls 설정**

- 개별 게시글 상세 페이지
- 글의 번호(pk)를 활용해서 각각의 페이지를 따로 구현해야 함
- 무엇을 활용할 수 있을까? → Variable Routing

```python
# articles/urls.py

path('<int:pk>/', views.detail, name='detail'),
```

<br>

**views 설정**

```python
# articles/views.py

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
```

<br>

**templates 설정**

```django
<!-- templates/articles/detail.html -->

{% extends 'base.html' %}

{% block content %}
  <h2>DETAIL</h2>
  <h3>{{ article.pk }} 번째 글</h3>
  <hr>
  <p>제목: {{ article.title }}</p>
  <p>내용: {{ article.content }}</p>
  <p>작성 시각: {{ article.created_at }}</p>
  <p>수정 시각: {{ article.updated_at }}</p>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock  %}
```

-  index 페이지에 게시글별 detail 링크작성

  ```django
  <!-- templates/articles/index.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  <h1 class="text-center">Articles</h1>
  <a href="{% url 'articles:new' %}">[new]</a>
  <hr>
  {% for article in articles %}
    <p>글 번호: {{ article.pk }}</p>
    <p>글 제목: {{ article.title }}</p>
    <p>글 내용: {{ article.content }}</p>
    <a href="{% url 'articles:detail' article.pk %}">[detail]</a>
    <hr>
  {% endfor %}
  {% endblock  %}
  ```

<br>

**create 후 detail로 이동**

```python
# articles/views.py

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()
    
    return redirect('articles:detail', article.pk)
```

<br>

------

<br>

## DELETE

**urls 설정**

```python
# articles/urls.py

path('<int:pk>/delete/', views.delete, name='delete'),
```

<br>

**views 설정**

```python
# articles/views.py

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
```

<br>

**templates 설정**

```django
<!-- articles/detail.html -->

{% extends 'base.html' %}

{% block content %}
  ...
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="삭제">
  </form><br>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}
```

- 그래서 POST 로 요청을 받기 위해 다음과 같이 조건을 만든다.

  ```python
  # articles/views.py
  
  def delete(request, pk):
      article = Article.objects.get(pk=pk)
      if request.method == 'POST':
          article.delete()
          return redirect('articles:index')
      else:
          return redirect('articles:detail', article.pk)
  ```

<br>

---

<br>

## UPDATE

### Edit

**urls 설정**

```python
# articles/urls.py

path('<int:pk>/edit/', views.delete, name='edit'),
```

<br>

**views 설정**

```python
# articles/views.py

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)
```

<br>

**templates 설정**

- 수정은 기존에 입력 되어 있던 데이터를 보여주는 것이 좋기 때문에 html 태그의 `value` 속성을 사용

```django
<!-- articles/edit.html -->

{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">EDIT</h1>
  <form action="#" method="POST">
    {% csrf_token %}
    <label for="title">Title: </label>
    <input type="text" name="title" value="{{ article.title }}"><br>
    <label for="content">Content: </label>
    <textarea name="content" cols="30" rows="5">{{ article.content }}</textarea><br>
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}
```

- `detail.html` 에 edit 으로 가는 링크 작성

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    ...
    <a href="{% url 'articles:edit' article.pk %}">EDIT</a><br>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="삭제">
    </form><br>
    <a href="{% url 'articles:detail' article.pk %}">[back]</a>
  {% endblock  %}
  ```

<br>

### Update

**urls 설정**

```python
# articles/urls.py

path('<int:pk>/update/', views.update, name='update'),
```

<br>

**views 설정**

```python
# articles/views.py

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)
```

```django
<!-- articles/edit.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>EDIT</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    ...
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}
```

