## Django Form

### Form Class

#### Django's forms

- 유효성 검사 툴
- 렌더링 데이터 준비, 재구성
- HTML forms 생성
- 데이터 수신, 처리

#### Form Class

- form 내 field 배치, 디스플레이 widget, label, 초기값, 에러 메세지 결정

- 선언

  ```python
  # articles/forms.py
  
  from django import forms
  class ArticleForm(forms.Form):
      title = forms.CharField(max_length=10)
      content = forms.CharField()
  ```
  - Model 선언 유사, 같은 필드
  - forms 라이브러리 파생 Form 클래스 상속

- 사용

  ```python
  # article.views.py
  
  from .forms import ArticleForm
  def new(request):
      form = ArticleForm()
      context = {
          'form' : form,
      }
      return render(request, 'articles/new.html', context)
  ```

  ```html
  <!-- new.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  	<h1 class="text-center">NEW</h1>
  	<form action="{% url 'articles:create' %}" method="POST">
      	{% csrf_token %}
          {{ form.as_p }}
          <input typ="submit">
  	</form>
  	<hr>
  	<a href="{% url 'articles:index' %}">[back]</a>
  {% endblock content %}
  ```

### Form rendering options

- `as_p()` : 각 필드 단락 (`<p>`)로 감싸져서 렌더링
- `as_ul()` : 각 필드 목록 항목 (`<li>`)로 감싸져서 렌더링, `<ul>` 태그는 직접 작성
- `as_table()` : 각 필드 테이블 (`<tr>`)로 감싸져서 렌더링, `<tr>` 태그는 직접 작성

### HTML input 요소 표현 방법

- form fields : input 유효성 검사 로직 처리, 템플릿에서 직접 사용

- widget : HTML input 요소 렌더링, GET/POST 딕셔너리에서 추출, form fields에 할당

  ```python
  # articles/forms.py
  from django import forms
  
  class ArticleForm(forms.Form):
      title = forms.CharField(max_length=10)
      content = forms.CharField(widget=forms.Textarea)
  ```

  ```python
  # articles/forms.py
  from django import forms
  
  class ArticleForm(forms.Form):
      REGION_A = 'sl'
      REGION_B = 'dj'
      REGION_C = 'gm'
      REGION_D = 'bs'
      REGION_E = 'sl'
      REGION_CHOICES = [
          (REGION_A, '서울'),
          (REGION_B, '대전'),
          (REGION_C, '광주'),
          (REGION_D, '구미'),
          (REGION_E, '부산'),
      ]
      
      title = forms.CharField(max_length=10)
      content = forms.CharField(widget=forms.Textarea)
      region = forms.ChoiceField(choices=REGIONS_CHOICES, widget=forms.Select())
  ```

### ModelForm

- Article 모델이 있고, 게시글 제출 양식 

- Model을 통해 Form Class 제작

  ```python
  # articles.forms.py
  
  from django import forms
  from .models import Article
  
  class ArticleForm(forms.ModelForm):
      class Meta:
          model = Article
          fields = '__all__'
          # exclude = ('title',)
  ```

  - ModelForm 상속

#### Meta Class

- 모델 정보 작성

```python
# articles.views.py

def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
   	return redirect('articles:new')
```

- `is_valid` : 유효성 검사 -> boolean
- `save()` 
  - form에 바인딩 된 데이터에서 DB 객체 제작 후 저장
  - ModelForm 하위 클래스 : 기존 모델 instance를 키워드 인자 instance로
    - 제공 시 : UPDATE
    - 제공 X : CREATE
  - 유효성 확인 X 시 : form.error 확인 

```python
# Create a form instance from POST data
form = ArticleFom(request.POST)

# CREATE
# Save a new article object from the form's data
new_article = f.save()

# UPDATE
# Create a form to edit an existing Article, but use POST data to populate the form
article = Article.objects.get(pk=1)
form = ArticleForm(request.POST, instance=article)
form.save()
```

```python
# articles.views.py

def create(request):
    if request.methpd == "POST":
    	form = ArticleForm(request.POST)
    	if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
        context = {
            'form' : form,
        }
   	return render('request, 'articles/create.html, context)
```

```html
<!-- create.html -->

{% extends 'base.html' %}

{% block content %}
	<h1 class="text-center">CREATE</h1>
	<form action="{% url 'articles:create' %}" method="POST">
    	{% csrf_token %}
        {{ form.as_p }}
        <input typ="submit">
	</form>
	<hr>
	<a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}

<!-- index.html -->

{% extends 'base.html' %}

{% block content %}
	<h1 class="text-center">Articles</h1>
	<a href="{% url 'articles:create' %}">CREATE</a>
	<hr>
	{% for article in articles %}
		<p>글 번호 : {{ article.pk }}</p>
		<p>글 제목 : {{ article.title }}</p>
		<p>글 내용 : {{ article.content }}</p>
		<a href="{% url 'articles:detail' article.pk %}">[detail]</a>
		<hr>
	{% endfor %}
{% endblock content %}
```

#### Widget 적용

```python
# articles.forms.py

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widget = {
            'title' : forms.TextInput(attrs={
                'class' : 'title',
                'placeholder' : 'Enter the title',
                'maxlength' : 10,
            })
        }
```

```python
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
    	label='제목',
        widget=forms.TextInput(
        	attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
                'maxlength' : 10,
            }
        )
    )
    content = forms.CharField(
    	label='내용'
        widget=forms.Textarea(
        	attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': 'Please enter your content'
        }
    )
    class Meta:
        model = Article
        fields = '__all__'
```

### Delete

```python
# views.py

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method = 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)
```

```html
<!-- detail.html -->
<form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
</form>
```

### UPDATE

```python
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method = 'POST':
        # Create a form to edit an existing Article,
        # but use POST data to populate the form.
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return rediect('articles:detail', article.pk)
    else:
        # Creating a form to change an existing article.
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
        'article' : article,
    }
    return redirect(request, 'articles/update.html', context)
```

```html
<!-- update.html -->

{% extends 'base.html' %}

{% block content %}
	<h1 class="text-center">UPDATE</h1>
	<form action="{% url 'articles:update' article.pk %}" method="POST">
    	{% csrf_token %}
        {{ form.as_p }}
        <input typ="submit">
	</form>
	<hr>
	<a href="{% url 'articles:detail' article.pk %}">[back]</a>
{% endblock content %}

<!-- detail.html -->

<a href="{% url 'articles:update' article.pk %}">UPDATE</a>
```

### Form & ModelForm

- Form
  - 유효성 검사 후 cleaned_data 딕셔너리 생성
  - 가져온 후 .save()
  - model 연관 X 데이터 받을 때
- ModelForm
  - django가 해당 model에서 양식에 필요한 정보 정의
  - 바로 .save()

### Rendering fields manually

```html
<!-- articles/create.html -->

<h1>CREATE</h1>
...
<hr>

<form action="" method="POST">
    {% csrf_token %}
    <div>
        {{ form.title.errors }}
        {{ form.title.label_tag }}
        {{ form.title }}
    </div>
    <div>
        {{ form.content.errors }}
        {{ form.content.label_tag }}
        {{ form.content }}
    </div>
    {% for field in form %}
    	{% if field.errors %}
    		{% for error in field.errors %}
    			<div class="alert alert-warning" role="alert">{{ error|escape }}</div>
    		{% endfor %}
    	{% endif %}
    	<div class="form-group">
    		{{ field.label_tag }}
            {{ field }}
    	</div>
    {% endfor %}
    <button class="btn btn-primary">작성</button>
</form>
```

```python
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
    	label='제목',
        widget=forms.TextInput(
        	attrs={
                'class': 'my-title form-control',
                'placeholder': 'Enter the title',
                'maxlength' : 10,
            }
        )
    )
    content = forms.CharField(
    	label='내용'
        widget=forms.Textarea(
        	attrs={
                'class': 'my-content form-control',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': 'Please enter your content'
        }
    )
```

```
$ pip install django-bootstrap-v5
```

```html
<!-- articles/base.html -->

{% load bootstrap5 %}

<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  {% bootstrap_css %}
  <title>Document</title>
</head>
<body>
  <div class="container">
    {% block content %}
    {% endblock content %}
  </div>
  {% bootstrap_javascript %}
</body>
</html>

```

### Handling HTTP requests

- Django shortcut functions
  - `render()`, `redirect()`, `get_list_or_404()`
  - `get_object_or_404()`
    - model manager object에서 get 호출 -> 없으면 HTTP 404
- View decorators
  - Allowed HTTP methods
    - 요청 메서드에 따라 view 함수 access 제한
    - HttpResponseNotAllowed
    - `require_http_methods()` : view 함수가 특정한 method 요청에만 허용
    - `require_POST()` : view 함수가 POST method만 요청 승인
    - `require_safe()`