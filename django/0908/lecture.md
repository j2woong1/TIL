## Managing Static Files

### Static files 

- 개발자 -> 변경 X
- 응답 시 별도 처리 없이 파일 내용 그대로 보여주기 : 요청한 것 그대로
- image, JS, CSS, font

#### 구성

- `django.contrib.staticfiles`가 `INSTALLED_APPS` 포함

- `settings.py`에서 **STATIC_URL** 정의

- templates에서 **static template tag** 사용해서 상대 경로 URL 빌드

  ```html
  {% load static %}
  <img src="{% static 'my_app/example.jpg' %}" alt="My image">
  ```

- 앱의 static 폴더에 정적 파일 저장

#### Django template tag

- load
  - 사용자 정의 템플릿 태그 세트 로드
  - 로드하는 라이브러리, 패키지에 등록된 모든 태그, 필터 로드
- static
  - STATIC_ROOT에 저장된 정적 파일에 연결

#### The staticfiles app

- STATIC_ROOT

  - collectstatic이 배포를 위해 정적 파일 수집하는 디렉토리 절대 경로

  - 사용하는 모든 정적 파일 한 곳에

  - `settings.py`에서 DEBUG가 True면 작용 X

  - 실 서비스 (배포) 환경에서 모든 정적 파일을 다른 웹 서버가 직접 제공하려고

    ```
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    ```

    ```
    $ python manage.py collectstatic
    ```

- STATIC_URL

  - STATIC_ROOT에 있는 정적 파일 참조 URL

  - URL로만 존재

  - /로 끝나야 함

    ```
    STATIC_URL = '/static/'
    ```

- STATICFILES_DIRS

  - 추가적 정적 파일 경로 목록 정의 리스트

  - 전체 경로를 포함하는 문자열 목록으로 작성

    ```
    STATICFILES_DIRS = [ BASE_DIR / 'static',]
    ```

### Media files 

- 사용자 -> 변경 O

#### Model field

- ImageField
  - 이미지 업로드
  - FileField 상속 서브 클래스 
  - `max_length` 사용 가능
  - Pillow 라이브러리 필요
- FileField
  - 파일 업로드

#### upload_to argument

- 문자열 값, 경로 지정

  ```python
  # models.py
  class MyModel(models.Model):
      # MEDIA_ROOT/uploads/ 경로
      upload = models.FileField(upload_to='uploads/')
      # MEDIA_ROOT/uploads/2021/01/01/ 경로
      upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
  ```

- 함수 호출

  - instance : FileField 정의 모델, PK 없을 수 O
  - filename : 기존 파일에 제공된 파일 이름

  ```python
  # models.py
  def articles_image_path(instance, filename):
      # MEDIA_ROOT/user_<pk> 경로로 <filename> 이름으로 업로드
      return f'user_{instance.user.pk}/{filename}'
  
  class Article(models.Model):
      image = models.ImageField(upload_to=articles_image_path)
  ```

  - `settings.py`에 MEDIA_ROOT, MEDIA_URL 설정

  - MEDIA_ROOT 하위 경로 지정

    ```html
    <img src="{{ article.image.url }}" alt="{{ article.image }}">
    ```

    - MEDIA_ROOT

      - 업로드한 파일을 보관할 디렉토리 절대 경로

      - STATIC_ROOT와 다른 경로로 지정

        ```python
        # settings.py
        MEDIA_ROOT = BASE_DIR / 'media'
        ```

    - MEDIA_URL

      - MEDIA_ROOT에서 제공되는 미디어 처리 URL

      - 업로드 파일 주소 제작

      - STATIC_URL과 다른 경로

        ```python
        # settings.py
        MEDIA_URL = '/media/'
        ```

#### 사용자 업로드 파일 제공

```python
# crud/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 업로드 파일 URL == settings.MEDIA_URL
# 참조 파일 실제 위치 == settings.MEDIA_ROOT
```

### Image Upload

#### ImageField 작성

- `upload_to='images/'` : 실제 이미지 저장 경로

- `blank=True` : 빈 값 허용

  ```python
  # articles/models.py
  
  class Article(models.Model):
      title = models.ChaField(max_length=20)
      content = models.TextField()
      # saved to 'MEDIA_ROOT/images'
      image = models.ImageField(blank=True, upload_to='images/')
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_not=True)
  ```

#### Model field option

- blank
  - 기본 값 : False
  - True : 필드 비워둠 => DB에 '' (빈 문자열) 저장
  - 유효성 검사 (`is_valid`) : blank=True -> form 유효성 검사에서 빈 값 입력 가능
  - Validation-related
- null
  - 기본 값 : False
  - True -> DB에 NULL 저장
  - 문자열 기반 필드 (CharField, TextField) 에 X
  - True -> 데이터 없음 (no data)에 빈 문자열, NULL 두가지 가능 값
    - 데이터 없음 : 중복, 빈 문자열 사용
  - Database-related

```python
# models.py

class Person(models.Model):
    name = models.CharField(max_length=10)
    
    # null=True 금지
    bio = models.TextField(max_length=50, blank=True)
    
    # null, blank 모두 설정 가능 -> 문자열 기반 필드 X
    birth_date = models.DateField(null=True, blank=True)
```

```
$ pip install Pillow # ImageField 사용하기 위해서
```

```html
<!-- articles/create.html -->

<form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-date"> 
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="작성"> <!-- 이거 사용할 때 -->
</form>
```

- form enctype 속성 지정 : 파일/이미지 업로드 시 반드시

```html
<!-- articles/create.html -->

<form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-date"> 
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="작성" accept="image/*"> 
</form>
```

- input accept 속성 지정
  - 입력 허용 파일 유형
  - 쉼표로 구분된 고유 파일 유형 지정자 (unique file type specifiers)

```python
# views.py

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        # data=, files= 생략
        if form.is_valid():
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create/html', context)
```

### 이미지 업로드 (READ)

#### 경로 불러오기

- `article.image.url` : 업로드 파일 경로

- `article.image ` : 업로드 파일 이름

  ```html
  <!-- detail.html -->
  
  {% extends 'base.html' %}
  {% block content %}
  	<h2 class='text-center'>DETAIL</h2>
  	<h3>{{ article.pk }} 번 글</h3>
  	<img src="{{ article.image.url }}" alt="{{ article.image }}">
  	<hr>
  {% endblock content %}
  ```

#### UPDATE

- 새로운 사진으로 덮어 씌우기

  ```html
  <!-- articles/update.html -->
  
  {% extends 'base.html' %}
  {% block content %}
  	<h1>UPDATE</h1>
  	<form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data">
      	{% csrf_token %}
          {{ form.as_p }}
          <button>수정</button>
  	</form>
  	<hr>
  	<a href="{% url 'articles:index' %}">[back]</a>
  {% endblock content %}
  
  <!-- detail.html -->
  {% extends 'base.html' %}
  
  {% block content %}
  	<h1>DETAIL</h1>
  	<h2>{{ article.pk }} 번 글</h2>
  	{% if article.image %}
  		<img src="{{ article.image.url }}" alt="{{ article.image }}">
  	{% endif %}
  {% endblock content %}
  ```

  ```python
  # views.py
  
  @require_http_methods(['GET', 'POST'])
  def update(request, pk):
      article = get_objects_or_404(Article, pk=pk)
      if request.method == "POST":
          form = ArticleForm(request.POST, request.FILES, instance=article)
          if form.is_valid():
              form.save()
              return redirect('articles:detail', article.pk)
      else:
          form = ArticleForm(instance=article)
      context = {
          'article' : article,
          'form' : form,
      }
      return render(request, 'articles/update.html', context)
  ```

### Image Resizing

- `django-imagekit` 라이브러리

  ```
  $ pip install django-imagekit
  ```

  ```python
  # settings.py
  
  INSTALLED_APP = [
      ...
      'imagekit',
      ...
  ]
  
  # models.py
  
  from django.db import models
  from imagekit.models import ProcessImageField
  from imagekit.processors import Thumbnail
  
  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
      image = ProcessedImageField(
      	blank=True,
          processors=[Thumbnail(200,300)],
          format='JPEG',
          options={'quality': 90},
      )
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_not=True)
      
      def __str__(self):
          return self.title
  ```

  

