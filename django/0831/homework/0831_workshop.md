# Django Project

> 아래 제시된 정보를 참고하여 사용자가 / 저녁메뉴 인원수 >/ URL 로 요청을 보냈을 때 , URL 을 통해 보낸 값을 html 에서 출력하는 페이지를 만드시오
>
> 1) intro/ 는 startproject 명령어로 생성되는 project 디렉토리이다
> 2) pages/ 는 startapp 명령어로 생성되는 application 디렉토리이다
>
> 작성해야 하는 파일 정보
>
> 1. intro/urls.py : dinner/< 저녁메뉴 인원수 >/ 형태의 요청 경로가 명시되는 파일
> 2. Variable Routing 의 개념을 활용한다 : 저녁메뉴는 string, 인원수는 integer 이다
> 3. pages/views.py : Variable Routing 을 통해 전달 받은 인자를 html 파일에서 사용할 수 있도록 렌더링 할 때 넘겨준다
> 4. templates/dinner.html : html 마크업이 작성된 문서이다. views.py 에서 넘어온 데이터가 해당 문서에서 출력된다

1. intro/urls.py

```python
from django.contrib import admin
from django.urls import path, include

# include 사용으로 pages앱을 별도로 관리하도록 지정
urlpatterns = [
    path('pages/', include('pages.urls')),
    
    path('admin/', admin.site.urls),
]
# pages/urls.py
from django.urls import path
from . import views

app_name = 'pages'
# ~/pages/
urlpatterns = [
    path('dinner/<str:menu>/<int:people>/', views.dinner, name='dinner'),
]
```

2. `pages/views.py`

```python
def dinner(request, menu, people):
    context = {
        'menu': menu,
        'people': people,
    }
    return render(request, 'pages/dinner.html', context)
```

3. `templates/dinner/html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
</head>
<body>
  <div class="container">
    {% block container %}
    {% endblock container %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
</body>
</html>

{% comment %} dinner.html 사용시 이부분을 내리거나 제거 {% endcomment %}
{% extends 'base.html' %}
{% block container %}
  <h1>저녁 메뉴</h1>
  <p>저녁 먹을 사람!? {{ people }}명</p>
  <p>어떤 메뉴?! {{ menu }}</p>
{% endblock container %}
```

