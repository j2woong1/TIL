from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta: # form에 대한 정보
        model = Article
        fields = '__all__'