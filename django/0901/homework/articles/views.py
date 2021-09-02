from django.shortcuts import redirect, render
from .models import Article

# Create your views here.
def index(request):

    articles = Article.objects.all()

    context = {
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    if request.method == "POST":
        articles = Article()

        articles.title = request.POST.get('title')
        articles.content = request.POST.get('content')

        articles.save()

    return redirect('articles:index')

def detail(request):
    return render(request, 'articles/detail.html')