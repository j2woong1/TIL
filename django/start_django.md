# Start Django

- 프로젝트 생성

```
$ django-admin startproject 프로젝트이름
```

- 앱 생성

```
$ python manage.py startapp 앱이름
```

- `models.py`

  ```python
  # articles/models.py
  class Article(models.Model):
      title = models.CharField(max_length=10) # 필드 -> 클래스 속성, 속성 -> 열
      content = models.TextField() # 필드 -> 클래스 속성, 속성 -> 열
  ```

  - 어떤 타입으로 정의
  - `CharField(max_length=None, **options)`
    - 길이 제한 문자열
    - `max_length` : 필수 인자
    - 필드 최대 길이, DB 레벨, 유효성 검사
  - `TextField(**options)`
    - 글자 수 많을 때
    - `max_length` : `textarea` 위젯  반영, 모델, DB 수준 적용 X

- `makemigrations`

  ```
  $ python manage.py makemigrations
  ```

- `migrate`

  ```
  $ python manage.py migrate
  ```

- `sqlmigrate`

  ```
  $ python manage.py sqlmigrate 앱이름 0001
  ```

  ```sql
  BEGIN;
  --
  -- Create model Article
  --
  CREATE TABLE "articles_article"
  ("id" integer NOT NULL PRIMARY KEY AUTOINCERMENT,
  "title" varchar(10) NOT NULL, "content" text NOT NULL);
  COMMIT;
  ```

- `showmigrations`

  ```
  $ python manage.py showmigrations
  ```

  ```
  
  ```

  

