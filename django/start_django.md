# Start Django

- 가상환경, 필요 라이브러리 설치

  ```
  $ python -m venv venv
  $ source venv/Scripts/activate
  $ pip install django
  $ pip install django-extensions
  $ pip install django-seed
  $ pip install ipython
  $ pip freeze > requirements.txt
  ```

- django 프로젝트 시작하기

  ```
  $ django-admin startproject crud
  $ cd crud
  $ python manage.py startapp articles
  $ python manage.py shell_plus
  ```

- `settings.py`

  ```
  INSTALLED_APPS = [
      # Local apps
      'articles',
  
      # Third Party apps
      'django_extensions',
      'django_seed',
  
      # Django Apps
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  
  TEMPLATES = [
      {
          ...,
          'DIRS': [BASE_DIR / 'templates'],
          ...,
      },
  ]
  
  LANGUAGE_CODE = 'ko-kr'
  
  TIME_ZONE = 'Asia/Seoul'
  ```

- `models.py`

  ```python
  # articles/models.py
  class Article(models.Model):
      title = models.CharField(max_length=10) 
      content = models.TextField() 
  ```

- `makemigrations` 

  ```
  $ python manage.py makemigrations
  ```

- `migrate` : DB 적용

  ```
  $ python manage.py migrate
  ```

- `sqlmigrate`

  ```
  $ python manage.py sqlmigrate 앱이름 0001
  ```

- `showmigrations`

  ```
  $ python manage.py showmigrations
  ```

- model 수정

  ```python
  # articles/models.py
  class Article(models.Model):
      title = models.CharField(max_length=10) 
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

  ```
  You are trying to add the field 'created' with 'auto_now_add=True' to article without a default; the database needs something to populate existing rows.
   1) Provide a one-off default now (will be set on all existing rows)
   2) Quit, and let me add a default in models.py
  ```

  - `created_at` default 설정 : 1

  ```
  Please enter the default value now, as valid Python
  The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
  Type 'exit' to exit this prompt
  ```

  - `timezone.now` 함수 자동 설정 : 빈 값으로 enter ->  `migrate`

- admin 생성

  ```
  $ python manage.py createsuperuser
  ```

- admin 등록

  ```python
  # articles/admin.py
  
  from django.contrib import admin
  from .models import Articles
  
  class ArticleAdmin(admin.ModelAdmin):
      list_display = ('pk', 'title', 'content', 'created_at', 'updated_at,')
  
  admin.site.register(Article)
  ```

  

