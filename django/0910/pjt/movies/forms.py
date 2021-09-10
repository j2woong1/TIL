from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'place_holder': '제목을 입력하세요.',
                'maxlength': 100,
            }
        )
    )
    overview = forms.CharField(
        label='줄거리',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'place_holder': '줄거리를 입력하세요.',
            }
        )
    )
    poster_path = forms.CharField(
        label='포스터',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'place_holder': '파일 경로',
                'maxlength': 500,
            }
        )
    )



    class Meta:
        model = Movie
        fields = '__all__'