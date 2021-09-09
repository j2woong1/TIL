from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta: # form에 대한 정보
        model = Article
        fields = '__all__'
        # fields = ['title', 'content'] # 전부다 적어주는 걸 권장함
        # fields = ('title', 'content')
        # exclude = ('title',)
        # exclude -> title 빼고 -> 필드가 100개가 있다면 title 빼고, 99개가 나옴
        # 참고로 ('title') -> 문자열이다. ('title') == 'title' 튜플로 쓰려면 ,를 찍어줘야함!