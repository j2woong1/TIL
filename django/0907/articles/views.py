from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_POST, require_http_methods

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

@require_http_methods(["GET", "POST"])
def create(request):
    # 5. create 경로로 요청이 들어옴 (POST) [case 1. 잘못된 입력] -> 사용자가 데이터 입력
    # 10. [case2. 올바른 입력]
    if request.method == 'POST':
        # 6. 데이터가 입력된 종이를 가져옴 -> ArticleForm로 instance 만듦(빈 종이 + 사용자 데이터)
        # 11. 데이터가 입력된 종이를 가져옴 -> ArticleForm로 instance 만듦(빈 종이 + 사용자 데이터)
        form = ArticleForm(request.POST) # 'data = ' 생략
        # 7. 데이터 유효성 검사
        # 12. 데이터 유효성 검사
        if form.is_valid():
            # 13. 데이터를 DB에 저장
            form.save()
            # 14. index로 redirect
            return redirect('articles:index')
        
    else: # 1. create 경로로 요청이 들어옴 (GET 요청 -> DB 영향 X) -> 빈 종이 (Form) 응답
        form = ArticleForm() # 2. ArticleForm으로 빈 종이 (instance) 생성

    # 3. user에게 빈 종이 주기 위해서 context에 form 담기
    # 8. 잘못된 데이터 재입력하기 위해서 context에 form
    context = { 
        'form' : form,
    }

    # 4. 사용자에게 데이터 받기 위해 빈 종이 넘기기 -> 데이터 입력
    # 9. 올바른 데이터 받기 위해 form 넘기기
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

@require_http_methods(["GET", "POST"])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save() # article에 수정 완료된 데이터 1줄 들어감
            return redirect('articles:detail', article.pk)

    else: # GET
        form = ArticleForm(instance=article)

    context = {
        'article': article, # article.pk를 a 태그에 사용하려고
        'form': form,
    }
    return render(request, 'articles/update.html', context)