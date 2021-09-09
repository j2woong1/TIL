from django.db import models

from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail

# def articles_image_path(instance, filename):
#     return f'user_{instance.user.pk}/{filename}'
# image = models.ImageField(blank=True, upload_to=articles_image_path)도 사용 가능!
# image = models.ImageField(blank=True, upload_to=f'user_{instance.user.pk}/{filename}')도 사용 가능!
# image = models.ImageField(blank=True, upload_to=f'user_woong/ssafy.png')도 사용 가능!
# 지금은 로그인한 user가 없기 때문에 에러 발생함.


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20) # max_length는 필수
    content = models.TextField()
    # image = models.ImageField(blank=True)
    # image_thumb = ProcessedImageField(
    #     blank=True,
    #     processors=[Thumbnail(200, 200)],
    #     format='JPEG',
    #     options={'quality': 90},
    # ) # 썸네일 이미지를 만듬! (원본 이미지를 가공하여 넣기 때문에, 원본은 저장X, 썸네일만 저장)
    # 원본(O), 썸네일(O)
    image = models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')
    image_thumbnail = ImageSpecField(
        source='image', # 원본 이미지 필드명
        processors=[Thumbnail(200, 200)],
        format='JPEG',
        options={'quality': 90},
    )

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title