from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)  # 필수 인자 존재 (문자열 길이 제한)
    content = models.TextField()

    def __str__(self):
        return 