## Django REST Framework

> - DRF를 활용하여 게시글 관련 REST API 서버를 구축하시오.
> - 프로젝트는 my_api, 앱은 articles으로 만들어 진행한다.
> - DRF 기본 템플릿을 활용하여 요청을 테스트한다.

### 1. Model

> admin 페이지 혹은 djang-seed 라이브러리를 활용하여 5개의 데이터를 생성한다.
>
> ```python
> class Article(models.Model):
>     title = models.CharField(max_length=100)
>     content = models.TextField()
>     created_at = models.DateTimeField(auto_now_add=True)
>     updated_at = models.DateTimeField(auto_now=True)
> ```

```bash
python manage.py seed articles --number=5
```



### 2. Serializers

> - ArticleListSerializer
>   - 모든 음악 정보를 반환하기 위한 ModelSerializer
>   - id, title 필드 정의
> - ArticleSerializer
>   - 음악 상세 정보를 반환 및 생성하기 위한 ModelSerializer
>   - 모든 필드 정의

```python
from rest_framework import serializers
from .models import Article

# 모든 음악 정보
class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', )

# 음악 상세 정보
class ArticleSeriailizer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'
```



### 3. URL & Views

> - GET api/v1/articles/
>   - 모든 게시글의 id와 title 컬럼을 JSON 데이터 타입으로 응답한다.
> - POST api/v1/articles/
>   - 검증에 성공하는 경우 새로운 게시글의 정보를 DB에 저장하고, 저장된 게시글의 정보를 응답한다.
>   - 검증에 실패하는 경우 400 Bad Request 예외를 발생시킨다.
> - GET api/v1/articles/<article_pk>/
>   - 특정 게시글의 모든 컬럼을 JSON 데이터 타입으로 응답한다.
> - PUT & DELETE api/v1/articles/<article_pk>/
>   - PUT 요청인 경우 특정 게시글의 정보를 수정한다.
>   - 검증에 성공하는 경우 수정된 게시글의 정보를 DB에 저장한다.
>   - 검증에 실패할 경우 400 Bad Request 예외를 발생시킨다.
>   - 수정이 완료되면 수정한 게시글의 정보를 응답한다.
>   - DELETE 요청인 경우 특정 게시글을 삭제한다.
>   - 삭제가 완료되면 삭제한 게시글의 id를 응답한다.

```python
### api/urls.py -- urlpatterns
    path('api/v1/', include('articles.urls')),

### articles/urls.py -- urlpatterns
	path('articles/', views.article_list_create),
    
### articles/views.py
from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article
from .serializers import ArticleListSerializer, ArticleSeriailizer

@api_view(['GET', 'POST'])
def article_list_create(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        serializer = ArticleSeriailizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_update_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)  
        return Response(serializer.data)  
    elif request.method == 'PUT':
        serializer = ArticleSerializer(instance=article, data=request.data)  
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)  
    else:
        article.delete()
        return Response({'message': f'{article_pk}번 글이 정상적으로 삭제되었습니다.'})
```

