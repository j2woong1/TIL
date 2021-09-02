import articles
from django.shortcuts import redirect, render
from .models import Article

# Create your views here.
def index(request):
    # articles = Article.objects.all()[::-1] # 파이썬이 변경
    articles = Article.objects.order_by('-id') # id 역순으로 정렬
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    print(request.POST)
    title = request.POST.get('title')
    content = request.POST.get('content')

    # same
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    article = Article(title=title, content=content)
    # 중간 과정 (Validation)
    article.save()

    return redirect('articles:detail', article.pk)

def detail(request, pk):
    article = Article.objects.get(pk=pk) # db pk = 위 pk
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST": # 버튼 눌렀을 떄
        article.delete()
        return redirect('articles:index')
    else: # 주소창에 입력
        return redirect('articles:detail', article.pk)
    
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('articles:detail', article.pk)