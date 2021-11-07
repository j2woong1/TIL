## JavaScript 심화

> 제공된 Django 프로젝트에서 팔로우 기능을 axios 라이브러리를 활용하여 AJAX 요청으로 처리될 수 있도록 구현하시오
>
> - 로그인 사용자의 팔로우 여부에 따라 버튼의 텍스트와 색깔이 변경되어야 한다
> - 변경된 총 팔로워 수가 반영되어야 한다
> - 위 모든 요구 사항은 페이지 새로고침 없이 진행되어야 한다

```html
<!-- accounts/profile.html -->
{% extends 'base.html' %}

{% block content %}
<h1>{{ person.username }}님의 프로필</h1>

{% with followings=person.followings.all followers=person.followers.all %}
  <div>
    <div id="follow-count">
      팔로잉 : {{ followings|length }} / 팔로워 : {{ followers|length }}
    </div>
    {% if request.user != person %}
      <div>
        <form id="follow-form" data-user-id ="{{ person.pk }}">
          {% csrf_token %}
          {% if request.user in followers %}
            <button>언팔로우</button>
          {% else %}
            <button class="btn-primary" role="button">팔로우</button>
          {% endif %}
        </form>
      </div>
    {% endif %}
  </div>
{% endwith %}

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  const followForm = document.querySelector('#follow-form') 
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

  followForm.addEventListener('submit', function (event) {
    event.preventDefault()
    const userId = event.target.dataset.userId

    axios({
      method: 'post',
      baseURL: 'http://127.0.0.1:8000/',
      url: `/accounts/${userId}/follow/`,
      headers: {'X-CSRFToken': csrftoken}
    })
  
    .then(response =>{
      const isFollowed = response.data.followed
      const followBtn = document.querySelector('#follow-form > button')
      if (isFollowed) {
        followBtn.innerText = '언팔로우'
        followBtn.setAttribute('class', 'btn-danger')
      } else {
        followBtn.innerText = '팔로우'
        followBtn.setAttribute('class', 'btn-primary')
      }

      const followers_count = response.data.followers_count
      const followings_count = response.data.followings_count
      const followCountDiv = document.querySelector('#follow-count')
      followCountDiv.innerText = `팔로잉 : ${followings_count} / 팔로워 : ${followers_count}`
      })

    })
</script>

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

<h2>{{ person.username }}'s likes</h2>
{% for article in person.like_articles.all %}
  <div>{{ article.title }}</div>
{% endfor %}

<hr>

<a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}
```

```python
# accounts/views.py

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        # 팔로우 받는 사람
        you = get_object_or_404(get_user_model(), pk=user_pk)
        me = request.user

        # 나 자신은 팔로우 할 수 없다.
        if you != me:
            if you.followers.filter(pk=me.pk).exists():
            # if request.user in person.followers.all():
                # 팔로우 끊음
                you.followers.remove(me)
                followed = False
            else:
                # 팔로우 신청
                you.followers.add(me)
                followed = True
            follow_status = {
                'followed': followed,
                'followers_count': you.followers.count(),
                'followings_count': you.followings.count(),
            }
        return JsonResponse(follow_status)
    return HttpResponse(status=401)
```

![image-20211102141059261](C:\Users\j2woo\AppData\Roaming\Typora\typora-user-images\image-20211102141059261.png)

![image-20211102141111987](C:\Users\j2woo\AppData\Roaming\Typora\typora-user-images\image-20211102141111987.png)

