> 아래 작성된 views.py 의 코드 일부를 보고 문제에 알맞은 답을 서술 하시오
>
> ```python
> from django.shortcuts import render, redirect
> from .forms import ArticleForm
> 
> def create(request):
>     if request.method == 'POST':
>         form = ArticleForm(request.POST)
>         if form.is_valid():
>             article = form.save()
>             return redirect('articles:detail', article.pk)
>     else:
>         form = ArticleForm()
>     context = {
>         'form' : form,
>     }
>     return render(request, 'articles/create.html', context)
> ```
>
> 

1. 왜 변수 context 는 if else 구문과 동일한 레벨에 작성 되어있는가
   - if, else 구문 요청이 와도 form을 사용하기 위해서
2. 왜 request 의 http method 는 POST 먼저 확인하도록 작성하는가
   - 변경 사항 확인 후 유효성 검사