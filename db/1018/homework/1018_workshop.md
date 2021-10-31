# Django Model Relationship

## Django Project

> 1. 댓글 기능을 구현한다
> 2. 각 게시글에는 여러 댓글이 작성될 수 있다
> 3. 댓글 모델은 댓글내용 , 작성시간 , 수정시간 컬럼을 가지고 있다
> 4. 댓글목록은 detail 페이지에서 출력되며 같은 곳에서 작성할 수 있다
> 5. 각 댓글은 삭제 할 수 있다

- `models.py`

  ```python
  from django.db import models
  from django.db.models.deletion import CASCADE
  
  # Create your models here.
  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      def __str__(self):
          return self.title
  
  
  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
      content = models.TextField(max_length=200)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      def __str__(self):
          return self.content
  ```

- `admin.py`

  ```python
  from .models import Article, Comment
  
  admin.site.register(Comment)
  ```
  
- `forms.py`

  ```python
  from django import forms
  from .models import Article, Comment
  
  
  class ArticleForm(forms.ModelForm):
  
      class Meta:
          model = Article
          fields = ('title', 'content',)
          # exclude = ('title',)
  
  class CommentForm(forms.ModelForm):
  
      class Meta:
          model = Comment
          # fields = '__all__'
          exclude = ('article',)
  ```

- `urls.py`

  ```python
  from django.urls import path
  from . import views
  
  
  app_name = 'articles'
  urlpatterns = [
      path('', views.index, name='index'),
      path('create/', views.create, name='create'),
      path('<int:pk>/', views.detail, name='detail'),
      path('<int:pk>/delete/', views.delete, name='delete'),
      path('<int:pk>/update/', views.update, name='update'),
      path('<int:pk>/comments/', views.comments_create, name='comments_create'),
      path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
  ]
  ```

- `views.py`

  ```python
  def detail(request, pk):
      article = get_object_or_404(Article, pk=pk)
      comment_form = CommentForm()            
      comments = article.comment_set.all()    
      context = {
          'article': article,
          'comment_form': comment_form,
          'comments': comments,
      }
      return render(request, 'articles/detail.html', context)
      
  @require_POST
  def comments_create(request, pk):
      article = get_object_or_404(Article, pk=pk)
      comments_form = CommentForm(request.POST)
      if comments_form.is_valid():
          comment = comments_form.save(commit=False)
          comment.article = article
          comment.save()
      return redirect('articles:detail', article.pk)
  
  @require_POST
  def comments_delete(request, article_pk, comment_pk):
      comment = get_object_or_404(Comment, pk=comment_pk)
      comment.delete()
      return redirect('articles:detail', article_pk)
  ```

- `detail.html`

  ```html
  <!-- 댓글 목록 -->
    <h4>댓글 목록</h4>
    <ul>
      {% for comment in comments %}
        <li>
          {{ comment.content }}
          <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method = "POST" class='d-inline'>
            {% csrf_token %}
            <input type="submit" value='DELETE'>      
          </form>      
        </li>
      {% endfor %}
    </ul>
    <hr>
    <!-- 댓글 작성 form -->
    <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
      {% csrf_token %}
      {{ comment_form }}
      <input type="submit">
    </form>
  ```

  

