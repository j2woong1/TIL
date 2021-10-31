## REST API

### HTTP

- HyperText Transfer Protocol
- 웹 상에서 컨텐츠 전송 약속, HTML 문서 리소스 가져오는 프로토콜
- 웹에서 이루어지는 모든 데이터 교환 기초
  - 요청 (request) : 클라이언트에 의해 전송되는 메시지
  - 응답 (response) : 서버에서 응답으로 전송되는 메시지
- 기본 특성
  - Stateless
  - Connectless
- 쿠키, 세션 -> 서버 상태 요청, 연결
- request methods
  - `GET`, `POST`, `PUT`, `DELETE`
- response status code
  - informational responses : 1xx
  - successful responses : 2xx
  - redirection messages : 3xx
  - client error responses : 4xx
  - server error responses : 5xx
- 리소스 식별 : URI (Uniform Resoruce Identifier)로 식별
  - URI : 주소
    - URL (Locator)
      - 웹 주소, 링크
    - URN (Name)
      - 자원 위치에 영향 X
    - 구조 : `https://www.example.com:80/path/to/myfile.html/?key=value#quick-start`
      - Scheme (protocol) : `https://`
      - Host : `www.example.com`, 요청 받는 웹 서버 이름
      - Port : `:80`
      - Path : `/path/to/myfile.html`, 리소스 경로, 추상화 형태 구조
      - Query (Identifier) : `?key=value`, 매개 변수, &로 구분 key-value 목록
      - Fragment : `#quick-start`, Anchor, 해당 문서 (HTML) 특정 부분 보여주기, 부분 식별자 (Fragment Identifier), # 뒤는 서버에 보내지 X

### RESTful API

- API
  - Application Programming Interface
  - 프로그래밍 언어가 제공하는 기능 수행하게 하는 인터페이스 : 애플리케이션과 프로그래밍으로 소통
  - HTML, XML, JSON
- REST : REpresentational State Transfer, 자원 정의 방법
  - 자원
    - URI
  - 행위
    - HTTP Method (GET, POST, PUT, DELETE)
  - 표현
    - 자원, 행위 -> 결과물
    - JSON
- JSON : JavaScript Object Notation
  - 사람 읽거나 쓰기, 기계 파싱 (해석, 분석)
  - key-value 구조
- RESTful API
  - REST 원리 설계 API
  - 클라이언트 요청 -> JSON 응답 서버

### Response

- Init Project

  ```python
  # 설치 app 확인
  # settings.py
  
  INSTALLED_APPS = [
      'articles',
      'django_seed',
  ]
  ```

  ```python
  # 작성 url 확인
  # my_api/urls.py
  
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/v1/', include('article.urls')),
  ]
  
  # articles/urls.py
  
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('html/', views.article_html),
      path('json-1/', views.article_json_1),
      path('json-2/', views.article_json_2),
      path('json-3/', views.article_json_3),
  ]
  ```

- Create Dummy Data

  ```python
  # models.py
  
  from django.db import models
  
  class Article(models.Model):
      title = models.CharField(max_length=100)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

  ```bash
  $ python manage.py migrate
  $ python manage.py seed articles --number=20
  ```

- HTML

  ```python
  # articles/urls.py
  
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('html/', views.article_html),  # HTML 응답 서버
      path('json-1/', views.article_json_1),
      path('json-2/', views.article_json_2),
      path('json-3/', views.article_json_3),
  ]
  ```

  ```python
  # articles/views.py
  
  from django.shortcuts import render
  from .models import Article
  
  def article_html(request):
      articles = Article.objects.all()
      context = {
          'articles': articles,
      }
      return render(request, 'articles/article.html', context)
  ```

  ```html
  <!-- articles/article.html -->
  
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
  </head>
  <body>
    <h1>Article List</h1>
    <hr>
    <p>
      {% for article in articles %}
        <h2>{{ article.pk }}번 글. {{ article.title }}</h2>
        <p>{{ article.content }}</p>
        <hr>
      {% endfor %}
    </p>
  </body>
  </html>
  ```

- JsonResponse

  ```python
  # articles/urls.py
  
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('html/', views.article_html),
      path('json-1/', views.article_json_1),  # JsonResponse 객체 -> JSON 데이터 응답
      path('json-2/', views.article_json_2),
      path('json-3/', views.article_json_3),
  ]
  ```

  ```python
  # articles/views.py
  
  from django.http.response import JsonResponse
  
  def article_json_1(request):
      articles = Article.objects.all()
      articles_json = []
  
      for article in articles:
          articles_json.append(
              {
                  'id': article.pk,
                  'title': article.title,
                  'content': article.content,
                  'created_at': article.created_at,
                  'updated_at': article.updated_at,
              }
          )
      return JsonResponse(articles_json, safe=False)
  ```

  - Content-Type entity header

    - 데이터 media type

  - JsonResponse objects

    - HttpResponse 서브 클래스 : JSON-encoded response 제작

    - `safe` parameter

      - Ture 기본 값
      - dict 이외 객체 직렬화 (Serialization) 시 False

      ```python
      # 예시
      
      response = JsonResponse({'foo': 'bar'})
      response = JsonResponse([1, 2, 3], safe=False)
      ```

  - Serialization

    - 직렬화
    - 데이터 구조, 객체 상태 -> 동일, 다른 컴퓨터 환경에 저장, 나중에 재구성 가능한 포맷 변환 과정

- Django Serializer

  ```python
  # articles/urls.py
  
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('html/', views.article_html),
      path('json-1/', views.article_json_1),  
      path('json-2/', views.article_json_2),  # HttpResponse -> JSON 응답
      path('json-3/', views.article_json_3),
  ]
  ```

  ```python
  # 주어진 모델 정보 활용 -> 필드 개별적으로 제작 필요 X
  from django.http.response import JsonResponse, HttpResponse
  from django.core import serializers
  
  def article_json_2(request):
      articles = Article.objects.all()
      data = serializers.serialize('json', articles)
      return HttpResponse(data, content_type='application/json')
  ```

- Django REST Framework

  ```bash
  $ pip install djangorestframework
  ```

  ```python
  # settings.py
  
  INSTALLED_APPS = [
      ...
      'rest_framework',
  ]
  ```

  ```python
  # articles/urls.py
  
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('html/', views.article_html),
      path('json-1/', views.article_json_1),  
      path('json-2/', views.article_json_2),  
      path('json-3/', views.article_json_3),  # DRF 라이브러리 -> JSON 응답 url 확인
  ]
  ```

  ```python
  # Article 모델 맞춰서 자동으로 필드 생성, serialize ModelSerializer 확인
  # articles/serializers.py
  
  from rest_framework import serializers
  from .models import Article
  
  
  class ArticleSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Article
          fields = '__all__'
  ```

  ```python
  # DEF Response() -> Serialize 된 JSON 객체 응답
  # articles/views.py
  
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  from .serializers import ArticleSerializer
  
  # @api_view(['GET'])
  @api_view()
  def article_json_3(request):
      articles = Article.objects.all()
      serializer = ArticleSerializer(articles, many=True)
      return Response(serializer.data)
  ```

  - Django REST Framework (DRF)

    - Serializer : Django Form, ModelForm 클래스와 유사

      |          |  Django   |     DRF     |
      | :------: | :-------: | :---------: |
      | Response |   HTML    |    JSON     |
      |  Model   | ModelForm | Serializers |

### Single Model

- DRF with Single Model

  - 단일 모델 data -> 직렬화 (Serialization) => JSON 변환

- Init Project

  ```python
  # settings.py
  
  INSTALLED_APPS = [
      'articles',
      'django_seed',
      'django_extensions',
      'rest_framework',
  ]
  ```

  ```python
  # my_api/urls.py
  
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/v1/', include('articles.urls')),
  ]
  ```

  ```python
  # articles/urls.py
  
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('html/', views.article_html),
      path('json-1/', views.article_json_1),
      path('json-2/', views.article_json_2),
      path('json-3/', views.article_json_3),
  ]
  ```

  ```python
  # models.py
  
  from django.db import models
  
  class Article(models.Model):
      title = models.CharField(max_length=100)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

- Create Dummy Data

  ```bash
  $ python manage.py migrate
  $ python manage.py seed articles --number=20
  ```

- ModelSerializer

  - 모델 필드에 해당 필드 있는 Serializer 클래스 자동 제작 shortcut
  - 기능
    - 모델 정보 맞춰서 자동으로 필드 생성
    - Serializer 유효성 검사기 자동 생성
    - `.create()`, `.update()` 간단 기본 구현 포함

  ```python
  # Model 필드 어떻게 직렬화 -> Django Model 필드 설정 동일
  # articles/serializers.py
  
  from rest_framework import serializers
  from .models import Article
  
  class ArticleSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Article
          fields = '__all__'
  ```

- Serializer in Shell

  ```bash
  # 1. shell_plus 실행
  $ python manage.py shell_plus
  
  # 2. 작성한 Serializer Import
  >>> from articles.serializers import ArticleListSerializer
  
  # 3. 기본 인스턴스 구조 확인
  >>> serializer = ArticleListSerializer()
  >>> serializer
  ArticleListSerializer():
  	id = IntegerField(label='ID', read_only=True)
  	title = CharField(max_length=100)
  	
  # 4. Model Instance 객체
  >>> article = Article.objects.get(pk=1)
  >>> article
  <Article: Article object (1)>
  
  >>> serializer = ArticleListSerializer(article)
  >>> serializer
  ArticleListSerializer(<Article: Article object (1)>):
  	id = IntegerField(label='ID', read_only=True)
  	title = CharField(max_length=100)
  >>> serializer.data
  {'id': 1, 'title': 'Site economic if two country science.'}
  
  # 5. QuerySet 객체
  >>> article = Article.objects.all()
  
  # 5-1 many=True 옵션 X
  >>> serializer = ArticleListSerializer(article)
  >>> serializer.data
  AttributeError: Got AttributeError when attempting to get a value for field 'title' on serializer 'ArticleListSerializer'.
  The serializer field might be name incorrectly and not match any attribute or key on the 'QuerySet' instance.
  Original exception text was: 'QuerySet' object has no attribute 'title'.
  
  # 5-2 many=True 옵션 O
  >>> serializer = ArticleListSerializer(article, many=True)
  >>> serializer.data
  [OrderedDict([('id', 1), ('title', 'Live left reserach.'), ('content', 'Small')])]
  ```

  - `many` argument

    - `many=True`
      - Serializing multiple objects
      - QuerySet 직렬화

    ```python
    @api_view(['GET'])
    def article_json_3(request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    ```

    ```python
    # many = True 예시
    
    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many=True)
    print(serializer.data)
    """
    [
    {'id': 0, 'title': 'The electric kook-aid acid test', 'author': 'Tom Wolfe'},
    {'id': 1, 'title': 'If this is a man', 'author': 'Primo Levi'},
    {'id': 2, 'title': 'The wind-up bird chronicle', 'author': 'Haruki Murakami'},
    ]
    """
    ```

- Build RESTful API

  |             |     GET      |  POST   |     PUT     |   DELETE    |
  | :---------: | :----------: | :-----: | :---------: | :---------: |
  |  articles/  | 전체 글 조회 | 글 작성 |             |             |
  | articles/1/ | 1번 글 조회  |         | 1번 글 수정 | 1번 글 삭제 |

- GET - Article List

  ```python
  # articles/urls.py
  
  urlpatterns = [
      path('articles', views.article_list),
  ]
  ```

  ```python
  # articles/views.py
  
  from rest_framework.response import Response
  from rest_framework.decorators import api_view
  
  from django.shortcuts import render, get_list_or_404
  
  from .models import Article
  from .serializers import ArticleSerializer
  
  @api_view(['GET'])
  def article_list(request):
      articles = get_list_or_404(Article)
      serializer = ArticleSerializer(articles, many=True)
      return Response(serializer.data)
  ```

  - `api_view` decorator

    - 기본적으로 GET 메서드만 허용, 다른 메서드 : 405 Method Not Allowed 응답
    - View 함수가 응답해야 하는 HTTP 메서드 목록 -> 리스트 인자로
    - DRF : 필수 작성

    ```python
    # 예시
    
    from rest_framework.decorators import api_view
    
    @api_view(['GET', 'POST'])
    def hello_world(request):
        if request.method == 'POST':
            return Response({'message': 'Got some data!', 'data': request.data})
        return Response({'message': 'Hello, world!'})
    ```

- GET - Article Detail

  ```python
  # Article List, Article Detail 구분 -> 추가 Serializer 정의
  class ArticleSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Article
          fields = '__all__'  # 모든 필드 직렬화
  ```

  ```python
  # articles/urls.py
  
  urlpatterns = [
      path('articles/<int:article_pk>/', views.article_detail),
  ]
  ```

  ```python
  # articles/views.py
  
  from django.shortcuts import get_object_or_404
  from .serializers import ArticleListSerializer, ArticleSerializer
  
  @api_view(['GET'])
  def article_detail(request, article_pk):
      article = get_object_or_404(Article, pk=article_pk)
      serializer = ArticleSerializer(article)
      return Response(serializer.data)
  ```

- POST - Create Article

  - 201 Created 상태 코드, 메시지 응답
  - RESTful 구조 맞게 작성
  - `article_list` 함수 -> 게시글 조회, 생성 모두 처리

  ```python
  # articles/views.py
  
  from rest_framework import status
  
  @api_view(['GET', 'POST'])
  def article_list(request):
      # 전체 게시글 조회
      if request.method == 'GET':
          articles = get_list_or_404(Article)
          serializer = ArticleListSerializer(articles, many=True) 
          return Response(serializer.data)
      # 게시글 생성
      elif request.method == 'POST':
          serializer = ArticleSerializer(data=request.data)
          if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  ```

  - Status Codes in DRF

    - `status` 모듈에 HTTP status code 집합 모두 포함

    ```python
    # 예시
    
    from rest_framework import status
    
    def example_list(request):
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    ```

  - `raise_exception` argument

    - serializers.ValidationError 예외 발생

    ```python
    # articles/views.py
    
    from rest_framework import status
    
    @api_view(['GET', 'POST'])
    def article_list(request):
        if request.method == 'GET':
            articles = get_list_or_404(Article)
            serializer = ArticleListSerializer(articles, many=True) 
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = ArticleSerializer(data=request.data)
            # Return a 400 response if the data was invalid
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) : 400 status code X
    ```

- DELETE - Delete Article

  - 204 No Content 상태 코드, 메시지 응답
  - `article_detail` 함수로 상세 게시글 조회, 삭제 가능

  ```python
  # articles/views.py
  
  @api_view(['GET', 'DELETE'])
  def article_detail(request, article_pk):
      article = get_object_or_404(Article, pk=article_pk)
      
      if request.method == 'GET':
          serializer = ArticleSerializer(article)
          return Response(serializer.data)
  	
      # 삭제
      elif request.method == 'DELETE':
          article.delete()
          data = {
              'delete': f'데이터 {article_pk}번이 삭제되었습니다.'
          }
          return Response(data, status=status.HTTP_204_NO_CONTENT)
  ```

- PUT - Update Article

  - `article_detail` 함수로 상세 게시글 조회, 삭제, 수정 가능

  ```python
  # articles/views.py
  
  @api_view(['GET', 'DELETE', 'PUT'])
  def article_detail(request, article_pk):
      ...
      
      elif request.method == 'PUT':
          serializer = ArticleSerializer(article, data=request.data)
          # serializer = ArticleSerializer(instance=article, data=request.data)
          if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response(serializer.data)
  ```

### 1:N Relation

- DRF with 1:N Relation

  - 1:N 관계 -> 모델 data 직렬화 후 JSON 변환

  ```python
  # articles/models.py
  
  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

- GET - Comment List

  ```python
  # articles/serializers.py
  
  class CommentSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Comment
          fields = '__all__'
  ```

  ```python
  # articles.urls.py
  
  urlpatterns = [
      ...
      path('comments/', views.comment_list),
  ]
  ```

  ```python
  # articles/views.py
  
  from .models import Article, Comment
  from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
  
  @api_view(['GET'])
  def comment_list(request):
      comments = get_list_or_404(Comment)
      serializer = CommentSerializer(comments, many=True)
      return Response(serializer.data)
  ```

- GET - Comment Detail

  ```python
  # articles.urls.py
  
  urlpatterns = [
      ...
      path('comments/<int:comment_pk>/', views.comment_detail),
  ]
  ```

  ```python
  # articles.views.py
  
  @api_view(['GET'])
  def comment_detail(request, comment_pk):
      comment = get_object_or_404(Comment, pk=comment_pk)
      serializer = CommentSerializer(comment)
      return Response(serializer.data) 
  ```

- POST - Create Comment

  ```python
  # articles.urls.py
  
  urlpatterns = [
      ...
      path('articles/<int:article_pk>/comments/', views.comment_create),
  ]
  ```

  ```python
  # articles.views.py
  
  @api_view(['POST'])
  def comment_create(request, article_pk):
      article = get_object_or_404(Article, pk=article_pk)
      serializer = CommentSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
  ```

  - 생성 시 참조 모델 객체 정보 필요 -> 외래 키

    ```python
    @api_view(['POST'])
    def comment_create(request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)  # 인스턴스 저장 시점에 추가 데이터 삽입 필요 시
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    ```

- Read Only Field

  - 직렬화 X, 반환 값에만 해당 필드 포함 설정

  ```python
  # articles/serializers.py
  
  class CommentSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Comment
          fields = '__all__'
          read_only_fields = ('article',)
  ```

- DELETE & PUT - delete, update Comment

  ```python
  # articles/views.py
  
  @api_view(['GET', 'DELETE', 'PUT'])
  def comment_detail(request, comment_pk):
      comment = get_object_or_404(Comment, pk=comment_pk)
      
      if request.method == 'GET':
          serializer = CommentSerializer(comment)
          return Response(serializer.data) 
  
      elif request.method == 'DELETE':
          comment.delete()
          data = {
              'message': f'댓글 {comment_pk}번이 삭제되었습니다.',
          }
          return Response(data, status=status.HTTP_204_NO_CONTENT)
  
      elif request.method == 'PUT':
          serializer = CommentSerializer(comment, data=request.data)
          if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response(serializer.data)
  ```

- 1:N Serializer

  - 특정 게시글에 작성된 댓글 목록 출력 : 기존 필드 override

    - `PrimaryKeyRelatedField`

      - pk 

      - to many relationships (N) -> many=True 필요

      - comment_set 필드 값을 form-data로 받지 않아서 read_only=True 필요

        ```python
        # articles/serializers.py
        
        class ArticleSerializer(serializers.ModelSerializer):
            comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        
            class Meta:
                model = Article
                fields = '__all__'
        ```

      - 역참조 시 생성되는 comment_set override

        ```python
        # articles/models.py
        
        class Comment(models.Model):
            article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
        ```

    - `Nested relationships`

      - 참조 대상 표현에 포함 or 중첩 (nested)

      - 상하위치 변경

        ```python
        # articles/serializers.py
        
        class CommentSerializer(serializers.ModelSerializer):
        
            class Meta:
                model = Comment
                fields = '__all__'
                read_only_fields = ('article',)
        
        class ArticleSerializer(serializers.ModelSerializer):
            comment_set = CommentSerializer(many=True, read_only=True)
            
            class Meta:
                model = Article
                fields = '__all__'
        ```

  - 특정 게시글에 작성된 댓글 개수 : 새로운 필드 추가

    - 별도 값 필드 사용 -> 필드 작성

      ```python
      # articles/serializers.py
      
      class ArticleSerializer(serializers.ModelSerializer):
          comment_set = CommentSerializer(many=True, read_only=True)
          comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
      
          class Meta:
              model = Article
              fields = '__all__'
      ```

      - `source` argument
        - 점 표기법 (dot notation) -> 속성 탐색
        - comment_set 필드에 . 을 통해 전체 댓글 개수 확인 가능
        - `.count()` : built-in QuerySet API 

  - `read_only_fields`

    - 안됨

      ```python
      # articles/serializers.py
      
      
      class ArticleSerializer(serializers.ModelSerializer):
          comment_set = CommentSerializer(many=True, read_only=True)
          comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
      
          class Meta:
              model = Article
              fields = '__all__'
              # read_only_fields = ('comment_set', 'comment_count',)
      ```

      

