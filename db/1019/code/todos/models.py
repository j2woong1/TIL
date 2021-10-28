from django.db import models
from django.conf import settings

# Create your models here.
# models.py 에서만 settings.AUTH_USER_MODEL씀 

# User(1) -> Todo(N)
class Todo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
