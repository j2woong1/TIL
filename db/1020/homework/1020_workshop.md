# Django Model Relationship

## Django Project

> 데이터베이스 M:N 관계를 활용하여 팔로우 기능을 구현하시오.
>
> ### 1. Model & Form
>
> 팔로우 기능 구현을 위한 모델을 세팅한다
> 팔로우 기능을 구현하기 위해 User 모델을 대체한다
>
> ### 2. url & view
>
> `/accounts/<username>/`
> 유저 프로필 페이지 기능을 구현한다
>
> - 로그인한 유저만 팔로우를 할 수 있다
>
> `/accounts/<int:user_pk>/follow/`
> 팔로우를 하기 위한 기능을 구현한다
>
> - 로그인한 유저만 팔로우를 할 수 있다
> - 본인은 팔로우를 할 수 없다
>
> ### 3. template
>
> index.html의 username 에 profile 로 갈 수 있는 링크를 설정한다 .
> 팔로잉 여부에 따라 팔로우와 언팔로우 버튼이 토글 될 수 있도록 구성한다 .
>
> - 로그인한 유저 자신의 프로필 페이지에서는 팔로우 & 언팔로우 버튼이 보이지 않는다
>
> - 작성자의 팔로잉 , 팔로워 숫자를 보여주고 유저의 이름을 모두 출력한다
>
>   (선택사항 )
>   해당 프로필 유저가 작성한 모든 글의 제목과 해당 글의 좋아요 개수를 함께 출력한다

![image-20211021144451752](C:\Users\j2woo\AppData\Roaming\Typora\typora-user-images\image-20211021144451752.png)

```python
# accounts/views.py
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
    
    
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
        return redirect('accounts:profile', person.username)
    return redirect('accounts:login')
```

```python
# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

```html
<!-- accounts/profile.html -->
{% extends 'base.html' %}

{% block content %}
  {% with followings=person.followings.all followers=person.followers.all %}
  <h1>{{ person.username }}님의 프로필</h1>
  <div>
    <div>팔로잉 수: {{ followings|length }} / 팔로워 수 : {{ followers|length }}</div>
  </div>
  <div>
    {% if user != person %}
      <div>
        <form action="{% url 'accounts:follow' person.pk %}" method="POST">
          {% csrf_token %}
          {% if user in followers %}
            <input type="submit" value="Unfollow">
          {% else %}
            <input type="submit" value="follow">
          {% endif %}
        </form>
      </div>
    {% endif %}
  </div>
  {% endwith %}

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

