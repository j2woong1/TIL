# 02_django_Admin

## Admin Site

> 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지 

**개념**

- 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
-  Article class를 `admin.py` 에 등록하고 관리
- record 생성 여부 확인에 매우 유용하고 CRUD 로직을 확인하기에 편리하다.

<br>

**관리자 생성**

```bash
$ python manage.py createsuperuser
```

- 관리자 계정 생성 후 서버를 실행한 다음 `/admin` 으로 가서 관리자 페이지 로그인

- 모델을 등록하지 않으면 기본적인 사용자 정보만 확인 할 수 있다.

- `admin.py` 로 가서 관리자 사이트에 등록하여 내가 만든 record를 보기 위해서는 Django 서버에 등록


<br>

**model 등록**

```python
# articles/admin.py

from django.contrib import admin
from .models import Article

# admin site에 등록(register)한다.
admin.site.register(Article)
```

<br>

**admin site확인**

- admin 사이트에 방문해서 우리가 현재까지 작성한 글들을 확인
- `admin.py` 는 관리자 사이트에 Article 객체가 관리 인터페이스를 가지고 있다는 것을 알려주는 것
- 이렇게 admin 사이트에 등록된 모습이 어딘가 익숙하다? 
- 바로 `models.py` 에 정의한 `__str__` 의 형태로 객체가 표현된다.

<br>

**ModelAdmin options**

> •[https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#modeladmin-options](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/)

`list_display`

- models.py 정의한 각각의 속성(컬럼)들의 값(레코드)를 admin 페이지에 출력하도록 설정

  ```python
  # articles/admin.py
  
  from django.contrib import admin
  from .models import Article
  
  class ArticleAdmin(admin.ModelAdmin):
      list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
  
  admin.site.register(Article, ArticleAdmin)
  ```

<br>

------
