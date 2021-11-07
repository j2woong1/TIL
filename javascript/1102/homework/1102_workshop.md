## JavaScript 심화

> 제공된 Django 프로젝트에서 게시글 좋아요 기능을 axios 라이브러리를 활용하여 AJAX 요청 처리될 수 있도록 구현하시오
>
> - 로그인 사용자의 좋아요 여부에 따라 아이콘이 변경되어야 한다
> - 변경된 총 좋아요 를 누른 사용자의 수가 반영되어야 한다
> - 위의 모든 요구 사항은 페이지 새로고침 없이 진행되어야 한다

```python
# articles/views.py

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)

        if article.like_users.filter(pk=request.user.pk).exists():
        # if request.user in article.like_users.all():
            # 좋아요 취소
            article.like_users.remove(request.user)
            liked = False
        else:
            # 좋아요 누름
            article.like_users.add(request.user)
            liked = True
        like_status = {
            'liked': liked,
            'count': article.like_users.count(),
        }
        return JsonResponse(like_status)
    return HttpResponse(status=401)
```

```html
<!-- articles/index.html -->
{% for article in articles %}
    <div>
      <form class="like-form" data-id="{{ article.pk }}">
        {% csrf_token %}
        {% if request.user in article.like_users.all %}
          <button id="like-{{ article.pk }}">좋아요 취소</button>
        {% else %}
          <button id="like-{{ article.pk }}">좋아요</button>
        {% endif %}
      </form>
    </div>
    <p>
      <span id="like-count-{{ article.pk }}">{{ article.like_users.all|length }}명이 이 글을 좋아합니다.</span>
    </p>
    <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
    <hr>
{% endfor %}
          
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const forms = document.querySelectorAll('.like-form')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

    forms.forEach(function (form) {
      form.addEventListener('submit', function (event) {
        event.preventDefault()
        const articleId = event.target.dataset.id
        
        axios.post(`http://127.0.0.1:8000/articles/${articleId}/likes/`, {}, {headers: {'X-CSRFToken': csrftoken}
        }).then(function (response) {
          const liked = response.data.liked
          const count = response.data.count

          const likeButton = document.querySelector(`#like-${articleId}`)
          if (liked) {
            likeButton.innerText = '좋아요 취소'
          } else {
            likeButton.innerText = '좋아요'
          }

          const likeCount = document.querySelector(`#like-count-${articleId}`)
          likeCount.innerText = `${count}명이 이 글을 좋아합니다.`
        })
      })
    })
    
  </script>
```

![image-20211102153510613](C:\Users\j2woo\AppData\Roaming\Typora\typora-user-images\image-20211102153510613.png)

![image-20211102153526127](C:\Users\j2woo\AppData\Roaming\Typora\typora-user-images\image-20211102153526127.png)

- 교수님 답안

  ```html
  {% for article in articles %}
      <div>
        <form class="like-form" data-id="{{ article.pk }}">
          {% csrf_token %}
          {% if request.user in article.like_users.all %}
            <button class="btn btn-link">
              <i id="like-{{ article.pk }}" class="fas fa-heart fa-lg" style="color:crimson;"></i>
            </button>
          {% else %}
            <button "btn btn-link">
              <i id="like-{{ article.pk }}" class="fas fa-heart fa-lg" style="color:black;"></i>
            </button>
          {% endif %}
        </form>
      </div>
      <p>
        <span id="like-count-{{ article.pk }}">
          {{ article.like_users.all|length }}
        </span>
        명이 이 글을 좋아합니다.
      </p>
      <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
      <hr>
  {% endfor %}
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css" integrity="sha512-YWzhKL2whUzgiheMoBFwW8CKV4qpHQAEuvilg9FAn5VJUDwKZZxkJNuGM4XkWuk94WCrrwslk8yWNGmY1EduTA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <script>
      const forms = document.querySelectorAll('.like-form')
      forms.forEach(function (form) {
        form.addEventListener('submit', function (event) {
          event.preventDefault()
          const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
          console.log(csrftoken)
          const articleId = event.target.dataset.id
          axios.post(`http://127.0.0.1:8000/articles/${articleId}/likes/`, {}, 
            {headers: {'X-CSRFToken': csrftoken}
          })
          .then(function (response) {
            console.log(response)
            console.log(response.data)
            const liked = response.data.liked
            const count = response.data.count
  
            const likeIconColor = document.querySelector(`#like-${articleId}`)
            if (liked) {
              likeIconColor.style.color = 'crimson'
            } else {
              likeIconColor.style.color = 'black'
            }
            const likeCount = document.querySelector(`#like-count-${articleId}`)
            likeCount.innerText = count
          })
          .catch((err) => {
            if (err.response.status === 401) {
              window.location.href = '/accounts/login/'
            }
          })
        })
      })
  </script>
  ```

  ![image-20211102173525089](C:\Users\j2woo\AppData\Roaming\Typora\typora-user-images\image-20211102173525089.png)

