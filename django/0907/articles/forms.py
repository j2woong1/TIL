from django import forms
from django.db.models import fields
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta: # form 정보
        model = Article
        # fields = '__all__'
        fields = ['title', 'content']
        # exclude = ('title', )
        # exclude -> title 빼고 
        # ('title') : 문자열. tuple로 쓰려면 ,