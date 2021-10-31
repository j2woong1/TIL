## Django REST Framework

> - DRF 를 활용하여 음악 정보 관련 REST API 서버를 구축하시오
> - 프로젝트는 my_api , 앱은 music 으로 만들어 진행한다
> - Postman 을 활용하여 각 HTTP Method 에 맞는 요청을 테스트하시오

### 1. Model & Admin

> - 작성 할 모델 및 필드 정보
> - admin 페이지를 활용하여 가수 해당 가수가 부른 노래를 2 개씩 작성한다
>
> ```python
> class Artist(models.Model):
>     name = models.CharField(max_length=200)
>     
> class Music(models.Model):
>     artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
>     title = models.CharField(max_length=200)
> ```

```python
# models.py
from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
```



### 2. Serializer

> - ArtistListSerializer
>   - 모든 가수의 정보를 반환하기 위한 Serializer
>   - id, name 필드 출력
> - ArtistSerializer
>   - 상세 가수의 정보를 생성 및 반환하기 위한 Serializer
>   - id, name, music_set , music_count 필드 출력
>     (music_count 필드는 music_set 을 count 한 결과이다)
> - MusicListSerializer
>   - 모든 음악의 정보를 반환하기 위한 Serializer
>   - id, title 필드 출력
> - MusicSerializer
>   - 상세 음악의 정보를 생성 및 반환하기 위한 Serializer
>   - id, title, artist 필드 출력

```python
# serializers.py
from rest_framework import serializers
from .models import Music, Artist

class ArtistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'name',)
        read_only_fields = ('artist',)

class MusicListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('id', 'title',)

class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True, read_only=True)
    music_count = serializers.IntegerField(source='music_set.count', read_only=True)

    class Meta:
        model = Artist
        fields = '__all__'
```



### 3. URL & View

> - GET & POST api/v1/artists/
>   - GET 요청인 경우 모든 가수의 id 와 name 컬럼을 JSON 으로 응답한다
>   - POST 요청인 경우 가수의 정보를 생성한다
>     - 검증에 성공하는 경우 가수의 정보를 DB 에 저장하고 생성된 가수의 정보와 201 Created 를 응답한다
>     - 검증에 실패하는 경우 400 Bad Request 를 응답한다
> - GET api/v1/artists/<artist_pk>/
>   - 특정 가수의 모든 컬럼을 JSON 으로 응답한다
>   - 특정 가수의 노래 정보와 노래의 개수 정보를 함께 응답한다
> - POST api/v1/artists/<artist_pk >/music/
>   - 특정 가수의 음악의 정보를 생성한다
>   - 검증에 성공하는 경우 음악의 정보를 DB 에 저장하고 생성된 음악의 정보와 201 Created 를 응답한다
>   - 검증에 실패하는 경우 400 Bad Request 를 응답한다
> - GET api/v1/music/
>   - 모든 음악의 id 와 title 컬럼을 JSON 으로 응답한다
> - GET & PUT & DELETE api/v1/music/<music_pk>
>   - GET 요청인 경우 특정 음악의 모든 컬럼을 JSON 으로 응답한다
>   - PUT 요청인 경우 특정 음악의 정보를 수정한다
>     - 검증에 성공하는 경우 수정된 음악의 정보를 DB 에 저장한다
>     - 검증에 실패하는 경우 400 Bad Request 를 응답한다
>     - 수정이 완료된 이후에 수정된 음악의 정보를 응답한다
>   - DELETE 요청일 경우 특정 음악의 정보를 삭제한다
>     - 삭제가 완료된 이후에 삭제한 음악의 id 와 204 No Content 를 응답한다

```python
# views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Music, Artist
from .serializers import MusicListSerializer, MusicSerializer, ArtistListSerializer, ArtistSerializer
from music import serializers


@api_view(['GET', 'POST'])
def artist_list(request):
    if request.method == 'GET':
        artists = get_list_or_404(Artist)
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtistListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)


@api_view(['POST'])
def music_create(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(artist=artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def music_list(request):
    music = get_list_or_404(Music)
    serializer = MusicListSerializer(music, many=True) 
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        music.delete()
        data = {
            'delete': f'데이터 {music_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```

