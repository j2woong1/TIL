## Model Relationship II

### 병원 진료 기록 시스템

- 1:N 모델 관계 설정

  ```python
  # hospitals/models.py
  
  class Doctor(models.Model):
      name = models.TextField()
      
      def __str__(self):
          return f'{self.pk}번 의사 {self.name}'
      
  class Patient(models.Model):
      doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
      name = models.TextField()
      
      def __str__(self):
          return f'{self.pk}번 환자 {self.name}'
  ```

  - 새로운 예약 생성 불가능
    - 새로운 객체 생성 필요
  - 여러 의사 진료 기록 환자 한 명에 저장 불가능

- 중개 모델

  ```python
  # hospitals/models.py
  from django.db import models
  
  class Doctor(models.Model):
      name = models.TextField()
      
      def __str__(self):
          return f'{self.pk}번 의사 {self.name}'
      
  class Patient(models.Model):
      doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
      name = models.TextField()
      
      def __str__(self):
          return f'{self.pk}번 환자 {self.name}'
      
  class Reservation(models.Model):
      doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
      patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
      
      def __str__(self):
          return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
  ```

- `ManyToManyField`

  - 다대다 (M:N, many-to-many) 관계 설정 시 사용 모델 필드
  - 하나의 필수 위치인자 필요 (M:N 관계로 설정할 모델 클래스)

  ```python
  # hospitals/models.py
  from django.db import models
  
  class Doctor(models.Model):
      name = models.TextField()
      
      def __str__(self):
          return f'{self.pk}번 의사 {self.name}'
      
  class Patient(models.Model):
      doctor = models.ManyToManyField(Doctor)
      name = models.TextField()
      
      def __str__(self):
          return f'{self.pk}번 환자 {self.name}'
  ```

- `related_name`

  - target model (관계 필드 X 모델) -> source model (관계 필드 모델) 참조 시 manager 이름 설정
  - 역참조 시 사용하는 manage 이름 설정
  - ForeignKey related_name 동일

  ```python
  class Patient(models.Model):
      doctor = models.ManyToManyField(Doctor, related_name='patients')
      name = models.TextField()
  ```

### ManyToManyField

- 개념, 특징

  - RelatedManager로 추가, 제거
    - add(), remove()

- Arguments

  - `related_name`

  - `through`

    - 중개 테이블 직접 작성

  - `symmetrical`

    - `ManyToManyField`가 동일한 ㅁ델 가리키는 정의에서만 (on self)
    - symmetrical = True -> person_set 매니저 추가 X
    - source 모델 인스턴스 -> target 모델 인스턴스 참조 시 => target 모델 인스턴스 -> source 모델 인스턴스 자동 참조

    ```python
    from django.db import models
    
    class Person(models.Model):
        friends = models.ManyToManyField('self')
        # friends = models.ManyToManyField('self', symmetrical=False)
    ```

- Related Manager

  - 1:N, M:N 관련 컨텍스트

  - 1:N : target 모델 인스턴스만

  - M:N : 관련 두 객체에서 모두 사용

  - `add()`

    - 지정 객체를 관련 객체 집합에 추가
    - 이미 존재하는 관계에 사용 시 관계 복제 X
    - 인자 : 모델 인스턴스, 필드 값 (PK)

    ```python
    doctor1 = Doctor.objects.create(name='justin')
    patient1 = Patient.objects.create(name='tony')
    
    doctor1.patient_set.add(patient1)
    # or
    patient1.doctors.add(doctor1)
    ```

  - `remove()`

    - 관련 객체 집합에서 지정 모델 객체 제거
    - 인자 : 모델 인스턴스, 필드 값 (PK)

    ```python
    doctor1 = Doctor.objects.get(pk=1)
    patient1 = Patient.objects.get(pk=1)
    
    doctor1.patient_set.remove(patient1)
    # or
    patient1.doctors.remove(doctor1)
    ```

- `through`

  ```python
  # hospitals/models.py
  from django.db import models
  
  class Doctor(models.Model):
      name = models.TextField()
      
      def __str__(self):
          return f'{self.pk}번 의사 {self.name}'
      
  class Patient(models.Model):
      doctor = models.ManyToManyField(Doctor, through='Reservation')
      name = models.TextField()
      
      def __str__(self):
          return f'{self.pk}번 환자 {self.name}'
      
  class Reservation(models.Model):
      doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
      patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
      symptom = models.TextField()
      reserved_at = models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
          return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
  ```

- 중개 테이블 필드 생성 규칙

  - source model != target model
    - id
    - `<containing_model_id`
    - `<other_model>_id`
  - `ManyToManyField`가 동일 모델 가리키는 경우
    - id
    - `from_<model>_id`
    - `to_<model>_id`

### Like

- ManyToManyField 작성 후

  ```python
  # articles/models.py
  
  class Article(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
  ```

- User ~ Article DB API

  - `article.user` : 게시물 작성 유저, 1:N
  - `article.like_users` : 게시물 좋아요 유저, M:N
  - `user.article_set` : 유저 작성 게시글, 역참조, 1:N
  - `user.like_articles` : 유저 좋아요 게시글, 역참조, M:N

- url 작성

  ```python
  # articles/urls.py
  urlpatterns = [
      path('<int:article_pk>/likes/', views.likes, name='likes'),
  ]
  ```

- view 함수 작성

  ```python
  # articles/views.py
  
  @require_POST
  def likes(request, article_pk):
      if request.user.is_authenticated:
          article = get_object_or_404(Article, pk=article.pk)
          if article.like_users.filter(pk=request.user.pk).exists():
          # if request.user in article.like_users.all():
          	article.like_users.remove(request.user)
          else:
              article.like_users.add(request.user)
          return redirect('articles:index')
      return redirect('accounts:login')
  ```

  - `exists()`
    - QuerySet에 결과 포함 시 True, 없으면 False
    - 특정 개체 존재 여부 검색
    - 고유 필드 (primary key) 있는 모델이 QuerySet 구성원인지 여부

  ```html
  <!-- articles/index.html -->
  {% extends 'base.html' %}
  {% block content %}
  	<h1>Articles</h1>
  	{% if request.user.is_authenticated %}
  		<a href="{% url 'articles:create' %}">[CREATE]</a>
  	{% else %}
  		<a href="{% url 'articles:login' %}">[새 글을 작성하려면 로그인하세요.]</a>
  	{% endif %}
  	<hr>
  	{% for article in articles %}
  		<p><b>작성자 : {{ article.user }}</b></p>
  		<p>글 번호 : {{ article.pk }}</p>
  		<p>글 제목 : {{ article.title }}</p>
  		<p>글 내용 : {{ article.content }}</p>
  		<div>  <!-- like 출력 -->
          	<form action="{% url 'articles:likes' article.pk %}" method="POST">
                  {% csrf_token %}
                  {% if user in article.like_users.all %}
                  	<input type="submit" value="좋아요 취소">
                  {% else %}
  					<input type="submit" value="좋아요">
                  {% endif %}
              </form>    
  		</div>
  		<a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
  	{% endfor %}
  {% endblock content %}
  ```

### Profile Page

- url 작성

  ```python
  # articles/urls.py
  urlpatterns = [
      path('<username>/', views.profile, name='profile'),
  ]
  ```

- view 함수 작성

  ```python
  # articles/views.py
  from django.shortcuts import render, get_object_or_404
  from django.contrib.auth import get_user_model
  
  def profile(request, username):
      person = get_object_or_404(get_user_model(), username=username)
      context = {
          'person': person,
      }
      return render(request, 'accounts/profile.html', context)
  ```

- 페이지 작성

  ```html
  <!-- accounts/profile.html -->
  {% extends 'base.html' %}
  {% block content %}
  	<h1>{{ person.username }}님의 프로필</h1>
  	<hr>
  	<h2>{{ person.username }}'s 게시글</h2>
  	{% for article in person.article_set.all %}
  		<div>{{ article.title }}</div>
  	{% endfor %}
  	<hr>
  	<h2>{{ person.username }}'s 댓글</h2>
  	{% for comment in person.comment_set.all %}
  		<div>{{ comment.content }}</div>
  	{% endfor %}
  	<hr>
  	<h2>{{ person.username }}'s 좋아요한 게시글</h2>
  	{% for article in person.like_articles.all %}
  		<div>{{ article.title }}</div>
  	{% endfor %}
  	<hr>
  	<a href="{% url 'articles:index' %}">back</a>
  {% endblock content %}
  ```

- base 페이지

  ```html
  <!-- base.html -->
  <body>
      <div class=container>
          {% if request.user.is_authenticated %}
          	<h3>Hello, {{ user }}</h3>
          	<a href="{% url 'accounts:profile' user.username %}">내 프로필</a>
          	...
      </div>
  </body>
  ```

- index 페이지

  ```html
  <!-- articles/index.html -->
  <p>
      <b>작성자 : <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></b>
  </p>
  ```

### Follow

- ManyToManyField 작성

  ```python
  # accounts/models.py
  
  class User(AbstractUser):
      followings = models.ManyToManyField('self', symmetrical=False, related_name='followings')
  ```

- url 작성

  ```python
  # articles/urls.py
  urlpatterns = [
      path('<int:user_pk>/follow/', views.follow, name='follow'),
  ]
  ```

- view 함수 작성

  ```python
  # articles/views.py
  
  @require_POST
  def follow(request, user_pk):
      if request.user.is_authenticated:
          person = get_object_or_404(get_user_model(), pk=user_pk)
          if person != request.user:
              if person.followers.filter(pk=request.user.pk).exists():
              # if request.user in person.followers.all():
              	person.followers.remove(request.user)
              else:
                  person.followers.add(request.user)
          return redirect('accounts:profile', person.username)
      return redirect('accounts:login')
  ```

- profile 페이지에 팔로우, 언팔로우 버튼 작성

  - 팔로잉 수 / 팔로워 수 출력
  - 자기 자신 팔로우 X

  ```html
  <!-- accounts/profile.html -->
  {% extends 'base.html' %}
  {% block content %}
  	<h1>{{ person.username }}님의 프로필</h1>
  	<div>
      	<div>
              팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length }}
          </div>  
          {% if user != person %}
          	<div>
                  <form action="{% url 'accounts:follow' person.pk %}" method="POST">
                      {% csrf_token %}
                      {% if user in person.followers.all %}
                      	<input type="submit" value="Unfollow">
                      {% else %}
                      	<input type="submit" value="Follow">
                      {% endif %}
                  </form>
  	        </div>
          {% endif %}
  	</div>
  {% endblock content %}
  ```

  