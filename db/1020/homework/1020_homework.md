

# Django Model Relationship

## 1. M:N True or False

> 각 문항을 읽고 맞으면 T, 틀리면 F를 작성하고 틀렸다면 그 이유도 함께 작성하시오
>
> 1. Django 에서 1: N 관계는 ForeignKeyField 를 사용하고 M :N 관계는 ManyToManyField 를 사용한다
> 2. ManyToManyField 를 설정하고 만들어지는 테이블 이름은 `앱이름_클래스이름_지정한 필드이름` 의 형태로 만들어진다.
> 3. ManyToManyField 의 첫번째 인자는 참조할 모델, 두번째 인자는 related_name 이 작성 되는데 두 가지 모두 필수적으로 들어가야 한다

1. T
2. T
3. F : `related_name` 필수 X



## 2. Like in templates

> 아래 빈 칸 (a) 와 (b) 에 들어갈 코드를 각각 작성하시오.
>
> ```python
> class Article(models.Model):
>     ...
>     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
>     like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
> ```
>
> ```html
> <!-- articles/index.html -->
> 
> {% for article in articles %}
> 	<p>{{ article.title }}</p>
> 	<form action="{% url 'articles:likes' article.pk %}" method="POST">
>     	{% csrf_token %}
>         {% if (a) in (b) %}
>         	<button>좋아요 취소</button>
>         {% else %}
>         	<button>좋아요</button>
>         {% endif%}
> 	</form>
> 	<span>{{ (b)|length }}명이 이 글을 좋아합니다.</span>
> {% endfor %}
> ```

- (a) : `request.user`
- (b) : `article.like.users`



## 3. Follow in views

> 모델 정보가 다음과 같을 때 빈칸 a, b, c, d, e 에 들어갈 코드를 각각 작성하시오
>
> ```python
> from django.db import models
> from django.conf import settings
> from django.contrib.auth.models import AbstractUser
> 
> class User(AbstractUser):
>     following = models.ManyToManyField('self', symmetrical=False, related_name="follower")
> ```
>
> ```python
> app_name = 'accounts'
> urlpatterns = [
> 	...,
>     path('<int:user_pk>/follow/', views.follow, name='follow'),
> ]
> ```
>
> ```python
> from django.contrib.auth import get_user_model
> 
> User = get_user_model()
> 
> @require_POST
> def follow(request, __(a)__):
>     person = get_object_or_404(User, pk=__(a)__)
>     user = request.user
>     
>     if user != person:
>         if person.__(b)__.__(c)__(pk=user.pk).exists():
>             person.__(b)__.__(d)__(user)
>         else:
>             person.__(b)__.__(e)__(user)
> 	return redirect('accounts:profile', person.username)
> ```

- (a) : `user_pk`
- (b) : `following`
- (c) : `filter`
- (d) : `remove`
- (e) : `add`



## 4. User AttributeError

> 아래와 같은 에러 메시지가 발생하는 이유와 이를 해결하기 위한 방법과 코드를 작성하시오
>
>  ![image-20211021095008998](C:\Users\j2woo\AppData\Roaming\Typora\typora-user-images\image-20211021095008998.png)

- `signup` 함수에서 `UserCreationForm` 사용, `auth.User` 모델 사용
- `CustomUserCreationForm` 정의

```python
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields
```



## 5. related _name

> 아래의 경우 related_name을 필수적으로 설정해야 한다. 그 이유를 설명하시오.
>
> ```python
> # articles/models.py
> from django.db import models
> from django.conf import settings
> 
> class Article(models.Model):
>     ...
>     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
>     like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
> ```

- `user`, `like_users` 모두 `user` 모델 참조 -> 기본 값 `article_set` 참조 중복

```python
# articles/models.py
from django.db import models
from django.conf import settings

class Article(models.Model):
    ...
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
```



## 6. follow templates

> person 변수에는 view함수에서 넘어온 유저 정보가 담겨 있고, 모델 정보가 아래와 같을 때, 빈칸 a, b, c, d, e에 들어갈 알맞은 코드를 각각 작성하시오.
>
> ```python
> app_name = 'accounts'
> urlpatterns = [
> 	...,
>     path('<int:user_pk>/follow/', views.follow, name='follow'),
> ]
> ```
>
> ```python
> from django.db import models
> from django.contrib.auth.models import AbstractUser
> 
> 
> class User(AbstractUser):
>     following = models.ManyToManyField('self', symmetrical=False, related_name="followers")
> ```
>
> ```html
> <!-- accounts/profile.html -->
> <h1>{{ person.username }}'s profile</h1>
> 
> <div>
>     <div>
>         팔로잉: {{ (a)|length }}
>         팔로워: {{ (b)|length }}
>     </div>
>     {% if (c) != (d) %}
>     	<div>
>         	<form action="{% url 'accounts:follow' (e) %}" method="POST">
>                 {% csrf_token %}
>                 {% if (c) in (b) %}
>                 	<button>Unfollow</button>
>                 {% else %}
>                 	<button>Follow</button>
>                 {% endif %}
>             </form>    
>     	</div>
>     {% endif %}
> </div>
> ```

- (a) : `following`
- (b) : `followers`
- (c) : `request.user`
- (d) : `person`
- (e) : `person.pk`
