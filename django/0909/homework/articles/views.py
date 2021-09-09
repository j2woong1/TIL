from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST
from .models import Article, ArticleImage
from .forms import ArticleForm, ArticleImageForm

# Create your views here.

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        imageform = ArticleImageForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            imageform.save()        
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
        imageform = ArticleImageForm()
    context = {
        'form': form,
        'imageform': imageform,
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    articleimage = get_object_or_404(ArticleImage, pk=pk)
    context = {
        'article': article,
        'articleimage': articleimage,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    articleimage = get_object_or_404(ArticleImage, pk=pk)
    article.delete()
    articleimage.delete()
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    articleimage = get_object_or_404(ArticleImage, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        imageform = ArticleForm(request.POST, request.FILES, instance=articleimage)
        if form.is_valid():
            form.save()
            imageform.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
        imageform = ArticleImageForm(instance=articleimage)
    context = {
        'article': article,
        'form': form,
        'imageform': imageform,
    }
    return render(request, 'articles/update.html', context)