# 1. static 파일 기본 설정

> 개발자가 작성한 CSS 파일이나 미리 업로드한 이미지 파일 등이 Django 프로젝트 폴더(my_pjt) 내부 assets 폴더에 있다. 이처럼 기존 static 파일 경로 외에 추가 경로를 정의해야 할 경우 settings.py에 추가해야 하는 설정과 값을 작성하시오.

```python
STATICFILES_DIRS = [
    BASE_DIR / 'my_pjt' / 'assets',
]
```



# 2. media 파일 기본 설정

> 사용자가 업로드 파일의 저장치를 Django 프로젝트 폴더(my_pjt) 내부 uploaded_files 폴더로 지정하고자 한다. 이 때, settings.py에 작성해야 하는 설정과 값을 모두 작성하시오.

```python
# 서버가 Media 파일을 요청할 때 사용할 가상의 URL
MEDIA_URL = '/media/'

# Media 파일이 실제 위치할 경로
MEDIA_ROOT = BASE_DIR / 'media'
```



# 3. Serving files uploaded by user during development

> settings.py에 MEDIA_URL 값이 작성되어 프로젝트에 사용자가 업로드한 파일이 업로드 될 수 있게 되었다 . 하지만 사용자가 실제 웹 페이지 내에서 이 파일을 조회 할 수 있도록 하기 위해선 업로드 된 파일에 대한 URL 을 생성 해주는 설정이 필요하다. 빈칸 (a), (b), (c), (d) 에 들어 갈 코드를 작성하시오

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

