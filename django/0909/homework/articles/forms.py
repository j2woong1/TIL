from django import forms
from .models import Article, ArticleImage


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목: ',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the Title',
                'maxlength': 10
            }
        )
    )
    content = forms.CharField(
        label='내용: ',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the Content',
                'rows': 5,
                'cols': 50,
            }
        )
    )
    class Meta:
        model = Article
        fields = ('title','content',)


class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(
        label='Image'
    )
    class Meta:
        model = ArticleImage
        fields = ('image',)