# Django 기본



## 가상환경 설정

```bash
$ python -m venv venv
$ source venv/Scripts/activate
$ pip install django django-extensions ipython django-bootstrap-v5 djangorestframework django-seed pip install drf-yasg   
$ pip freeze > requirements.txt
```



## 프로젝트 시작

```bash
$ django-admin startproject project_name  # 이름
$ cd project_name  # 이름
$ python manage.py startapp app_name  # 이름
```

```python
# settings.py

INSTALLED_APPS = [
    # Local apps
    'articles',
    'accounts',

    # Third Party apps
    'django_extensions',
    'bootstrap5',

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



## Custom User ⭐⭐⭐

```python
# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # pass
    
    # followings
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

```python
# settings.py

AUTH_USER_MODEL = 'accounts.User'
```



그 다음 **06_django_model_relationship_ll** 폴더 코드 복붙



## 순서

#### 템플릿 폴더 생성

```bash
$ mkdir templates
$ mkdir -p articles/templates/articles
$ mkdir -p accounts/templates/accounts
```



#### 프로젝트 루트

- urls.py
- templates/base.html



### Articles 코드 복붙

- model.py - forms.py - urls.py - views.py - templates



### Accounts 코드 복붙

model.py - forms.py - urls.py - views.py - templates



#### 관리자

```bash
$ python manage.py createsuperuser
```

```python
# articles/admin.py

from django.contrib import admin
from .models import Article, Comment

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
```

```python
# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

admin.site.register(User, UserAdmin)
```

